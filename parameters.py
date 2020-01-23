# Defines the parameters that users might need to change
# Must be included manually in each script

# /!\ Two types of files need to be filled with users parameters 
#           - parameters.py (mort important one)
#           - sampleList.py (on what samples to run)
#           (optionnaly NeuralNet.py for early_stopping etc)
import multiprocessing
from keras.losses import binary_crossentropy, mean_squared_error, logcosh, cosine_proximity
from keras.optimizers import RMSprop, Adam, Nadam, SGD            
from keras.activations import relu, elu, selu, softmax, tanh, sigmoid
from keras.regularizers import l1,l2 

##################################  Path variables ####################################

main_path = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/'   
path_out = '/nfs/scratch/fynu/fbury/MoMEMta_output/NNOutput/' 
path_model = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/model'

##############################  Datasets proportion   #################################
# Total must be 1 #
training_ratio = 0.7    # Training set sent to keras
validation_ratio = 0.1  # Validation set sent to autom8
output_ratio = 0.2      # Output set for plotting later
# Will only be taken into account for the masks generation, ignored after

############################### Slurm parameters ######################################
partition = 'cp3-gpu'  # Def, cp3 or cp3-gpu
QOS = 'cp3-gpu' # cp3 or normal
time = '5-00:00:00' # days-hh:mm:ss
mem = '60000' # ram in MB
tasks = '20' # Number of threads(as a string)

######################################  Names  ########################################
# Model name (only for scans)
#model = 'NeuralNetModel' 
#model = 'ClassificationModel'
#model = 'BinaryModel'
model = 'NeuralNetGeneratorModel' 
# scaler and mask names #
#suffix = 'binary' 
#suffix = 'class_param_test' 
suffix = 'gen_ME' 
# scaler_name -> 'scaler_{suffix}.pkl'  If does not exist will be created 
# mask_name -> 'mask_{suffix}_{sample}.npy'  If does not exist will be created 

# Training resume #
resume_model = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/model/GPU_10x100_elu_100epochs_batchNorm_ME.zip'
#resume_model = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/model/GPU_8x500_elu_300epochs_withBatchNorm_ME.zip'   # Must be turned on in the argparse arguments
#resume_model = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/model/GPU_split_ME.zip'   # Must be turned on in the argparse arguments

# Generator #
#path_gen_training = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/ME_TTBar_generator_mix/path3' # For training
#path_gen_validation = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/ME_TTBar_generator_mix/path0' # For val_loss during training
#path_gen_evaluation = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/ME_TTBar_generator_mix/path1' # for model evaluation
#path_gen_output = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/ME_TTBar_generator_mix/path2' # for output
path_gen_training = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/ME_TTBar_generator_all/path3' # For training
path_gen_validation = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/ME_TTBar_generator_all/path0' # For val_loss during training
path_gen_evaluation = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/ME_TTBar_generator_all/path1' # for model evaluation
path_gen_output = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/ME_TTBar_generator_all/path2' # for output

weights_generator = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/utils/weights.root' # Must be turned on in the argparse arguments
#weights_generator = ''


workers = 20

# Output #
output_batch_size = 1000

##############################  Evaluation criterion   ################################

eval_criterion = "eval_error" # either val_loss or eval_error
    
#################################  Scan dictionary   ##################################
# /!\ Lists must always contain something (even if 0), otherwise 0 hyperparameters #
# Classification #
#p = { 
#    'lr' : [0.001], 
#    'first_neuron' : [500],
#    'activation' : [relu],
#    'dropout' : [0],
#    'hidden_layers' : [3], # does not take into account the first layer
#    'output_activation' : [selu],
#    'l2' : [0],
#    'optimizer' : [Adam],  
#    'epochs' : [1],   
#    'batch_size' : [50000], 
#    'loss_function' : [mean_squared_error] 
#}
#p = { 
#    'lr' : [0.0001], 
#    'first_neuron' : [300],
#    'activation' : [relu],
#    'dropout' : [0],
#    'hidden_layers' : [4], # does not take into account the first layer
#    'output_activation' : [sigmoid],
#    'l2' : [0],
#    'optimizer' : [Adam],  
#    'epochs' : [5],   
#    'batch_size' : [512], 
#    'loss_function' : [binary_crossentropy] 
#}
# Regression #
#p = { 
#    'lr' : [0.001], 
#    'first_neuron' : [100],
#    'activation' : [relu],
#    'dropout' : [0],
#    'hidden_layers' : [5], # does not take into account the first layer
#    'output_activation' : [elu],
#    'l2' : [0],
#    'optimizer' : [Adam],  
#    'epochs' : [100],   
#    'batch_size' : [50000], 
#    'loss_function' : [mean_squared_error]
#}
p = { 
    'lr' : [0.01], 
    'first_neuron' : [200],
    'activation' : [relu],
    'dropout' : [0],
    'hidden_layers' : [5], # does not take into account the first layer
    'output_activation' : [elu],
    'l2' : [0],
    'optimizer' : [Adam],  
    'epochs' : [200],   
    'batch_size' : [50000], 
    'loss_function' : [mean_squared_error],
}
repetition = 1 # How many times each hyperparameter has to be used 

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
         #'-log10(weight_TT)',
         #'-log10(weight_DY)',
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
         #'lep2_p4_Phi _minus_ lep1_p4_Phi',
         #'jet1_p4_Pt',
         #'jet1_p4_Eta',
         #'jet1_p4_Phi _minus_ lep1_p4_Phi',
         #'jet2_p4_Pt',
         #'jet2_p4_Eta',
         #'jet2_p4_Phi _minus_ lep1_p4_Phi',
         #'met_pt',
         #'met_phi _minus_ lep1_p4_Phi',

         # Reprocess #
         #'lep1_p4_Pt',
         #'lep1_p4_Eta',
         #'lep2_p4_Pt',
         #'lep2_p4_Eta',
         #'lep2_p4_Phi-lep1_p4_Phi',
         #'jet1_p4_Pt',
         #'jet1_p4_Eta',
         #'jet1_p4_Phi-lep1_p4_Phi',
         #'jet2_p4_Pt',
         #'jet2_p4_Eta',
         #'jet2_p4_Phi-lep1_p4_Phi',
         #'met_pt',
         #'met_phi-lep1_p4_Phi',

         # Matrix Element #
        'init1_p4.E()',
        'init2_p4.E()',
        'positron_p4.Px()',
        'positron_p4.Py()',
        'positron_p4.Pz()',
        'positron_p4.E()',
        'neutrino_p4.Px()',
        'neutrino_p4.Py()',
        'neutrino_p4.Pz()',
        'neutrino_p4.E()',
        'bjet_p4.Px()',
        'bjet_p4.Py()',
        'bjet_p4.Pz()',
        'bjet_p4.E()',
        'electron_p4.Px()',
        'electron_p4.Py()',
        'electron_p4.Pz()',
        'electron_p4.E()',
        'antineutrino_p4.Px()',
        'antineutrino_p4.Py()',
        'antineutrino_p4.Pz()',
        'antineutrino_p4.E()',
        'antibjet_p4.Px()',
        'antibjet_p4.Py()',
        'antibjet_p4.Pz()',
        'antibjet_p4.E()',
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
         ########  Matrix Element ##########
        '-log10(MEPdf)'
          ] 
