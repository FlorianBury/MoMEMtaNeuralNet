import sys
import glob
import os
import math
import logging
import pickle

import numpy as np
import keras

import ROOT

from root_numpy import root2array, rec2array

class DataGenerator(keras.utils.Sequence):
    def __init__(self,path,inputs,outputs,batch_size=32,training=True):
        self.path       = path                          # Path to root file 
        self.inputs     = inputs                        # List of strings of the variables as inputs
        self.outputs    = outputs                       # List of strings of the variables as outputs
        self.batch_size = batch_size                    # Batch size
        self.list_files = glob.glob(path+'/*.root')     # List of files obtained from path
        self.training   = training                      # True if training, False if validation (for printing purpose)
        self.get_fractions()

        self.n          = 0
        self.max        = self.__len__()

        if (len(self.list_files)>self.batch_size):
            logging.warning("Fewer files than requested batch size, might be errors")
        if self.training:
            logging.info("Starting importation for training set")
        else:
            logging.info("Starting importation for validation set")

    def get_fractions(self):
        entries = dict() # fraction inside each dataset compared to total
        self.batch_sample = dict() # number of events in each dataset that will enter the batch
        self.pointer = dict()  # Keep memory of how far we have extracted the chunk
        # Compute entries #
        self.n_tot = 0
        for f in self.list_files:
            rootFile = ROOT.TFile(f)
            tree = rootFile.Get('tree')
            n = tree.GetEntries()
            logging.info("Number of entries of file %s : %d"%(f,n))
            entries[f] = n
            self.n_tot += n

        # Fill batch contributions #
        total_in_batch = 0
        for i,(filename,n_entries) in enumerate(entries.items()):
            size_in_batch = math.ceil((n_entries/self.n_tot)*self.batch_size)# keep same ratios in batch as in total sample
            self.batch_sample[filename] = size_in_batch 
            total_in_batch += size_in_batch
        # IF all contributions are too much
        if total_in_batch > self.batch_size: # taken too much, remove from most present sample
            key, value = max(self.batch_sample.items(), key = lambda p: p[1])
            self.batch_sample[key] -= (total_in_batch - self.batch_size)
        # Get maximum number of batches #
        self.n_batches = np.inf
        for filename,n_entries in entries.items():
            size = self.batch_sample[filename]
            if n_entries//size < self.n_batches : 
                self.n_batches = n_entries//size

        logging.info("Total number of events : %d"%(self.n_tot))
        logging.info("Will use %d batches of %d events"%(self.n_batches,self.batch_size))
        logging.info("="*80)

    def __getitem__(self,index): # gets the batch for the supplied index
        # return a tuple (numpy array of image, numpy array of labels) or None at epoch end
        logging.debug("-"*80)
        logging.debug("New batch importation")
        X = np.zeros((self.batch_size,len(self.inputs)))
        Y = np.zeros((self.batch_size,len(self.outputs)))
        pointer = 0

        for f,size in self.batch_sample.items():
            size = int(size) # For python2
            X[pointer:pointer+size,:]= rec2array(root2array(f,treename='tree',branches=self.inputs,start=index*size,stop=(index+1)*size))
            Y[pointer:pointer+size,:] = rec2array(root2array(f,treename='tree',branches=self.outputs,start=index*size,stop=(index+1)*size))
            pointer += size
            if self.training:
                logging.debug('Training   - Added %d entries from file %s'%(size,os.path.basename(f)))
            else:
                logging.debug('Validation - Added %d entries from file %s'%(size,os.path.basename(f)))

        return X,Y

    def __len__(self): # gets the number of batches
        # return the number of batches in this epoch (do not change in the middle of an epoch)
        return self.n_batches
    def on_epoch_end(self): # performs auto shuffle if enabled
        # Do what we need to do between epochs
        pass

    def __next__(self):
        if self.n >= self.max:
           self.n = 0
        result = self.__getitem__(self.n)
        self.n += 1
        return result
