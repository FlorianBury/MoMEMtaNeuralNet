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


import matplotlib.pyplot as plt

# Personal files #
from NeuralNet import HyperModel
from submit_on_slurm import submit_on_slurm
from generate_mask import GenerateMask
from split_training import DictSplit
from concatenate_csv import ConcatenateCSV
from sampleList import samples_dict, samples_path
from signal_decouple import Decoupler, Repeater
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
    a.add_argument('-dy','--DY', action='store_true', required=False, default=False,
        help='Use DY MEM weights (must be specified if --scan or --report or --output are used')
    a.add_argument('-tt','--TT', action='store_true', required=False, default=False,
        help='Use TT MEM weights (must be specified if --scan or --report or --output are used')
    a.add_argument('-hza','--HToZA', action='store_true', required=False, default=False,
        help='Use HToZA MEM weights (must be specified if --scan or --report or --output are used')
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

    if not opt.DY and not opt.TT and not opt.HToZA:
        if opt.scan!='' or opt.report!='' or opt.submit!='':
            logging.critical('Either -dy, -tt or -hza must be specified')  
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
        logging.warning('Since you have specified a csv concatenation, all the other arguments will be skipped')
    if opt.report!='' and (opt.output!='' or opt.scan!=''):
        logging.warning('Since you have specified a scan report, all the other arguments will be skipped')
    if opt.output == '' and (opt.invalid_DY or opt.invalid_TT ):
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
                submit_on_slurm(name=opt.submit+'_resubmit',debug=opt.debug,tt=opt.TT,dy=opt.DY,hza=opt.HToZA)
            else:
                submit_on_slurm(name=opt.submit,debug=opt.debug,tt=opt.TT,dy=opt.DY,hza=opt.HToZA)
        sys.exit()

    #############################################################################################
    # CSV concatenation #
    #############################################################################################
    if opt.csv!='':
        logging.info('Concatenating csv files from : %s'%(opt.csv))
        dict_DY = ConcatenateCSV(opt.csv,'DY')
        dict_TT = ConcatenateCSV(opt.csv,'TT')
        dict_HToZA = ConcatenateCSV(opt.csv,'HToZA')
        
        dict_DY.Concatenate()
        dict_DY.WriteToFile()

        dict_TT.Concatenate()
        dict_TT.WriteToFile()

        dict_HToZA.Concatenate()
        dict_HToZA.WriteToFile()

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

    # If HToZA weights, add the masses as inputs and make the repetition for each mass #
    if opt.HToZA:
        # Modify data #
        logging.info("Starting the decoupling")
        data_HToZA = Decoupler(data_HToZA)
        logging.info("\tHToZA decoupled : new size = %d"%data_HToZA.shape[0])
        data_DY = Decoupler(data_DY)
        logging.info("\tDY decoupled : new size = %d"%data_DY.shape[0])
        data_TT = Decoupler(data_TT)
        logging.info("\tTT decoupled : new size = %d"%data_TT.shape[0])
        # Update the list of variables #
        list_inputs += ['mH','mA']


    # Weight equalization #
    weight_HToZA = data_HToZA[parameters.weights]
    weight_DY = data_DY[parameters.weights]
    weight_TT = data_TT[parameters.weights]

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
    mask_HToZA = GenerateMask(data_HToZA.shape[0],'signal_weights_HToZA')
    mask_DY = GenerateMask(data_DY.shape[0],'signal_weights_DY')
    mask_TT = GenerateMask(data_TT.shape[0],'signal_weights_TT')
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

    # Randomize order, we don't want only one type per batch #
    random_train = np.arange(0,train_all.shape[0]) # needed to randomize x,y and w in same fashion
    random_test = np.arange(0,test_all.shape[0])
    np.random.shuffle(random_train)
    np.random.shuffle(random_test)

    train_all = train_all.iloc[random_train]
    test_all = test_all.iloc[random_test]
      
    # Preprocessing #
    # The purpose is to create a scaler object and save it
    # The preprocessing will be implemented in the network with a custom layer
    if not os.path.exists(parameters.scaler_name):
        scaler = preprocessing.StandardScaler().fit(train_all[parameters.inputs])
        with open(parameters.scaler_name, 'wb') as handle:
            pickle.dump(scaler, handle)
        logging.warning('Scaler %s has been created'%parameters.scaler_name)
    else:
        with open(parameters.scaler_name, 'rb') as handle:
            scaler = pickle.load(handle)
        logging.warning('Scaler %s has been imported'%parameters.scaler_name)

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
        
    if opt.output!='': 
    # Make path #
        tmp_output = copy.copy(opt.output)
        path_output = os.path.join(path_out,tmp_output,'valid_weights')
        path_output_inv_DY = os.path.join(path_out,tmp_output,'invalid_DY_weights')
        path_output_inv_TT = os.path.join(path_out,tmp_output,'invalid_TT_weights')
        #path_output_JEC = os.path.join(path_out,tmp_output,'JEC')
        if not os.path.exists(path_output):
            os.makedirs(path_output)
        if not os.path.exists(path_output_inv_DY):
            os.makedirs(path_output_inv_DY)
        if not os.path.exists(path_output_inv_TT):
            os.makedirs(path_output_inv_TT)
        #if not os.path.exists(path_output_JEC):
        #    os.makedirs(path_output_JEC)

        # Make basic dtype #
        #if opt.HToZA:
        #    dtype_base = parameters.make_dtype(parameters.inputs+['mH','mA','weight_HToZA']+parameters.other_variables+parameters.weights)
        #else:
        #    dtype_base = parameters.make_dtype(parameters.inputs+parameters.outputs+parameters.other_variables+parameters.weights)
    
        # Instance of output class #
        inst_out = ProduceOutput(model=os.path.join(parameters.main_path,'model',opt.output))

        # Use it on test samples #
        logging.info(' HToZA sample '.center(80,'*'))
        inst_out.OutputFromTraining(data=test_all,path_output=path_output)
        sys.exit()
        logging.info('')
        logging.info(' DY sample '.center(80,'*'))
        inst_out.OutputFromTraining(inputs_scaled=x_test_DY,outputs_scaled=y_test_DY,other=z_test_DY,tag='DY',path_output=path_output)
        logging.info('')
        logging.info(' TT sample '.center(80,'*'))
        inst_out.OutputFromTraining(inputs_scaled=x_test_TT,outputs_scaled=y_test_TT,other=z_test_TT,tag='TT',path_output=path_output)
        logging.info('')

        # Apply model on unknown samples #
        #cut_invalid = "weight_TT>weight_TT_err && weight_DY>weight_DY_err"
        #if opt.invalid_DY:
        #    logging.info('Starting invalid DY output'.center(80,'*'))
        #    inst_out.OutputNewData(input_dir=samples_path,list_sample=samples_dict['invalid_DY'],path_output=path_output_inv_DY,cut=cut_invalid)

        #if opt.invalid_TT:
        #    logging.info('Starting invalid TT output'.center(80,'*'))
        #    inst_out.OutputNewData(input_dir=samples_path,list_sample=samples_dict['invalid_TT'],path_output=path_output_inv_TT,cut=cut_invalid)

        #if opt.JEC:
        #    logging.info('Starting JEC output'.center(80,'*'))
        #    inst_out.OutputNewData(input_dir=samples_path,list_sample=samples_dict['JEC'],path_output=path_output_JEC,cut=cut_invalid)

             
   
if __name__ == "__main__":
    main()
