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
from keras.callbacks import EarlyStopping, ReduceLROnPlateau, TensorBoard
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
from preprocessing import PreprocessLayer
from data_generator import DataGenerator

#################################################################################################
# LossHistory #
#################################################################################################
class LossHistory(keras.callbacks.Callback):
    """ Records the history of the training per epoch and per batch """
    def on_train_begin(self, logs={}):
        self.batch_loss         = {'batch':[], 'loss':[]}
        self.epoch_loss         = {'epoch':[], 'loss':[]}
        self.epoch_val_loss     = {'epoch':[], 'loss':[]}
        self.epoch_lr           = {'epoch':[], 'lr':[]}
        self.epoch_counter      = 0
        self.batch_counter      = 0
        self.epoch_to_batch     = 0

    def on_batch_end(self, batch, logs={}):
        self.batch_loss['batch'].append(batch + self.epoch_to_batch)
        self.batch_loss['loss'].append(logs.get('loss'))
        self.batch_counter += 1

    def on_epoch_end(self, epoch, logs={}):
        self.epoch_loss['epoch'].append(epoch)
        self.epoch_loss['loss'].append(logs.get('loss'))
        self.epoch_val_loss['epoch'].append(epoch)
        self.epoch_val_loss['loss'].append(logs.get('val_loss'))
        self.epoch_lr['epoch'].append(epoch)
        self.epoch_lr['lr'].append(K.eval(self.model.optimizer.lr))

        # Batch counting #
        self.epoch_counter += 1
        self.epoch_to_batch += self.batch_counter
        self.batch_counter = 0

#################################################################################################
# PlotHistory #
#################################################################################################
def PlotHistory(history):
    # Figure #
    fig = plt.figure(figsize=(6,9))
    ax1 = plt.subplot(311)
    ax2 = plt.subplot(312)
    ax3 = plt.subplot(313)
    plt.subplots_adjust(hspace=0.4)

    # Plots #
    ax1.plot(history.epoch_loss['epoch'],history.epoch_loss['loss'],c='r',label='train')
    ax1.plot(history.epoch_val_loss['epoch'],history.epoch_val_loss['loss'],c='g',label='test')
    ax2.plot(history.batch_loss['batch'],history.batch_loss['loss'],c='r',label='train')
    #ax2.set_yscale("log")
    ax3.plot(history.epoch_lr['epoch'],history.epoch_lr['lr'])
    
    # Labels and titles #
    ax1.set_ylabel('loss')
    ax2.set_ylabel('loss')
    ax1.set_xlabel('epoch')
    ax2.set_xlabel('batch')
    ax3.set_xlabel('epoch')
    ax1.set_title('Loss over epochs')
    ax2.set_title('Loss over batches')
    ax3.set_title('Learning rate')
    ax1.legend(loc='upper right')
    ax2.legend(loc='upper right')
    #ax1.set_yscale('log')
    #ax2.set_yscale('log')

    # Save #
    rand_hash = ''.join(random.choice(string.ascii_uppercase) for _ in range(10)) # avoids overwritting
    png_name = 'Loss_%s.png'%rand_hash
    fig.savefig(png_name)
    logging.info('Curves saved as %s'%png_name)

#################################################################################################
# NeuralNetModel #
#################################################################################################
def NeuralNetModel(x_train,y_train,x_val,y_val,params):
    """
    Keras model for the Neural Network, used to scan the hyperparameter space by Talos
    Careful : y -> [output[N],weight[1]]
    In this case : regress the MEM using the 4-momentas
    """
    # Use the log of the output #
    y_train = y_train.astype(np.float64) # because type issues
    y_val = y_val.astype(np.float64) # because type issues
    w_train = y_train[:,-1]
    w_val = y_val[:,-1]
    #y_train = -np.log10(y_train[:,:-1])
    #y_val = -np.log10(y_val[:,:-1])
    y_train = y_train[:,:-1]
    y_val = y_val[:,:-1]
    
    # Design network #
    with open(os.path.join(parameters.main_path,'scaler_'+parameters.suffix+'.pkl'), 'rb') as handle: # Import scaler that was created before
        scaler = pickle.load(handle)
    IN = Input(shape=(x_train.shape[1],),name='IN')
    L0 = PreprocessLayer(batch_size=params['batch_size'],mean=scaler.mean_,std=scaler.scale_,name='Preprocess')(IN)
    L1 = Dense(params['first_neuron'],
               activation=params['activation'],
               kernel_regularizer=l2(params['l2']))(L0)
    HIDDEN = hidden_layers(params,1,batch_normalization=False).API(L1)
    OUT = Dense(1,activation=params['output_activation'],name='OUT')(HIDDEN)

    # Define model #
    model = Model(inputs=[IN], outputs=[OUT])
    utils.print_summary(model=model) #used to print model

    # Callbacks #
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0., patience=25, verbose=1, mode='min')
    reduceLR = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=10, verbose=1, mode='min', cooldown=1, min_lr=1e-6)
    loss_history = LossHistory()
    Callback_list = [loss_history,early_stopping,reduceLR]

    # Check normalization ##
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
                    verbose=2,
                    validation_data=({'IN':x_val},{'OUT':y_val},w_val),
                    callbacks=Callback_list
                    )

    # Plot history #
    PlotHistory(loss_history)
    
    return history,model

