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
path_to_files = '/nfs/scratch/fynu/fbury/MoMEMta_output/NNOutput/BestModel_newvar/valid_weights/'
path_out = '/nfs/scratch/fynu/fbury/MoMEMta_output/Classifier/' 
path_invalid_DY = '/nfs/scratch/fynu/fbury/MoMEMta_output/invalid_DY_weights_recomputed/'
path_invalid_TT = '/nfs/scratch/fynu/fbury/MoMEMta_output/invalid_TT_weights_recomputed/'

# Scan dictionary #
p = { 
    'lr' : [0.1], 
    'first_neuron' : [50,100,150,200],
    'activation' : [relu],
    'dropout' : [0,0.05,0.1],
    'hidden_layers' : [3,4,5,6,7],
    'output_activation' : [selu],
    'l2' : [0,0.05,0.1],
    'optimizer' : [Adam],  
    'epochs' : [10000],   
    'batch_size' : [500], 
    'loss_function' : [mean_squared_error] 
}    
repetition = 5

inputs = [
         'weight_DY',
         'weight_TT',
          ] 
output = []
other_variables = [
                     'output_DY',
                     'output_TT',
                     'weight_DY_time',
                     'weight_DY_err',
                     'weight_TT_time',
                     'weight_TT_err',
                  ]
weights = ['total_weight']

def make_dtype(list_names):
    list_dtype = [(name.replace('.','_').replace('()','').replace('-','_minus_').replace('*','_times_'),'float64') for name in list_names]
    return list_dtype
        



                                



