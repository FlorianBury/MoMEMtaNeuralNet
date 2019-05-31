import os
import sys
import re
import json
import glob
import logging
import copy
import numpy as np
import pandas as pd
import enlighten
from sklearn import metrics
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from root_numpy import array2root

sys.path.insert(0,"..") # We need our own version of talos
                        # If we import our modules after the version is sites-package, our version is ignored
from NeuralNet import HyperModel
from import_tree import Tree2Pandas
from cutWindow import massWindow
from signal_coupling import Repeater, Transposer
from Utils import ListBranches

# PYPLOT STYLE # 
SMALL_SIZE = 10
MEDIUM_SIZE = 20 
BIGGER_SIZE = 24
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes 
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels 
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels 
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title


#################################################################################################
# ProcessDNN #
#################################################################################################
class ProcessDNN:
    def __init__(self,model_name,list_inputs,label,list_files,variables,cuts=None,save_path=None,force=False):
        self.label = label              # For printing purposes
        self.model_name = model_name    
        # Name of the DNN model (same with disctinction for categories : 
        #       model_+ [DY,TT,HToZA,class]
        self.list_inputs = list_inputs  # inputs of the DNN
        self.list_files = list_files    # List of files to apply the DNN and ellipse later
        self.variables = variables      # Variables to be extracted from tree
        self.cuts = cuts                # Cuts to apply
        self.save_path = save_path      # Wether to look for a save
        self.force = force              # Wether to force the processing and erase the save

        print ('Extracting data for %s sample'%self.label)
        # Check if save exists #
        if force: print ('Careful, will replace the save')
        save_exists = False if force else os.path.exists(self.save_path) 
            
        # Process #
        if save_exists:
            self._recoverFromROOT()
        else:
            self._getData()
            self._produceWeights()
            self._produceProbabilities()
            self._saveAsROOT()

    def _getData(self):
        data = []
        manager = enlighten.get_manager()
        pbar = manager.counter(total=len(self.list_files), desc='Progress', unit='File')
        for f in self.list_files:
            df = Tree2Pandas(input_file = f, 
                             variables = self.variables, 
                             cut = self.cuts,
                             reweight_to_cross_section=True, 
                             n = 1000000,
                             tree_name='t')
            data.append(df)
            pbar.update()
        manager.stop()
        self.data = pd.concat(data, axis=0)
        self.size = self.data.shape[0]
        print ('Sample size : %d'%(self.size))
 
    def _produceWeights(self):
        """
        Careful, weights will be in -log10 !
        """
        print ('Producing weights for %s sample'%self.label)
        # Initialize DNN model #
        model_DY = HyperModel(self.model_name,'DY')
        model_TT = HyperModel(self.model_name,'TT')
        model_HToZA = HyperModel(self.model_name,'HToZA')

        inputs = self.data[self.list_inputs].values
        # Background weights #
        weight_DY = model_DY.HyperRestore(inputs,batch_size=512,verbose=1)
        print ('...... DY weights done')
        weight_TT = model_TT.HyperRestore(inputs,batch_size=512,verbose=1)
        print ('...... TT weights done')
        self.weight_names = ['weight_DY','weight_TT']

        # Signal weights #
        masses = np.array([[200,50],
                           [200,100],
                           [250,50],
                           [250,100],
                           [300,50],
                           [300,100],
                           [300,200],
                           [500,50],
                           [500,100],
                           [500,200],
                           [500,300],
                           [500,400],
                           [650,50],
                           [800,50],
                           [800,100],
                           [800,200],
                           [800,400],
                           [800,700],
                           [1000,50],
                           [1000,200],
                           [1000,500],
                           [2000,1000],
                           [3000,2000]
                          ])
        self.weight_names.extend(['weight_HToZA_mH_%d_mA_%d'%(masses[i,0],masses[i,1]) for i in range(masses.shape[0])])
        print ('...... Decoupling signal inputs')
        inputs = Repeater(inputs,masses.shape[0])
        inputs = np.c_[inputs,np.tile(masses,(self.size,1))]
        print ('...... Processing signal inputs')
        weight_HToZA = model_HToZA.HyperRestore(inputs,batch_size=512,verbose=1)
        print ('...... Recoupling signal inputs')
        weight_HToZA = Transposer(weight_HToZA,masses.shape[0])
        print ('...... HToZA weights done')

        # Make into DF #
        weights = np.c_[weight_DY,weight_TT,weight_HToZA]
        weights = pd.DataFrame(weights)
        weights.columns = self.weight_names
        weights = weights.reset_index(drop=True)
        self.data = self.data.reset_index(drop=True)
        self.data = pd.concat([self.data,weights],axis=1)
        del inputs
        del weights
        print ('...... Concatenation done')

    def _produceProbabilities(self):
        print ('Producing probabilities for %s sample'%self.label)
        # Initialize DNN model #
        model_class = HyperModel(self.model_name,'class')
        # Get probs #
        probs = model_class.HyperRestore(self.data[self.weight_names].values,batch_size=512,verbose=1)
        print ('...... Classification probabilities done')
        # Save in DF #
        self.prob_names = ['Prob_DY','Prob_HToZA','Prob_TT']
        probs = pd.DataFrame(probs)
        probs.columns = self.prob_names
        self.data = pd.concat([self.data,probs],axis=1)
        print ('...... Concatenation done')
        del probs

    def _saveAsROOT(self):
        output = self.data.to_records(index=False,column_dtypes='float64')
        output.dtype.names = [(name.replace('.','_').replace('(','').replace(')','').replace('-','_minus_').replace('*','_times_')) for name in output.dtype.names] # root_numpy issues
        array2root(output,self.save_path,mode='recreate') 
        print('Output saved as : '+self.save_path)

    def _recoverFromROOT(self):
        list_variables = ListBranches(self.save_path)
        self.data = Tree2Pandas(input_file=self.save_path,variables=list_variables)
        self.size = self.data.shape[0]
        print ('Output recovered from : '+self.save_path)

       
