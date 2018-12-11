import glob
import os
import sys
import re
import math
import socket
import json

import array
import numpy as np

from ROOT import TChain, TFile, TTree
from root_numpy import tree2array, rec2array


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

    cross_section = 1
    relative_weight = 1
    if reweight_to_cross_section:
        cross_section = file_handle.Get('cross_section').GetVal()
        relative_weight = cross_section / file_handle.Get("event_weight_sum").GetVal()

    # Read the tree and convert it to a numpy structured array
    a = tree2array(tree, branches=variables + [weight], selection=cut)

    # Rename the last column to 'weight'
    a.dtype.names = variables + ['weight']

    dataset = a[variables]
    weights = a['weight'] * relative_weight

    # Convert to plain numpy arrays
    dataset = rec2array(dataset)

    if n:
        print("Reading only {} from input tree".format(n))
        dataset = dataset[:n]
        weights = weights[:n]

    return dataset, weights

###############################################################################
# LoopOverTrees #
###############################################################################

def LoopOverTrees(input_dir, variables, weight, part_name=None, cut=None, reweight_to_cross_section=False, n=None, verbose=False):
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
        sys.exit("[WARNING] LoopOverTrees : Not a directory")

    if verbose:
        print ("\tAccessing directory : ",input_dir)

    N = len(variables)
    datasets = np.empty((0,N))
    weights = np.empty((0,))

    for name in glob.glob(input_dir+"*.root"):
        filename = name.replace(input_dir,'')

        if verbose:
            print ("\t\tAccessing file : ",filename)
            
        if part_name is not None:
            if re.search(part_name,filename):
                if verbose:
                    print ('\t\t\tFound match')
            else:
                if verbose:
                    print ('\t\t\tCould not find match')
                continue 
        
        d,w = Tree2Numpy(name,variables,weight,cut,reweight_to_cross_section,n) 
        datasets= np.append(datasets,d,axis=0)
        weights = np.append(weights,w,axis=0)
    
    return datasets,weights.reshape(-1,1)