#################################################################################################
# ClassificationModel #
#################################################################################################
def ClassificationModel(x_train,y_train,x_val,y_val,params):
    """
    Keras model for the Neural Network, used to scan the hyperparameter space by Talos
    Careful : y -> [output[N],weight[1]]
    In this case : classify in three categories using the MEM
    """
    # Use the log of the output #
    #y_train = y_train.astype(np.float64) # because type issues
    #y_val = y_val.astype(np.float64) # because type issues
    w_train = y_train[:,-1]
    w_val = y_val[:,-1]
    y_train = y_train[:,:-1]
    y_val= y_val[:,:-1]
    
    # Design network #
    with open(os.path.join(parameters.main_path,'scaler_'+parameters.suffix+'.pkl'), 'rb') as handle: # Import scaler that was created before
        scaler = pickle.load(handle)
    IN = Input(shape=(x_train.shape[1],),name='IN')
    L0 = PreprocessLayer(batch_size=params['batch_size'],mean=scaler.mean_,std=scaler.scale_,name='Preprocess')(IN)
    L1 = Dense(params['first_neuron'],
               activation=params['activation'],
               kernel_regularizer=l2(params['l2']))(IN)
    HIDDEN = hidden_layers(params,3,batch_normalization=False).API(L0)
    OUT = Dense(3,activation=params['output_activation'],name='OUT')(HIDDEN)

    # Define model #
    model = Model(inputs=[IN], outputs=[OUT])
    utils.print_summary(model=model) #used to print model

    # Callbacks #
    early_stopping = EarlyStopping(monitor='val_acc', min_delta=0., patience=15, verbose=1, mode='max')
    reduceLR = ReduceLROnPlateau(monitor='val_acc', factor=0.5, patience=8, verbose=1, mode='max', cooldown=1, min_lr=1e-6)
    loss_history = LossHistory()
    Callback_list = [loss_history,early_stopping,reduceLR]

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
                    verbose=2,
                    validation_data=({'IN':x_val},{'OUT':y_val},w_val),
                    callbacks=Callback_list
                    )

    # Plot history #
    PlotHistory(loss_history)

    return history,model

#################################################################################################
# BinaryModel #
#################################################################################################
def BinaryModel(x_train,y_train,x_val,y_val,params):
    """
    Keras model for the Neural Network, used to scan the hyperparameter space by Talos
    Careful : y -> [output[N],weight[1]]
    In this case : classify between background and signal 
e   """
    # Use the log of the output #
    #y_train = y_train.astype(np.float64) # because type issues
    #y_val = y_val.astype(np.float64) # because type issues
    w_train = y_train[:,-1]
    w_val = y_val[:,-1]
    y_train = y_train[:,:-1]
    y_val= y_val[:,:-1]
    
    # Design network #
    with open(os.path.join(parameters.main_path,'scaler_'+parameters.suffix+'.pkl'), 'rb') as handle: # Import scaler that was created before
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
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0., patience=50, verbose=1, mode='min')
    reduceLR = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=10, verbose=1, mode='min', cooldown=1, min_lr=1e-6)
    loss_history = LossHistory()
    Callback_list = [loss_history,early_stopping,reduceLR]

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
                    verbose=2,
                    validation_data=({'IN':x_val},{'OUT':y_val},w_val),
                    callbacks=Callback_list
                    )

    # Plot history #
    PlotHistory(loss_history)
    
    return history,model


