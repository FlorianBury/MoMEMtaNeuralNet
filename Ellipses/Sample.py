import os
import sys
import re
import argparse
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
from signal_coupling import Repeater, Decoupler, Recoupler

#from ROOT import TFile, TH1F, TH2F, TCanvas, gROOT, TGraph2D, gPad, TObject
#
#gROOT.SetBatch(True)
#ROOT.gErrorIgnoreLevel = 2000#[ROOT.kPrint, ROOT.kInfo]#, kWarning, kError, kBreak, kSysError, kFatal;

class Sample:
    def __init__(self,label):
        self.label = label

    def GetData(self,list_files,variables,cuts=None):
        print ('Extracting data for %s'%self.label)
        data = []
        manager = enlighten.get_manager()
        pbar = manager.counter(total=len(list_files), desc='Progress', unit='File')
        for f in list_files:
            df = Tree2Pandas(input_file = f, 
                             variables = variables, 
                             cut = cuts,
                             reweight_to_cross_section=True, 
                             tree_name='t') 
            data.append(df)
            break
            pbar.update()
        manager.stop()
        self.data = pd.concat(data, axis=0)
        self.size = self.data.shape[0]
        print ('Sample size : %d'%(self.size))

    def InitializeEllipses(self,path_json):
        ellipse = massWindow(path_json)
    
    def ProduceWeights(self,model,list_inputs,list_signal_outputs):
        model_DY = HyperModel(model,'DY')
        model_TT = HyperModel(model,'TT')
        model_HToZA = HyperModel(model,'HToZA')

        inputs = self.data[list_inputs].values
        print (inputs)
        print (inputs.shape)
        # Background weights #
        weight_DY = model_DY.HyperRestore(inputs)
        weight_TT = model_TT.HyperRestore(inputs)

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
                                
        inputs = Repeater(inputs,masses.shape[0])
        inputs = np.c_[inputs,np.tile(masses,(self.size,1))]



        del inputs



