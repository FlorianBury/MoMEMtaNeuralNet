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
from preprocessing import PreprocessLayer

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
    In this case : regress the MEM using the 4-momentas
    """
    # Use the log of the output #
    y_train = y_train.astype(np.float64) # because type issues
    y_val = y_val.astype(np.float64) # because type issues
    w_train = y_train[:,-1]
    w_val = y_val[:,-1]
    y_train = -np.log10(y_train[:,:-1])
    y_val = -np.log10(y_val[:,:-1])
    
    # Design network #
    with open(os.path.join(parameters.main_path,parameters.scaler_name), 'rb') as handle: # Import scaler that was created before
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
    fig = plt.figure()
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    ax1.plot(history.history['loss'],c='r',label='train')
    ax1.plot(history.history['val_loss'],c='g',label='test')
    ax2.plot(loss_history.losses,c='r',label='train')
    ax2.plot(loss_history.val_losses,c='g',label='test')
    ax1.set_ylabel('loss')
    ax2.set_ylabel('loss')
    ax1.set_xlabel('epoch')
    ax2.set_xlabel('batch')
    ax1.set_title('Loss over epochs')
    ax2.set_title('Loss over batches')
    ax1.legend(loc='upper right')
    ax2.legend(loc='upper right')
    #ax1.set_yscale('log')
    #ax2.set_yscale('log')
    rand_hash = ''.join(random.choice(string.ascii_uppercase) for _ in range(10)) # avoids overwritting
    png_name = 'Loss_%s.png'%rand_hash
    fig.savefig(png_name)
    logging.info('Curves saved as %s'%png_name)

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
    #x_train = -np.log10(x_train)
    #x_val = -np.log10(x_val)
    
    # Design network #
    with open(os.path.abspath(parameters.scaler_name), 'rb') as handle: # Import scaler that was created before
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
    fig = plt.figure()
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    ax1.plot(history.history['loss'],c='r',label='train')
    ax1.plot(history.history['val_loss'],c='g',label='test')
    ax2.plot(loss_history.losses,c='r',label='train')
    ax2.plot(loss_history.val_losses,c='g',label='test')
    ax1.set_ylabel('loss')
    ax2.set_ylabel('loss')
    ax1.set_xlabel('epoch')
    ax2.set_xlabel('batch')
    ax1.set_title('Loss over epochs')
    ax2.set_title('Loss over batches')
    ax1.legend(loc='upper right')
    ax2.legend(loc='upper right')
    #ax1.set_yscale('log')
    #ax2.set_yscale('log')
    rand_hash = ''.join(random.choice(string.ascii_uppercase) for _ in range(10)) # avoids overwritting
    png_name = 'Loss_%s.png'%rand_hash
    fig.savefig(png_name)
    logging.info('Curves saved as %s'%png_name)

    return history,model





