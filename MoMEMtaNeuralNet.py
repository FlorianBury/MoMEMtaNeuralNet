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
        help='Wether to submit on slurm and nname for the save (must have specified --split)')
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

    if opt.scan!='' or opt.report!='' :
        if not opt.DY and not opt.TT:
            logging.critical('Either -dy or -tt must be specified')  
            sys.exit(1)
        if opt.split!=0 or opt.submit:
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
    if opt.output == '' and (opt.invalid_DY or opt.invalid_TT):
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
        DictSplit(opt.split,opt.submit)
        
        logging.info('Splitting jobs done')

        if opt.submit!='':
            logging.info('Submitting jobs')
            if not opt.debug:
                submit_on_slurm(name=opt.submit)
            else:
                logging.info("Don't worry, the jobs were not sent")
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
    weight_HToZA = weight_HToZA/np.sum(weight_HToZA)*10000
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

    if opt.scan != '':
        # DY network #
        if opt.DY:
            instance = HyperModel(opt.scan,'DY')
            instance.HyperScan(x_train,np.c_[w_train,y_train[:,0]],task=opt.task)
            instance.HyperEvaluate(x_test,y_test[:,0],folds=5) 
            instance.HyperDeploy(best='eval_error')
        # TT network #
        if opt.TT:
            instance = HyperModel(opt.scan,'TT')
            instance.HyperScan(x_train,np.c_[w_train,y_train[:,0]],task=opt.task)
            instance.HyperEvaluate(x_test,y_test[:,0],folds=5) 
            instance.HyperDeploy(best='eval_error')
        
    if opt.output!='': 
        # Make path #
        path_model_output = os.path.join(path_out,opt.output)
        if not os.path.exists(path_model_output):
            os.makedirs(path_model_output)

        # Make basic dtype #
        dtype_base = [('lep1_px','float64'),
                 ('lep1_py','float64'),
                 ('lep1_pz','float64'),
                 ('lep1_E','float64'),
                 ('lep2_px','float64'),
                 ('lep2_py','float64'),
                 ('lep2_pz','float64'),
                 ('lep2_E','float64'),
                 ('jet1_px','float64'),
                 ('jet1_py','float64'),
                 ('jet1_pz','float64'),
                 ('jet1_E','float64'),
                 ('jet2_px','float64'),
                 ('jet2_py','float64'),
                 ('jet2_pz','float64'),
                 ('jet2_E','float64'),
                 ('met_pt','float64'),
                 ('met_phi','float64'),
                 ('weight','float64'),
                 ('MEM_weight_DY','float64'),
                 ('MEM_weight_TT','float64')]

        # Get output, concatenate and make root file # 
        def produce_output(inputs,weights,MEM,tag):
            # De-preprocess inputs #
            inputs_unscaled = inputs*scaler.scale_+scaler.mean_
            # Concatenate #
            output = np.c_[inputs_unscaled,weights,MEM] # without NN output
            dtype = copy.deepcopy(dtype_base)

            try:
                logging.info('Applying DY model')
                instance = HyperModel(opt.output,'DY')
                out_DY = instance.HyperRestore(inputs)
                output = np.c_[output,out_DY]
                dtype.append(('output_DY','float64'))
            except:
                logging.warning('Could not find the DY model')
            try:
                logging.info('Applying TT model')
                instance = HyperModel(opt.output,'TT')
                out_TT = instance.HyperRestore(inputs)
                output = np.c_[output,out_TT]
                dtype.append(('output_TT','float64'))
            except:
                logging.warning('Could not find the TT model')

            # Save root file #
            output.dtype = dtype
            output_name = os.path.join(path_model_output,tag+'.root')
            array2root(output,output_name,mode='recreate')
            logging.info('Output saved as : '+output_name)

        # Use it on different samples #
        logging.info(' HToZA sample '.center(80,'*'))
        produce_output(inputs=x_test_HToZA,weights=w_test_HToZA,MEM=y_test_HToZA,tag='HToZA')
        logging.info('')
        logging.info(' DY sample '.center(80,'*'))
        produce_output(inputs=x_test_DY,weights=w_test_DY,MEM=y_test_DY,tag='DY')
        logging.info('')
        logging.info(' TT sample '.center(80,'*'))
        produce_output(inputs=x_test_TT,weights=w_test_TT,MEM=y_test_TT,tag='TT')
        logging.info('')

        # Same but for invalid weights #
        def loop_invalid(path,tag):
            for inv_file in glob.glob(path+'*.root'):
                inv_name = inv_file.replace(path,'').replace('.root','') 
                # Get data #
                data_inv, weight_inv = LoopOverTrees(input_dir=path,variables=variables,weight='total_weight',reweight_to_cross_section=False,part_name=inv_name)
                if data_inv.shape[0]==0: # There is no invalid weights in this case
                    continue
                # Separate and process #
                inv_inputs = scaler.transform(data_inv[:,:18])
                inv_MEM = -np.log10(data_inv[:,18:])
                # Concatenate #
                full_outputs = np.c_[data_inv[:,:18],weight_inv,inv_MEM]
                dtype = copy.deepcopy(dtype_base)
                # NN Outputs #
                try:
                    logging.info('Applying DY model')
                    instance = HyperModel(opt.output,'DY')
                    inv_outputs_DY = instance.HyperRestore(inv_inputs)
                    full_outputs = np.c_[full_outputs,inv_outputs_DY]
                    dtype.append(('output_DY','float64'))
                except:
                    logging.warning('Could not find the DY model')
                try:
                    logging.info('Applying TT model')
                    instance = HyperModel(opt.output,'TT')
                    inv_outputs_TT = instance.HyperRestore(inv_inputs)
                    full_outputs = np.c_[full_outputs,inv_outputs_TT]
                    dtype.append(('output_TT','float64'))
                except:
                    logging.warning('Could not find the TT model')
                
                # Save to file #
                full_outputs.dtype = dtype
                output_name = os.path.join(path_model_output,'invalid_'+tag+'_'+inv_name+'.root')
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