#################################################################################################
# ProcessEllipse #
#################################################################################################
class ProcessEllipse:
    def __init__(self,inst_DY,inst_TT,inst_HToZA,path_json,mA,mH,sigmas,save_path,force=False):
        self.inst_DY = inst_DY          # Process DNN instance for DY sample
        self.inst_TT = inst_TT          # Process DNN instance for TT sample 
        self.inst_HToZA = inst_HToZA    # Process DNN instance for HToZA sample 
        self.list_inst = [self.inst_DY,self.inst_TT,self.inst_HToZA] # List of instances
        self.path_json = path_json                      # Path to get the ellipse config
        self.window = massWindow(self.path_json)        # 
        self.mA = mA
        self.mH = mH
        self.save_path = save_path      # Wether to look for a save
        self.force = force              # Wether to force the processing and erase the save

        print ('Beginning the ellipse computation')
        # Check if save exists #
        if force: print ('Careful, will replace the save')
        save_exists = False if force else os.path.exists(self.save_path) 
    
        self.sigmas = sigmas
        self.sigmas_columns = [('sigma_%0.1f'%s).replace('.','p') for s in self.sigmas]
        self.root_path = os.path.join('/home/ucl/cp3/fbury/scratch/MoMEMta_output/EllipsesOutput/',os.path.basename(self.inst_HToZA.list_files[0]))

        if save_exists:
            self._recoverFromROOT()
        else:
            self._getCenter()
            self._insideEllipses()
            self._makeTargets()
            self._concatenate()
            self._saveAsROOT()

    def _getCenter(self):
        with open(self.path_json) as json_file:
            data_json = json.load(json_file)
        center = ()
        for (mbb, mllbb, a, b, theta, mA, mH) in data_json:
            if mA == self.mA and mH == self.mH:
                self.center = (mbb,mllbb)
        if len(self.center)==0:
            sys.exit('Could not find mA = %0.2f and mH = %0.2f in config file'%(self.mA,self.mH))


    def _insideEllipses(self):
        for inst in self.list_inst:
            print ('Computing ellipses for %s sample'%inst.label)
            manager = enlighten.get_manager()
            pbar = manager.counter(total=len(self.sigmas)*inst.size, desc='Progress', unit='Events %s'%inst.label)
            for idx,sigma in enumerate(self.sigmas):
                print ('....... Counting ellipse with sigma = %0.1f'%sigma)
                inside = np.zeros(inst.size)
                for i in range(inst.size):
                    masspoint = inst.data.iloc[i,:][['jj_M','lljj_M']]
                    check = self.window.isInWindow(self.center,sigma,masspoint)
                    if check : inside[i] = 1
                    pbar.update()
                inside = pd.DataFrame(inside) 
                inside.columns = [self.sigmas_columns[idx]]
                inst.data = pd.concat([inst.data,inside],axis=1)
            manager.stop()

    def _makeTargets(self):
        self.inst_DY.data = pd.concat([self.inst_DY.data,pd.DataFrame(np.zeros(self.inst_DY.size),columns=['target'])],axis=1) 
        self.inst_TT.data = pd.concat([self.inst_TT.data,pd.DataFrame(np.zeros(self.inst_TT.size),columns=['target'])],axis=1) 
        self.inst_HToZA.data = pd.concat([self.inst_HToZA.data,pd.DataFrame(np.ones(self.inst_HToZA.size),columns=['target'])],axis=1) 

    def _concatenate(self):
        df = []
        for inst in self.list_inst:
            df.append(inst.data)
        df = pd.concat(df,axis=0)
        self.data = df
        del df
       

    def _saveAsROOT(self):
        output = self.data.to_records(index=False,column_dtypes='float64')
        output.dtype.names = [(name.replace('.','_').replace('(','').replace(')','').replace('-','_minus_').replace('*','_times_')) for name in output.dtype.names] # root_numpy issues
        array2root(output,self.root_path,mode='recreate') 
        print('Output saved as : '+self.root_path)
    def _recoverFromROOT(self):
        selection = self.sigmas_columns + ['Prob_HToZA','target'] # TODO remove later
        list_variables = ListBranches(self.save_path)
        #self.data = Tree2Pandas(input_file=self.root_path,variables=list_variables)
        self.data = Tree2Pandas(input_file=self.root_path,variables=selection)
        print ('Output recovered from : '+self.root_path)
        

