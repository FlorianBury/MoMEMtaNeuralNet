# Defines the parameters that users might need to change
# Must be included manually in each script

from keras.losses import binary_crossentropy, mean_squared_error   
from keras.optimizers import RMSprop, Adam, Nadam, SGD            
from keras.activations import relu, elu, selu, softmax, tanh     
from keras.regularizers import l1,l2 

# Global variables #
global main_path
global path_to_files
global path_out   
global path_invalid_DY
global path_invalid_TT
main_path = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/'   
path_to_files = '/nfs/scratch/fynu/fbury/MoMEMta_output/valid_weights/'
path_out = '/nfs/scratch/fynu/fbury/MoMEMta_output/NNOutput/' 
path_invalid_DY = '/nfs/scratch/fynu/fbury/MoMEMta_output/invalid_DY_weights_recomputed/'
path_invalid_TT = '/nfs/scratch/fynu/fbury/MoMEMta_output/invalid_TT_weights_recomputed/'

# Scan dictionary #
p = { 
    'lr' : [0.3], 
    'first_neuron' : [50,100,150,200],
    'activation' : [selu],
    'dropout' : [0],
    'hidden_layers' : [4],
    'output_activation' : [selu],
    'l2' : [0],
    'optimizer' : [Adam],  
    'epochs' : [1],   
    'batch_size' : [100], 
    'loss_function' : [mean_squared_error] 
}    


