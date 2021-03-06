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
from keras.losses import binary_crossentropy, mean_squared_error, logcosh
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
from data_generator import DataGenerator
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
        self.custom_objects =  {'PreprocessLayer': PreprocessLayer} # Needs to be specified when saving and restoring

    #############################################################################################
    # HyperScan #
    #############################################################################################
    def HyperScan(self,data,list_inputs,list_outputs,task,generator=False,generator_weights=False,resume=False):
        """
        Performs the scan for hyperparameters
        If task is specified, will load a pickle dict splitted from the whole set of parameters
        Data is a pandas dataframe containing all the event informations (inputs, outputs and unused variables)
        The column to be selected are given in list_inputs, list_outputs as lists of strings
        Reference : /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/scan/Scan.py
        """
        logging.info(' Starting scan '.center(80,'-'))

        # Printing #
        logging.info('Number of features : %d'%len(list_inputs))
        for name in list_inputs:
            logging.info('..... %s'%name)
        logging.info('Number of outputs : %d'%len(list_outputs))
        for name in list_outputs:
            logging.info('..... %s'%name)
            
        # Records #
        if not generator:
            self.x = data[list_inputs].values
            self.y = data[list_outputs+['learning_weights']].values
            # Data splitting #
            size = parameters.training_ratio/(parameters.training_ratio+parameters.validation_ratio)
            self.x_train, self.x_val, self.y_train, self.y_val = train_test_split(self.x,self.y,train_size=size)
            logging.info("Training set   : %d"%self.x_train.shape[0])
            logging.info("Evaluation set : %d"%self.x_val.shape[0])
        else:
            dummyX = np.ones((1,len(list_inputs)))
            dummyY = np.ones((1,len(list_outputs)+1)) # emulates output + weights
            self.x_train = dummyX
            self.y_train = dummyY
            self.x_val = dummyX
            self.y_val = dummyY

        # Talos hyperscan parameters #
        self.task = task
        if self.task != '': # if task is specified load it otherwise get it from parameters.py
            with open(os.path.join(parameters.main_path,'split',self.name,self.task), 'rb') as f:
                self.p = pickle.load(f)
        else: # We need the full dict
            self.p = parameters.p

        # If resume, puts it as argument ot be passed to function #
        # Also, needs to change the dictionary parameters for the one in the imported model #
        if resume:
            logging.info("Will resume training of model %s"%parameters.resume_model)
            # Get model and extract epoch range #
            a = Restore(parameters.resume_model,custom_objects=self.custom_objects)
            initial_epoch = a.params['epochs'][0]
            supp_epochs = self.p['epochs'][0] # Will update the param dict, so must keep that in memory
            batch_size_save = self.p['batch_size'] # Might want to change batch_size in retraining
            # Update params dict with the one from the trained model #
            self.p = a.params
            self.p['resume'] = [parameters.resume_model]
            self.p['initial_epoch'] = [initial_epoch]  # Save initial epoch to be passed to Model
            self.p['epochs'][0] = initial_epoch+supp_epochs # Initial = last epoch of already trained model (is a list)
            self.p['batch_size'] = batch_size_save
            logging.warning("Since you asked to resume training of model %s, the parameters dictionary has been set to the one used to train the model"%parameters.resume_model)
            logging.info("Will train the model from epoch %d to %d"%(self.p['initial_epoch'][0],self.p['epochs'][0]))

        # Specify that weights should be used by generator #
        if generator_weights:
            self.p['generator_weights'] = [True] # Add to dictionary to be passed to Model

        # Check if no already exists then change it -> avoids rewriting  #
        no = 1
        if self.task == '': # If done on frontend
            self.name = self.name+'_'+self.sample
            self.path_model = os.path.join(parameters.main_path,'model',self.name)
            while os.path.exists(os.path.join(parameters.path_model,self.name+'_'+str(no)+'.csv')):
                no +=1
            self.name_model = self.name+'_'+str(no)
        else:               # If job on cluster
            self.name_model = self.name+'_'+self.sample+self.task.replace('.pkl','')

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
                   path_model = parameters.path_model,
                   custom_objects=self.custom_objects,
                )
        if not generator:
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
            self.autom8 = True
        else:
            error_arr = np.zeros(self.h.data.shape[0])
            for i in range(self.h.data.shape[0]):
                logging.info("Evaluating model %d"%i)
                model_eval = model_from_json(self.h.saved_models[i],custom_objects=self.custom_objects)   
                model_eval.set_weights(self.h.saved_weights[i])
                #model_eval.compile(optimizer=Adam(),loss={'OUT':parameters.p['loss_function']},metrics=['accuracy'])
                model_eval.compile(optimizer=Adam(),loss={'OUT':mean_squared_error},metrics=['accuracy'])
                evaluation_generator = DataGenerator(path = parameters.path_gen_evaluation,
                                                     inputs = parameters.inputs,
                                                     outputs = parameters.outputs,
                                                     batch_size = parameters.p['batch_size'][0],
                                                     state_set = 'evaluation')

                eval_metric = model_eval.evaluate_generator(generator             = evaluation_generator,
                                                            workers               = parameters.workers,
                                                            use_multiprocessing   = True)
                error_arr[i] = eval_metric[0]
                logging.info('Error is %f'%error_arr[i])
            self.h.data['eval_mean'] = error_arr
            self.h.data.to_csv(self.name_model+'.csv') # save to csv including error
            self.autom8 = True
            
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
        if self.task == '':     # On frontend
            path_model = parameters.path_model
        else:                   # On cluster
            path_model = ''

        # Save models #
        if best == 'eval_error' and not self.autom8:
            logging.warning('You asked for the evaluation error but it was not computed, will switch to val_loss') 
            best = 'val_loss'
        if best == 'eval_error':
            Deploy(self.h,model_name=self.name_model,metric='eval_mean',asc=True,path_model=path_model)
        elif best == 'val_loss':
            Deploy(self.h,model_name=self.name_model,metric='val_loss',asc=True,path_model=path_model)
            logging.warning('Best model saved according to val_loss')
        else: 
            logging.error('Argument of HyperDeploy not understood')
            sys.exit(1)

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
            logging.info('Best params no %d'%(i+1))
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
    def HyperRestore(self,inputs,verbose=0,generator=False,generator_filepath=None):
        """
        Retrieve a zip containing the best model, parameters, x and y data, ... and restores it
        Produces an output from the input numpy array
        Reference :
            /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/commands/restore.py
        """
        logging.info((' Starting restoration of sample %s with model %s_%s.zip '%(self.sample,self.name,self.sample)).center(80,'-'))
        # Load the preprocessing layer #
        # Restore model #
        loaded = False
        while not loaded:
            try:
                a = Restore(os.path.join(parameters.main_path,'model',self.name+'_'+self.sample+'.zip'),custom_objects=self.custom_objects)
                loaded = True
            except Exception as e:
                logging.warning('Could not load model due to "%s", will try again in 3s'%e)
                time.sleep(3)

        # Output of the model #
        if not generator:
            outputs = a.model.predict(inputs,batch_size=parameters.output_batch_size,verbose=verbose)
        else:
            if generator_filepath is None:
                logging.error("Generator output must be provided with a filepath")
                sys.exit(1)
            output_generator = DataGenerator(path = generator_filepath,
                                             inputs = parameters.inputs,
                                             outputs = parameters.outputs,
                                             batch_size = parameters.output_batch_size,
                                             state_set = 'output')
            outputs = a.model.predict_generator(output_generator,
                                              workers=parameters.workers,
                                              use_multiprocessing=True,
                                              verbose=1)
        return outputs
