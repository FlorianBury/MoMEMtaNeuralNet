#!/usr/bin/env python

import re
import glob
import csv
import os
import sys
import logging
import copy
import pickle

import argparse
import numpy as np
import pandas as pd

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


import matplotlib.pyplot as plt

# Personal files #
from NeuralNet import HyperModel
from submit_on_slurm import submit_on_slurm
from generate_mask import GenerateMask
from split_training import DictSplit
from concatenate_csv import ConcatenateCSV
from sampleList import samples_dict, samples_path
from signal_coupling import Decoupler, Repeater
import parameters
    


def get_options():
    """
    Parse and return the arguments provided by the user.
    """
    parser = argparse.ArgumentParser(description='MoMEMtaNeuralNet : A tool to regress the Matrix Element Method with a Neural Network')

    # Scan, deploy and restore arguments #
    a = parser.add_argument_group('Scan, deploy and restore arguments')
    a.add_argument('-s','--scan', action='store', required=False, type=str, default='',
        help='Name of the scan to be used (modify scan parameters in NeuralNet.py)')
    a.add_argument('-dy','--DY', action='store_true', required=False, default=False,
        help='Use DY MEM weights (must be specified if --scan or --report or --output are used')
    a.add_argument('-tt','--TT', action='store_true', required=False, default=False,
        help='Use TT MEM weights (must be specified if --scan or --report or --output are used')
    a.add_argument('-hza','--HToZA', action='store_true', required=False, default=False,
        help='Use HToZA MEM weights (must be specified if --scan or --report or --output are used')
    a.add_argument('--class', dest='classes', action='store_true', required=False, default=False,
        help='Turn the tags into a one-hot vector for the classification')
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
    c.add_argument('-m','--model', action='store', required=False, type=str, default='',                                                                                                          
        help='Loads the provided model name (without .zip and type, it will find them)') 
    c.add_argument('--test', action='store_true', required=False, default=False,
        help='Applies the provided model (do not forget -o) on the test set and output the tree') 
    c.add_argument('-o','--output', action='store', required=False, nargs='+', type=str, default=[], 
        help='Applies the provided model (do not forget -o) on the list of keys from sampleList.py (separated by spaces)') 

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

    if not opt.DY and not opt.TT and not opt.HToZA and not opt.classes:
        if opt.scan!='' or opt.report!='' or opt.submit!='':
            logging.critical('Either --DY, --TT, --HToZA or --classes must be specified')  
            sys.exit(1)
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
        logging.warning('Since you have specifised a csv concatenation, all the other arguments will be skipped')
    if opt.report!='' and (opt.output!='' or opt.scan!=''):
        logging.warning('Since you have specified a scan report, all the other arguments will be skipped')
    if (opt.test or len(opt.output)!=0) and opt.output == '': 
        logging.critical('You must specify the model with --output')
        sys.exit(1)
    return opt

