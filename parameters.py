# Defines the parameters that users might need to change
# Must be included manually in each script

from keras.losses import binary_crossentropy, mean_squared_error   
from keras.optimizers import RMSprop, Adam, Nadam, SGD            
from keras.activations import relu, elu, selu, softmax, tanh, sigmoid
from keras.regularizers import l1,l2 

# Global variables #
global main_path
global path_to_files
global path_out   
main_path = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/'   
#path_to_files = '/nfs/scratch/fynu/fbury/MoMEMta_output/NNOutput/BestModel_newvar/valid_weights/'
path_to_files = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/Adversarial/adv_lowlr_highreg_1/valid_weights/'
path_out = '/nfs/scratch/fynu/fbury/MoMEMta_output/Classifier/' 

# Scan dictionary #
p = { 
    'lr' : [0.1], 
    'first_neuron' : [30,50,100],
    'activation' : [relu],
    'dropout' : [0.1,0.2,0.3,0.4,0.5],
    'hidden_layers' : [2,3,4],
    'output_activation' : [sigmoid],
    'l2' : [0.1,0.2,0.3,0.4,0.5],
    'optimizer' : [Adam],  
    'epochs' : [10000],   
    'batch_size' : [100], 
    'loss_function' : [binary_crossentropy] 
}
#p = { 
#    'lr' : [0.5], 
#    'first_neuron' : [30,50,100,200],
#    'activation' : [selu],
#    'dropout' : [0],
#    'hidden_layers' : [3],
#    'output_activation' : [sigmoid],
#    'l2' : [0],
#    'optimizer' : [Adam],  
#    'epochs' : [1],   
#    'batch_size' : [1000], 
#    'loss_function' : [binary_crossentropy] 
#}     
repetition = 1

inputs = [
         'weight_DY',
         'weight_TT',
          ] 
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
        



                                



