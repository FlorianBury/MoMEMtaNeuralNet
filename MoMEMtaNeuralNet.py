#!/usr/bin/env python

import re
import glob
import csv
import os
import sys
import logging
import copy

import argparse
import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from keras.utils import to_categorical

import matplotlib.pyplot as plt

# Personal files #
from NeuralNet import HyperModel
from submit_on_slurm import submit_on_slurm
from generate_mask import GenerateMask
from split_training import DictSplit
from concatenate_csv import ConcatenateCSV
import parameters


def get_options():
    """
    Parse and return the arguments provided by the user.
    """
    parser = argparse.ArgumentParser(description='Compare names of input and output files for matches and potentiel failed files')

    # Scan, deploy and restore arguments #
    a = parser.add_argument_group('Scan, deploy and restore arguments')
    a.add_argument('-s','--scan', action='store', required=False, type=str, default='',
        help='Name of the scan to be used (modify scan parameters in NeuralNet.py)')
    a.add_argument('-task','--task', action='store', required=False, type=str, default='',
        help='Name of dict to be used for scan (Used by function itself when submitting jobs or DEBUG)')

    # Splitting and submitting jobs arguments #
    b = parser.add_argument_group('Splitting and submitting jobs arguments')
    b.add_argument('-split','--split', action='store', required=False, type=int, default=0,
        help='Number of parameter sets per jobs to be used for splitted training for slurm submission (if -1, will create a single subdict)')
    b.add_argument('-submit','--submit', action='store', required=False, default='', type=str,
        help='Wether to submit on slurm and name for the save (must have specified --split)')
    b.add_argument('-resubmit','--resubmit', action='store', required=False, default='', type=str,
        help='Wether to resubmit failed jobs given a specific path containing the jobs that succeded')
    b.add_argument('-debug','--debug', action='store_true', required=False, default=False,
        help='Debug mode of the slurm submission, does everything except submit the jobs')

    # Analyzing or producing outputs for given model (csv or zip file) #
    c = parser.add_argument_group('Analyzing or producing outputs for given model (csv or zip file)')
    c.add_argument('-r','--report', action='store', required=False, type=str, default='',
        help='Name of the csv file for the reporting (without .csv)')
    c.add_argument('-o','--output', action='store', required=False, type=str, default='',                                                                                                          
        help='Applies the provided model name (without .zip and type, aka DY or TT) on test set and outputs root trees \
             (no need for -tt or -dy, if the models are there it will find them)') 
    c.add_argument('-inv_dy','--invalid_DY', action='store_true', required=False, default=False,
        help='Wether to also apply the output to the invalid DY weights (must be used with --output)')
    c.add_argument('-inv_tt','--invalid_TT', action='store_true', required=False, default=False,
        help='Wether to also apply the output to the invalid TT weights (must be used with --output)')
    c.add_argument('-smear','--smear', action='store', required=False, default=0, type=float,
        help='Random gaussian variations (must provide the width, eg 0.1) to smear in the inputs')

    # Concatenating csv files arguments #
    d = parser.add_argument_group('Concatenating csv files arguments')
    d.add_argument('-csv','--csv', action='store', required=False, type=str, default='',                                                                                                          
        help='Wether to concatenate the csv files from different slurm jobs into a main one, \
              please provide the path to the csv files')

    # Additional arguments #
    e = parser.add_argument_group('Additional arguments')
    e.add_argument('-v','--verbose', action='store_true', required=False, default=False,
        help='Show DEGUG logging')

    opt = parser.parse_args()

    if opt.split!=0 or opt.submit:
        if opt.scan!='' or opt.report!='':
            logging.critical('These parameters cannot be used together')  
            sys.exit(1)
    if opt.submit and opt.split==0:
        logging.critical('You forgot to specify --split')
        sys.exit(1)
    if opt.split!=0 and (opt.report!='' or opt.output!='' or opt.csv!='' or opt.scan!=''):
        logging.warning('Since you have specified a split, all the other arguments will be skipped')
    if opt.csv!='' and (opt.report!='' or opt.output!='' or opt.scan!=''):
        logging.warning('Since you have specified a csv concatenation, all the other arguments will be skipped')
    if opt.report!='' and (opt.output!='' or opt.scan!=''):
        logging.warning('Since you have specified a scan report, all the other arguments will be skipped')
    if opt.output == '' and (opt.invalid_DY or opt.invalid_TT or opt.smear!=0):
        logging.critical('You must specify the model with --output')
        sys.exit(1)

    return opt