#################################################################################################
# NeuralNetGeneratorModel#
#################################################################################################
def NeuralNetGeneratorModel(x_train,y_train,x_val,y_val,params):
    """
    Keras model for the Neural Network, used to scan the hyperparameter space by Talos
    Uses the generator rather than the input data (which are dummies)
    """
    
    # Design network #
    with open(os.path.join(parameters.main_path,'scaler_'+parameters.suffix+'.pkl'), 'rb') as handle: # Import scaler that was created before
        scaler = pickle.load(handle)
    IN = Input(shape=(x_train.shape[1],),name='IN')
    L0 = PreprocessLayer(batch_size=params['batch_size'],mean=scaler.mean_,std=scaler.scale_,name='Preprocess')(IN)
    L1 = Dense(params['first_neuron'],
               activation=params['activation'],
               kernel_regularizer=l2(params['l2']))(L0)
    HIDDEN = hidden_layers(params,1,batch_normalization=True).API(L1)
    OUT = Dense(1,activation=params['output_activation'],name='OUT')(HIDDEN)


    #preprocess = Model(inputs=[IN],outputs=[L0])
    #utils.print_summary(model=preprocess)
    
    # Tensorboard logs #
    path_board = os.path.join(parameters.main_path,"TensorBoard")
    suffix = 0
    while(os.path.exists(os.path.join(path_board,"Run_"+str(suffix)))):
        suffix += 1
    path_board = os.path.join(path_board,"Run_"+str(suffix))
    os.makedirs(path_board)
    logging.info("TensorBoard log dir is at %s"%path_board)

    # Callbacks #
    early_stopping = EarlyStopping(monitor='val_loss', 
                                   min_delta=0., 
                                   patience=50, 
                                   verbose=1, 
                                   mode='min')
    reduceLR = ReduceLROnPlateau(monitor='val_loss', 
                                 factor=0.5, 
                                 patience=20, 
                                 verbose=1, 
                                 mode='min', 
                                 cooldown=10,
                                 min_lr=1e-5)
    loss_history = LossHistory()
    board = TensorBoard(log_dir=path_board, 
                        histogram_freq=1, 
                        batch_size=params['batch_size'], 
                        write_graph=True, 
                        write_grads=True, 
                        write_images=True)
                        #embeddings_freq=0, 
                        #embeddings_layer_names=None, 
                        #embeddings_metadata=None, 
                        #embeddings_data=None, 
                        #update_freq='epoch')
    Callback_list = [loss_history,early_stopping,reduceLR,board]
    #Callback_list = [loss_history,reduceLR,board]

    # Check if generator weights has been asked #
    weights_generator = parameters.weights_generator if 'generator_weights' in params and params['generator_weights'] else ''

    # Compile #
    if 'resume' not in params: 
        # Define model #
        model = Model(inputs=[IN], outputs=[OUT])
        utils.print_summary(model=model) #used to print model
        # Compile it #
        model.compile(optimizer=Adam(lr=params['lr']),
                      loss={'OUT':params['loss_function']},
                      metrics=['accuracy'])
        initial_epoch = 0
    else: # a model has to be imported and resumes training
        custom_objects =  {'PreprocessLayer': PreprocessLayer}
        logging.info("Loaded model %s"%params['resume'])
        a = Restore(params['resume'],custom_objects=custom_objects,method='h5')
        model = a.model
        model.compile(optimizer=Adam(lr=params['lr']),
                      loss={'OUT':params['loss_function']},
                      metrics=['accuracy'])
        utils.print_summary(model=model) #used to print model
        #initial_epoch = a.params['epochs'][0]  
        initial_epoch = params['initial_epoch']
        
    # Generator #
    training_generator = DataGenerator(path = parameters.path_gen_training,
                                       inputs = parameters.inputs,
                                       outputs = parameters.outputs,
                                       batch_size = params['batch_size'],
                                       state_set = 'training',
                                       weights_generator = weights_generator)
    validation_generator = DataGenerator(path = parameters.path_gen_validation,
                                       inputs = parameters.inputs,
                                       outputs = parameters.outputs,
                                       batch_size = params['batch_size'],
                                       state_set = 'validation')
                                       #weights_generator = weights_generator) # Might be unnecessary

        # Fit #
    logging.info("Will use %d workers"%parameters.workers)
    logging.warning("Keras location " + keras.__file__)
    logging.warning("Tensorflow location "+ tf.__file__)
    logging.warning("GPU ")
    logging.warning(K.tensorflow_backend._get_available_gpus())
    history = model.fit_generator(generator             = training_generator,
                                  validation_data       = validation_generator,
                                  epochs                = params['epochs'], 
                                  verbose               = 1,
                                  max_queue_size        = parameters.workers*2,
                                  callbacks             = Callback_list,
                                  initial_epoch         = initial_epoch,
                                  workers               = parameters.workers,
                                  shuffle               = True,
                                  #steps_per_epoch       = 20,
                                  use_multiprocessing   = True)
                                  
    #test_generator = DataGenerator(path = parameters.path_gen_output,
    #                                   inputs = parameters.inputs,
    #                                   outputs = parameters.outputs,
    #                                   batch_size = params['batch_size'],
    #out_preprocess = preprocess.predict_generator(test_generator,
    #                                              workers=10,
    #                                              steps=10, 
    #                                              use_multiprocessing=False,
    #                                              verbose=1)    
    #print ("Mean preprocessing")
    #print (np.mean(out_preprocess))
    #print (np.std(out_preprocess))
    #                                                
    #out_all = model.predict_generator(test_generator,
    #                                              workers=10,
    #                                              steps=10, 
    #                                              use_multiprocessing=False,
    #                                              verbose=1)    
    #                                                
    #print (out_all)
    #print ("Mean output")
    #print (np.mean(out_all))
    #print (np.std(out_all))

                               
    # Plot history #
    PlotHistory(loss_history)

    return history,model


