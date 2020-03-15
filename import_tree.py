import glob
import os
import sys
import logging
import re
import collections
import copy

import array
import numpy as np
import pandas as pd

import parameters
from root_numpy import tree2array, rec2array
from ROOT import TChain, TFile, TTree


###############################################################################
# Tree2Pandas#
###############################################################################

def Tree2Pandas(input_file, variables, weight=None, cut=None, reweight_to_cross_section=False, n=None, tree_name='tree',start=None):
    """
    Convert a ROOT TTree to a numpy array.
    """
    # Check for repetitions in variables -> makes root_numpy crash #
    variables = copy.copy(variables) # Otherwise will add the weight and have a duplicate branch
    rep = [item for item, count in collections.Counter(variables).items() if count > 1]
    if len(rep) != 0:
        for r in rep:
            logging.critical('The argument "%s" is repeated in the variables'%r)
        sys.exit(1)

    file_handle = TFile.Open(input_file)
    tree = file_handle.Get(tree_name)
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
    if weight is not None:
        variables += [weight]
    data = tree2array(tree, branches=variables, selection=cut, start=start, stop=n)
    
    # Convert to pandas dataframe #
    df = pd.DataFrame(data)
    if weight is not None:
        df[weight] *= relative_weight

    # Only part of tree #
    if n:
        if n == -1:
            n = N # Get all entries
        if start:
            if n < start:
                logging.critical('Importing tree with start higher than end, will output empty tree')
            logging.info("Reading from {} to {} in input tree".format(start,n))
        else:
            logging.info("Reading only {} from input tree".format(n))
        

    return df

###############################################################################
# LoopOverTrees #
###############################################################################

def LoopOverTrees(input_dir, variables, weight=None, tag=None, cut=None, reweight_to_cross_section=False, n=None, list_sample=None, start=None):
    """
    Loop over ROOT trees inside input_dir and process them using Tree2Pandas.
    """
    # Check if directory #
    if not os.path.isdir(input_dir):
        logging.critical("LoopOverTrees : Not a directory")
        sys.exit(1)

    logging.debug("Accessing directory : "+input_dir)

    # Add potential cut to the one in parameters.py file #
    if cut is not None:
        cut += " && "+parameters.cut
    else:
        cut : parameters.cut

    # Wether to use a given sample list or loop over files inside a dir #
    if list_sample is None:
        list_sample = glob.glob(os.path.join(input_dir,"*.root"))
    else:
        list_sample = [input_dir + s for s in list_sample]

    # Loop over the files #
    first_file = True
    all_df = pd.DataFrame() 
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
        df = Tree2Pandas(input_file                 = name,
                         variables                  = variables,
                         weight                     = weight,
                         cut                        = cut,
                         reweight_to_cross_section  = reweight_to_cross_section,
                         n                          = n,
                         tree_name                  = 'tree',
                         start                      = start) 

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
        all_df = all_df.reset_index(drop=True) # Otherwise there will be an index repetition for each file
    return all_df
