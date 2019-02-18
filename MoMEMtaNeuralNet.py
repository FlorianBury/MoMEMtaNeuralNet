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
    a.add_argument('-dy','--DY', action='store_true', required=False, default=False,
        help='Use DY MEM weights (must be specified if --scan or --report or --output are used')
    a.add_argument('-tt','--TT', action='store_true', required=False, default=False,
        help='Use TT MEM weights (must be specified if --scan or --report or --output are used')
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

    if not opt.DY and not opt.TT:
        if opt.scan!='' or opt.report!='' or opt.submit!='':
            logging.critical('Either -dy or -tt must be specified')  
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
                submit_on_slurm(name=opt.submit+'_resubmit',debug=opt.debug,tt=opt.TT,dy=opt.DY)
            else:
                submit_on_slurm(name=opt.submit,debug=opt.debug,tt=opt.TT,dy=opt.DY)
        sys.exit()

    #############################################################################################
    # CSV concatenation #
    #############################################################################################
    if opt.csv!='':
        logging.info('Concatenating csv files from : %s'%(opt.csv))
        dict_DY = ConcatenateCSV(opt.csv,'DY')
        dict_TT = ConcatenateCSV(opt.csv,'TT')
        
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
            instance = HyperModel(opt.report,'DY')
            instance.HyperReport()
        if opt.TT:
            instance = HyperModel(opt.report,'TT')
            instance.HyperReport()

        sys.exit()

    #############################################################################################
    # Data Input and preprocessing #
    #############################################################################################
    # Input path #
    logging.info('Starting histograms input')

    # Import variables from parameters.py
    variables = parameters.inputs+parameters.outputs+parameters.other_variables
    NIn = len(parameters.inputs)
    NOut = len(parameters.outputs)
    NOther = len(parameters.other_variables)

    # Import arrays #
    logging.info('HToZA samples')
    data_HToZA, weight_HToZA = LoopOverTrees(input_dir=path_to_files,variables=variables,weight=parameters.weights[0],reweight_to_cross_section=False,part_name='HToZA')
    logging.info('HToZA sample size : {}'.format(data_HToZA.shape[0]))
    logging.info('DY samples')
    data_DY, weight_DY = LoopOverTrees(input_dir=path_to_files,variables=variables,weight=parameters.weights[0],reweight_to_cross_section=True,part_name='DY')
    logging.info('DY sample size : {}'.format(data_DY.shape[0]))
    logging.info('TT samples')
    data_TT, weight_TT = LoopOverTrees(input_dir=path_to_files,variables=variables,weight=parameters.weights[0],reweight_to_cross_section=True,part_name='TT',n=500000)
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
    mask_HToZA = GenerateMask(data_HToZA.shape[0],'HToZA')
    mask_DY = GenerateMask(data_DY.shape[0],'DY')
    mask_TT = GenerateMask(data_TT.shape[0],'TT')
       # Needs to keep the same testing set for the evaluation of model that was selected earlier
    x_train_HToZA = data_HToZA[mask_HToZA==True,:NIn]
    x_train_DY = data_DY[mask_DY==True,:NIn]
    x_train_TT = data_TT[mask_TT==True,:NIn]
    x_test_HToZA = data_HToZA[mask_HToZA==False,:NIn]
    x_test_DY = data_DY[mask_DY==False,:NIn]
    x_test_TT = data_TT[mask_TT==False,:NIn]

    if opt.smear != 0:
        logging.warning('A smearing of %0.2f has been applied'%opt.smear)
        x_train_HToZA = np.random.normal(x_train_HToZA,opt.smear)
        x_train_DY = np.random.normal(x_train_DY,opt.smear)
        x_train_TT = np.random.normal(x_train_TT,opt.smear)
        x_test_HToZA = np.random.normal(x_test_HToZA,opt.smear)
        x_test_DY = np.random.normal(x_test_DY,opt.smear)
        x_test_TT = np.random.normal(x_test_TT,opt.smear)

    # Rescale outputs #
    #max_log_weight = np.amax(np.concatenate((data_HToZA[:,18:],data_DY[:,18:],data_TT[:,18:]),axis=0),axis=0)
    max_log_weight = 1

    y_train_HToZA = -np.log10(data_HToZA[mask_HToZA==True,NIn:NIn+NOut]/max_log_weight)
    y_train_DY = -np.log10(data_DY[mask_DY==True,NIn:NIn+NOut]/max_log_weight)
    y_train_TT = -np.log10(data_TT[mask_TT==True,NIn:NIn+NOut]/max_log_weight)
    y_test_HToZA = -np.log10(data_HToZA[mask_HToZA==False,NIn:NIn+NOut]/max_log_weight)
    y_test_DY = -np.log10(data_DY[mask_DY==False,NIn:NIn+NOut]/max_log_weight)
    y_test_TT = -np.log10(data_TT[mask_TT==False,NIn:NIn+NOut]/max_log_weight)

    # Variables outside training #
    z_test_HToZA = data_HToZA[mask_HToZA==False,NIn+NOut:NIn+NOut+NOther]
    z_test_DY = data_DY[mask_DY==False,NIn+NOut:NIn+NOut+NOther]
    z_test_TT = data_TT[mask_TT==False,NIn+NOut:NIn+NOut+NOther]
        # We don't need training because only test is used in output 
    
    # Learning weights #
    w_train_HToZA = weight_HToZA[mask_HToZA==True]
    w_train_DY = weight_DY[mask_DY==True]
    w_train_TT = weight_TT[mask_TT==True]
    w_test_HToZA = weight_HToZA[mask_HToZA==False]
    w_test_DY = weight_DY[mask_DY==False]
    w_test_TT = weight_TT[mask_TT==False]
        
    # y -> [weight_DY, weight_TT]

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
        # DY network #
        if opt.DY:
            instance = HyperModel(opt.scan,'DY')
            instance.HyperScan(x_train,np.c_[w_train,y_train[:,0]],task=opt.task)
            #instance.HyperEvaluate(x_test,y_test[:,0],folds=5) 
            instance.HyperDeploy(best='eval_error')
        # TT network #
        if opt.TT:
            instance = HyperModel(opt.scan,'TT')
            instance.HyperScan(x_train,np.c_[w_train,y_train[:,1]],task=opt.task)
            #instance.HyperEvaluate(x_test,y_test[:,1],folds=5) 
            instance.HyperDeploy(best='eval_error')
        
    if opt.output!='': 
        # Make path #
        tmp_output = copy.copy(opt.output)
        if opt.smear != 0:
            tmp_output += '_smear_'+str(opt.smear)
        path_model_output = os.path.join(path_out,tmp_output,'valid_weights')
        path_model_output_inv_dy = os.path.join(path_out,tmp_output,'invalid_DY_weights')
        path_model_output_inv_tt = os.path.join(path_out,tmp_output,'invalid_TT_weights')
        if not os.path.exists(path_model_output):
            os.makedirs(path_model_output)
        if not os.path.exists(path_model_output_inv_dy):
            os.makedirs(path_model_output_inv_dy)
        if not os.path.exists(path_model_output_inv_tt):
            os.makedirs(path_model_output_inv_tt)

        # Make basic dtype #
        dtype_base = parameters.make_dtype(parameters.inputs+parameters.outputs+parameters.other_variables+parameters.weights)

        # Get output, concatenate and make root file # 
        def produce_output(inputs,MEM,other,tag):
            # De-preprocess inputs #
            inputs_unscaled = inputs*scaler.scale_+scaler.mean_
            MEM = np.power(10,-MEM) # All in real weights
            # Concatenate #
            output = np.c_[inputs_unscaled,MEM,other] # without NN output
            dtype = copy.deepcopy(dtype_base)

            try:
                instance = HyperModel(opt.output,'DY')
                out_DY = np.power(10,-instance.HyperRestore(inputs))
                output = np.c_[output,out_DY]
                dtype.append(('output_DY','float64'))
            except Exception as e:
                logging.warning('Could not find the DY model due to "%s"'%e)
            try:
                instance = HyperModel(opt.output,'TT')
                out_TT = np.power(10,-instance.HyperRestore(inputs))
                output = np.c_[output,out_TT]
                dtype.append(('output_TT','float64'))
            except Exception as e:
                logging.warning('Could not find the TT model due to "%s"'%e)

            # Save root file #
            output.dtype = dtype
            output_name = os.path.join(path_model_output,tag+'.root')
            array2root(output,output_name,mode='recreate')
            logging.info('Output saved as : '+output_name)

        # Use it on different samples #
        logging.info(' HToZA sample '.center(80,'*'))
        produce_output(inputs=x_test_HToZA,MEM=y_test_HToZA,other=z_test_HToZA,tag='HToZA')
        logging.info('')
        logging.info(' DY sample '.center(80,'*'))
        produce_output(inputs=x_test_DY,MEM=y_test_DY,other=z_test_DY,tag='DY')
        logging.info('')
        logging.info(' TT sample '.center(80,'*'))
        produce_output(inputs=x_test_TT,MEM=y_test_TT,other=z_test_TT,tag='TT')
        logging.info('')

        # Same but for invalid weights #
        def loop_invalid(path,tag):
            for inv_file in glob.glob(path+'*.root'):
                inv_name = inv_file.replace(path,'').replace('.root','') 
                # Get data #
                variables = parameters.inputs+parameters.outputs+parameters.other_variables
                data_inv, weight_inv = LoopOverTrees(input_dir=path,variables=variables,weight=parameters.weights[0],reweight_to_cross_section=False,part_name=inv_name)
                data_inv = np.append(data_inv,weight_inv,axis=1)
                if data_inv.shape[0]==0: # There is no invalid weights in this case
                    continue
                # Separate and process #
                inv_inputs = scaler.transform(data_inv[:,:NIn])

                # Smearing #
                if opt.smear != 0:
                    inv_inputs = np.random.normal(inv_inputs,opt.smear) 

                inv_MEM = data_inv[:,NIn:NIn+NOut]
                # Concatenate #
                full_outputs = np.c_[data_inv[:,:NIn],inv_MEM,data_inv[:,NIn+NOut:NIn+NOut+NOther]]

                dtype = copy.deepcopy(dtype_base)
                # NN Outputs #
                try:
                    instance = HyperModel(opt.output,'DY')
                    inv_outputs_DY = np.power(10,-instance.HyperRestore(inv_inputs))
                    full_outputs = np.c_[full_outputs,inv_outputs_DY]
                    dtype.append(('output_DY','float64'))
                except Exception as e:
                    logging.warning('Could not find the DY model due to "%s"'%e)
                try:
                    instance = HyperModel(opt.output,'TT')
                    inv_outputs_TT = np.power(10,-instance.HyperRestore(inv_inputs))
                    full_outputs = np.c_[full_outputs,inv_outputs_TT]
                    dtype.append(('output_TT','float64'))
                except Exception as e:
                    logging.warning('Could not find the TT model due to "%s"'%e)
                
                # Save to file #
                full_outputs.dtype = dtype
                if tag=='DY':
                    output_name = os.path.join(path_model_output_inv_dy,inv_name+'.root')
                elif tag=='TT':
                    output_name = os.path.join(path_model_output_inv_tt,inv_name+'.root')
                else:
                    logging.error('Incorrect tag for invalid evaluation')

                array2root(full_outputs,output_name,mode='recreate')
                logging.info('Output saved as : '+output_name)

        # Depending on user request #
        if opt.invalid_DY:
            logging.info('Starting invalid DY output'.center(80,'*'))
            loop_invalid(path=parameters.path_invalid_DY,tag='DY')

        if opt.invalid_TT:
            logging.info('Starting invalid TT output'.center(80,'*'))
            loop_invalid(path=parameters.path_invalid_TT,tag='TT')


        
   
if __name__ == "__main__":
    main()
