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

sys.path.insert(0,"..") # We need our own version of talos
                        # If we import our modules after the version is sites-package, our version is ignored
from NeuralNet import HyperModel
from import_tree import Tree2Pandas
from cutWindow import massWindow
from signal_coupling import Repeater, Transposer

#from ROOT import TFile, TH1F, TH2F, TCanvas, gROOT, TGraph2D, gPad, TObject
#
#gROOT.SetBatch(True)
#ROOT.gErrorIgnoreLevel = 2000#[ROOT.kPrint, ROOT.kInfo]#, kWarning, kError, kBreak, kSysError, kFatal;

##################################################################################################
# Sample #
##################################################################################################
class Sample:
    def __init__(self,model_name,list_inputs,label,list_files,variables,cuts=None):
        self.label = label
        self.model_name = model_name
        self.list_inputs = list_inputs
        self.label = label
        self.list_files = list_files
        self.variables = variables
        self.cuts = cuts

        # Process #
        self._getData()
        self._produceWeights()
        self._produceProbabilities()

    def _getData(self):
        print ('Extracting data for %s'%self.label)
        data = []
        manager = enlighten.get_manager()
        pbar = manager.counter(total=len(self.list_files), desc='Progress', unit='File')
        for f in self.list_files:
            df = Tree2Pandas(input_file = f, 
                             variables = self.variables, 
                             cut = self.cuts,
                             reweight_to_cross_section=True, 
                             tree_name='t') 
            data.append(df)
            break
            pbar.update()
        manager.stop()
        self.data = pd.concat(data, axis=0)
        self.size = self.data.shape[0]
        print ('Sample size : %d'%(self.size))
 
    def _produceWeights(self):
        """
        Careful, weights will be in -log10 !
        """
        # Initialize DNN model #
        model_DY = HyperModel(self.model_name,'DY')
        model_TT = HyperModel(self.model_name,'TT')
        model_HToZA = HyperModel(self.model_name,'HToZA')

        inputs = self.data[self.list_inputs].values
        # Background weights #
        weight_DY = model_DY.HyperRestore(inputs)
        weight_TT = model_TT.HyperRestore(inputs)
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
                                
        inputs = Repeater(inputs,masses.shape[0])
        inputs = np.c_[inputs,np.tile(masses,(self.size,1))]
        weight_HToZA = model_HToZA.HyperRestore(inputs)
        weight_HToZA = Transposer(weight_HToZA,masses.shape[0])

        # Make into DF #
        weights = np.c_[weight_DY,weight_TT,weight_HToZA]
        weights = pd.DataFrame(weights)
        weights.columns = self.weight_names
        self.data = pd.concat([self.data,weights],axis=1)
        del inputs
        del weights

    def _produceProbabilities(self):
        # Initialize DNN model #
        model_class = HyperModel(self.model_name,'class')
        # Get probs #
        probs = model_class.HyperRestore(self.data[self.weight_names].values)
        # Save in DF #
        self.prob_names = ['Prob_DY','Prob_HToZA','Prob_TT']
        probs = pd.DataFrame(probs)
        probs.columns = self.prob_names
        self.data = pd.concat([self.data,probs],axis=1)
        del probs
       
##################################################################################################
# Ellipse #
##################################################################################################
class Ellipse:
    def __init__(self,inst_DY,inst_TT,inst_HToZA,path_json,mA,mH):
        self.inst_DY = inst_DY
        self.inst_TT = inst_TT
        self.inst_HToZA = inst_HToZA
        self.path_json = path_json
        self.window = massWindow(self.path_json)
        self.mA = mA
        self.mH = mH
    
        self.sigmas = [0.1,0.5,1,1.5,2,2.5,3,3.5,4]
        self.tpr = [0]*len(self.sigmas) # signal interpreted as signal
        self.fpr = [0]*len(self.sigmas) # background interpreted as signal
        self.tnr = [0]*len(self.sigmas) # background interpreted as background
        self.fnr = [0]*len(self.sigmas) # signal interpreted as background

        self._getCenter()
        self._ellipseROC()

    def _ellipseROC(self):
        manager = enlighten.get_manager()
        pbar = manager.counter(total=len(self.sigmas)*self.inst_DY.size, desc='Progress', unit='Events')
        for idx,sigma in enumerate(self.sigmas):
            print ('Counting ellipse with sigma = %0.1f'%sigma)
            for i in range(self.inst_DY.size):
                #masspoint = (self.inst_DY.data.iloc['jj_M'],self.inst_DY.data['lljj_M'])
                masspoint = self.inst_DY.data.iloc[i,:][['jj_M','lljj_M']]
                check = self.window.isInWindow(self.center,sigma,masspoint)
                self.fpr[idx] += int(check == True)
                self.tnr[idx] += int(check == False)
                pbar.update()


            self.tpr[idx] /= self.inst_DY.size
            self.fpr[idx] /= self.inst_DY.size
            self.tnr[idx] /= self.inst_DY.size
            self.fnr[idx] /= self.inst_DY.size
            print ('\ttpr = %0.5f / fpr = %0.5f / tnr = %0.5f / fnr = %0.5f '%(self.tpr[idx],self.fpr[idx],self.tnr[idx],self.fnr[idx]))
        manager.stop()
        sys.exit()


    def _getCenter(self):
        with open(self.path_json) as json_file:
            data_json = json.load(json_file)
        center = ()
        for (mbb, mllbb, a, b, theta, mA, mH) in data_json:
            if mA == self.mA and mH == self.mH:
                self.center = (mbb,mllbb)
        if len(self.center)==0:
            sys.exit('Could not find mA = %0.2f and mH = %0.2f in config file'%(self.mA,self.mH))



        

