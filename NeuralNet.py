import os
import re
import sys
import json
import shutil
import pickle
import logging
import csv

import array
import numpy as np
import itertools


import keras
from keras import utils
from keras.layers import Input, Dense, Concatenate, BatchNormalization, LeakyReLU, Lambda, Dropout
from keras.losses import binary_crossentropy, mean_squared_error
from keras.optimizers import RMSprop, Adam, Nadam, SGD
from keras.activations import relu, elu, selu, softmax, tanh
from keras.models import Model, model_from_json, load_model
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.regularizers import l1,l2
import keras.backend as K
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # removes annoying warning

from talos import Scan, Reporting, Predict, Evaluate, Deploy, Restore
from talos.utils.best_model import *
from talos.model.layers import *
from talos.model.normalizers import lr_normalizer
from talos.utils.gpu_utils import parallel_gpu_jobs
import talos

import astetik as ast # For the plot section

import matplotlib.pyplot as plt

# Personal files #
from split_training import DictSplit
import parameters
from plot_scans import PlotScans

#################################################################################################
# InterpolationModel #
#################################################################################################
def InterpolationModel(x_train,y_train,x_val,y_val,params):
    """
    Keras model for the Neural Network, used to scan the hyperparameter space by Talos
    Inputs :
        - x_train = training inputs (aka : 4-vec of 4 particles + MET)
        - y_train = training [weights, outputs (aka MEM weights)]
        - x_val = test inputs
        - y_val = test [weights, outputs (aka MEM weights)]
        - params = dict of parameters for the talos scan
    Outputs :
        - out =  predicted outputs from network
        - model = fitted models with weights
    """
    # Design network #
    IN = Input(shape=(x_train.shape[1],),name='IN')
    L1 = Dense(params['first_neuron'],
               activation=params['activation'],
               kernel_regularizer=l2(params['l2']))(IN)
    HIDDEN = hidden_layers(params,1).API(L1)
    OUT = Dense(1,activation=params['output_activation'],name='OUT')(HIDDEN)

    # Define model #
    model = Model(inputs=[IN], outputs=[OUT])
    #utils.print_summary(model=model) #used to print model

    # Callbacks #
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0., patience=10, verbose=1, mode='min')
    reduceLR = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, verbose=1, mode='min', epsilon=0.001, cooldown=0, min_lr=0.00001)
    Callback_list = [early_stopping,reduceLR]

    # Compile #
    model.compile(optimizer=params['optimizer'](lr_normalizer(params['lr'], params['optimizer'])),
                  loss={'OUT':params['loss_function']},
                  metrics=['accuracy'])

    # Fit #
    out = model.fit({'IN':x_train},
                    {'OUT':y_train[:,1]},
                    sample_weight=y_train[:,0],
                    epochs=params['epochs'],
                    batch_size=params['batch_size'],
                    verbose=2,
                    validation_data=({'IN':x_val},{'OUT':y_val[:,1]},y_val[:,0]),
                    callbacks=Callback_list
                    )

    return out,model

class HyperModel:
    #################################################################################################
    # __init ___#
    #################################################################################################
    def __init__(self,name,sample):
        self.name = name
        self.sample = sample
        logging.info((' Starting '+self.sample+' case ').center(80,'='))

    #################################################################################################
    # HyperScan #
    #################################################################################################
    def HyperScan(self,x_train,y_train,task):
        """
        Performs the scan for hyperparameters
        Inputs :
            - x_train : numpy array [:,18]
                input training values (aka : 4-vec of 4 particles + MET)
            - y_train : numpy array [:,2]
                y_train = [weights, outputs (aka MEM weights)] 
            - name : str
                name of the dataset
            - sample : str
                name of the sample time : either DY or TT
            - task : str
                name of the dict to be used if specified (otherwise, use the full one)
        Outputs :
            - h = Class Scan() object
                object from class Scan to be used by other functions
        Reference : /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/scan/Scan.py
        """
        logging.info(' Starting scan '.center(80,'-'))

        # Records #
        self.x_train = x_train
        self.y_train = y_train
        self.task = task

        # Talos hyperscan parameters #
        if self.task!='': # if task is specified load it otherwise get it from parameters.py
            with open(os.path.join(parameters.main_path,'split',self.name,self.task), 'rb') as f:
                self.p = pickle.load(f)
        else: # We need the full dict
            self.p = parameters.p

        #p = {
        #        'lr' : 0.001,
        #        'first_neuron' : 20,
        #        'activation' : tanh,
        #        'dropout' : 0.5,
        #        'hidden_layers' : 1,
        #        'output_activation' : relu,
        #        'epochs' : 50,
        #        'batch_size' : 5,
        #        'loss_function' : binary_crossentropy,
        #        'optimizer': RMSprop
        #    }
        #out, model = InterpolationModel(x_train,y_train,x_train,y_train,p)
        #sys.exit()
        no = 1
        self.name = self.name+'_'+self.sample+self.task.replace('.pkl','')
        self.path_model = os.path.join(parameters.main_path,'model',self.name)
        while os.path.exists(self.name+str(no)+'.csv'):
            no +=1
        
        self.name_model = self.name+'_'+str(no)

        parallel_gpu_jobs(0.5)
        self.h = Scan(  x=self.x_train,
                   y=self.y_train,
                   params=self.p,
                   dataset_name=self.name,
                   experiment_no=str(no),
                   model=InterpolationModel,
                   val_split=0.3,
                   reduction_metric='val_loss',
                   #grid_downsample=0.1,
                   #random_method='lhs',
                   #reduction_method='spear',
                   #reduction_window=1000,
                   #reduction_interval=100,
                   #last_epoch_value=True,
                   print_params=True
                )

        # returns the experiment configuration details
        logging.info('='*80)
        logging.debug('Details')
        logging.debug(self.h.details)

