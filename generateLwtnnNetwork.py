from __future__ import print_function
import sys
import os
import json
import h5py    
import copy
import pprint 
import numpy as np


def removeJsonPreprocess(json_file):
    with open(json_file, 'r') as f:
        arch = json.load(f)
    #pprint.pprint(arch) 
    preprocess_layer = arch['config']['layers'][1]
    mean = preprocess_layer['config']['mean']
    std = preprocess_layer['config']['std']

    del arch['config']['layers'][1]

    arch['config']['layers'][1]['inbound_nodes'][0][0][0] = arch['config']['input_layers'][0][0]


    with open('new_'+json_file, 'w') as f:
        json.dump(arch,f)

def print_structure(weight_file_path):
    """
    Prints out the structure of HDF5 file.

    Args:
      weight_file_path (str) : Path to the file to analyze
    """
    f = h5py.File(weight_file_path,'r')
    try:
        if len(f.attrs.items()):
            print("{} contains: ".format(weight_file_path))
            print("Root attributes:")

        print("f.attrs.items(): ")
        for key, value in f.attrs.items():           
            print("  {}: {}".format(key, value))

        if len(f.items())==0:
            print("Terminate # len(f.items())==0: ")
            return 

        print("layer, g in f.items():")
        for layer, g in f.items():            
            print("  {}".format(layer))
            print("    g.attrs.items(): Attributes:")
            for key, value in g.attrs.items():
                print("      {}: {}".format(key, value))

            print("    Dataset:")
            for p_name in g.keys():
                param = g[p_name]
                subkeys = param.keys()
                print("    Dataset: param.keys():")
                for k_name in param.keys():
                    print("      {}/{}: {}".format(p_name, k_name, param.get(k_name)[:]))
            print()
    finally:
        f.close()

def removeH5Preprocess(h5_file):
    f = h5py.File(h5_file, 'r')
    new_f = h5py.File('new_'+h5_file, 'w')

    
    for key, value in f.attrs.items(): # Needs to copy h5 attributes
        print (key)
        if isinstance(value,np.ndarray): # Need to exclude the preprocess name from list of layers
            new_value = np.ndarray(shape=(value.shape[0]-1,),dtype=value.dtype)
            j = 0
            for i in range(value.shape[0]):
                if b'Preprocess' not in value[i]:
                    new_value[j] = value[i]
                    j += 1
            new_f.attrs[key] = new_value
        else:
            new_f.attrs[key] = value

    for layer, group in f.items():     # Loop on groups and their names 'layer)
        print ("Layer {}".format(layer))
        # Check if preprocess layer #
        if 'Preprocess' in layer:
            print ('  Skipped')
            continue
        # Empty layers (dropout, ...)
        if (len(list(group.keys())) == 0): # Does not contain subgroups of datasets
            new_g = new_f.create_group(layer)
            for key, value in group.attrs.items():
                new_g.attrs.create(key,value)
            print ("  Empty group, has been copied")
        # Non-Empty layers (dense, ...)
        else: # Does contain something
            new_g = new_f.create_group(layer)       # Create first level group
            for key, value in group.attrs.items():  # Copy attributes of group
                new_g.attrs.create(key,value) 
            for subname, subgroup in group.items(): # Loop through subgroups
                print ("  Contains subgroup ",subname)
                print ("  Group {}/{} has been added".format(layer,subname))
                new_subg = new_f.create_group("{}/{}".format(layer,subname)) # Create subgroup
                for dataset_name in subgroup.keys():    # Loop through datasets in the given layer and add them to new file
                    print ("    Added dataset {}/{}/{} to group".format(layer,subname,dataset_name))
                    new_f.create_dataset("{}/{}/{}".format(layer,subname,dataset_name),data=subgroup.get(dataset_name)[:])
                    
    new_f.close()

if __name__ == '__main__':
    removeJsonPreprocess(sys.argv[1])
    removeH5Preprocess(sys.argv[2])
    #print_structure(sys.argv[2])
    print_structure('new_'+sys.argv[2])
