import os
import copy
import sys
import logging
import numpy as np
import pandas as pd
from root_numpy import array2root

from NeuralNet import HyperModel
from import_tree import Tree2Pandas
from signal_coupling import Decoupler, Recoupler
from parameterize_classifier import ParametrizeClassifier
import parameters


class ProduceOutput:
    def __init__(self,model,list_model,is_signal=False,is_class_param=False,list_inputs=None):
        self.model = model              # Model of the NeuralNet
        self.is_signal = is_signal
        self.is_class_param = is_class_param
        self.list_model = list_model
        self.list_inputs = list_inputs
        if self.list_inputs is None:
            self.list_inputs = copy.deepcopy(parameters.inputs) 

    def OutputFromTraining(self,data,path_output,output_name=None):
        """
            Get the output of the model from the test set
            This is data separated from the training
            If output_name is specified, the whole data will be written in 'output_name'.root
                if not, the tags in the dataframe are used to split into different files with names 'tag'.root
        """
        # If signal, decouple the data #
        if self.is_signal:
            decoupled_name = 'weight_HToZA'
            list_to_decouple = parameters.outputs
            self.list_inputs += ['mH_MEM','mA_MEM'] 
            data = Decoupler(data,decoupled_name,list_to_decouple)
        if self.is_class_param:
            signal_name = '-log10(weight_HToZA)'
            data = ParametrizeClassifier(data,name=signal_name) 
            self.list_inputs = ['-log10(weight_DY)','-log10(weight_TT)',signal_name,'mH_gen','mA_gen']
            #decoupled_name = '-log10(weight_HToZA)'
            #list_to_decouple = [s for s in parameters.inputs if s.find('HToZA')!=-1]
            #data = Decoupler(data,decoupled_name,list_to_decouple)
            #self.list_inputs = [s for s in parameters.inputs if s not in list_to_decouple] + [decoupled_name] 
            #self.list_inputs += ['mH_MEM','mA_MEM'] 

        inputs = data[self.list_inputs].values
        output = np.empty((inputs.shape[0],0))
        columns = []

        # Get Model Output #
        for model in self.list_model:
            if model not in ['DY','TT','HToZA','class','class_param','binary']:
                logging.critical('Wrong model type specified : %s must be either "DY", "TT", "HToZA", "class", "class_param", or binary')
                sys.exit(1)

            instance = HyperModel(self.model,model)
            if model in ['DY','TT','HToZA']:
                out = np.power(10,-instance.HyperRestore(inputs))
                columns.append('output_%s'%model)
            else:
                out = instance.HyperRestore(inputs)
                if model in ['binary']:
                    columns.extend(['Prob_MEM_signal'])
                if model in ['class_param','global']:
                    columns.extend(['Prob_MEM_DY','Prob_MEM_HToZA','Prob_MEM_TT'])
                
            output = np.c_[output,out]

        # From numpy output array to df #
        output_df = pd.DataFrame(output,columns=columns,index=data.index)

        # Make full df #
        full_df = pd.concat([data,output_df],axis=1)
        if self.is_signal:
            logging.info("Signal case : Recoupling of the data")
            full_df = Recoupler(full_df,col_to_recouple = ['weight_HToZA','output_HToZA'],N=len(list_to_decouple))
        #if self.is_class_param:
        #    logging.info("Parametric classifier case : Recoupling of the data")
        #    full_df = Recoupler(full_df,col_to_recouple = ['Prob_MEM_DY','Prob_MEM_TT','Prob_MEM_HToZA'],N=len(list_to_decouple))
        # Get the unique tags as a list #
        if output_name is None:
            tag_list = list(full_df['tag'].unique())

            # Loop over tags #
            for tag in tag_list:
                tag_df = full_df.loc[full_df['tag']==tag] # We select the rows corresponding to this tag
                tag_df = tag_df.drop('tag',axis=1)

                # From df to numpy array with dtype #
                tag_output = tag_df.to_records(index=False,column_dtypes='float64')
                tag_output.dtype.names = parameters.make_dtype(tag_output.dtype.names)# because ( ) and . are an issue for root_numpy
                tag_output_name = os.path.join(path_output,tag+'.root')

                # Save as root file #
                array2root(tag_output,tag_output_name,mode='recreate')
                logging.info('Output saved as : '+tag_output_name)
        else:
            # From df to numpy array with dtype #
            full_output = full_df.to_records(index=False,column_dtypes='float64')
            full_output.dtype.names = parameters.make_dtype(full_output.dtype.names)# because ( ) and . are an issue for root_numpy
            full_output_name = os.path.join(path_output,output_name)
            array2root(full_output,full_output_name,mode='recreate')
            logging.info('Output saved as : '+full_output_name)

         
    def OutputNewData(self,input_dir,list_sample,path_output,variables=None):
        """
            Given a model, produce the output 
            The Network has never seen this data !
        """
        # Loop over datasets #
        logging.info('Input directory : %s'%input_dir)
        for f in list_sample: 
            name = os.path.basename(f)
            full_path = os.path.join(input_dir,f)
            logging.info('Looking at %s'%f)

            # Get the data #
            if variables is None:
                var = parameters.inputs+parameters.outputs+parameters.other_variables
            else:
                var = copy.deepcopy(variables)
            data = Tree2Pandas(input_file=full_path,
                               variables=var,
                               weight=parameters.weights,
                               reweight_to_cross_section=False)
            if data.shape[0]==0:
                logging.info('\tEmpty tree')
                continue # Avoids empty trees
            self.OutputFromTraining(data=data,path_output=path_output,output_name=name)



        


   
    







