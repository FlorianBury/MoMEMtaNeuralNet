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

import array
import numpy as np
import itertools

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
from preprocessing import PreprocessLayer, MakeArrayMultiple, GenDictExtract
from plot_scans import PlotScans

#################################################################################################
# LossHistory #
#################################################################################################
class LossHistory(keras.callbacks.Callback):
    """ Records the history of the training per epoch and per batch """
    def on_train_begin(self, logs={}):
        self.losses = []
        self.val_losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))

#################################################################################################
# NeuralNetModel #
#################################################################################################
def NeuralNetModel(x_train,y_train,x_val,y_val,params):
    """
    Keras model for the Neural Network, used to scan the hyperparameter space by Talos
    Careful : y -> [output[N],weight[1]]
    """
    # Use the log of the output #
    y_train = y_train.astype(np.float64) # because type issues
    y_val = y_val.astype(np.float64) # because type issues
    w_train = y_train[:,-1]
    w_val = y_val[:,-1]
    y_train = -np.log10(y_train[:,:-1])
    y_val = -np.log10(y_val[:,:-1])
    print ("Number of features : ",x_train.shape[1])
    
    # Check if batch_size is divisor of training set, if not extend it #
    N_train = x_train.shape[0]
    N_val = x_val.shape[0]
    #if N_train%params['batch_size']!=0:
    #    x_train, y_train, w_train = MakeArrayMultiple([x_train, y_train, w_train],params['batch_size'],repeat=True)
    #    logging.warning("The batch size is not a divisor of the training set size (which is a problem for the preprocessing layer)")
    #    logging.warning("\tThe set has been extended with its own elements : size = %d -> %d (added %d)"%(N_train,x_train.shape[0],x_train.shape[0]-N_train))
    #if N_val%params['batch_size']!=0:
    #    x_val, y_val, w_val = MakeArrayMultiple([x_val, y_val, w_val],params['batch_size'],crop=True)
    #    logging.warning("The batch size is not a divisor of the validation set size (which is a problem for the preprocessing layer)")
    #    logging.warning("\tThe set has been cropped : size = %d -> %d (removed %d)"%(N_val,x_val.shape[0],N_val-x_val.shape[0]))
         

    # Design network #
    with open(os.path.abspath(parameters.scaler_name), 'rb') as handle: # Import scaler that was created before
        scaler = pickle.load(handle)
    IN = Input(shape=(x_train.shape[1],),name='IN')
    L0 = PreprocessLayer(batch_size=params['batch_size'],mean=scaler.mean_,std=scaler.scale_,name='Preprocess')(IN)
    L1 = Dense(params['first_neuron'],
               activation=params['activation'],
               kernel_regularizer=l2(params['l2']))(IN)
    HIDDEN = hidden_layers(params,1,batch_normalization=False).API(L0)
    OUT = Dense(1,activation=params['output_activation'],name='OUT')(HIDDEN)

    # Define model #
    model = Model(inputs=[IN], outputs=[OUT])
    utils.print_summary(model=model) #used to print model

    # Callbacks #
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0., patience=10, verbose=1, mode='min')
    reduceLR = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, verbose=1, mode='min', epsilon=0.001, cooldown=0, min_lr=0.00001)
    loss_history = LossHistory()
    Callback_list = [loss_history]#[early_stopping,reduceLR]

    # Check normalization #
    preprocess = Model(inputs=[IN],outputs=[L0])
    out_preprocess = preprocess.predict(x_train,batch_size=params['batch_size'])
    mean_scale = np.mean(out_preprocess)
    std_scale = np.std(out_preprocess)
    if abs(mean_scale)>0.01 or abs((std_scale-1)/std_scale)>0.01: # Check that scaling is correct to 1%
        logging.critical("Something is wrong with the preprocessing layer (mean = %0.6f, std = %0.6f), maybe you loaded an incorrect scaler"%(mean_scale,std_scale))
        sys.exit()

   # Compile #
    model.compile(optimizer=Adam(lr=params['lr']),
                  loss={'OUT':params['loss_function']},
                  metrics=['accuracy'])
    # Fit #
    history = model.fit({'IN':x_train},
                    {'OUT':y_train},
                    sample_weight=w_train,
                    epochs=params['epochs'],
                    batch_size=params['batch_size'],
                    verbose=1,
                    validation_data=({'IN':x_val},{'OUT':y_val},w_val),
                    callbacks=Callback_list
                    )

    # Plot history #
    fig = plt.figure()
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    ax1.plot(history.history['loss'],c='r',label='train')
    ax1.plot(history.history['val_loss'],c='g',label='test')
    ax2.plot(loss_history.losses,c='r',label='train')
    ax2.plot(loss_history.val_losses,c='g',label='test')
    plt.title('model loss')
    ax1.set_ylabel('loss')
    ax2.set_ylabel('loss')
    ax1.set_xlabel('epoch')
    ax2.set_xlabel('batch')
    ax1.legend(loc='upper right')
    ax2.legend(loc='upper right')
    ax1.set_yscale('log')
    ax2.set_yscale('log')
    rand_hash = ''.join(random.choice(string.ascii_uppercase) for _ in range(10)) # avoids overwritting
    png_name = 'Loss_%s.png'%rand_hash
    fig.savefig(png_name)
    logging.info('Curves saved as %s'%png_name)

    return history,model

