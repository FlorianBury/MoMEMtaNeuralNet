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
main_path = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/'   
path_to_files = '/nfs/scratch/fynu/fbury/MoMEMta_output/valid_weights/'
path_out = '/nfs/scratch/fynu/fbury/MoMEMta_output/' 

# Scan dictionary #
p = { 
    'lr' : [0.01,0.1,0.5], 
    'first_neuron' : [100],
    'activation' : [selu],
    'dropout' : [0,0.1,0.2,0.3,0.4,0.5],
    'hidden_layers' : [4,5,6,7,8],
    'output_activation' : [relu],
    'l2' : [0,0.1,0.2,0.3,0.4,0.5],   
    'optimizer' : [Adam],  
    'epochs' : [300],   
    'batch_size' : [100,200,300,400,500], 
    'loss_function' : [mean_squared_error] 
}    


