import glob
import os
import re
import math
import sys
import json
import shutil
import pickle

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
#from parameters import * # Get the global variables 
import parameters

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
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0.0001, patience=10, verbose=1, mode='min')
    reduceLR = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, verbose=1, mode='min', epsilon=0.00001, cooldown=0, min_lr=0.00001)
    Callback_list = [early_stopping]

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
                    verbose=1,
                    validation_data=({'IN':x_val},{'OUT':y_val[:,1]},y_val[:,0]),
                    callbacks=Callback_list
                    )

    return out,model

#################################################################################################
# HyperScan #
#################################################################################################
def HyperScan(x_train,y_train,name,sample,task):
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
    Outputs :
        - h = Class Scan() object
            object from class Scan to be used by other functions
    Reference : /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/scan/Scan.py
    """
    # Talos hyperscan parameters #
    if task!='': # if task is specified load it otherwise get it from parameters.py
        with open(os.path.join(parameters.main_path,'split',task), 'rb') as f:
            p = pickle.load(f)
    else: # We need the full dict
        p = parameters.p

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
    name = name+'_'+sample+'_'+task
    path_name = parameters.main_path+name
    while os.path.exists(path_name+str(no)+'.csv'):
        no +=1


    parallel_gpu_jobs(0.5)
    h = Scan(  x=x_train,
               y=y_train,
               params=p,
               dataset_name=name,
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
    print
    print ('='*80,end='\n\n')
    print ('Details',end='\n\n')
    print (h.details)

    return h, name+'_'+str(no)

#################################################################################################
# HyperEvaluate #
#################################################################################################
def HyperEvaluate(h,x_test,y_test,folds=5):
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
    Outputs :
        - idx_best_eval : idx
            Index of best model according to cross-validation

    Reference :
        /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/commands/evaluate.py
    """


    # Predict to get number of round #
    r = Reporting(h)
    n_rounds = r.rounds()

    # Evaluation #
    print
    print ('='*80,end='\n\n')
    scores = []
    idx_best_model = best_model(h, 'val_loss', asc=True)

    for i in range(0,n_rounds):
        e = Evaluate(h)
        score = e.evaluate(x=x_test,
                           y=y_test,
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
    idx_best_eval = sorted_scores[0][2]

    # Print ordered scores #
    count = 0
    for m_err,std_err, idx in sorted_scores:
        count += 1
        if count == 10:
            print ('...')
        if count >= 10 and n_rounds-count>5: # avoids printing intermediate useless states
            continue
        # Print model and error in order #
        print ('Model index %d -> Error = %0.5f (+/- %0.5f))'%(idx,m_err,std_err))
        if idx==idx_best_model:
            print ('\t-> Best model from val_loss')

    print
    print ('='*80,end='\n\n')

    # Prints best model accordind to cross-validation and val_loss #

    print ('Best model from val_loss -> id ',idx_best_model)
    print ('Eval error : %0.5f (+/- %0.5f))'%(scores[idx_best_model][0],scores[idx_best_model][1]))
    print (h.data.iloc[idx_best_model,:])
    print ('-'*80,end='\n\n')

    print ('Best model from cross validation -> id ',idx_best_eval)
    if idx_best_eval==idx_best_model:
        print ('Same model')
    else:
        print ('Eval error : %0.5f (+/- %0.5f))'%(scores[idx_best_eval][0],scores[idx_best_eval][1]))
        print (h.data.iloc[idx_best_eval,:])
    print ('-'*80,end='\n\n')

    # WARNING : model id's starts with 0 BUT on panda dataframe h.data, models start at 1

    return idx_best_eval

#################################################################################################
# HyperDeploy #
#################################################################################################
def HyperDeploy(h,name,best):
    """
    Performs the cross-validation of the different models
    Inputs :
        - h = Class Scan() object
            object from class Scan coming from HyperScan
        - name : str
            Name of the model package to be saved on disk
        - best : int
            index of the best model
                -> -1 : not used HyperEvaluate => select the one with lowest val_loss
                -> >0 : comes from HyperEvaluate => the one with best error from cross-validation

    Reference :
        /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/commands/deploy.py
    """

    if best == -1:
        idx = best_model(h, 'val_loss', asc=True)
    else: # From HyperEvaluate
        idx = best


    Deploy(h,model_name=name,best_idx=idx,metric='val_loss',asc=True)

    try:
        shutil.move(name+'.zip',os.path.join(parameters.main_path,'model'))
    except:
        print ('[WARNING] Could not move file to model folder, maybe folder does not exits of file already present')
        print ('\tAttempted to move '+os.getcwd()+name+'.zip'+'  ->  '+parameters.main_path+'/model/'+name+'.zip') 


#################################################################################################
# HyperReport #
#################################################################################################
def HyperReport(name):
    """
    Reports the model from csv file of previous scan
    Plot several quantities and comparisons in dir /$name/
    Inputs :
        - name : str
            Name of the csv file
      
    Reference :
        /home/ucl/cp3/fbury/.local/lib/python3.6/site-packages/talos/commands/reporting.py
    """
    r = Reporting(name+'.csv')

    # returns the results dataframe
    print
    print ('='*80,end='\n\n')
    print ('Complete data after n_round = ',r.rounds(),':\n',r.data,end='\n\n')

    # Lowest val_loss #
    print
    print ('-'*80)
    print ('Lowest val_loss = ',r.low('val_loss'),' obtained after ',r.rounds2high('val_loss'))

    # Best params #
    print
    print ('='*80)
    print ('Best parameters sets')
    sorted_data = r.data.sort_values('val_loss',ascending=True)
    for i in range(0,3):
        print ('-'*80)
        print ('Best params n°',i+1)
        print (sorted_data.iloc[i])

    print ('='*80)

    # Few plots #
    path = os.path.join(parameters.main_path,name+'report')
    if not os.path.isdir(path):
        os.makedirs(path)

    print ('[INFO] Starting plot section')
    # Correlation #
    r.plot_corr(metric='val_loss')
    plt.savefig(path+'/correlation.png')

    # val_loss VS loss #
    r.plot_regs('loss','val_loss')
    plt.savefig(path+'/val_loss_VS_loss.png')

    # KDE #
    r.plot_kde('val_loss')
    plt.savefig(path+'/KDE_val_loss.png')

    #r.plot_kde(x='val_loss',y='lr')
    ast.kde(r.data,x='val_loss',y='lr',x_label='val_loss',y_label='learning_rate')
    plt.savefig(path+'/KDE_val_loss_lr.png')

    # Plot bars #
    ast.bargrid(r.data,x='epochs',y='val_loss',hue='batch_size',col='optimizer',col_wrap=2)
    plt.savefig(path+'/barplot_1.png')
    ast.bargrid(r.data,x='epochs',y='val_loss',hue='batch_size',col='loss_function',col_wrap=1)
    plt.savefig(path+'/barplot_2.png')
    ast.bargrid(r.data,x='first_neuron',y='val_loss',hue='activation',col='hidden_layers')
    plt.savefig(path+'/barplot_3.png')
    ast.bargrid(r.data,x='first_neuron',y='val_loss',hue='output_activation',col='hidden_layers')
    plt.savefig(path+'/barplot_4.png')
    ast.bargrid(r.data,x='dropout',y='val_loss',hue='lr',col='hidden_layers')
    plt.savefig(path+'/barplot_5.png')
#################################################################################################
# HyperRestore #
#################################################################################################
def HyperRestore(inputs,path):
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
    # Restore model #
    a = Restore(path)

    # Output of the model #
    outputs = a.model.predict(inputs)

    return outputs