#################################################################################################
# HyperEvaluate #
#################################################################################################
    def HyperEvaluate(self,x_test,y_test,folds=5):
        """
        Performs the cross-validation of the different models
        Inputs :
            - h = Class Scan() object
                object from class Scan coming from HyperScan
            - x_test : numpy array [:,18]
                input testing values (aka : 4-vec of 4 particles + MET)
            - y_test : numpy array [:,1]
                output testing values (aka : weight), not used during learning
            - folds : int (default = 5)
                Number of cross-validation folds
            - name : str
                Name of the csv file (without .csv) created by the scan
        Outputs :
            - idx_best_eval : idx
                Index of best model according to cross-validation

        Reference :
            /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/commands/evaluate.py
        """
        logging.info(' Starting evaluation '.center(80,'-'))

        # Records #
        self.x_test = x_test
        self.y_test = y_test


        # Predict to get number of round #
        r = Reporting(self.h)
        n_rounds = r.rounds()

        # Evaluation #
        logging.info('='*80)
        scores = []
        self.idx_best_model = best_model(self.h, 'val_loss', asc=True)

        for i in range(0,n_rounds):
            e = Evaluate(self.h)
            score = e.evaluate(x=self.x_test,
                               y=self.y_test,
                               model_id = i,
                               folds=folds,
                               shuffle=True,
                               metric='val_loss',
                               average='macro',
                               asc=True  # because loss
                              )
            score.append(i) # score = [mean(error),std(error),model_index]
            scores.append(score)

        # Sort scores #
        sorted_scores = sorted(scores,key=lambda x : x[0])
        self.idx_best_eval = sorted_scores[0][2]

        # Print ordered scores #
        count = 0
        for m_err,std_err, idx in sorted_scores:
            count += 1
            if count == 10:
                logging.info('...')
            if count >= 10 and n_rounds-count>5: # avoids printing intermediate useless states
                continue
            # Print model and error in order #
            logging.info('Model index %d -> Error = %0.5f (+/- %0.5f))'%(idx,m_err,std_err))
            if idx==self.idx_best_model:
                logging.info('\t-> Best model from val_loss')

        logging.info('='*80)

        # Prints best model accordind to cross-validation and val_loss #

        logging.info('Best model from val_loss -> id %d'%(self.idx_best_model))
        logging.info('Eval error : %0.5f (+/- %0.5f))'%(scores[self.idx_best_model][0],scores[self.idx_best_model][1]))
        logging.info(self.h.data.iloc[self.idx_best_model,:])
        logging.info('-'*80)

        logging.info('Best model from cross validation -> id %d'%(self.idx_best_eval))
        if self.idx_best_eval==self.idx_best_model:
            logging.info('Same model')
        else:
            logging.info('Eval error : %0.5f (+/- %0.5f))'%(scores[self.idx_best_eval][0],scores[self.idx_best_eval][1]))
            logging.info(self.h.data.iloc[self.idx_best_eval,:])
        logging.info('-'*80)

        # WARNING : model id's starts with 0 BUT on panda dataframe h.data, models start at 1

        # Add error to csv file #
        try:
            # Input scan csv file #
            with open(os.path.abspath(self.name_model+'.csv'), 'r') as the_file:
                lis=[line for line in the_file]  
                
            # Append the list with the error of each model #
            lis[0] = lis[0].rstrip() 
            lis[0] +=',eval_error,eval_std_error\n'
            for i in range(1,len(lis)):
                lis[i] = lis[i].rstrip()
                lis[i] += (',%0.5f,%0.5f\n'%(scores[i-1][0],scores[i-1][1]))

            # Re-write the csv file #
            with open(os.path.abspath(self.name_model+'.csv'), 'w') as the_file:
                for line in lis:
                    the_file.write(line)
        except:
            logging.warning('Could not append csv file with the model error')

