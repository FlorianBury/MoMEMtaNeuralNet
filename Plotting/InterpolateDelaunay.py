import os
import sys
import re
import argparse
import glob
import logging
import copy
import enlighten

import numpy as np
import pandas as pd
from scipy.interpolate import interp2d
from root_numpy import array2root

sys.path.insert(0,"..") # We need our own version of talos
                        # If we import our modules after the version is sites-package, our version is ignored
from import_tree import Tree2Pandas
from Utils import ListBranches
from signal_coupling import Decoupler

from ROOT import TGraph2D

import CMS_lumi
import tdrstyle

class InterpolationDelaunay:
    def __init__(self,x,y,z):
        self.graph = copy.deepcopy(TGraph2D(x.shape[0],x,y,-np.log10(z)))
    def interpolate(self,x,y):
        z = self.graph.Interpolate(x,y)
        return np.power(10,-z)

def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='From given set of root files, interpolate the MEM weight to a given mass points')
    parser.add_argument('-f','--file', action='store', required=True, type=str, default='',
                  help='File (fulle path) to be used')
    parser.add_argument('--MA', action='store', required=True, type=int, default=0,
                  help='MA value for the interpolation')
    parser.add_argument('--MH', action='store', required=True, type=int, default=0,
                  help='MH value for the interpolation')
    parser.add_argument('-v','--verbose', action='store_true', required=False, default=False,
            help='Show DEGUG logging')
    opt = parser.parse_args() 

    # Logging #
    if opt.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s') 
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
   #############################################################################################
    # Make likelihood map #
    #############################################################################################
    # Get events from tree #
    logging.info('Looking at file %s'%opt.file)
    variables  = [
                             'weight_HToZA_mH_200_mA_50',
                             'weight_HToZA_mH_200_mA_100',  
                             'weight_HToZA_mH_250_mA_50',   
                             'weight_HToZA_mH_250_mA_100',  
                             'weight_HToZA_mH_300_mA_50',   
                             'weight_HToZA_mH_300_mA_100',  
                             'weight_HToZA_mH_300_mA_200',  
                             'weight_HToZA_mH_500_mA_50',   
                             'weight_HToZA_mH_500_mA_100',  
                             'weight_HToZA_mH_500_mA_200',  
                             'weight_HToZA_mH_500_mA_300',  
                             'weight_HToZA_mH_500_mA_400',  
                             'weight_HToZA_mH_650_mA_50',   
                             'weight_HToZA_mH_800_mA_50',   
                             'weight_HToZA_mH_800_mA_100',  
                             'weight_HToZA_mH_800_mA_200',  
                             'weight_HToZA_mH_800_mA_400',  
                             'weight_HToZA_mH_800_mA_700',  
                             'weight_HToZA_mH_1000_mA_50',  
                             'weight_HToZA_mH_1000_mA_200', 
                             'weight_HToZA_mH_1000_mA_500', 
                             'weight_HToZA_mH_2000_mA_1000',
                             'weight_HToZA_mH_3000_mA_2000',
                 ]
    N = len(variables)
    #cuts =  " weight_HToZA_mH_200_mA_50>weight_HToZA_mH_200_mA_50_err && weight_HToZA_mH_200_mA_100>weight_HToZA_mH_200_mA_100_err && weight_HToZA_mH_250_mA_50>weight_HToZA_mH_250_mA_50_err && weight_HToZA_mH_250_mA_100>weight_HToZA_mH_250_mA_100_err && weight_HToZA_mH_300_mA_50>weight_HToZA_mH_300_mA_50_err && weight_HToZA_mH_300_mA_100>weight_HToZA_mH_300_mA_100_err && weight_HToZA_mH_300_mA_200>weight_HToZA_mH_300_mA_200_err && weight_HToZA_mH_500_mA_50>weight_HToZA_mH_500_mA_50_err && weight_HToZA_mH_500_mA_100>weight_HToZA_mH_500_mA_100_err && weight_HToZA_mH_500_mA_200>weight_HToZA_mH_500_mA_200_err && weight_HToZA_mH_500_mA_300>weight_HToZA_mH_500_mA_300_98             err && weight_HToZA_mH_500_mA_400>weight_HToZA_mH_500_mA_400_err && weight_HToZA_mH_650_mA_50>weight_HToZA_mH_650_mA_50_err && weight_HToZA_mH_800_mA_50>weight_HToZA_mH_800_mA_50_err && weight_HToZA_mH_800_mA_100>weight_HToZA_mH_800_mA_100_err && weight_HToZA_mH_800_mA_200>weight_HToZA_mH_800_mA_200_err && weight_HToZA_mH_800_mA_400>weight_HToZA_mH_800_mA_400_err && weight_HToZA_mH_800_mA_700>weight_HToZA_mH_800_mA_700_err && weight_HToZA_mH_1000_mA_50>weight_HToZA_mH_1000_mA_50_err && weight_HToZA_mH_1000_mA_200>weight_HToZA_mH_1000_mA_200_err && weight_HToZA_mH_1000_mA_500>weight_HToZA_mH_1000_mA_500_err && weight_HToZA_mH_2000_mA_1000>weight_HToZA_mH_2000_mA_1000_err && weight_HToZA_mH_3000_mA_2000>weight_HToZA_mH_3000_mA_2000_err && weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err" 
    cuts =''
    other_variables = [s for s in ListBranches(opt.file) if s not in variables]
    events = Tree2Pandas(input_file=opt.file, variables=variables+other_variables,cut=cuts)
    points = Decoupler(events[variables],list_outputs=variables) # [mH,mA,weight]xlen(variables) for each event 
    points = points.apply(pd.to_numeric) # change dtypes to float64

    inter_weight = np.zeros(events.shape[0])
    manager = enlighten.get_manager()
    pbar = manager.counter(total=events.shape[0], desc='Progress', unit='Event')
    for i in range(events.shape[0]):
        x = points.iloc[i*N:(i+1)*N,1].values # mA is x
        y = points.iloc[i*N:(i+1)*N,0].values # mH is x
        z = points.iloc[i*N:(i+1)*N,2].values # weight is x

        inst = InterpolationDelaunay(x,y,z)
        inter_weight[i] = inst.interpolate(opt.MA,opt.MH)
        pbar.update()
    manager.stop()
    inter_weight = np.nan_to_num(inter_weight) # Put nan at 0

    # Make output #
    new_df = pd.DataFrame(inter_weight)
    new_df.columns = ['inter_HToZA_mH_%d_mA_%d'%(opt.MH,opt.MA)]
    out_df = pd.concat([events,new_df],axis=1)
    output = out_df.to_records(index=False,column_dtypes='float64')                                                                                                                       
    array2root(output,opt.file.replace('.root','_delaunay.root'),mode='recreate')   
    print ('Output saved as %s'%opt.file.replace('.root','_delaunay.root'))

if __name__ == "__main__":
    main()   