def main():
    #############################################################################################
    # Preparation #
    #############################################################################################
    # Get options from user #
    opt = get_options()

    # Logging #
    if opt.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    # Private modules containing Pyroot #
    from import_tree import LoopOverTrees, Tree2Numpy
    from root_numpy import array2root
    # Needed because PyROOT messes with argparse

    logging.info("="*88)
    logging.info("___  ___     ___  ___ ________  ____        _   _                      _ _   _      _   ")
    logging.info("|  \/  |     |  \/  ||  ___|  \/  | |      | \ | |                    | | \ | |    | | ") 
    logging.info("| .  . | ___ | .  . || |__ | .  . | |_ __ _|  \| | ___ _   _ _ __ __ _| |  \| | ___| |_ ")
    logging.info("| |\/| |/ _ \| |\/| ||  __|| |\/| | __/ _` | . ` |/ _ \ | | | '__/ _` | | . ` |/ _ \ __|")
    logging.info("| |  | | (_) | |  | || |___| |  | | || (_| | |\  |  __/ |_| | | | (_| | | |\  |  __/ |_ ")
    logging.info("\_|  |_/\___/\_|  |_/\____/\_|  |_/\__\__,_\_| \_/\___|\__,_|_|  \__,_|_\_| \_/\___|\__|")
    logging.info("="*88)

    main_path = parameters.main_path
    path_to_files = parameters.path_to_files
    path_out = parameters.path_out

    # Make path model #
    path_model = os.path.join(main_path,'model')
    if not os.path.exists(path_model):
        os.mkdir(path_model)

    #############################################################################################
    # Splitting into sub-dicts and slurm submission #
    #############################################################################################
    if opt.split!=0:
        DictSplit(opt.split,opt.submit,opt.resubmit)
        
        logging.info('Splitting jobs done')

        if opt.submit!='':
            logging.info('Submitting jobs')
            if opt.resubmit:
                submit_on_slurm(name=opt.submit+'_resubmit',debug=opt.debug)
            else:
                submit_on_slurm(name=opt.submit,debug=opt.debug)
        sys.exit()

    #############################################################################################
    # CSV concatenation #
    #############################################################################################
    if opt.csv!='':
        logging.info('Concatenating csv files from : %s'%(opt.csv))
        dict_DY = ConcatenateCSV(opt.csv)
        dict_TT = ConcatenateCSV(opt.csv)
        
        dict_DY.Concatenate()
        dict_DY.WriteToFile()

        dict_TT.Concatenate()
        dict_TT.WriteToFile()

        sys.exit()

    #############################################################################################
    # Reporting given scan in csv file #
    #############################################################################################
    if opt.report != '':
        if opt.DY: 
            instance = HyperModel(opt.report)
            instance.HyperReport()
        if opt.TT:
            instance = HyperModel(opt.report)
            instance.HyperReport()

        sys.exit()

    #############################################################################################
    # Data Input and preprocessing #
    #############################################################################################
    # Input path #
    logging.info('Starting input')

    # Import variables from parameters.py
    variables = parameters.inputs+parameters.other_variables
    NIn = len(parameters.inputs)
    NOther = len(parameters.other_variables)

    # Import arrays #
    logging.info('HToZA samples')
    data_HToZA, weight_HToZA = LoopOverTrees(input_dir=path_to_files,variables=variables,weight=parameters.weights[0],reweight_to_cross_section=False,part_name='HToZA')
    logging.info('HToZA sample size : {}'.format(data_HToZA.shape[0]))
    logging.info('DY samples')
    data_DY, weight_DY = LoopOverTrees(input_dir=path_to_files,variables=variables,weight=parameters.weights[0],reweight_to_cross_section=False,part_name='DY')
    logging.info('DY sample size : {}'.format(data_DY.shape[0]))
    logging.info('TT samples')
    data_TT, weight_TT = LoopOverTrees(input_dir=path_to_files,variables=variables,weight=parameters.weights[0],reweight_to_cross_section=False,part_name='TT')
    # Save weights in data #
    data_HToZA = np.append(data_HToZA,weight_HToZA,axis=1)
    data_DY = np.append(data_DY,weight_DY,axis=1)
    data_TT = np.append(data_TT,weight_TT,axis=1)
    NOther+=1

    # Weight equalization #
    weight_HToZA = weight_HToZA/np.sum(weight_HToZA)*10000 # because event_weight is not correct
    weight_DY = weight_DY/np.sum(weight_DY)*10000
    weight_TT = weight_TT/np.sum(weight_TT)*10000
    if np.sum(weight_HToZA) != np.sum(weight_DY) or np.sum(weight_HToZA) != np.sum(weight_TT) or np.sum(weight_TT) != np.sum(weight_DY):
        logging.warning ('Sum of weights different between the samples')
        logging.warning('\tHToZA : '+str(np.sum(weight_HToZA)))
        logging.warning('\tDY : '+str(np.sum(weight_DY)))
        logging.warning('\tTT : '+str(np.sum(weight_TT)))

    # Preprocessing #
    mask_HToZA = GenerateMask(data_HToZA.shape[0],'HToZA_classifier')
    mask_DY = GenerateMask(data_DY.shape[0],'DY_classifier')
    mask_TT = GenerateMask(data_TT.shape[0],'TT_classifier')
       # Needs to keep the same testing set for the evaluation of model that was selected earlier
    x_train_HToZA = -np.log10(data_HToZA[mask_HToZA==True,:NIn])
    x_train_DY = -np.log10(data_DY[mask_DY==True,:NIn])
    x_train_TT = -np.log10(data_TT[mask_TT==True,:NIn])
    x_test_HToZA = -np.log10(data_HToZA[mask_HToZA==False,:NIn])
    x_test_DY = -np.log10(data_DY[mask_DY==False,:NIn])
    x_test_TT = -np.log10(data_TT[mask_TT==False,:NIn])

    # Smearing #
    if opt.smear != 0:
        logging.warning('A gaussian smearing of std %0.2f has been applied'%opt.smear)
        x_train_HToZA = np.random.normal(x_train_HToZA,opt.smear)
        x_train_DY = np.random.normal(x_train_DY,opt.smear)
        x_train_TT = np.random.normal(x_train_TT,opt.smear)
        x_test_HToZA = np.random.normal(x_test_HToZA,opt.smear)
        x_test_DY = np.random.normal(x_test_DY,opt.smear)
        x_test_TT = np.random.normal(x_test_TT,opt.smear)


    # Define outputs #
    y_train_HToZA = np.zeros(x_train_HToZA.shape[0])
    y_train_DY = np.ones(x_train_DY.shape[0])
    y_train_TT = np.ones(x_train_TT.shape[0])*2
    y_test_HToZA = np.zeros(x_test_HToZA.shape[0])
    y_test_DY = np.ones(x_test_DY.shape[0])
    y_test_TT = np.ones(x_test_TT.shape[0])*2
         # output : 0 -> HToZA
         #          1 -> DY
         #          2 -> TT
         # Will categorize after
    # Variables outside training #
    z_test_HToZA = data_HToZA[mask_HToZA==False,NIn:NIn+NOther]
    z_test_DY = data_DY[mask_DY==False,NIn:NIn+NOther]
    z_test_TT = data_TT[mask_TT==False,NIn:NIn+NOther]
        # We don't need training because only test is used in output 
    
    # Learning weights #
    w_train_HToZA = weight_HToZA[mask_HToZA==True]
    w_train_DY = weight_DY[mask_DY==True]
    w_train_TT = weight_TT[mask_TT==True]
    w_test_HToZA = weight_HToZA[mask_HToZA==False]
    w_test_DY = weight_DY[mask_DY==False]
    w_test_TT = weight_TT[mask_TT==False]
        
    all_train = np.concatenate((x_train_HToZA,x_train_DY,x_train_TT),axis=0)
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

    # Categorization #
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

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

    if opt.scan != '':
        instance = HyperModel(opt.scan)
        instance.HyperScan(x_train,np.c_[w_train,y_train],task=opt.task)
        instance.HyperDeploy(best='eval_error')
        
    if opt.output!='': 
        # Make path #
        tmp_output = copy.copy(opt.output)
        if opt.smear != 0:
            tmp_output += '_smear_'+str(opt.smear)
        path_model_output = os.path.join(path_out,tmp_output)
        if not os.path.exists(path_model_output):
            os.makedirs(path_model_output)

        # Make basic dtype #
        dtype_base = parameters.make_dtype(parameters.inputs+parameters.other_variables+parameters.weights)

        # Get output, concatenate and make root file # 
        def produce_output(inputs,other,tag):
            # De-preprocess inputs #
            inputs_unscaled = inputs*scaler.scale_+scaler.mean_
            inputs_base = np.power(10,-inputs_unscaled) # All in real weights
            # Concatenate #
            output = np.c_[inputs_base,other] # without NN output
            dtype = copy.deepcopy(dtype_base)

            instance = HyperModel(opt.output)
            out = instance.HyperRestore(inputs)
            output = np.c_[output,out]
            dtype.extend([('prob_HToZA','float64'),('prob_DY','float64'),('prob_TT','float64')])

            # Save root file #
            output.dtype = dtype
            output_name = os.path.join(path_model_output,tag+'.root')
            array2root(output,output_name,mode='recreate')
            logging.info('Output saved as : '+output_name)

        # Use it on different samples #
        logging.info(' HToZA sample '.center(80,'*'))
        produce_output(inputs=x_test_HToZA,other=z_test_HToZA,tag='HToZA')
        logging.info('')
        logging.info(' DY sample '.center(80,'*'))
        produce_output(inputs=x_test_DY,other=z_test_DY,tag='DY')
        logging.info('')
        logging.info(' TT sample '.center(80,'*'))
        produce_output(inputs=x_test_TT,other=z_test_TT,tag='TT')
        logging.info('')

        
   
if __name__ == "__main__":
    main()
