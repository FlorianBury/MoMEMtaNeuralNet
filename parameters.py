# Defines the parameters that users might need to change
# Must be included manually in each script

from keras.losses import binary_crossentropy, mean_squared_error   
from keras.optimizers import RMSprop, Adam, Nadam, SGD            
from keras.activations import relu, elu, selu, softmax, tanh     
from keras.regularizers import l1,l2 

# Global variables #
global main_path
global path_out   
main_path = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/'   
path_out = '/nfs/scratch/fynu/fbury/MoMEMta_output/NNOutput/' 

# Scan dictionary #
p = { 
    'lr' : [0.01], 
    'first_neuron' : [200],
    'activation' : [relu],
    'dropout' : [0],
    'hidden_layers' : [4],
    'output_activation' : [selu],
    'l2' : [0],
    'optimizer' : [Adam],  
    'epochs' : [50],   
    'batch_size' : [256], 
    'loss_function' : [mean_squared_error] 
}    
repetition = 1

scaler_name = 'scaler_signal_weights.pkl' # If does not exist will be created
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
         'met_pt',
         'met_phi-lep1_p4.Phi()',
         ]
outputs = [
         'weight_HToZA_mH_200_mA_50',
         'weight_HToZA_mH_200_mA_100',
         'weight_HToZA_mH_250_mA_50', 
         'weight_HToZA_mH_250_mA_100',
         'weight_HToZA_mH_300_mA_50', 
         'weight_HToZA_mH_300_mA_100',
         'weight_HToZA_mH_300_mA_200',
         'weight_HToZA_mH_500_mA_50', 
         'weight_HToZA_mH_500_mA_100',
         'weight_HToZA_mH_500_mA_200',
         'weight_HToZA_mH_500_mA_300',
         'weight_HToZA_mH_500_mA_400',
         'weight_HToZA_mH_650_mA_50', 
         'weight_HToZA_mH_800_mA_50', 
         'weight_HToZA_mH_800_mA_100',
         'weight_HToZA_mH_800_mA_200',
         'weight_HToZA_mH_800_mA_400',
         'weight_HToZA_mH_800_mA_700',
         'weight_HToZA_mH_1000_mA_50',
         'weight_HToZA_mH_1000_mA_200', 
         'weight_HToZA_mH_1000_mA_500', 
         'weight_HToZA_mH_2000_mA_1000',
         'weight_HToZA_mH_3000_mA_2000',
          ] 
other_variables = [
                     'lep1_p4.Phi()',
                     'lep2_p4.Phi()',
                     'jet1_p4.Phi()',
                     'jet2_p4.Phi()',

                     'lep1_p4.Px()',
                     'lep1_p4.Py()',
                     'lep1_p4.Pz()',
                     'lep1_p4.E()',
                     'lep2_p4.Px()',
                     'lep2_p4.Py()',
                     'lep2_p4.Pz()',
                     'lep2_p4.E()',
                     'jet1_p4.Px()',
                     'jet1_p4.Py()',
                     'jet1_p4.Pz()',
                     'jet1_p4.E()',
                     'jet2_p4.Px()',
                     'jet2_p4.Py()',
                     'jet2_p4.Pz()',
                     'jet2_p4.E()',

                     'weight_DY',
                     'weight_TT',
                     'weight_DY_time',
                     'weight_DY_err',
                     'weight_TT_time',
                     'weight_TT_err',
                     'weight_HToZA_mH_200_mA_100_err',
                     'weight_HToZA_mH_250_mA_50_err', 
                     'weight_HToZA_mH_250_mA_100_err',
                     'weight_HToZA_mH_300_mA_50_err', 
                     'weight_HToZA_mH_300_mA_100_err',
                     'weight_HToZA_mH_300_mA_200_err',
                     'weight_HToZA_mH_500_mA_50_err', 
                     'weight_HToZA_mH_500_mA_100_err',
                     'weight_HToZA_mH_500_mA_200_err',
                     'weight_HToZA_mH_500_mA_300_err',
                     'weight_HToZA_mH_500_mA_400_err',
                     'weight_HToZA_mH_650_mA_50_err', 
                     'weight_HToZA_mH_800_mA_50_err', 
                     'weight_HToZA_mH_800_mA_100_err',
                     'weight_HToZA_mH_800_mA_200_err',
                     'weight_HToZA_mH_800_mA_400_err',
                     'weight_HToZA_mH_800_mA_700_err',
                     'weight_HToZA_mH_1000_mA_50_err',
                     'weight_HToZA_mH_1000_mA_200_err', 
                     'weight_HToZA_mH_1000_mA_500_err', 
                     'weight_HToZA_mH_2000_mA_1000_err',
                     'weight_HToZA_mH_3000_mA_2000_err',
                     'weight_HToZA_mH_200_mA_100_time',
                     'weight_HToZA_mH_250_mA_50_time', 
                     'weight_HToZA_mH_250_mA_100_time',
                     'weight_HToZA_mH_300_mA_50_time', 
                     'weight_HToZA_mH_300_mA_100_time',
                     'weight_HToZA_mH_300_mA_200_time',
                     'weight_HToZA_mH_500_mA_50_time', 
                     'weight_HToZA_mH_500_mA_100_time',
                     'weight_HToZA_mH_500_mA_200_time',
                     'weight_HToZA_mH_500_mA_300_time',
                     'weight_HToZA_mH_500_mA_400_time',
                     'weight_HToZA_mH_650_mA_50_time', 
                     'weight_HToZA_mH_800_mA_50_time', 
                     'weight_HToZA_mH_800_mA_100_time',
                     'weight_HToZA_mH_800_mA_200_time',
                     'weight_HToZA_mH_800_mA_400_time',
                     'weight_HToZA_mH_800_mA_700_time',
                     'weight_HToZA_mH_1000_mA_50_time',
                     'weight_HToZA_mH_1000_mA_200_time', 
                     'weight_HToZA_mH_1000_mA_500_time', 
                     'weight_HToZA_mH_2000_mA_1000_time',
                     'weight_HToZA_mH_3000_mA_2000_time',
                  ]
weights = 'total_weight'

def make_dtype(list_names):
    list_dtype = [(name.replace('.','_').replace('()','').replace('-','_minus_').replace('*','_times_'),'float64') for name in list_names]
    return list_dtype
        



                                



