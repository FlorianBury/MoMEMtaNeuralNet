import numpy as np
import os

def GenerateMask(N,name):
    path_mask = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/mask'+name+'.txt'    
    if not os.path.exists(path_mask):                     
        mask = np.full((N,), False, dtype=bool)     
        mask[:int(0.7*N)] = True                         
        np.random.shuffle(mask)                                     
        np.savetxt(path_mask,mask)                                 
        # False => Evaluation set, True => Training set           
    else:                                                        
        mask = np.genfromtxt(path_mask)     

    return mask
