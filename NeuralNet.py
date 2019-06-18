import os
import re
import sys
import json
import shutil
import pickle
import string
import logging
import random
import csv
import time

import array
import numpy as np
import itertools
import plotille # For plots in terminal

from sklearn.model_selection import train_test_split

import keras
from keras import utils
from keras.layers import Layer, Input, Dense, Concatenate, BatchNormalization, LeakyReLU, Lambda, Dropout
from keras.losses import binary_crossentropy, mean_squared_error
from keras.optimizers import RMSprop, Adam, Nadam, SGD
from keras.activations import relu, elu, selu, softmax, tanh
from keras.models import Model, model_from_json, load_model
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.regularizers import l1,l2
import keras.backend as K
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # removes annoying warning

from talos import Scan, Reporting, Predict, Evaluate, Deploy, Restore, Autom8
from talos.utils.best_model import *
from talos.model.layers import *
from talos.model.normalizers import lr_normalizer
from talos.utils.gpu_utils import parallel_gpu_jobs
import talos

import astetik as ast # For the plot section

import matplotlib.pyplot as plt

# Personal files #
import parameters
from split_training import DictSplit
from plot_scans import PlotScans
from preprocessing import PreprocessLayer
import Model

#################################################################################################
# HyperModel #
#################################################################################################
class HyperModel:
    #############################################################################################
    # __init ___#
    #############################################################################################
    def __init__(self,name,sample):
        self.name = name
        self.sample = sample
        logging.info((' Starting '+self.sample+' case ').center(80,'='))

    #############################################################################################
    # HyperScan #
    #############################################################################################
    def HyperScan(self,data,list_inputs,list_outputs,task):
        """
        Performs the scan for hyperparameters
        If task is specified, will load a pickle dict splitted from the whole set of parameters
        Data is a pandas dataframe containing all the event informations (inputs, outputs and unused variables)
        The column to be selected are given in list_inputs, list_outputs as lists of strings
        Reference : /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/scan/Scan.py
        """
        logging.info(' Starting scan '.center(80,'-'))

        # Records #
        self.x = data[list_inputs].values
        self.y = data[list_outputs+['learning_weights']].values
        self.task = task
        logging.info('Number of features : %d'%self.x.shape[1])
        for name in list_inputs:
            logging.info('..... %s'%name)

        # Talos hyperscan parameters #
        if self.task!='': # if task is specified load it otherwise get it from parameters.py
            with open(os.path.join(parameters.main_path,'split',self.name,self.task), 'rb') as f:
                self.p = pickle.load(f)
        else: # We need the full dict
            self.p = parameters.p

        # Check if no already exists then change it -> avoids rewriting  #
        no = 1
        self.name = self.name+'_'+self.sample+self.task.replace('.pkl','')
        self.path_model = os.path.join(parameters.main_path,'model',self.name)
        while os.path.exists(self.name+str(no)+'.csv'):
            no +=1
        
        self.name_model = self.name+'_'+str(no)

        # Data spltting splitting #
        size = parameters.training_ratio/(parameters.training_ratio+parameters.validation_ratio)
        self.x_train, self.x_val, self.y_train, self.y_val = train_test_split(self.x,self.y,train_size=size)
        logging.info("Training set   : %d"%self.x_train.shape[0])
        logging.info("Evaluation set : %d"%self.x_val.shape[0])

        # Define scan object #
        #parallel_gpu_jobs(0.5)
        self.h = Scan(  x=self.x_train,
                   y=self.y_train,
                   params=self.p,
                   dataset_name=self.name,
                   experiment_no=str(no),
                   model=getattr(Model,parameters.model),
                   val_split=0.1,
                   reduction_metric='val_loss',
                   #grid_downsample=0.1,
                   #random_method='lhs',
                   #reduction_method='spear',
                   #reduction_window=1000,
                   #reduction_interval=100,
                   #last_epoch_value=True,
                   print_params=True,
                   repetition=parameters.repetition,
                   custom_objects = {'PreprocessLayer': PreprocessLayer}
                )
        self.h_with_eval = Autom8(scan_object = self.h,
                     x_val = self.x_val,
                     y_val = self.y_val[:,:-1], # last column is weight
                     n = -1,
                     folds = 10,
                     metric = 'val_loss',
                     asc = True,
                     shuffle = True,
                     average = None)  
        self.h_with_eval.data.to_csv(self.name_model+'.csv') # save to csv including error

        # returns the experiment configuration details
        logging.info('='*80)
        logging.debug('Details')
        logging.debug(self.h.details)

    #############################################################################################
    # HyperDeploy #
    #############################################################################################
    def HyperDeploy(self,best='eval_error'):
        """
        Deploy the model according to the evaluation error (default) or val_loss if not found
        Reference :
            /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/commands/deploy.py
        """
        logging.info(' Starting deployment '.center(80,'-'))

        # Check arguments #
        if best != 'val_loss' and best != 'eval_error' : 
            logging.critical('Model not saved as .zip due to incorrect best model parameter')
        #if self.idx_best_model==self.idx_best_eval:
        #    logging.warning('Best models according to val_loss and cross-validation are the same')

        # Save models #
        if best == 'val_loss':
            Deploy(self.h,model_name=self.name_model,metric='val_loss',asc=True)
            logging.warning('Best model saved according to val_loss')
        if best == 'eval_error':
            Deploy(self.h,model_name=self.name_model,metric='eval_mean',asc=True)

        # Move csv file to model dir #
        if self.task == '': # if not split+submit -> because submit will put it in slurm dir
            try:
                shutil.move(self.name_model+'.csv',os.path.join(parameters.main_path,'model',self.name_model+'.csv'))
            except:
                logging.warning('Could not move file to model folder')
                logging.warning('\tAttempted to move '+(os.path.abspath(self.name_model+'.csv') +' -> ' +os.path.join(parameters.main_path,'model',self.name_model+'.csv'))) 
        
        # Move zip file to model dir #
        if self.task == '': # if not split+submit -> because submit will put it in slurm dir
            try:
                shutil.move(self.name_model+'.zip',os.path.join(parameters.main_path,'model',self.name_model+'.zip'))
            except:
                logging.warning('Could not move file to model folder')
                logging.warning('\tAttempted to move '+(os.path.abspath(self.name_model+'.zip') +' -> ' +os.path.join(parameters.main_path,'model',self.name_model+'.zip'))) 

    #############################################################################################
    # HyperReport #
    #############################################################################################
    def HyperReport(self,eval_criterion='val_loss'):
        """
        Reports the model from csv file of previous scan
        Plot several quantities and comparisons in dir /$name/
        Selects the best models according to the eval_criterion (val_loss or eval_error)
        Reference :
        """
        logging.info(' Starting reporting '.center(80,'-'))

        # Get reporting #
        report_file = os.path.join('model',self.name+'_'+self.sample+'.csv')
        if os.path.exists(report_file):
            r = Reporting(report_file)
        else:
            logging.critical('Could not find %s'%(report_file))
            sys.exit(1)

        # returns the results dataframe
        logging.info('='*80)
        logging.info('Complete data after n_round = %d'%(r.rounds()))
        logging.debug(r.data)

        # Lowest eval_error #
        logging.info('-'*80)
        if eval_criterion == 'eval_error':
            logging.info('Lowest eval_error = %0.5f obtained after %0.f rounds'%(r.low('eval_mean'),r.rounds2high('eval_mean')))
        elif eval_criterion == 'val_loss':
            logging.info('Lowest val_loss = %0.5f obtained after %0.f rounds'%(r.low('val_loss'),r.rounds2high('val_loss')))
        else:
            logging.critical('Could not find evaluation criterion "%s" in the results'%eval_criterion)
            sys.exit(1)

        # Best params #
        logging.info('='*80)
        logging.info('Best parameters sets')
        if eval_criterion == 'eval_error':
            sorted_data = r.data.sort_values('eval_mean',ascending=True)
        elif eval_criterion == 'val_loss':
            sorted_data = r.data.sort_values('val_loss',ascending=True)

        for i in range(0,10):
            logging.info('-'*80)
            logging.info('Best params n°%d'%(i+1))
            try:
                logging.info(sorted_data.iloc[i])
            except:
                logging.warning('\tNo more parameters')
                break
        # Hist in terminal #
        eval_mean_arr = r.data['eval_mean'].values
        val_loss_arr = r.data['val_loss'].values
        fig1 = plotille.Figure()
        fig1.width = 150
        fig1.height = 50
        fig1.set_x_limits(min_=np.amin(eval_mean_arr),max_=np.amax(eval_mean_arr))
        fig1.color_mode = 'byte'
        fig1.histogram(eval_mean_arr, bins=200, lc=25)
        print ('  Evaluation error  '.center(80,'-'))
        print ('Best model : ',sorted_data.iloc[0][['eval_mean']])
        print(fig1.show(legend=True))

        fig2 = plotille.Figure()
        fig2.width = 150
        fig2.height = 50
        fig2.set_x_limits(min_=np.amin(val_loss_arr),max_=np.amax(val_loss_arr))
        fig2.color_mode = 'byte'
        fig2.histogram(val_loss_arr, bins=200, lc=100)
        print ('  Val loss  '.center(80,'-'))
        print ('Best model : ',sorted_data.iloc[0][['val_loss']])
        print(fig2.show(legend=True))

        logging.info('='*80)

        # Generate dir #
        path_plot = os.path.join(parameters.main_path,'model',self.name+'_'+self.sample)
        if not os.path.isdir(path_plot):
            os.makedirs(path_plot)
        
        logging.info('Starting plots')
        # Make plots #
        PlotScans(data=r.data,path=path_plot,tag=self.sample)

    #############################################################################################
    # HyperRestore #
    #############################################################################################
    def HyperRestore(self,inputs,batch_size=32,verbose=0):
        """
        Retrieve a zip containing the best model, parameters, x and y data, ... and restores it
        Produces an output from the input numpy array
        Reference :
            /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/commands/restore.py
        """
        logging.info((' Starting restoration of sample %s with model %s_%s.zip '%(self.sample,self.name,self.sample)).center(80,'-'))
        # Load the preprocessing layer #
        custom_objects =  {'PreprocessLayer': PreprocessLayer}
        # Restore model #
        loaded = False
        while not loaded:
            try:
                a = Restore(os.path.join(parameters.main_path,'model',self.name+'_'+self.sample+'.zip'),custom_objects = custom_objects)
                loaded = True
            except Exception as e:
                logging.warning('Could not load model due to "%s", will try again in 3s'%e)
                time.sleep(3)

        # Output of the model #
        outputs = a.model.predict(inputs,batch_size=batch_size,verbose=verbose)

        return outputs
