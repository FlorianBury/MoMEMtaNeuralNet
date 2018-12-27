#!/usr/bin/env python

import os
import sys
import logging

import argparse
import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split


import matplotlib.pyplot as plt

# Personal files #
from submit_on_slurm import submit_on_slurm
from generate_mask import GenerateMask
from split_training import DictSplit
import parameters


def get_options():
    """
    Parse and return the arguments provided by the user.
    """
    parser = argparse.ArgumentParser(description='Compare names of input and output files for matches and potentiel failed files')
    parser.add_argument('-s','--scan', action='store', required=False, type=str, default='',
        help='Name of the scan to be used (modify scan parameters in NeuralNet.py)')
    parser.add_argument('-split','--split', action='store', required=False, type=int, default=0,
        help='Number of parameter sets per jobs to be used for splitted training for slurm submission')
    parser.add_argument('-submit','--submit', action='store', required=False, default='', type=str,
        help='Wether to submit on slurm and nname for the save (must have specified --split)')
    parser.add_argument('-task','--task', action='store', required=False, type=str, default='',
        help='Name of dict to be used for scan (ONLY used by submit_on_slurm.py or debug)')
    parser.add_argument('-dy','--DY', action='store_true', required=False, default=False,
        help='Use DY MEM weights (must be specified if --scan or --report or --output are used')
    parser.add_argument('-tt','--TT', action='store_true', required=False, default=False,
        help='Use TT MEM weights (must be specified if --scan or --report or --output are used')
    parser.add_argument('-r','--report', action='store', required=False, type=str, default='',
        help='Name of the csv file for the reporting (without .csv)')
    parser.add_argument('-o','--output', action='store', required=False, type=str, default='',                                                                                                          
        help='Applies the provided model name (without .zip and type, aka DY or TT) on test set and outputs root trees') 
    opt = parser.parse_args()

    if opt.scan!='' or opt.report!='' or opt.output!='':
        if not opt.DY and not opt.TT:
            logging.critical('Either -dy or -tt must be specified')  
            sys.exit(1)
        if opt.split!=0 or opt.submit:
            logging.critical('These parameters cannot be used together')  
            sys.exit(1)
    if opt.submit and opt.split==0:
        logging.critical('You forgot to specify --split')
        sys.exit(1)

    return opt

