import os
import sys
import logging
import shutil
import glob
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import argparse
import enlighten
import parse
import pickle
from collections import OrderedDict 

from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression
from scipy.stats import pearsonr
import tensorflow as tf
from keras.models import model_from_json
from keras import backend as k

import innvestigate
import innvestigate.utils as iutils

sys.path.append(os.path.abspath('..'))
import parameters


class Analyze:
    def __init__(self,N,suffix):
        self.inputs      = parameters.inputs
        self.outputs     = parameters.outputs
        self.path_files  = parameters.path_gen_output
        self.path_out    = os.path.join(os.path.abspath("."),suffix)
        self.N           = N
        self.suffix      = suffix
        self.path_scores = os.path.join(self.path_out,"scores.pkl")
        self.scores      = pd.DataFrame(columns=self.inputs)

        if not os.path.exists(self.path_out):
            os.makedirs(self.path_out)
    
        self.makeVarNames()
        if self.N != 0:
            self.getDF()

    def fromStringToLatexNames(self,s):
        particles = []
        if 'electron' in s:
            particles.append(r"e^{-}")
        if 'positron' in s: 
            particles.append(r"e^{+}")
        if 'antineutrino' in s: # Because neutrino is in antineutrino
            particles.append(r"\bar{\nu}")
        elif 'neutrino' in s: 
            particles.append(r"\nu")
        if 'antibjet' in s:  # Because bjet is in antibjet
            particles.append(r"\bar{b}")
        elif 'bjet' in s: 
            particles.append(r"b")
        if 'init1' in s: 
            particles.append(r"q_{1}")
        if 'init2' in s: 
            particles.append(r"q_{2}")

        if len(particles)==0:
            return s
        elif len(particles)==1:
            return particles[0]
        else:
            return particles

    def makeVarNames(self):
        self.inputs_names = OrderedDict()
        from parameters import product2Momentas, invMass2Momentas, invMass3Momentas
        for inp in self.inputs:
            if parse.parse(product2Momentas,inp) is not None:
                part1 = self.fromStringToLatexNames(parse.parse(product2Momentas,inp)[0])
                part2 = self.fromStringToLatexNames(parse.parse(product2Momentas,inp)[1])
                self.inputs_names[inp] = r"$P_{%s} P_{%s}$"%(part1,part2)
            elif parse.parse(invMass3Momentas,inp) is not None: # invMass2Momentas passes the invMass3Momentas selection
                part1 = self.fromStringToLatexNames(parse.parse(invMass3Momentas,inp)[0])
                part2 = self.fromStringToLatexNames(parse.parse(invMass3Momentas,inp)[1])
                part3 = self.fromStringToLatexNames(parse.parse(invMass3Momentas,inp)[2])
                self.inputs_names[inp] = r"$(P_{%s}+P_{%s}+P_{%s})^{2}$"%(part1,part2,part3)
            elif parse.parse(invMass2Momentas,inp) is not None:
                part1 = self.fromStringToLatexNames(parse.parse(invMass2Momentas,inp)[0])
                part2 = self.fromStringToLatexNames(parse.parse(invMass2Momentas,inp)[1])
                self.inputs_names[inp] = r"$(P_{%s}+P_{%s})^{2}$"%(part1,part2)
            else:
                part = self.fromStringToLatexNames(inp)
                if not isinstance(part,list):
                    if 'Pt()' in inp: 
                        self.inputs_names[inp] = r"$P_{T}(%s)$"%part
                    elif 'Eta()' in inp: 
                        self.inputs_names[inp] = r"$\eta(%s)$"%part
                    elif 'Phi()' in inp: 
                        self.inputs_names[inp] = r"$\phi(%s)$"%part
                    elif 'E()' in inp: 
                        self.inputs_names[inp] = r"$E(%s)$"%part
                    elif 'Px()' in inp: 
                        self.inputs_names[inp] = r"$P_x(%s)$"%part
                    elif 'Py()' in inp: 
                        self.inputs_names[inp] = r"$P_x(%s)$"%part
                    elif 'Pz()' in inp: 
                        self.inputs_names[inp] = r"$P_z(%s)$"%part
                    else:
                        self.inputs_names[inp] = inp
                elif len(part)==2:
                    if 'Pt()' in inp: 
                        self.inputs_names[inp] = r"$\Delta P_{T}(%s,%s)$"%(part[0],part[1])
                    elif 'Eta()' in inp: 
                        self.inputs_names[inp] = r"$\Delta \eta(%s,%s)$"%(part[0],part[1])
                    elif 'Phi()' in inp: 
                        self.inputs_names[inp] = r"$\Delta \phi(%s,%s)$"%(part[0],part[1])
                    else:
                        self.inputs_names[inp] = inp
                else:
                    self.inputs_names[inp] = inp

    def getDF(self):
        from import_tree import LoopOverTrees
        df = LoopOverTrees(input_dir  = self.path_files,
                           variables  = self.inputs+self.outputs,
                           n          = self.N)
        df = df.sample(frac=1).reset_index(drop=True) # Shuffle dataframe
        self.df_inputs = df[self.inputs]
        self.df_outputs = df[self.outputs]
        del df
        logging.info("Number of events in sample : %d"%(self.df_inputs.shape[0]))
        logging.info("Number of input variables  : %d"%(self.df_inputs.shape[1]))
        logging.info("Number of output variables : %d"%(self.df_outputs.shape[1]))

    def loadModel(self,basemodel):
        # Need to find basemodel.json and basemodel.h5 #
        self.basemodel = basemodel
        with open(basemodel+'.json','r') as f:
            loaded_model_json = f.read()
        self.model = model_from_json(loaded_model_json)
        self.model.load_weights(basemodel+".h5")
        # Load scaler as basemodel.pkl#
        with open(basemodel+'.pkl', 'rb') as handle:
            self.scaler = pickle.load(handle)

        # Normalize inputs (so that done only once) #
        if self.N != 0:
            self.norm_inputs = self.scaler.transform(self.df_inputs.values)


    def saveScores(self):
        # Load saved DF if exists #
        if os.path.exists(self.path_scores):
            saved_scores = pd.read_pickle(self.path_scores)
            if saved_scores.shape[0] == 0:
                logging.warning("Loaded empty DF, will not do anything")
            else:
                logging.info("Loaded DF containing")
                for index in saved_scores.index:
                    logging.info("..... "+index)
                # Only take from save the index not calculated here #
                unknown_index = [idx for idx in saved_scores.index if idx not in self.scores.index]
                if len(unknown_index) != 0:
                    logging.info("List of values that have not been recalculated and will come from the save")
                    for idx in unknown_index:
                        logging.info("..... "+idx)
                # If some values have been calculated, append the ones coming from the save #
                if self.scores.shape[0] != 0:
                    self.scores = self.scores.append(saved_scores.loc[unknown_index])
                else:
                    logging.warning("Nothing has been calculated, all will com from the save")
                    self.scores = saved_scores

        # Save to pickle #
        if self.scores.shape[0] != 0:
            self.scores.to_pickle(self.path_scores)
            logging.info("Scores saved as %s"%self.path_scores)
            for index in self.scores.index:
                logging.info("..... "+index)
        else:
            logging.warning("No scores available, will not save")
            

    def addScore(self,arr,title):
        # Check if title already in score DF #
        if title in self.scores.index:
            logging.warning('Score entry "%s" has been rewritten'%title)
            self.scores.drop([title])

        new_row = pd.DataFrame(arr.reshape(1,-1),columns=self.scores.columns,index=[title])
        self.scores = self.scores.append(new_row,verify_integrity=True)

    def makeInputsGridPlot(self):
        logging.info("Starting the input map plot")
        g = sns.PairGrid(self.df_inputs)
        g.map_upper(plt.scatter)
        #g.map_lower(sns.kdeplot)
        g.map_lower(plt.scatter)
        #g.map_diag(sns.kdeplot, lw=3, legend=True);
        g.map_diag(plt.hist)
        name = os.path.join(self.path_out,'input_map_%s.png'%self.suffix)
        plt.savefig(name)
        logging.info("... saved as %s"%name)

    def makeCorrelationMatrix(self):
        logging.info("Starting the correlation matrix plot")
        # Compute the correlation matrix
        #corr = pd.concat([self.df_inputs,self.df_outputs],axis=1).corr()
        corr = self.df_inputs.corr()

        # Renaming the index and columns #
        new_col = []
        for col in corr.columns:
            new_col.append(self.inputs_names[col])
        corr.columns = new_col
        new_idx = []
        for idx in corr.index:
            new_idx.append(self.inputs_names[idx])
        corr.index = new_idx

        # Generate a mask for the upper triangle
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True

        # Set up the matplotlib figure
        f, ax = plt.subplots(figsize=(11, 9))
        f.subplots_adjust(left=0.05, right=1., top=0.95, bottom=0.1)
        f.suptitle("Correlation matrix",fontsize=22)

        # Generate a custom diverging colormap
        cmap = sns.diverging_palette(250, 15, s=75, l=40, n=10, center='light', as_cmap=True)

        # Draw the heatmap with the mask and correct aspect ratio
        sns.heatmap(corr, mask=mask, cmap=cmap,  center=0,
                    square=True, linewidths=.5, cbar_kws={"shrink": .5})
        name = os.path.join(self.path_out,'correlation_matrix_%s.png'%self.suffix)
        plt.savefig(name)
        logging.info("... saved as %s"%name)

        # ClusterMap #
        #f, ax = plt.subplots(figsize=(11, 9))
        #f.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.3)
        #f.suptitle("Cluster map")

        #

        #sns.clustermap(corr, center=0, cmap=cmap,
        #               #row_colors=network_colors, col_colors=network_colors,
        #                              linewidths=.75, figsize=(13, 13))
        #name = 'cluster_map.png'
        #plt.savefig(name)
        #logging.info("... saved as %s"%name)

    def outputsCorrelation(self):
        logging.info("Processing correlation")
        scores = []
        for inp in self.inputs:
            r = pearsonr(self.df_inputs[inp].values,self.df_outputs.values.ravel()) 
            scores.append(r[0])
        # Add to scores DF #
        self.addScore(np.array(scores),"Pearson correlation")
        logging.info("... done")

    def outputsMutualInformation(self):
        logging.info("Processing mutual information")
        scores = []
        for inp in self.inputs:
            r = mutual_info_regression(self.df_inputs[inp].values.reshape(-1,1),self.df_outputs.values.ravel())
            scores.append(r[0])
        # Add to scores DF #
        self.addScore(np.array(scores),"Mutual information")
        logging.info("... done")

    def extractFirstLayerWeights(self):
        logging.info("Processing network first layer averaged sum")
        import h5py
        f = h5py.File(self.basemodel+'.h5','r')
        weights = f['dense_1']['dense_1_1']['kernel:0'][()]
        avg_sum_weights = np.sum(np.absolute(weights),axis=1)/weights.shape[1]
        # Add to scores DF #
        self.addScore(avg_sum_weights,"First layer weights averaged sum")
        logging.info("... done")

    def getQuantiles(self):
        xq = np.array([0.05,0.95]) # Quantiles
        yq = np.array([0.,0.])
        self.quantiles_dict = {}
        filename = "quantiles_"+self.suffix+".json"

        # Check if file exists #
        if os.path.exists(filename): # Load it
            logging.info("Found quantiles file %s"%filename)
            with open(filename,'r') as handle:
                self.quantiles_dict = json.load(handle)

        else: # Create it
            logging.info("Generating quantiles")
            # get TChain over files #  
            import ROOT
            ROOT.gROOT.SetBatch(True)
            chain = ROOT.TChain("tree")
            for path in glob.glob(os.path.join(self.path_files,'*.root')):
                chain.Add(path)
            # Loop over inputs and get histogram quantiles#
            pbar = enlighten.Counter(total=len(self.inputs), desc='Progress', unit='Inputs')
            for inp in self.inputs:
                # Get hist #
                chain.Draw(inp+">>h(1000)")
                h = ROOT.gROOT.FindObject("h")
                # Get quantile #
                h.GetQuantiles(2,yq,xq)
                self.quantiles_dict[inp] = list(yq)
                pbar.update()
            # Save file #
            with open(filename,'w') as handle:
                json.dump(self.quantiles_dict, handle,indent=4)

            logging.info("... Quantiles saved in %s"%filename)

    def makeInputsVariations(self,inputs,index,varmin,varmax,Nvar):
        # Generate all variations of input at index #
        allvars = np.linspace(varmin,varmax,Nvar)
        # Generate full array #
        arrayLeft  = np.tile(inputs[0:index],(Nvar,1))
        arrayRight = np.tile(inputs[index+1:],(Nvar,1))
        arrayFull  = np.c_[arrayLeft,allvars,arrayRight]
        return arrayFull

    def differentiateNetwork(self):
        logging.info("Processing network differentiation")
        #bias = np.zeros(self.df_inputs.shape[1])
        std  = np.zeros(self.df_inputs.shape[1])

        self.getQuantiles()

        # Loop over inputs #
        Nevents = 100000
        pbar = enlighten.Counter(total=min(Nevents,self.df_inputs.shape[0]), desc='Progress', unit='Event')
        dict_dist = dict((k,np.array([])) for k in self.inputs)
        badevents = 0
        for i in range(min(Nevents,self.df_inputs.shape[0])): # Loop over events 
            pbar.update()
            # Get one event entry and scale it #
            inputs = self.df_inputs.loc[i].values.reshape(1,-1)
            output_exact = self.df_outputs.loc[i].values[0]
            output_model = self.model.predict(self.scaler.transform(inputs))
            # Loop over each variable #
            for j in range(inputs.shape[1]):
                # get min and max values from quantiles #
                yq = self.quantiles_dict[self.inputs[j]]
                # make variations #
                inputsvar = self.makeInputsVariations(inputs  = inputs[0], # Inputs is 2D
                                                      index   = j,
                                                      varmin  = yq[0],
                                                      varmax  = yq[1],
                                                      Nvar    = 50) 
                inputsvar  = self.scaler.transform(inputsvar) 
                outputsvar = self.model.predict(inputsvar,batch_size=inputsvar.shape[0])
                outputdiff = outputsvar-output_model 
                dict_dist[self.inputs[j]] = np.append(dict_dist[self.inputs[j]],outputdiff)

                # Remove weird events for which variations blow up : TODO find better way #
                if (outputdiff>1000).any():
                    continue

                # Record bias and std #
                #bias[j] += np.mean(outputsvar)-output_model
                std[j]  += np.std(outputsvar)


        # Make dir for distributions #
        path_deriv = os.path.join(self.path_out,"diff")
        if os.path.exists(path_deriv):
            shutil.rmtree(path_deriv)
        os.mkdir(path_deriv)

        # Make distribution plots #
        bins = np.linspace(-10.,10.,100)
        for name, arr in dict_dist.items():
            latexname = self.inputs_names[name]
            fig, ax = plt.subplots(1,figsize=(9,8))
            fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1,hspace=0.1)
            ax.hist(arr,bins=bins)
            ax.set_title("Quantiles variations [0.05,0.95] of "+latexname+ " [%0.2f,%0.2f]"%(self.quantiles_dict[name][0],self.quantiles_dict[name][1]),fontsize=18)
            ax.set_xlabel("$\Delta - log_{10}(DNN \ output)_{Variations - Input}$",fontsize=19)
            ax.set_xlim(np.amin(bins),np.amax(bins))
            name = os.path.join(path_deriv,"diff_"+latexname.replace("$","")+".png")
            print ("... Saved %s"%name)
            plt.savefig(name)
            plt.close()

        # Combine png into pdf #
        os.system("convert "+path_deriv+"/*png "+path_deriv+"/allplot.pdf")

        #bias /= Nevents
        std  /= Nevents

        #bias_row = pd.DataFrame(bias.reshape(1,-1),columns=self.scores.columns,index=['Derivative bias'])
        #self.scores = self.scores.append(bias_row,verify_integrity=True)
        # Add to scores DF #
        self.addScore(std,"Input variations between quantiles [0.05,0.95]")
        logging.info("... done")

    def LRPAnalysis(self):
        logging.info("Processing network LRP")
        analyzers = {"Guided backpropagation":"guided_backprop","LRP (z method)":"lrp.z"}
        for title,analyzer_func in analyzers.items():
            analyzer = innvestigate.create_analyzer(analyzer_func,self.model)
            analysis = analyzer.analyze(self.norm_inputs)
            result   = np.sum(analysis,axis=0)/analysis.shape[0]
            # Add to scores DF #
            self.addScore(result,title)
        logging.info("... done")

    def networkGradient(self):
        logging.info("Processing network gradient")
        session = k.get_session()
        outgrad = session.run(tf.gradients(self.model.output, self.model.input), feed_dict={self.model.input: self.norm_inputs})[0] # Returns a list of one numpy array
        outgrad = np.sum(outgrad,axis=0)/outgrad.shape[0] # Average
        # Add to scores DF #
        self.addScore(outgrad,"Network gradient over inputs")
        logging.info("... done")

    def plotScores(self):
        # Reorder plots #
        order = ["Pearson correlation",
                 "Mutual information",
                 "First layer weights averaged sum",
                 "Network gradient over inputs",
                 "Input variations between quantiles [0.05,0.95]",
                 "Guided backpropagation",
                 "LRP (z method)"]

        logging.info("Starting the score plot")
        logging.info("Scores available")
        for index in self.scores.index:
            logging.info("..... "+index)


        self.scores = self.scores.loc[order]

        N = self.scores.shape[0]
        bins = np.arange(self.scores.shape[1])
        labels = []

        # --- separate bar plots ---#
        color=iter(plt.cm.rainbow(np.linspace(0.3,1,N))) 
        for col in self.scores.columns:
            labels.append(self.inputs_names[col])

        # Plot the different scores separately  #
        for i,(index, row) in enumerate(self.scores.iterrows()): # Index is title, row is data
            c = next(color)
            fig, ax = plt.subplots(1,figsize=(18,6))
            fig.subplots_adjust(left=0.05, right=0.99, top=0.90, bottom=0.2,hspace=0.1)
            #ax[i].bar(bins,row,tick_label=labels,color=c)
            row = np.abs(row) #  TODO : might not be correct
            ax.bar(bins,(row-np.amin(row))/(np.amax(row)-np.amin(row)),tick_label=labels,color=c)
            ax.set_xticklabels(labels,rotation='vertical')
            ax.set_title(index,fontsize=20)
            name = os.path.join(self.path_out,(index+'_%s.png'%self.suffix).replace(" ","_"))
            plt.savefig(name)
            plt.close()
            logging.info("... saved as %s"%name)

        # --- stage bar plots --- #
        # Plotting options  #
        color=iter(plt.cm.rainbow(np.linspace(0.3,1,N))) 
        fig, ax = plt.subplots(N,figsize=(18,N*6))
        fig.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.1,hspace=0.4)

        # Plot the different scores separately  #
        for i,(index, row) in enumerate(self.scores.iterrows()): # Index is title, row is data
            c = next(color)
            #ax[i].bar(bins,row,tick_label=labels,color=c)
            row = np.abs(row) #  TODO : might not be correct
            ax[i].bar(bins,(row-np.amin(row))/(np.amax(row)-np.amin(row)),tick_label=labels,color=c)
            ax[i].set_xticklabels(labels,rotation='vertical')
            ax[i].set_title(index,fontsize=20)

        name = os.path.join(self.path_out,'separateScores_%s.png'%self.suffix)
        plt.savefig(name)
        plt.close()
        logging.info("... saved as %s"%name)

        # --- combined bar plots --- #
        # Plotting options  #
        fig, ax = plt.subplots(1,figsize=(36,9))
        fig.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.1,hspace=0.2)
        color=iter(plt.cm.rainbow(np.linspace(0.3,1,N)))

        # Define binning #
        bin_dict = {} # Will contain the bins for each hist
        i = 0
        for name in self.scores.index:
            if i==0:
                bin_dict[name] = np.arange(self.scores.shape[1])
            else:
                bin_dict[name] = np.arange(self.scores.shape[1])+i/(N)
            i += 1
        
        # Loop over data and plot #
        for i,(index, row) in enumerate(self.scores.iterrows()): # Index is title, row is data
            c = next(color)
            row = np.abs(row) #  TODO : might not be correct
            ax.bar(bin_dict[index],
                        #row/np.sum(row),
                        (row-np.amin(row))/(np.amax(row)-np.amin(row)),
                        align ='edge',
                        width = 1/N,
                        color = c,
                        linewidth = 2,
                        label = index,
                        tick_label=None)
                        #tick_label=labels)
        ax.set_xlim(0,self.scores.shape[1])
        ax.set_xticks(np.arange(self.scores.shape[1])+0.5)
        ax.set_xticklabels(labels)

        # Vertical lines at ticks #
        for i in range(1,self.scores.shape[1]):
            plt.axvline(x=i, color='k', linestyle='--')

        plt.legend(loc='upper right')
        name = os.path.join(self.path_out,'combineScores_%s.png'%self.suffix)
        plt.savefig(name)
        plt.close()
        logging.info("... saved as %s"%name)


