import glob
import os
import re
import math
import sys
import json
import shutil
import pickle
import pprint
import logging

import numpy as np
import itertools

from talos.parameters.ParamGrid import ParamGrid
from talos import Scan

# Personal files #
import parameters 

#################################################################################################
# SplitTraining #
#################################################################################################

class SplitTraining:

    def __init__(self,p,params_per_job,dir_name):
        self.params = p
        self.grid_downsample = None
        self.params_per_job = params_per_job
        self.dir_name = dir_name
    
        self.paramgrid_object = ParamGrid(self)

        # Generate grid #
        self.param_log, self.param_grid = self._generate_grid()
        logging.info("Number of hyperparameters : "+str(self.param_grid.shape[0]))
        if self.param_grid.shape[0] < self.params_per_job: # If more params_per_job than actual parameters, equal them
            self.params_per_job = self.param_grid.shape[0] 
            logging.warning('You specified a number of parameters per job higher than the actual number of parameters, will use the latter')
        if self.params_per_job == -1: # params_per_job = number of params in set  
            self.params_per_job = self.param_grid.shape[0]
            logging.info('Single dict of %d parameters has been created'%(self.params_per_job))



        # Split the list into dict #
        self.list_dict = self._split_dict()

        # Save as pickle file #
        self._save_as_pickle()

    def _generate_grid(self):

        _param_log = self.paramgrid_object.param_log
        _param_grid = self.paramgrid_object.param_grid  
        
        return _param_log,_param_grid 
        

    def _split_dict(self):
        _list_dict = []
        i = 0
        count = 0
        for param in self.param_grid:
            if i==0:
                # Initialize dict #
                one_dict = {}
                for key in self.params.keys():
                    one_dict[key] = []

            # Append each case #
            for p,k in zip(param,self.params.keys()):
                one_dict[k].append(p)

            i += 1
            count += 1
            if i == self.params_per_job:
                i=0
                _list_dict.append(one_dict)
            logging.debug("Creating the list - current status : %d/%d"%(count,self.param_grid.shape[0]))
        return _list_dict

    def _save_as_pickle(self):
        # Remove content of dir if already exists #
        path_dict = os.path.join(parameters.main_path,'split',self.dir_name)
        logging.debug('Directory containing the dict : %s'%(path_dict))
        if os.path.exists(path_dict):
            logging.debug('Removing older files')
            for file_pkl in glob.glob(os.path.join(path_dict,'*.pkl')):
                logging.debug('Removed file %s'%(file_pkl)) 
                os.remove(file_pkl)
        else:
            os.makedirs(path_dict)

        # Dump each dict into separate pkl file #
        for i,d in enumerate(self.list_dict):
            logging.debug("Writing the dict - current status : %d/%d"%(i,len(self.list_dict)))
            with open(path_dict+'/dict_'+str(i)+'.pkl', 'wb') as f: 
                pickle.dump(d, f)  
        logging.info('Generated %d dict of parameters at \t%s'%(len(self.list_dict),path_dict))

#################################################################################################
# DictSplit #
#################################################################################################
    
def DictSplit(params_per_job,name):
        
    # Retrieve Hyperparameter dict #    
    p = parameters.p

       # Split into sub dict #
    SplitTraining(p,params_per_job=params_per_job,dir_name=name)

if __name__ == '__main__':
    main()
