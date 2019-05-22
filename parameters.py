# Defines the parameters that users might need to change
# Must be included manually in each script

# /!\ Three types of files need to be filled with users parameters 
#           - parameters.py (mort important one)
#           - sampleList.py (on what samples to run)
#           - submit_on_slurm.py (for time and partition)
#           (optionnaly NeuralNet.py for early_stopping etc)
# TODO : all parmameters on parameters.py and samples in sampleList.py

from keras.losses import binary_crossentropy, mean_squared_error   
from keras.optimizers import RMSprop, Adam, Nadam, SGD            
from keras.activations import relu, elu, selu, softmax, tanh, sigmoid
from keras.regularizers import l1,l2 

##################################  Path variables ####################################

main_path = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/'   
path_out = '/nfs/scratch/fynu/fbury/MoMEMta_output/NNOutput/' 

##############################  Datasets proportion   #################################
# Total must be 1 #
training_ratio = 0.7    # Training set sent to keras
validation_ratio = 0.1  # Validation set sent to autom8
output_ratio = 0.2      # Output set for plotting later
# Will only be taken into account for the masks generation, ignored after

######################################  Name   ########################################
# Model name (only for scans)
#model = 'NeuralNetModel' 
model = 'ClassificationModel'
# scaler and mask names #
suffix = 'class_back' 
# scaler_name -> 'scaler_{suffix}.pkl'  If does not exist will be created 
# mask_name -> 'mask_{suffix}_{sample}.npy'  If does not exist will be created 

##############################  Evaluation criterion   ################################

eval_criterion = "eval_error" # either val_loss or eval_error
    
#################################  Scan dictionary   ##################################
# Classification #
# /!\ Lists mus always contain something (even if 0), otherwise 0 hyperparameters #
p = { 
    'lr' : [0.0001], 
    'first_neuron' : [100,200,300,400,500],
    'activation' : [relu],
    'dropout' : [0],
    'hidden_layers' : [2,3,4,5,6], # does not take into account the first layer
    'output_activation' : [sigmoid],
    'l2' : [0,0.1,0.2,0.3,0.4,0.5],
    'optimizer' : [Adam],  
    'epochs' : [300],   
    'batch_size' : [512], 
    'loss_function' : [binary_crossentropy] 
}
#p = { 
#    'lr' : [0.0001], 
#    'first_neuron' : [300],
#    'activation' : [relu],
#    'dropout' : [0],
#    'hidden_layers' : [5], # does not take into account the first layer
#    'output_activation' : [sigmoid],
#    'l2' : [0],
#    'optimizer' : [Adam],  
#    'epochs' : [10],   
#    'batch_size' : [512], 
#    'loss_function' : [binary_crossentropy] 
#}
# Regression #
#p = { 
#    'lr' : [0.001], 
#    'first_neuron' : [100,200,300,400,500],
#    'activation' : [relu],
#    'dropout' : [0,0.1,0.2,0.3],
#    'hidden_layers' : [5,6,7,8], # does not take into account the first layer
#    'output_activation' : [selu],
#    'l2' : [0,0.1,0.2,0.3],
#    'optimizer' : [Adam],  
#    'epochs' : [100],   
#    'batch_size' : [512], 
#    'loss_function' : [mean_squared_error] 
#}
repetition = 1

###################################  Variables   ######################################
inputs = [
         #######   Regression ##########
         #'lep1_p4.Pt()',
         #'lep1_p4.Eta()',
         #'lep2_p4.Pt()',
         #'lep2_p4.Eta()',
         #'lep2_p4.Phi()-lep1_p4.Phi()',
         #'jet1_p4.Pt()',
         #'jet1_p4.Eta()',
         #'jet1_p4.Phi()-lep1_p4.Phi()',
         #'jet2_p4.Pt()',
         #'jet2_p4.Eta()',
         #'jet2_p4.Phi()-lep1_p4.Phi()',
         #'met_pt',
         #'met_phi-lep1_p4.Phi()',

         #######   Classification ##########
         '-log10(weight_TT)',
         '-log10(weight_DY)',
         #'-log10(weight_HToZA_mH_200_mA_50)',
         #'-log10(weight_HToZA_mH_200_mA_100)',
         #'-log10(weight_HToZA_mH_250_mA_50)', 
         #'-log10(weight_HToZA_mH_250_mA_100)',
         #'-log10(weight_HToZA_mH_300_mA_50)', 
         #'-log10(weight_HToZA_mH_300_mA_100)',
         #'-log10(weight_HToZA_mH_300_mA_200)',
         #'-log10(weight_HToZA_mH_500_mA_50)', 
         #'-log10(weight_HToZA_mH_500_mA_100)',
         #'-log10(weight_HToZA_mH_500_mA_200)',
         #'-log10(weight_HToZA_mH_500_mA_300)',
         #'-log10(weight_HToZA_mH_500_mA_400)',
         #'-log10(weight_HToZA_mH_650_mA_50)', 
         #'-log10(weight_HToZA_mH_800_mA_50)', 
         #'-log10(weight_HToZA_mH_800_mA_100)',
         #'-log10(weight_HToZA_mH_800_mA_200)',
         #'-log10(weight_HToZA_mH_800_mA_400)',
         #'-log10(weight_HToZA_mH_800_mA_700)',
         #'-log10(weight_HToZA_mH_1000_mA_50)',
         #'-log10(weight_HToZA_mH_1000_mA_200)', 
         #'-log10(weight_HToZA_mH_1000_mA_500)', 
         #'-log10(weight_HToZA_mH_2000_mA_1000)',
         #'-log10(weight_HToZA_mH_3000_mA_2000)',

         # Reprocess #
         #'lep1_p4_Pt',
         #'lep1_p4_Eta',
         #'lep2_p4_Pt',
         #'lep2_p4_Eta',
         #'lep2_p4_Phi_minus_lep1_p4_Phi',
         #'jet1_p4_Pt',
         #'jet1_p4_Eta',
         #'jet1_p4_Phi_minus_lep1_p4_Phi',
         #'jet2_p4_Pt',
         #'jet2_p4_Eta',
         #'jet2_p4_Phi_minus_lep1_p4_Phi',
         #'met_pt',
         #'met_phi_minus_lep1_p4_Phi',
         ]
