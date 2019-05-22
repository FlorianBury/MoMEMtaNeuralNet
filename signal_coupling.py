import os
import sys
import re
import numpy as np
import pandas as pd
import logging
import enlighten
import copy

import parameters

def Decoupler(data,list_outputs=None):
    """ 
    Data is a pandas dataFrame
    For each event we have : [Pt,eta,phi]x4 and 23 weights (with mH, mA) as parameters
    We want to have as : (inputs) [Pt,eta,phi]x4 + mH + mA -> (output) weight_mA_mH
                                  [Pt,eta,phi]x4 + mH' + mA' -> (output) weight_mA'_m'H 
                                  [Pt,eta,phi]x4 + mH" + mA" -> (output) weight_mA"_mH" 
                                  ...
    So that each event is presented 23 times with different parameters mH, mA and according weight
    inputs = [Pt,eta,phi]x4
    outputs = 23 set of weights
    """
    list_out = parameters.outputs if list_outputs is None else copy.copy(list_outputs)
    # Get the arrays of mH, mA ordered as in the outputs
    list_rest = [i for i in data.columns if i not in list_out] # All but outputs
    n_weights = len(list_out)
    mHmA = np.empty((0,2))
    for ol in list_out:
        arr = np.array([[int(re.findall(r'\d+', ol)[0]),int(re.findall(r'\d+', ol)[1])]])
        mHmA = np.append(mHmA,arr,axis=0)

    # Get the numpy arrays #
    decouple = data[list_out].values
    repeat = data[list_rest].values

    # Repeat and decouple #
    repeat = Repeater(repeat,n_weights)
    masses = np.tile(mHmA,(data.shape[0],1))
    decouple = decouple.flatten()

    # Concatenate and make DF #
    new_arr = np.c_[repeat,masses,decouple]
    df = pd.DataFrame(new_arr,columns=list_rest+['mH_MEM','mA_MEM','weight_HToZA'])

    return df

def Repeater(arr,n):
    """
    arr = [[a,b,c],
           [d,e,f],
           [g,h,i],
           ...]
    if n = 2 => returns [[a,b,c],
                         [a,b,c],
                         [d,e,f],
                         [d,e,f],
                         [g,h,i],
                         [g,h,i],
                         ...]
    """
    new_arr = np.zeros((arr.shape[0]*n,arr.shape[1]),dtype=object)
    for i in range(0,arr.shape[0]):
        new_row = np.tile(arr[i,:],(n,1))
        new_arr[i*n:(i+1)*n,:] = new_row
    return new_arr

def Recoupler(data):
    """ 
    Do the opposite of Decoupler.
    For the output we want one event with the different weights and outputs for each mass configuration
    Data is a pandas dataFrame
    """
    # Parameters #
    N = len(parameters.outputs) # number of repetitions
    columns = data.columns 
    col_to_recouple = ['mH_MEM','mA_MEM','weight_HToZA','output_HToZA'] # the colmuns we need to transpose and concatenate in one line
    col_repeated = [s for s in columns if s not in col_to_recouple] # The ones that are repeated N times, need to keep only one time
    
    # Get the basic repeated values @
    #entry_base = np.unique(data[col_repeated].values.astype('float64'),axis=0)
    idx_base = np.arange(0,data.shape[0],N)
    entry_base = data.iloc[idx_base][col_repeated].values # select one entry among the repeated

    # generate the new columns #
    mH = data.iloc[0:N]['mH_MEM'].values.tolist()
    mA = data.iloc[0:N]['mA_MEM'].values.tolist() 
    new_col = ['weight_HToZA_mH_%d_mA_%d'%(H,A) for H,A in zip(mH,mA)] + ['output_HToZA_mH_%d_mA_%d'%(H,A) for H,A in zip(mH,mA)]
    
    # Transpose on one line #
    data_to_recouple = data[['weight_HToZA','output_HToZA']].values
    data_recoupled = Transposer(data_to_recouple,N)

    # Concatenate and make into DF #
    full_arr = np.c_[entry_base,data_recoupled]
    new_df = pd.DataFrame(full_arr,columns=col_repeated+new_col)

    return new_df


def Transposer(arr,n):
    """
    arr = [[a,b,c],
           [d,e,f],
           [g,h,i],
           [j,k,l],
           ...]
    if n = 2,   returns [[a,d,b,e,c,f],
                         [g,j,h,k,i,l],
                         ...]
    if n = 3,   returns [[a,d,g,b,e,h,c,f,i],
                         ...]
    """
    # Check that the requested special transposition is feasible #
    if arr.shape[0]%n != 0:
        logging.critical('Cannot apply the recoupling on the array, the requested repetition is not a divisor of the array size')
        sys.exit()

    # Define new array #
    x = arr.shape[0]
    y = arr.shape[1]
    new_x = x//n
    new_y = y*n
    new_arr = np.zeros((new_x,new_y))

    # Loop #
    idx_row = 0 # row index of new array
    for i in range(arr.shape[0]//n):
        arr_slice = arr[i*n:(i+1)*n,:] # Slice that we need to "transpose"
        idx_col = 0 # col index of new array
        for col in range(arr_slice.shape[1]): # loop over slice to fill the row of new array
            for row in range(arr_slice.shape[0]):
                new_arr[idx_row,idx_col] = arr_slice[row,col]
                idx_col += 1
        idx_row += 1

    return new_arr
    


