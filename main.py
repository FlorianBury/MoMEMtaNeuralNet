#!/usr/bin/env python

import os
import sys
import warnings

import argparse
import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


def get_options():
    """
    Parse and return the arguments provided by the user.
    """
    parser = argparse.ArgumentParser(description='Compare names of input and output files for matches and potentiel failed files')
    parser.add_argument('-s','--scan', action='store', required=False, type=str, default='',
        help='Name of the scan to be used (modify scan parameters in NeuralNet.py)')
    parser.add_argument('-n','--name', action='store', required=False, type=str, default='',
        help='Name of the model saved as zip file (without .zip)')

    opt = parser.parse_args()

    return opt

def main():
    #############################################################################################
    # Preparation #
    #############################################################################################
    # Get options from user #
    opt = get_options()

    # Private modules #
    #from NeuralNet import HyperScan, HyperReport, HyperEvaluate, HyperDeploy, HyperRestore
    from import_tree import LoopOverTrees, Tree2Numpy
    # Needed because PyROOT messes with argparse

    #############################################################################################
    # Data Input and preprocessing #
    #############################################################################################
    # Input path #
    print ('[INFO] Starting histograms input')

    path_to_files = '/nfs/scratch/fynu/fbury/MoMEMta_output/slurm/'
    variables = ['lep1_p4.Px()',
                 'lep1_p4.Py()',
                 'lep1_p4.Pz()',
                 'lep1_p4.E()',
                 'lep2_p4.Px()',
                 'lep2_p4.Py()',
                 'lep2_p4.Pz()',
                 'lep2_p4.E()',
                 'jet1_p4.Px()',
                 'jet1_p4.Py()',
                 'jet1_p4.Pz()',
                 'jet1_p4.E()',
                 'jet2_p4.Px()',
                 'jet2_p4.Py()',
                 'jet2_p4.Pz()',
                 'jet2_p4.E()',
                 'met_pt',
                 'met_phi',
                 'weight_DY',
                 'weight_TT']
    #data, weight = Tree2Numpy(input_file=path_to_files+'HToZATo2L2B_MH-1000_MA-200.root',variables=variables,weight='total_weight',reweight_to_cross_section=False)
    print ('[INFO] HToZA samples')
    data_HToZA, weight_HToZA = LoopOverTrees(input_dir=path_to_files,variables=variables,weight='total_weight',reweight_to_cross_section=False,part_name='HToZA',verbose=False)
    print ('HToZA sample size : {}'.format(data_HToZA.shape[0]))
    print ('[INFO] DY samples')
    data_DY, weight_DY = LoopOverTrees(input_dir=path_to_files,variables=variables,weight='total_weight',reweight_to_cross_section=True,part_name='DY',verbose=False)
    print ('DY sample size : {}'.format(data_DY.shape[0]))
    print ('[INFO] TT samples')
    data_TT, weight_TT = LoopOverTrees(input_dir=path_to_files,variables=variables,weight='total_weight',reweight_to_cross_section=True,part_name='TT',verbose=False)
    print ('TT sample size : {}'.format(data_TT.shape[0]))

    # Weight equalization #
    weight_HToZA = weight_HToZA/np.sum(weight_HToZA)
    weight_DY = weight_DY/np.sum(weight_DY)
    weight_TT = weight_TT/np.sum(weight_TT)
    if np.sum(weight_HToZA) != np.sum(weight_DY) or np.sum(weight_HToZA) != np.sum(weight_TT) or np.sum(weight_TT) != np.sum(weight_DY):
        print ('[WARNING] Sum of weights different between the samples')
        print ('\tHToZA : ',np.sum(weight_HToZA))
        print ('\tDY : ',np.sum(weight_DY))
        print ('\tTT : ',np.sum(weight_TT))

    # Preprocessing #
    print (-np.log10(data_DY[:,18:]))
    x_train_HToZA, x_test_HToZA, y_train_HToZA, y_test_HToZA, w_train_HToZA, w_test_HToZA = train_test_split(data_HToZA[:,:18],-np.log10(data_HToZA[:,18:]),weight_HToZA,test_size=0.3,shuffle=True)
    x_train_DY, x_test_DY, y_train_DY, y_test_DY, w_train_DY, w_test_DY = train_test_split(data_DY[:,:18],-np.log10(data_DY[:,18:]),weight_DY,test_size=0.3,shuffle=True)
    #x_train_TT, x_test_TT, y_train_TT, y_test_TT, w_train_TT, w_test_TT = train_test_split(data_TT[:,:18],-np.log10(data_TT[:,18:]),weight_TT,test_size=0.3,shuffle=True)

    all_train = np.concatenate((x_train_HToZA,x_train_DY),axis=0) # FIXME : add TT samples
    scaler = preprocessing.StandardScaler().fit(all_train)

    x_train_HToZA = scaler.transform(x_train_HToZA)
    x_test_HToZA = scaler.transform(x_test_HToZA)
    x_train_DY = scaler.transform(x_train_DY)
    x_test_DY = scaler.transform(x_test_DY)
   # x_train_TT = scaler.transform(x_train_TT)
   # x_test_TT = scaler.transform(x_test_TT)

    x_train = np.concatenate((x_train_HToZA,x_train_DY),axis=0) # FIXME : add TT samples 
    y_train = np.concatenate((y_train_HToZA,y_train_DY),axis=0) # FIXME : add TT samples 
    w_train = np.concatenate((w_train_HToZA,w_train_DY),axis=0) # FIXME : add TT samples 

    x_test = np.concatenate((x_test_HToZA,x_test_DY),axis=0) # FIXME : add TT samples 
    y_test = np.concatenate((y_test_HToZA,y_test_DY),axis=0) # FIXME : add TT samples 
    w_test = np.concatenate((w_test_HToZA,w_test_DY),axis=0) # FIXME : add TT samples 

    #############################################################################################
    # DNN #
    #############################################################################################
    if opt.scan != '':
        h = HyperScan(x_train)
        
    

   
if __name__ == "__main__":
    main()