outputs = [
         #######   Regression ##########
         #'weight_TT',
         #'weight_DY',
         #'weight_HToZA_mH_200_mA_50',
         #'weight_HToZA_mH_200_mA_100',
         #'weight_HToZA_mH_250_mA_50', 
         #'weight_HToZA_mH_250_mA_100',
         #'weight_HToZA_mH_300_mA_50', 
         #'weight_HToZA_mH_300_mA_100',
         #'weight_HToZA_mH_300_mA_200',
         #'weight_HToZA_mH_500_mA_50', 
         #'weight_HToZA_mH_500_mA_100',
         #'weight_HToZA_mH_500_mA_200',
         #'weight_HToZA_mH_500_mA_300',
         #'weight_HToZA_mH_500_mA_400',
         #'weight_HToZA_mH_650_mA_50', 
         #'weight_HToZA_mH_800_mA_50', 
         #'weight_HToZA_mH_800_mA_100',
         #'weight_HToZA_mH_800_mA_200',
         #'weight_HToZA_mH_800_mA_400',
         #'weight_HToZA_mH_800_mA_700',
         #'weight_HToZA_mH_1000_mA_50',
         #'weight_HToZA_mH_1000_mA_200', 
         #'weight_HToZA_mH_1000_mA_500', 
         #'weight_HToZA_mH_2000_mA_1000',
         #'weight_HToZA_mH_3000_mA_2000',
         #'weight_HToZA_mH_600_mA_250', # interpolation 
         #######   Classification ##########
          ] 
other_variables = [
                     #'lep1_p4.Pt()',
                     #'lep1_p4.Eta()',
                     #'lep1_p4.Phi()',
                     #'lep2_p4.Pt()',
                     #'lep2_p4.Eta()',
                     #'lep2_p4.Phi()',
                     #'jet1_p4.Pt()',
                     #'jet1_p4.Eta()',
                     #'jet1_p4.Phi()',
                     #'jet2_p4.Pt()',
                     #'jet2_p4.Eta()',
                     #'jet2_p4.Phi()',
                     #'met_pt',
                     #'met_phi',

                     #'lep1_p4.Px()',
                     #'lep1_p4.Py()',
                     #'lep1_p4.Pz()',
                     #'lep1_p4.E()',
                     #'lep2_p4.Px()',
                     #'lep2_p4.Py()',
                     #'lep2_p4.Pz()',
                     #'lep2_p4.E()',
                     #'jet1_p4.Px()',
                     #'jet1_p4.Py()',
                     #'jet1_p4.Pz()',
                     #'jet1_p4.E()',
                     #'jet2_p4.Px()',
                     #'jet2_p4.Py()',
                     #'jet2_p4.Pz()',
                     #'jet2_p4.E()',
                    
                     'll_M',
                     'jj_M',
                     'lljj_M',

                     'weight_TT',
                     'weight_DY',
                     #'output_DY',
                     #'output_TT',

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

                     #'output_HToZA_mH_200_mA_50',
                     #'output_HToZA_mH_200_mA_100',
                     #'output_HToZA_mH_250_mA_50', 
                     #'output_HToZA_mH_250_mA_100',
                     #'output_HToZA_mH_300_mA_50', 
                     #'output_HToZA_mH_300_mA_100',
                     #'output_HToZA_mH_300_mA_200',
                     #'output_HToZA_mH_500_mA_50', 
                     #'output_HToZA_mH_500_mA_100',
                     #'output_HToZA_mH_500_mA_200',
                     #'output_HToZA_mH_500_mA_300',
                     #'output_HToZA_mH_500_mA_400',
                     #'output_HToZA_mH_650_mA_50', 
                     #'output_HToZA_mH_800_mA_50', 
                     #'output_HToZA_mH_800_mA_100',
                     #'output_HToZA_mH_800_mA_200',
                     #'output_HToZA_mH_800_mA_400',
                     #'output_HToZA_mH_800_mA_700',
                     #'output_HToZA_mH_1000_mA_50',
                     #'output_HToZA_mH_1000_mA_200', 
                     #'output_HToZA_mH_1000_mA_500', 
                     #'output_HToZA_mH_2000_mA_1000',
                     #'output_HToZA_mH_3000_mA_2000',

                     'weight_DY_time',
                     'weight_DY_err',
                     'weight_TT_time',
                     'weight_TT_err',
                     'weight_HToZA_mH_200_mA_50_err',
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
                     #'weight_HToZA_mH_600_mA_250_err', 
                     #'weight_HToZA_mH_600_mA_250_time', 
                  ]
weights = 'total_weight'

################################  dtype operation ##############################

def make_dtype(list_names): # root_numpy does not like . and ()
    list_dtype = [(name.replace('.','_').replace('(','').replace(')','').replace('-','_minus_').replace('*','_times_')) for name in list_names]
    return list_dtype
        



                                