#################################################################################################
# HyperDeploy #
#################################################################################################
    def HyperDeploy(self,best='eval_error'):
        """
        Performs the cross-validation of the different models
        Inputs :
            - h = Class Scan() object
                object from class Scan coming from HyperScan
            - name : str
                Name of the model package to be saved on disk
            - best : str
                index of the best model
                    -> 'eval_error' (default) : Select the one with best error from cross-validation
                    -> 'val_loss' : Select the one with lowest val_loss

        Reference :
            /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/commands/deploy.py
        """
        logging.info(' Starting deployment '.center(80,'-'))

        # Check arguments #
        if best != 'val_loss' and best != 'eval_error' : 
            logging.critical('Model not saved as .zip due to incorrect best model parameter')
        if self.idx_best_model==self.idx_best_eval:
            logging.warning('Best models according to val_loss and cross-validation are the same')

        # Save models #
        if best == 'val_loss':
            Deploy(self.h,model_name=self.name_model,best_idx=self.idx_best_model,metric='val_loss',asc=True)
            logging.warning('Best model saved according to val_loss')
        if best == 'eval_error':
            Deploy(self.h,model_name=self.name_model,best_idx=self.idx_best_eval,metric='val_loss',asc=True)

        # Move csv file to model dir #
        if self.task == '': # if not split+submit -> because submit will put it in slurm dir
            try:
                shutil.move(self.name_model+'.csv',os.path.join(parameters.main_path,'model',self.name_model+'.csv'))
            except:
                logging.warning('[WARNING] Could not move file to model folder')
                logging.warning('\tAttempted to move '+(os.path.abspath(self.name_model+'.csv') +' -> ' +os.path.join(parameters.main_path,'model',self.name_model+'.csv'))) 
        
        # Move zip file to model dir #
        if self.task == '': # if not split+submit -> because submit will put it in slurm dir
            try:
                shutil.move(self.name_model+'.zip',os.path.join(parameters.main_path,'model',self.name_model+'.zip'))
            except:
                logging.warning('[WARNING] Could not move file to model folder')
                logging.warning('\tAttempted to move '+(os.path.abspath(self.name_model+'.zip') +' -> ' +os.path.join(parameters.main_path,'model',self.name_model+'.zip'))) 

#################################################################################################
# HyperReport #
#################################################################################################
    def HyperReport(self):
        """
        Reports the model from csv file of previous scan
        Plot several quantities and comparisons in dir /$name/
        Inputs :
            - name : str
                Name of the csv file
            - sample : str
                either TT or DY 
        Reference :
        """
        logging.info(' Starting reporting '.center(80,'-'))

        # Get reporting #
        report_file = os.path.join('model',self.name+'_'+self.sample+'_1'+'.csv')
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
        try:
            logging.info('Lowest eval_error = %0.5f obtained after %0.f rounds'%(r.low('eval_error'),r.rounds2high('eval_error')))
        except:
            logging.warning("Could not find key 'eval_error', will switch to 'val_loss'")
            logging.info('Lowest val_loss = %0.5f obtained after %0.f rounds'%(r.low('val_loss'),r.rounds2high('val_loss')))

        # Best params #
        logging.info('='*80)
        logging.info('Best parameters sets')
        try:
            sorted_data = r.data.sort_values('eval_error',ascending=True)
        except:
            logging.warning("Could not find key 'eval_error', will swith to val_loss")
            sorted_data = r.data.sort_values('val_loss',ascending=True)

        for i in range(0,5):
            logging.info('-'*80)
            logging.info('Best params n°%d'%(i+1))
            try:
                logging.info(sorted_data.iloc[i])
            except:
                logging.warning('\tNo more parameters')
                break

        logging.info('='*80)

        # Generate dir #
        path_plot = os.path.join(parameters.main_path,'model',self.name+'_'+self.sample)
        if not os.path.isdir(path_plot):
            os.makedirs(path_plot)
        
        logging.info('Starting plots')
        # Make plots #
        PlotScans(data=r.data,path=path_plot,tag=self.sample)

#################################################################################################
# HyperRestore #
#################################################################################################
    def HyperRestore(self,inputs):
        """
        Retrieve a zip containing the best model, parameters, x and y data, ... and restores it
        Produces an output from the input numpy array
        Inputs :
            - inputs :  numpy array [:,18]
                Inputs to be evaluated
            - path : str
                path to the model archive
        Outputs
            - output : numpy array [:,1]
                output of the given model

        Reference :
            /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/commands/restore.py
        """
        logging.info(' Starting restoration '.center(80,'-'))
        # Restore model #
        a = Restore(os.path.join(parameters.main_path,'model',self.name+'_'+self.sample+'_1.zip'))

        # Output of the model #
        outputs = a.model.predict(inputs)

        return outputs