#################################################################################################
# HyperModel #
#################################################################################################
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
        self.x_train, self.x_val, self.y_train, self.y_val = train_test_split(self.x,self.y,train_size=0.7)
        logging.info("Training set   : %d"%self.x_train.shape[0])
        logging.info("Evaluation set : %d"%self.x_val.shape[0])

        # Define scan object #
        #parallel_gpu_jobs(0.5)
        self.h = Scan(  x=self.x_train,
                   y=self.y_train,
                   params=self.p,
                   dataset_name=self.name,
                   experiment_no=str(no),
                   model=NeuralNetModel,
                   val_split=0.2,
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
                     folds = 5,
                     metric = 'val_loss',
                     asc = True,
                     shuffle = True,
                     average = None)  
        self.h_with_eval.data.to_csv(self.name_model+'.csv') # save to csv including error

        # returns the experiment configuration details
        logging.info('='*80)
        logging.debug('Details')
        logging.debug(self.h.details)

#################################################################################################
# HyperDeploy #
#################################################################################################
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

#################################################################################################
# HyperReport #
#################################################################################################
    def HyperReport(self):
        """
        Reports the model from csv file of previous scan
        Plot several quantities and comparisons in dir /$name/
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
        try:
            logging.info('Lowest eval_error = %0.5f obtained after %0.f rounds'%(r.low('eval_mean'),r.rounds2high('eval_mean')))
        except:
            logging.warning("Could not find key 'eval_mean', will switch to 'val_loss'")
            logging.info('Lowest val_loss = %0.5f obtained after %0.f rounds'%(r.low('val_loss'),r.rounds2high('val_loss')))

        # Best params #
        logging.info('='*80)
        logging.info('Best parameters sets')
        try:
            sorted_data = r.data.sort_values('eval_mean',ascending=True)
        except:
            logging.warning("Could not find key 'eval_mean', will swith to val_loss")
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
    def HyperRestore(self,inputs,batch_size=32):
        """
        Retrieve a zip containing the best model, parameters, x and y data, ... and restores it
        Produces an output from the input numpy array
        Reference :
            /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/commands/restore.py
        """
        logging.info((' Starting restoration of sample %s with model %s '%(self.sample,self.name)).center(80,'-'))
        # Load the scaler #
        custom_objects =  {'PreprocessLayer': PreprocessLayer}
        # Restore model #
        a = Restore(os.path.join(parameters.main_path,'model',self.name+'_'+self.sample+'.zip'),custom_objects = custom_objects)
        print (a.params)
        print (a.items)
        sys.exit()

        # Output of the model #
        outputs = a.model.predict(inputs,batch_size=batch_size)

        return outputs