#################################################################################################
# ProcessROC#
#################################################################################################
class ProcessROC:
    def __init__(self,inst_ellipse):
        self.inst_ellipse = inst_ellipse
        self.path_ROC = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/Ellipses/ROC/'

        self._getFPRAndTPR()
        self._makeROC()


    def _getFPRAndTPR(self):
        selection = self.inst_ellipse.sigmas_columns + ['Prob_HToZA','target'] #TODO : weight

        self.scores = {}
        # Loop over the ellipses #
        print ('Process the ellipse with the DNN')
        for i in range(len(self.inst_ellipse.sigmas)):
            print ('....... Processing ellipse with sigma = %0.1f'%self.inst_ellipse.sigmas[i])
            #Select subDF #
            df = copy.deepcopy(self.inst_ellipse.data[selection])

            # Get ellipses FPR and TPR #
            idx_ell_in = df[self.inst_ellipse.sigmas_columns[i]]==1
            idx_ell_out = np.invert(idx_ell_in)
            tp_ell = np.sum(np.logical_and(idx_ell_in,df['target']==1)*1)
            tn_ell = np.sum(np.logical_and(idx_ell_out,df['target']==0)*1)
            fp_ell = np.sum(np.logical_and(idx_ell_in,df['target']==0)*1)
            fn_ell = np.sum(np.logical_and(idx_ell_out,df['target']==1)*1)
            tpr_ell = tp_ell/(tp_ell+fn_ell)
            fpr_ell = fp_ell/(fp_ell+tn_ell)

            # loop over DNN cuts #
            cuts = np.linspace(0,1,1000)
            tpr = []
            fpr = []
            for c in range(cuts.shape[0]):
                # What is in or out #
                idx_in = np.logical_and(df['Prob_HToZA']>cuts[c],idx_ell_in)
                idx_out = np.invert(idx_in) 
                
                # Get the FPR and TPr #
                tp = np.sum(np.logical_and(idx_in,df['target']==1)*1)
                tn = np.sum(np.logical_and(idx_out,df['target']==0)*1)
                fp = np.sum(np.logical_and(idx_in,df['target']==0)*1)
                fn = np.sum(np.logical_and(idx_out,df['target']==1)*1)
                tpr.append(tp/(tp+fn))
                fpr.append(fp/(fp+tn))

            self.scores[(self.inst_ellipse.sigmas[i],tpr_ell,fpr_ell)] = np.c_[tpr,fpr]
            del df


    def _makeROC(self):
        # Make figure #
        fig = plt.figure(figsize=(9,7))
        color= iter(cm.rainbow(np.linspace(0,1,len(self.scores))))
        print ('Starting the ROC section')
        # Get the roc curve for ellipses #
        list_tpr_ell = [e[1] for e in self.scores.keys()]
        list_fpr_ell = [e[2] for e in self.scores.keys()]
        # Loop over ellipses #
        for key,val in self.scores.items():
            # Unpack 
            sigma, tpr_ell, fpr_ell = key
            tpr = val[:,0]
            fpr = val[:,1]
            print ('....... Processing sigma %0.1f'%sigma)
            # plot #
            c = next(color)
            plt.plot(tpr,fpr,color=c,label='Ellipse + DNN')
            plt.scatter(tpr_ell,fpr_ell,marker='X',s=100,color=c,label='Ellipse WP : %0.1f sigmas'%sigma)
        plt.plot(list_tpr_ell,list_fpr_ell,color='k',label='Ellipse ROC curve')
        plt.legend(loc='lower right',ncol=2)
        plt.yscale('symlog', linthreshy=0.00001)
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.xlabel('Signal selection efficiency')
        plt.ylabel('Background selection efficiency')
        plt.suptitle('ROC curve MH = %0.2f GeV MA = %0.2f GeV'%(self.inst_ellipse.mH,self.inst_ellipse.mA))
        plt.grid(b=True,which='both',axis='both')
        roc_name = os.path.join(self.path_ROC,('ROC_mH_%0.2f_mA_%0.2f'%(self.inst_ellipse.mH,self.inst_ellipse.mA)).replace('.','p')+'.png')
        fig.savefig(roc_name)
        print ('ROC curve saved as %s'%roc_name)
     
