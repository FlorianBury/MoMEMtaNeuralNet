import numpy as np
import os
import logging

import parameters                                                                                                                                                                                      

def GenerateMask(N,name):
    path_mask = os.path.join(parameters.main_path,'mask'+name+'.txt')
    if not os.path.exists(path_mask):                     
        mask = np.full((N,), False, dtype=bool)     
        mask[:int(0.7*N)] = True                         
        np.random.shuffle(mask)                                     
        np.savetxt(path_mask,mask)                                 
        # False => Evaluation set, True => Training set           
        logging.debug('Mask not found at '+path_mask+' -> Has been generated')
    else:                                                        
        mask = np.genfromtxt(path_mask)     
        logging.debug('Mask found at '+path_mask)

    return mask