def main():
    #############################################################################################
    # Preparation #
    #############################################################################################
    # Logging #
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    # Get options from user #
    opt = get_options()
    # Verbose logging #
    if opt.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    # Private modules containing Pyroot #
    from import_tree import LoopOverTrees
    from produce_output import ProduceOutput
    # Needed because PyROOT messes with argparse

    logging.info("="*88)
    logging.info("___  ___     ___  ___ ________  ____        _   _                      _ _   _      _   ")
    logging.info("|  \/  |     |  \/  ||  ___|  \/  | |      | \ | |                    | | \ | |    | | ") 
    logging.info("| .  . | ___ | .  . || |__ | .  . | |_ __ _|  \| | ___ _   _ _ __ __ _| |  \| | ___| |_ ")
    logging.info("| |\/| |/ _ \| |\/| ||  __|| |\/| | __/ _` | . ` |/ _ \ | | | '__/ _` | | . ` |/ _ \ __|")
    logging.info("| |  | | (_) | |  | || |___| |  | | || (_| | |\  |  __/ |_| | | | (_| | | |\  |  __/ |_ ")
    logging.info("\_|  |_/\___/\_|  |_/\____/\_|  |_/\__\__,_\_| \_/\___|\__,_|_|  \__,_|_\_| \_/\___|\__|")
    logging.info("="*88)

    # Make path model #
    path_model = os.path.join(parameters.main_path,'model')
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
                submit_on_slurm(name=opt.submit+'_resubmit',debug=opt.debug,tt=opt.TT,dy=opt.DY,hza=opt.HToZA,classes=opt.classes)
            else:
                submit_on_slurm(name=opt.submit,debug=opt.debug,tt=opt.TT,dy=opt.DY,hza=opt.HToZA,classes=opt.classes)
        sys.exit()

    #############################################################################################
    # CSV concatenation #
    #############################################################################################
    if opt.csv!='':
        logging.info('Concatenating csv files from : %s'%(opt.csv))
        dict_DY = ConcatenateCSV(opt.csv,'DY')
        dict_TT = ConcatenateCSV(opt.csv,'TT')
        dict_HToZA = ConcatenateCSV(opt.csv,'HToZA')
        dict_class = ConcatenateCSV(opt.csv,'class')
        
        dict_DY.Concatenate()
        dict_DY.WriteToFile()

        dict_TT.Concatenate()
        dict_TT.WriteToFile()

        dict_HToZA.Concatenate()
        dict_HToZA.WriteToFile()

        dict_class.Concatenate()
        dict_class.WriteToFile()

        sys.exit()

    #############################################################################################
    # Reporting given scan in csv file #
    #############################################################################################
    if opt.report != '':
        if opt.DY: 
            instance = HyperModel(opt.report,'DY')
            instance.HyperReport()
        if opt.TT:
            instance = HyperModel(opt.report,'TT')
            instance.HyperReport()
        if opt.HToZA:
            instance = HyperModel(opt.report,'HToZA')
            instance.HyperReport()
        if opt.classes:
            instance = HyperModel(opt.report,'class')
            instance.HyperReport()

        sys.exit()

    #############################################################################################
    # Output of given files from given model #
    #############################################################################################
    if opt.model != '' and len(opt.output) != 0:
        # Create directory #
        path_output = os.path.join(parameters.path_out,opt.model)#,key+'_weights')
        if not os.path.exists(path_output):
            os.mkdir(path_output)

        # Check if need to decouple signal #
        is_signal = True if opt.HToZA else False
        # Instantiate #
        inst_out = ProduceOutput(model=os.path.join(parameters.main_path,'model',opt.model),is_signal=is_signal)
        # Loop over output keys #
        for key in opt.output:
            # Create subdir #
            path_output_sub = os.path.join(path_output,key+'_weights')
            if not os.path.exists(path_output_sub):
                os.mkdir(path_output_sub)
            try:
                inst_out.OutputNewData(input_dir=samples_path,list_sample=samples_dict[key],path_output=path_output_sub)
            except Exception as e:
                logging.critical('Could not process key "%s" due to "%s"'%(key,e))
        sys.exit()

    #############################################################################################
    # Data Input and preprocessing #
    #############################################################################################
    # Input path #
    logging.info('Starting histograms input')

    # Import variables from parameters.py
    variables = parameters.inputs+parameters.outputs+parameters.other_variables

    # Import arrays #
    logging.info('HToZA samples')
    data_HToZA = LoopOverTrees(input_dir=samples_path,
                               variables=variables,
                               weight=parameters.weights,
                               reweight_to_cross_section=False,
                               list_sample=samples_dict['HToZA'],
                               tag = 'HToZA')
    logging.info('HToZA sample size : {}'.format(data_HToZA.shape[0]))
    logging.info('DY samples')
    data_DY = LoopOverTrees(input_dir=samples_path,
                            variables=variables,
                            weight=parameters.weights,
                            reweight_to_cross_section=True,
                            list_sample=samples_dict['DY'],
                            tag='DY')
    logging.info('DY sample size : {}'.format(data_DY.shape[0]))
    logging.info('TT samples')
    data_TT = LoopOverTrees(input_dir=samples_path,
                            variables=variables,
                            weight=parameters.weights,
                            reweight_to_cross_section=True,
                            list_sample=samples_dict['TT'],
                            tag='TT')
    logging.info('TT sample size : {}'.format(data_TT.shape[0]))

    list_inputs = parameters.inputs

    # Weight equalization #
    weight_HToZA = data_HToZA[parameters.weights]
    weight_DY = data_DY[parameters.weights]
    weight_TT = data_TT[parameters.weights]
    min_weight = np.min(np.concatenate((weight_HToZA,weight_DY,weight_TT),axis=0))-0.001 # 0.001 tl avoid zero weights
    # By rescaling with min_weight, one avoids the negative weights and keep the difference between them
    weight_HToZA -= min_weight
    weight_DY -= min_weight
    weight_TT -= min_weight

    # We need the different types to have the same sumf of weight to equalize training
    weight_HToZA = weight_HToZA/np.sum(weight_HToZA)*10000 
    weight_DY = weight_DY/np.sum(weight_DY)*10000
    weight_TT = weight_TT/np.sum(weight_TT)*10000


    if np.sum(weight_HToZA) != np.sum(weight_DY) or np.sum(weight_HToZA) != np.sum(weight_TT) or np.sum(weight_TT) != np.sum(weight_DY):
        logging.warning ('Sum of weights different between the samples')
        logging.warning('\tHToZA : '+str(np.sum(weight_HToZA)))
        logging.warning('\tDY : '+str(np.sum(weight_DY)))
        logging.warning('\tTT : '+str(np.sum(weight_TT)))

    data_HToZA['learning_weights'] = pd.Series(weight_HToZA)
    data_DY['learning_weights'] = pd.Series(weight_DY)
    data_TT['learning_weights'] = pd.Series(weight_TT)

    # Data splitting #
    mask_HToZA = GenerateMask(data_HToZA.shape[0],parameters.mask_name+'_HToZA')
    mask_DY = GenerateMask(data_DY.shape[0],parameters.mask_name+'_weights_DY')
    mask_TT = GenerateMask(data_TT.shape[0],parameters.mask_name+'_weights_TT')
       # Needs to keep the same testing set for the evaluation of model that was selected earlier
    try:
        train_HToZA = data_HToZA[mask_HToZA==True]
        train_DY = data_DY[mask_DY==True]
        train_TT = data_TT[mask_TT==True]
        test_HToZA = data_HToZA[mask_HToZA==False]
        test_DY = data_DY[mask_DY==False]
        test_TT = data_TT[mask_TT==False]
    except ValueError:
        logging.critical("Problem with the mask you imported, has the data changed since it was generated ?")
        sys.exit(1)
        

    train_all = pd.concat([train_HToZA,train_DY,train_TT])
    test_all = pd.concat([test_HToZA,test_DY,test_TT])
    del train_HToZA,train_DY,train_TT # Save space
    del test_HToZA,test_DY,test_TT

    # If HToZA weights, add the masses as inputs and make the repetition for each mass #
    if opt.HToZA and opt.scan!='': # We only need the training set for the scan
        # Modify data #
        logging.info("Starting the training set decoupling")
        train_all = Decoupler(train_all)
        logging.info("\tTraining set decoupled : new size = %d"%train_all.shape[0])
        # Update the list of variables #
        list_inputs += ['mH_MEM','mA_MEM']
        # For testing -> Done in produce_output.py


    # Randomize order, we don't want only one type per batch #
    random_train = np.arange(0,train_all.shape[0]) # needed to randomize x,y and w in same fashion
    np.random.shuffle(random_train) # Not need for testing
    train_all = train_all.iloc[random_train]
      
    # Preprocessing #
    # The purpose is to create a scaler object and save it
    # The preprocessing will be implemented in the network with a custom layer
    if opt.scan!='': # If we don't scan we don't need to scale the data
        scaler_path = os.path.join(parameters.main_path,parameters.scaler_name)
        if not os.path.exists(scaler_path):
            scaler = preprocessing.StandardScaler().fit(train_all[parameters.inputs])
            with open(scaler_path, 'wb') as handle:
                pickle.dump(scaler, handle)
            logging.info('Scaler %s has been created'%parameters.scaler_name)
        else:
            with open(scaler_path, 'rb') as handle:
                scaler = pickle.load(handle)
            logging.info('Scaler %s has been imported'%parameters.scaler_name)

        # Test the scaler #
        try:
            mean_scale = np.mean(scaler.transform(train_all[parameters.inputs]))
            var_scale = np.var(scaler.transform(train_all[parameters.inputs]))
        except ValueError:
            logging.critical("Problem with the scaler you imported, has the data changed since it was generated ?")
            sys.exit(1)
        if abs(mean_scale)>0.01 or abs((var_scale-1)/var_scale)>0.01: # Check that scaling is correct to 1%
            logging.critical("Something is wrong with scaler (mean = %0.6f, var = %0.6f), maybe you loaded an incorrect scaler"%(mean_scale,var_scale))
            sys.exit()

    # Turns tags into one-hot vector #
    if opt.classes:
        # Instantiate #
        label_encoder = LabelEncoder()
        onehot_encoder = OneHotEncoder(sparse=False)
        label_encoder.fit(train_all['tag'])
        # From strings to labels #
        train_integers = label_encoder.transform(train_all['tag']).reshape(-1, 1)
        test_integers = label_encoder.transform(test_all['tag']).reshape(-1, 1)
        # From labels to strings #
        train_onehot = onehot_encoder.fit_transform(train_integers)
        test_onehot = onehot_encoder.fit_transform(test_integers)
        # From arrays to pd DF #
        train_cat = pd.DataFrame(train_onehot,columns=label_encoder.classes_,index=train_all.index)
        test_cat = pd.DataFrame(test_onehot,columns=label_encoder.classes_,index=test_all.index)
        # Add to full #
        train_all = pd.concat([train_all,train_cat],axis=1)
        test_all = pd.concat([test_all,test_cat],axis=1)

    logging.info("Sample size seen by network : %d"%train_all.shape[0])
    logging.info("Sample size for the output  : %d"%test_all.shape[0])

    #############################################################################################
    # DNN #
    #############################################################################################

    if opt.scan != '':
        # DY network #
        if opt.DY:
            instance = HyperModel(opt.scan,'DY')
            instance.HyperScan(data=train_all,list_inputs=list_inputs,list_outputs=['weight_DY'],task=opt.task)
            instance.HyperDeploy(best='eval_error')
        # TT network #
        if opt.TT:
            instance = HyperModel(opt.scan,'TT')
            instance.HyperScan(data=train_all,list_inputs=list_inputs,list_outputs=['weight_TT'],task=opt.task)
            instance.HyperDeploy(best='eval_error')
        if opt.HToZA:
            instance = HyperModel(opt.scan,'HToZA')
            instance.HyperScan(data=train_all,list_inputs=list_inputs,list_outputs=['weight_HToZA'],task=opt.task)
            instance.HyperDeploy(best='eval_error')
        if opt.classes:
            instance = HyperModel(opt.scan,'class')
            instance.HyperScan(data=train_all,list_inputs=list_inputs,list_outputs=['DY','HToZA','TT'],task=opt.task)
            instance.HyperDeploy(best='eval_error')
            
        
    if opt.model!='': 
    # Make path #
        path_output = os.path.join(parameters.path_out,opt.model,'valid_weights')
        if not os.path.exists(path_output):
            os.makedirs(path_output)

        # Instance of output class #
        is_signal = True if opt.HToZA else False
        inst_out = ProduceOutput(model=os.path.join(parameters.main_path,'model',opt.model),is_signal=is_signal)

        # Use it on test samples #
        if opt.test:
            logging.info('Processing test output sample '.center(80,'*'))
            inst_out.OutputFromTraining(data=test_all,path_output=path_output)
            logging.info('')
             
   
if __name__ == "__main__":
    main()
