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
    'lr' : [0.1], 
    'first_neuron' : [50,100,150,200],
    'activation' : [relu],
    'dropout' : [0,0.05,0.1],
    'hidden_layers' : [3,4,5,6,7],
    'output_activation' : [selu],
    'l2' : [0,0.05,0.1],
    'optimizer' : [Adam],  
    'epochs' : [10],   
    'batch_size' : [500], 
    'loss_function' : [mean_squared_error] 
}    
repetition = 5
#inputs = [
#         'lep1_p4.Px()',
#         'lep1_p4.Py()',
#         'lep1_p4.Pz()',
#         'lep1_p4.E()',
#         'lep2_p4.Px()',
#         'lep2_p4.Py()',
#         'lep2_p4.Pz()',
#         'lep2_p4.E()',
#         'jet1_p4.Px()',
#         'jet1_p4.Py()',
#         'jet1_p4.Pz()',
#         'jet1_p4.E()',
#         'jet2_p4.Px()',
#         'jet2_p4.Py()',
#         'jet2_p4.Pz()',
#         'jet2_p4.E()',
#         'met_pt',
#         'met_phi',
#         ]
#
inputs = [
         'lep1_p4.Pt()',
         'lep1_p4.Eta()',
         'lep2_p4.Pt()',
         'lep2_p4.Eta()',
         'lep2_p4.Phi()-lep1_p4.Phi()',
         'jet1_p4.Pt()',
         'jet1_p4.Eta()',
         'jet1_p4.Phi()-lep1_p4.Phi()',
         'jet2_p4.Pt()',
         'jet2_p4.Eta()',
         'jet2_p4.Phi()-lep1_p4.Phi()',
         'met_pt*1.1',
         'met_phi',
         ]
outputs = [
         'weight_DY',
         'weight_TT',
          ] 
other_variables = [
                     'weight_DY_time',
                     'weight_DY_err',
                     'weight_TT_time',
                     'weight_TT_err',
                  ]
weights = ['total_weight']

def make_dtype(list_names):
    list_dtype = [(name.replace('.','_').replace('()','').replace('-','_minus_').replace('*','_times_'),'float64') for name in list_names]
    return list_dtype
        



                                



