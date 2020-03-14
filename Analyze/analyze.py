import os
import sys
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns
import argparse
import parse
from collections import OrderedDict 

from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression
from scipy.stats import pearsonr

sys.path.append(os.path.abspath('..'))
import parameters


class Analyze:
    def __init__(self,N,suffix,model=None):
        self.inputs     = parameters.inputs
        self.outputs    = parameters.outputs
        self.path_files = parameters.path_gen_output
        self.path_out   = os.path.abspath(".")
        self.N          = N
        self.suffix     = suffix
        self.model      = model
        self.scores     = pd.DataFrame(columns=self.inputs)

        self.makeVarNames()
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
                    if 'Pt' in inp: 
                        self.inputs_names[inp] = r"$P_{T}(%s)$"%part
                    elif 'Eta' in inp: 
                        self.inputs_names[inp] = r"$\eta(%s)$"%part
                    elif 'Phi' in inp: 
                        self.inputs_names[inp] = r"$\phi(%s)$"%part
                elif len(part)==2:
                    if 'Pt' in inp: 
                        self.inputs_names[inp] = r"$\Delta P_{T}(%s,%s)$"%(part[0],part[1])
                    elif 'Eta' in inp: 
                        self.inputs_names[inp] = r"$\Delta \eta(%s,%s)$"%(part[0],part[1])
                    elif 'Phi' in inp: 
                        self.inputs_names[inp] = r"$\Delta \phi(%s,%s)$"%(part[0],part[1])

    def getDF(self):
        from import_tree import LoopOverTrees
        df = LoopOverTrees(input_dir  = self.path_files,
                           variables = self.inputs+self.outputs,
                           n         = self.N)
        self.df_inputs = df[self.inputs]
        self.df_outputs = df[self.outputs]
        del df
        logging.info("Number of events in sample : %d"%(self.df_inputs.shape[0]))
        logging.info("Number of input variables  : %d"%(self.df_inputs.shape[1]))
        logging.info("Number of output variables : %d"%(self.df_outputs.shape[1]))

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
        scores = []
        for inp in self.inputs:
            r = pearsonr(self.df_inputs[inp].values,self.df_outputs.values.ravel()) 
            scores.append(r[0])
        new_row = pd.DataFrame(np.array(scores).reshape(1,-1),columns=self.scores.columns,index=["Pearson correlation"])
        self.scores = self.scores.append(new_row,verify_integrity=True)

    def outputsMutualInformation(self):
        scores = []
        for inp in self.inputs:
            r = mutual_info_regression(self.df_inputs[inp].values.reshape(-1,1),self.df_outputs.values.ravel())
            scores.append(r[0])
        new_row = pd.DataFrame(np.array(scores).reshape(1,-1),columns=self.scores.columns,index=["Mutual information"])
        self.scores = self.scores.append(new_row,verify_integrity=True)

    def extractFirstLayerWeights(self):
        import h5py
        f = h5py.File(self.model,'r')
        weights = f['dense_1']['dense_1_1']['kernel:0'][()]
        avg_sum_weights = np.sum(np.absolute(weights),axis=1)/weights.shape[1]
        new_row = pd.DataFrame(avg_sum_weights.reshape(1,-1),columns=self.scores.columns,index=['First layer weights averaged sum'])
        self.scores = self.scores.append(new_row,verify_integrity=True)

    def plotScores(self):
        # Calling basic score functions #
        logging.info("Processing correlation")
        self.outputsCorrelation()
        logging.info("Processing mutual information")
        self.outputsMutualInformation()
        logging.info("Starting the score plot")


        # Plotting options  #
        fig, ax = plt.subplots(self.scores.shape[0],figsize=(18,18))
        fig.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.1,hspace=0.4)
        width = 0.3
        bins = np.arange(self.scores.shape[1])
        labels = []
        for col in self.scores.columns:
            labels.append(self.inputs_names[col])

        # Plot the different scors #
        for i,(index, row) in enumerate(self.scores.iterrows()): # Index is title, row is data
            ax[i].bar(bins,row,tick_label=labels)
            ax[i].set_xticklabels(labels,rotation='vertical')
            ax[i].set_title(index,fontsize=20)

        name = os.path.join(self.path_out,'scores_%s.png'%self.suffix)
        plt.savefig(name)
        logging.info("... saved as %s"%name)



if __name__ == '__main__':
    #--- Argparse ---#
    parser = argparse.ArgumentParser(description='Analyzer : variables and/or network')
    parser.add_argument('-n','--number', action='store', required=True, type=int,
        help='Number of events max per file')
    parser.add_argument('--suffix', action='store', required=False, type=str, default = '',
        help='Suffix for the png plots (default is "")')
    parser.add_argument('-v','--verbose', action='store_true', required=False, default=False,
        help='Verbose mode')
    inputsplots = parser.add_argument_group('Make plots about the inputs alone')
    inputsplots.add_argument('-c','--correlation', action='store_true', required=False, default=False,
        help='Wether to plot the correlation matrix')
    inputsplots.add_argument('-g','--gridplot', action='store_true', required=False, default=False,
        help='Wether to plot input grid')
    outputsplots = parser.add_argument_group('Make plots about the inputs with respect to the output')
    outputsplots.add_argument('-s','--scoreplot', action='store_true', required=False, default=False,
        help='Wether to plot the scores')
    outputsplots.add_argument('-m','--model', action='store', required=False, default=None, type=str,
        help='Model name, required for the arguments looking at the network')
    outputsplots.add_argument('--firstlayer', action='store_true', required=False, default=False,
        help='Wether to plot the sum of the weights of the first layer')
    outputsplots.add_argument('--LRP', action='store_true', required=False, default=False,
        help='Wether to plot Layer-Wise Relevance Propagation')
    outputsplots.add_argument('--derivative', action='store_true', required=False, default=False,
        help='Wether to plot derivative')

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
                       suffix = opt.suffix,
                       model  = opt.model)
    if opt.correlation:
        instance.makeCorrelationMatrix()
    if opt.gridplot:
        instance.makeInputsGridPlot()
    if opt.firstlayer: # Needs to be before plotScores()
        instance.extractFirstLayerWeights()
    if opt.scoreplot:
        instance.plotScores()


# f['dense_1']['dense_1_1']['kernel:0'].value
# np.sum(np.absolue(a),axis=1)/200

