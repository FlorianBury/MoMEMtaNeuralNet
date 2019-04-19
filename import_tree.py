import glob
import os
import sys
import logging
import re

import array
import numpy as np
import pandas as pd

from root_numpy import tree2array, rec2array
from ROOT import TChain, TFile, TTree


###############################################################################
# Tree2Pandas#
###############################################################################

def Tree2Pandas(input_file, variables, weight, cut=None, reweight_to_cross_section=False, n=None):
    """
    Convert a ROOT TTree to a numpy array.
    """

    file_handle = TFile.Open(input_file)
    tree = file_handle.Get('tree')
    N = tree.GetEntries()
    logging.debug('\t\tNumber of events : '+str(N))

    relative_weight = 1
    if reweight_to_cross_section:
        cross_section = file_handle.Get('cross_section').GetVal()
        event_weight_sum = file_handle.Get("event_weight_sum").GetVal()
        relative_weight = cross_section / event_weight_sum
        logging.debug('\t\tReweighting requested')
        logging.debug('\t\t\tCross section : '+str(cross_section))
        logging.debug('\t\t\tEvent weight sum : '+str(event_weight_sum))
        logging.debug('\t\t\tRelative weight : '+str(relative_weight))
    # Read the tree and convert it to a numpy structured array
    data = tree2array(tree, branches=variables + [weight], selection=cut)
    
    # Convert to pandas dataframe #
    df = pd.DataFrame(data)
    df[weight] *= relative_weight
    if n:
        logging.info("Reading only {} from input tree".format(n))
        df = df[:n]

    return df

###############################################################################
# LoopOverTrees #
###############################################################################

def LoopOverTrees(input_dir, variables, weight, tag=None, cut=None, reweight_to_cross_section=False, n=None, list_sample=None):
    """
    Loop over ROOT trees inside input_dir and process them using Tree2Pandas.
    """
    # Check if directory #
    if not os.path.isdir(input_dir):
        logging.critical("LoopOverTrees : Not a directory")
        sys.exit(1)

    logging.debug("Accessing directory : "+input_dir)

    # Wether to use a given sample list or loop over files inside a dir #
    if list_sample is None:
        list_sample = glob.glob(input_dir+"*.root")
    else:
        list_sample = [input_dir + s for s in list_sample]

    # Loop over the files #
    first_file = True
    for name in list_sample:
        filename = name.replace(input_dir,'')
        logging.debug("\tAccessing file : %s"%filename)

        # If a tag for specific files has been requested # 
        if tag is not None:
            if re.search(tag,filename):
                logging.debug('\t\t-> Matched sample')
            else:
                continue 
       
        # Get the data as pandas df #
        df = Tree2Pandas(name,variables,weight,cut,reweight_to_cross_section,n) 

        # Find mH, mA #
        if filename.find('HToZA')!=-1: # Signal -> Search for mH and mA
            mH = [int(re.findall(r'\d+', filename)[2])]*df.shape[0]    
            mA = [int(re.findall(r'\d+', filename)[3])]*df.shape[0]    
        else: # Background, set them at 0
            mH = [0]*df.shape[0]
            mA = [0]*df.shape[0]

        # Register in DF #
        df['mH_gen'] = pd.Series(mH)
        df['mA_gen'] = pd.Series(mA)
        
        # Register the tag if provided #
        if tag is not None:
            df['tag'] = pd.Series([tag]*df.shape[0])

        # Concatenate into full df #
        if first_file:
            all_df = df
            first_file = False
        else:
            all_df = pd.concat([all_df,df])
    return all_df