if __name__ == '__main__':
    #--- Argparse ---#
    parser = argparse.ArgumentParser(description='Analyzer : variables and/or network')

    # Main args #
    parser.add_argument('-n','--number', action='store', required=False, type=int, default=0,
        help='Number of events max per file')
    parser.add_argument('--suffix', action='store', required=False, type=str, default = '',
        help='Suffix for the png plots (default is "")')
    parser.add_argument('-v','--verbose', action='store_true', required=False, default=False,
        help='Verbose mode')

    # Inputs plots args #
    inputsplots = parser.add_argument_group('Make plots about the inputs alone')
    inputsplots.add_argument('--correlationplot', action='store_true', required=False, default=False,
        help='Wether to plot the correlation matrix')
    inputsplots.add_argument('--gridplot', action='store_true', required=False, default=False,
        help='Wether to plot input grid')

    # Output plots arg #
    outputsplots = parser.add_argument_group('Make plots about the inputs with respect to the output')
    outputsplots.add_argument('--correlation', action='store_true', required=False, default=False,
        help='Wether add the Pearson correlation to the scores')
    outputsplots.add_argument('--mi', action='store_true', required=False, default=False,
        help='Wether add the mutual information to the scores')
    outputsplots.add_argument('-m','--model', action='store', required=False, default=None, type=str,
        help='Model name (base + .json and +.h5), required for the arguments looking at the network')
    outputsplots.add_argument('--firstlayer', action='store_true', required=False, default=False,
        help='Wether to plot the sum of the weights of the first layer')
    outputsplots.add_argument('--LRP', action='store_true', required=False, default=False,
        help='Wether to plot Layer-Wise Relevance Propagation')
    outputsplots.add_argument('--derivative', action='store_true', required=False, default=False,
        help='Wether to plot derivative by varying the inputs')
    outputsplots.add_argument('--gradient', action='store_true', required=False, default=False,
        help='Wether to plot the gradient with Tensorflow')
    outputsplots.add_argument('--plotscores', action='store_true', required=False, default=False,
        help='Wether to plot the scores')

    opt = parser.parse_args()
    if opt.model == None and (opt.firstlayer or opt.LRP or opt.derivative):
        sys.exit("You need to specify a model for these options")

    #--- Logging ---#
    if opt.verbose:
        logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %H:%M:%S')
    else:
        logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %H:%M:%S')

    #--- Instantiation ---#
    instance = Analyze(N      = opt.number,
                       suffix = opt.suffix)
    if opt.model is not None:
        instance.loadModel(opt.model)

    if opt.correlationplot:
        instance.makeCorrelationMatrix()
    if opt.gridplot:
        instance.makeInputsGridPlot()

    if opt.correlation:
        instance.outputsCorrelation()
    if opt.mi:
        instance.outputsMutualInformation()
    if opt.firstlayer: 
        instance.extractFirstLayerWeights()
    if opt.derivative: 
        instance.differentiateNetwork()
    if opt.gradient:   
        instance.networkGradient()
    if opt.LRP: 
        instance.LRPAnalysis()

    # Save scores (and load entries that were already calculated) #
    instance.saveScores()
    if opt.plotscores:
        instance.plotScores()