def main():
    #############################################################################################
    # Preparation #
    #############################################################################################
    # Logging #
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Get options from user #
    opt = get_options()

    # Private modules # TODO : move the out 
    from NeuralNet import HyperScan, HyperReport, HyperEvaluate, HyperDeploy, HyperRestore
    from import_tree import LoopOverTrees, Tree2Numpy
    from root_numpy import array2root
    # Needed because PyROOT messes with argparse

    main_path = parameters.main_path
    path_to_files = parameters.path_to_files
    path_out = parameters.path_out

    #############################################################################################
    # Splitting into sub-dicts and slurm submission #
    #############################################################################################
    if opt.split!=0:
        DictSplit(opt.split,opt.submit)
        
        logging.info('Splitting jobs done')

        if opt.submit!='':
            logging.info('Submitting jobs')
            submit_on_slurm(name=opt.submit)
        sys.exit()

    #############################################################################################
    # Data Input and preprocessing #
    #############################################################################################
    # Input path #
    logging.info('Starting histograms input')

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
    logging.info('HToZA samples')
    data_HToZA, weight_HToZA = LoopOverTrees(input_dir=path_to_files,variables=variables,weight='total_weight',reweight_to_cross_section=False,part_name='HToZA')
    logging.info('HToZA sample size : {}'.format(data_HToZA.shape[0]))
    logging.info('DY samples')
    data_DY, weight_DY = LoopOverTrees(input_dir=path_to_files,variables=variables,weight='total_weight',reweight_to_cross_section=True,part_name='DY')
    logging.info('DY sample size : {}'.format(data_DY.shape[0]))
    logging.info('TT samples')
    data_TT, weight_TT = LoopOverTrees(input_dir=path_to_files,variables=variables,weight='total_weight',reweight_to_cross_section=True,part_name='TT',n=500000)
    logging.info('TT sample size : {}'.format(data_TT.shape[0]))

    # Weight equalization #
    weight_HToZA = weight_HToZA/np.sum(weight_HToZA)*1000
    weight_DY = weight_DY/np.sum(weight_DY)*10000
    weight_TT = weight_TT/np.sum(weight_TT)*10000
    if np.sum(weight_HToZA) != np.sum(weight_DY) or np.sum(weight_HToZA) != np.sum(weight_TT) or np.sum(weight_TT) != np.sum(weight_DY):
        logging.warning ('Sum of weights different between the samples')
        logging.warning('\tHToZA : '+str(np.sum(weight_HToZA)))
        logging.warning('\tDY : '+str(np.sum(weight_DY)))
        logging.warning('\tTT : '+str(np.sum(weight_TT)))

    # Preprocessing #
    mask_HToZA = GenerateMask(data_HToZA.shape[0],'HToZA')
    mask_DY = GenerateMask(data_DY.shape[0],'DY')
    mask_TT = GenerateMask(data_TT.shape[0],'TT')
       # Needs to keep the same testing set for the evaluation of model that was selected earlier
    x_train_HToZA = data_HToZA[mask_HToZA==True,:18]
    x_train_DY = data_DY[mask_DY==True,:18]
    x_train_TT = data_TT[mask_TT==True,:18]
    x_test_HToZA = data_HToZA[mask_HToZA==False,:18]
    x_test_DY = data_DY[mask_DY==False,:18]
    x_test_TT = data_TT[mask_TT==False,:18]

    y_train_HToZA = -np.log10(data_HToZA[mask_HToZA==True,18:])
    y_train_DY = -np.log10(data_DY[mask_DY==True,18:])
    y_train_TT = -np.log10(data_TT[mask_TT==True,18:])
    y_test_HToZA = -np.log10(data_HToZA[mask_HToZA==False,18:])
    y_test_DY = -np.log10(data_DY[mask_DY==False,18:])
    y_test_TT = -np.log10(data_TT[mask_TT==False,18:])

    w_train_HToZA = weight_HToZA[mask_HToZA==True]
    w_train_DY = weight_DY[mask_DY==True]
    w_train_TT = weight_TT[mask_TT==True]
    w_test_HToZA = weight_HToZA[mask_HToZA==False]
    w_test_DY = weight_DY[mask_DY==False]
    w_test_TT = weight_TT[mask_TT==False]
   
    #x_train_HToZA, x_test_HToZA, y_train_HToZA, y_test_HToZA, w_train_HToZA, w_test_HToZA = train_test_split(data_HToZA[:,:18],-np.log10(data_HToZA[:,18:]),weight_HToZA,test_size=0.3,shuffle=True)
    #x_train_DY, x_test_DY, y_train_DY, y_test_DY, w_train_DY, w_test_DY = train_test_split(data_DY[:,:18],-np.log10(data_DY[:,18:]),weight_DY,test_size=0.3,shuffle=True)
    #x_train_TT, x_test_TT, y_train_TT, y_test_TT, w_train_TT, w_test_TT = train_test_split(data_TT[:,:18],-np.log10(data_TT[:,18:]),weight_TT,test_size=0.3,shuffle=True)

    # y -> [weight_DY, weight_TT]

    #all_train = np.concatenate((x_train_HToZA,x_train_DY,x_train_TT),axis=0)
    all_train = np.concatenate((x_train_HToZA,x_train_DY),axis=0)
    scaler = preprocessing.StandardScaler().fit(all_train)

    x_train_HToZA = scaler.transform(x_train_HToZA)
    x_test_HToZA = scaler.transform(x_test_HToZA)
    x_train_DY = scaler.transform(x_train_DY)
    x_test_DY = scaler.transform(x_test_DY)
    x_train_TT = scaler.transform(x_train_TT)
    x_test_TT = scaler.transform(x_test_TT)

    # Concatenation #

    x_train = np.concatenate((x_train_HToZA,x_train_DY,x_train_TT),axis=0)
    y_train = np.concatenate((y_train_HToZA,y_train_DY,y_train_TT),axis=0)
    w_train = np.concatenate((w_train_HToZA,w_train_DY,w_train_TT),axis=0)

    x_test = np.concatenate((x_test_HToZA,x_test_DY,x_test_TT),axis=0) 
    y_test = np.concatenate((y_test_HToZA,y_test_DY,y_test_TT),axis=0) 
    w_test = np.concatenate((w_test_HToZA,w_test_DY,w_test_TT),axis=0) 

    # Randomization (not show input from same sample in one batch) #

    random_train = np.arange(0,x_train.shape[0]) # needed to randomize x,y and w in same fashion
    random_test =np.arange(0,x_test.shape[0])
    np.random.shuffle(random_train)
    np.random.shuffle(random_test)
    
    x_train = x_train[random_train] 
    y_train = y_train[random_train] 
    w_train = w_train[random_train] 
    x_test = x_test[random_test] 
    y_test = y_test[random_test] 
    w_test = w_test[random_test] 

    #############################################################################################
    # DNN #
    #############################################################################################
        # Make path #
    path_model = os.path.join(main_path,'model')
    if not os.path.exists(path_model):
        os.mkdir(path_model)

    if opt.scan != '':
        # DY network #
        if opt.DY:
            logging.info('Starting scan DY case')
            h_DY, name_DY = HyperScan(x_train,np.c_[w_train,y_train[:,0]],name=opt.scan,sample='DY',task=opt.task)
            logging.info('Starting evaluation DY case')
            idx_DY = HyperEvaluate(h_DY,x_test,y_test[:,0],folds=5) 
            logging.info('Starting deployment TT case')
            HyperDeploy(h_DY,name_DY,-1)
            #HyperDeploy(h_DY,name_DY,idx_DY)
        # TT network #
        if opt.TT:
            logging.info('Starting scan TT case')
            h_TT, name_TT = HyperScan(x_train,np.c_[w_train,y_train[:,1]],name=opt.scan,sample='TT',task=opt.task)
            logging.info('Starting evaluation TT case')
            idx_TT = HyperEvaluate(h_TT,x_test,y_test[:,1],folds=5) 
            logging.info('Starting deployment TT case')
            HyperDeploy(h_TT,name_TT,-1)
            #HyperDeploy(h_TT,path_model+opt.scan+'_cross_val_TT',idx_TT)
        
    if opt.report != '':
        if opt.DY: 
            logging.info('Reporting DY case')
            HyperReport(path_model+opt.report+'_DY.csv')
        if opt.TT:
            logging.info('Reporting TT case')
            HyperReport(path_model+opt.report+'_TT.csv')

    if opt.output!='': 
        if opt.DY:
            logging.info('Restoring DY model')
            out_DY = HyperRestore(x_test,path_model+opt.output+'.zip')
        if opt.TT:
            logging.info('Restoring TT model')
            out_TT = HyperRestore(x_test,path_model+opt.output+'.zip')

        # de-preprocess, concatenate and dtype#
        inputs = x_test*scaler.scale_+scaler.mean_
        output = np.c_[inputs,w_test,y_test] # without NN output
        output.dtype = [('lep1_px','float64'),('lep1_py','float64'),('lep1_pz','float64'),('lep1_E','float64'),('lep2_px','float64'),('lep2_py','float64'),('lep2_pz','float64'),('lep2_E','float64'),('jet1_px','float64'),('jet1_py','float64'),('jet1_pz','float64'),('jet1_E','float64'),('jet2_px','float64'),('jet2_py','float64'),('jet2_pz','float64'),('jet2_E','float64'),('met_pt','float64'),('met_phi','float64'),('weight','float64'),('MEM_weight_DY','float64'),('MEM_weight_TT','float64')]
        if opt.DY:
            output = np.c_[output,out_DY]
            output.dtype = np.append(output.dtype,('output_DY','float64'))
        if opt.TT:
            output = np.c_[output,out_TT]
            output.dtype = np.append(output.dtype,('output_TT','float64'))

        output_name = os.path.join(path_out,opt.output,'output_'+opt.output)
        array2root(output,output_name,mode='recreate') 
        logging.info('Output saved as : '+output_name)

        
   
if __name__ == "__main__":
    main()