other_variables = [
                    'MEPdf',
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
                    
                     #'ll_M',
                     #'jj_M',
                     #'lljj_M',

                     #'weight_TT',
                     #'weight_DY',
                     #'output_DY',
                     #'output_TT',

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

                     #'weight_DY_time',
                     #'weight_DY_err',
                     #'weight_TT_time',
                     #'weight_TT_err',
                     #'weight_HToZA_mH_200_mA_50_err',
                     #'weight_HToZA_mH_200_mA_100_err',
                     #'weight_HToZA_mH_250_mA_50_err', 
                     #'weight_HToZA_mH_250_mA_100_err',
                     #'weight_HToZA_mH_300_mA_50_err', 
                     #'weight_HToZA_mH_300_mA_100_err',
                     #'weight_HToZA_mH_300_mA_200_err',
                     #'weight_HToZA_mH_500_mA_50_err', 
                     #'weight_HToZA_mH_500_mA_100_err',
                     #'weight_HToZA_mH_500_mA_200_err',
                     #'weight_HToZA_mH_500_mA_300_err',
                     #'weight_HToZA_mH_500_mA_400_err',
                     #'weight_HToZA_mH_650_mA_50_err', 
                     #'weight_HToZA_mH_800_mA_50_err', 
                     #'weight_HToZA_mH_800_mA_100_err',
                     #'weight_HToZA_mH_800_mA_200_err',
                     #'weight_HToZA_mH_800_mA_400_err',
                     #'weight_HToZA_mH_800_mA_700_err',
                     #'weight_HToZA_mH_1000_mA_50_err',
                     #'weight_HToZA_mH_1000_mA_200_err', 
                     #'weight_HToZA_mH_1000_mA_500_err', 
                     #'weight_HToZA_mH_2000_mA_1000_err',
                     #'weight_HToZA_mH_3000_mA_2000_err',
                     #'weight_HToZA_mH_200_mA_100_time',
                     #'weight_HToZA_mH_250_mA_50_time', 
                     #'weight_HToZA_mH_250_mA_100_time',
                     #'weight_HToZA_mH_300_mA_50_time', 
                     #'weight_HToZA_mH_300_mA_100_time',
                     #'weight_HToZA_mH_300_mA_200_time',
                     #'weight_HToZA_mH_500_mA_50_time', 
                     #'weight_HToZA_mH_500_mA_100_time',
                     #'weight_HToZA_mH_500_mA_200_time',
                     #'weight_HToZA_mH_500_mA_300_time',
                     #'weight_HToZA_mH_500_mA_400_time',
                     #'weight_HToZA_mH_650_mA_50_time', 
                     #'weight_HToZA_mH_800_mA_50_time', 
                     #'weight_HToZA_mH_800_mA_100_time',
                     #'weight_HToZA_mH_800_mA_200_time',
                     #'weight_HToZA_mH_800_mA_400_time',
                     #'weight_HToZA_mH_800_mA_700_time',
                     #'weight_HToZA_mH_1000_mA_50_time',
                     #'weight_HToZA_mH_1000_mA_200_time', 
                     #'weight_HToZA_mH_1000_mA_500_time', 
                     #'weight_HToZA_mH_2000_mA_1000_time',
                     #'weight_HToZA_mH_3000_mA_2000_time',
                     #'weight_HToZA_mH_600_mA_250_err', 
                     #'weight_HToZA_mH_600_mA_250_time', 
                     #'is_JEC',
                  ]
#weights = 'total_weight'
weights = None

################################  dtype operation ##############################

def make_dtype(list_names): # root_numpy does not like . and ()
    list_dtype = [(name.replace('.','_').replace('(','').replace(')','').replace('-','_minus_').replace('*','_times_')) for name in list_names]
    return list_dtype
        



                                



