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
    def __init__(self,path,inputs,outputs,batch_size=32,training=True,preload=1,scaler_path=None):
        self.path       = path                          # Path to root file 
        self.inputs     = inputs                        # List of strings of the variables as inputs
        self.outputs    = outputs                       # List of strings of the variables as outputs
        self.batch_size = batch_size                    # Batch size
        self.list_files = glob.glob(path+'/*.root')     # List of files obtained from path
        self.training   = training                      # True if training, False if validation (for printing purpose)
        self.preload    = preload                       # Multiple of batch_size to load already
        self.X          = np.zeros((self.batch_size*self.preload,len(self.inputs))) # array of inputs
        self.Y          = np.zeros((self.batch_size*self.preload,len(self.outputs)))# array of outputs
        self.get_fractions()

        self.n          = 0
        self.max        = self.__len__()

        if (len(self.list_files)>self.batch_size):
            logging.warning("Fewer files than requested batch size, might be errors")
        if self.training:
            logging.info("Starting importation for training set")
        else:
            logging.info("Starting importation for validation set")


        # Preprocessing #
        if scaler_path is not None:
            with open(scaler_path, 'rb') as handle:
                self.scaler = pickle.load(handle)
            logging.info('A preprocessing scaler has been imported')

            

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
        for i,(key,val) in enumerate(entries.items()):
            size_in_batch = math.ceil((val//self.n_tot)*self.batch_size)# keep same ratios in batch as in total sample
            self.batch_sample[key] = size_in_batch 
            total_in_batch += size_in_batch
            self.pointer[key] = 0 # Keep track of chunks
        # IF all contributions are too much
        if total_in_batch > self.batch_size: # taken too much, remove from most present sample
            key, value = max(self.batch_sample.items(), key = lambda p: p[1])
            self.batch_sample[key] -= (total_in_batch - self.batch_size)
        # Get maximum number of batches #
        #self.n_batches = np.inf
        self.n_batches = np.inf
        for filename,entries in entries.items():
            size = self.batch_sample[filename]
            if entries//size < self.n_batches : 
                self.n_batches = entries//size

        logging.info("Total number of events : %d"%(self.n_tot))
        logging.info("Will use %d batches of %d events"%(self.n_batches,self.batch_size))
        logging.info("="*80)

#    def load_array(self):
#        logging.debug("-"*80)
#        logging.debug("Load new chunk of size %d"%(self.batch_size*self.preload))
#
#        # Get chunks for each sample #
#        chuncks = dict()
#        for f,size in self.batch_sample.items():
#            chunk_size = size*self.preload
#            chuncks[self.pointer[f]:self.pointer[k]+chunk_size,:] = rec2array(root2array(f,treename='tree',branches=self.inputs+self.outputs,start=self.pointer[f],stop=self.pointer[k]+chunk_size))
#            self.pointer[f] += chunk_size
#
#        # Split the chunks into full arrays #
#        idx = 0
#        for i in range(0,preload):
#            for f in chunks.keys():
#                size = self.batch_sample[f]
#                arr  = chunks[f][i*size:(i+1)*size]
#                self.X[idx,idx+size] = arr[:,:len(self.inputs)] 
#                self.Y[idx,idx+size] = arr[:,-len(self.outputs):] 
#                idx += size
#
#    def reset_pointers(self):
#        for key in self.pointers.keys():
#            self.pointers[key] = 0

    def __getitem__(self,index): # gets the batch for the supplied index
        # return a tuple (numpy array of image, numpy array of labels) or None at epoch end
        logging.debug("-"*80)
        logging.debug("New batch importation")
        # First importation #
        #if index == 0:
        #    self.reset_pointers()
        #    self.load_arrays()
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

        # Preprocessing #
        try:
            X = self.scaler.transform(X)
        except:
            pass


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
