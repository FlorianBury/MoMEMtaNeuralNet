import glob
import os
import re
import math
import sys
import json
import shutil
import pickle
import pprint

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
            if i == self.params_per_job:
                i=0
                _list_dict.append(one_dict)

        return _list_dict

    def _save_as_pickle(self):
        # Remove dir if already exist #
        path_dict = os.path.join(parameters.main_path,'split',self.dir_name)
        if os.path.exists(path_dict):
            shutil.rmtree(path_dict) 

        # Create dir #
        os.makedirs(path_dict)

        # Dump each dict into separate pkl file #
        for i,d in enumerate(self.list_dict):
            with open(path_dict+'/dict_'+str(i)+'.pkl', 'wb') as f: 
                pickle.dump(d, f)  
        print ('[INFO] Generated ',len(self.list_dict),' dict of parameters at \n\t',path_dict)

#################################################################################################
# DictSplit #
#################################################################################################
    
def DictSplit(params_per_job,name):
        
    # Retrieve Hyperparameter dict #    
    p = parameters.p

    if params_per_job == -1: # params_per_job = number of params in set  
        tot = 0
        for val in p.values():
            tot += len(val)
        params_per_job = tot
        logging.info('Single dict of %d parameters has been created'%(params_per_job))
    # Split into sub dict #
    SplitTraining(p,params_per_job=params_per_job,dir_name=name)

if __name__ == '__main__':
    main()
