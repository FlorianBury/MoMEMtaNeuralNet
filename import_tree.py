import glob
import os
import sys
import logging
import re

import array
import numpy as np

from root_numpy import tree2array, rec2array
from ROOT import TChain, TFile, TTree


###############################################################################
# Tree2Numpy#
###############################################################################

def Tree2Numpy(input_file, variables, weight, cut=None, reweight_to_cross_section=False, n=None):
    """
    Convert a ROOT TTree to a numpy array.
    Inputs :
        input_file = name of the ROOT file
        variables = list of names of the variables to be extracted
        weight = name of the weights
        cut = optionnal cut on data 
        reweight_to_cross_section = wether to reweight according to the cross-section
        n = number of events to be printed for tests
    Outputs :
        dataset = array containing events in rows with variable in columns
        weight = array of weights following dataset
    """

    file_handle = TFile.Open(input_file)
    tree = file_handle.Get('tree')
    N = tree.GetEntries()
    logging.debug('\t\tNumber of events : '+str(N))

    cross_section = 1
    relative_weight = 1
    if reweight_to_cross_section:
        cross_section = file_handle.Get('cross_section').GetVal()
        event_weight_sum = file_handle.Get("event_weight_sum").GetVal()
        logging.debug('\t\tReweighting requested')
        logging.debug('\t\t\tCross section : '+str(cross_section))
        logging.debug('\t\t\tEvent weight sum: '+str(event_weight_sum))
        relative_weight = cross_section / event_weight_sum
    # Read the tree and convert it to a numpy structured array
    a = tree2array(tree, branches=variables + [weight], selection=cut)

    # Rename the last column to 'weight'
    a.dtype.names = variables + ['weight']

    dataset = a[variables]
    weights = a['weight'] * relative_weight

    # Convert to plain numpy arrays
    dataset = rec2array(dataset)

    if n:
        logging.info("Reading only {} from input tree".format(n))
        dataset = dataset[:n]
        weights = weights[:n]

    return dataset, weights

###############################################################################
# LoopOverTrees #
###############################################################################

def LoopOverTrees(input_dir, variables, weight, part_name=None, cut=None, reweight_to_cross_section=False, n=None):
    """
    Loop over ROOT trees inside input_dir and process them using Tree2Numpy.
    Inputs :
        input_dir = directory of the ROOT files
        part_name = optionnal string included in the name of the file (used to differentiate different ROOT files inside directory)
        variables = list of names of the variables to be extracted
        weight =  name of the weights
        cut = optionnal cut on data 
        reweight_to_cross_section = wether to reweight according to the cross-section
        n = number of events to be printed for tests
    Outputs :
        datasets = array containing events in rows with variable in columns
        weights = array of weights following dataset
    """

    if not os.path.isdir(input_dir):
        logging.critical("LoopOverTrees : Not a directory")
        sys.exit(1)

    logging.debug("Accessing directory : "+input_dir)

    N = len(variables)
    datasets = np.empty((0,N))
    weights = np.empty((0,))

    for name in glob.glob(input_dir+"*.root"):
        filename = name.replace(input_dir,'')

            
        if part_name is not None:
            if re.search(part_name,filename):
                logging.debug(("\tAccessing file : "+filename).ljust(60,'-')+'-> Correct sample')
            else:
                logging.debug(("\tAccessing file : "+filename).ljust(60,'*'))
                continue 
        
        d,w = Tree2Numpy(name,variables,weight,cut,reweight_to_cross_section,n) 
        datasets= np.append(datasets,d,axis=0)
        weights = np.append(weights,w,axis=0)
    
    return datasets,weights.reshape(-1,1)
