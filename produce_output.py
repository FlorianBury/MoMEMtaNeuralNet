import os
import copy
import logging
import numpy as np
import pandas as pd
from root_numpy import array2root

from NeuralNet import HyperModel
from import_tree import Tree2Pandas
from signal_coupling import Decoupler, Recoupler
import parameters


class ProduceOutput:
    def __init__(self,model,is_signal=False):
        self.model = model              # Model of the NeuralNet
        self.is_signal = is_signal

    def OutputFromTraining(self,data,path_output,output_name=None):
        """
            Get the output of the model from the test set
            This is data separated from the training
            If output_name is specified, the whole data will be written in 'output_name'.root
                if not, the tags in the dataframe are used to split into different files with names 'tag'.root
        """
        list_inputs = copy.deepcopy(parameters.inputs)
        # If signal, decouple the data #
        if self.is_signal:
            data = Decoupler(data)
            list_inputs += ['mH_MEM','mA_MEM'] 

        inputs = data[list_inputs].values
        output = np.empty((inputs.shape[0],0))
        columns = []

        # Get Model Output #

        try:
            instance = HyperModel(self.model,'DY')
            out_DY = np.power(10,-instance.HyperRestore(inputs))
            output = np.c_[output,out_DY]
            columns.append('output_DY')
        except Exception as e:
            logging.warning('Could not find the DY model due to "%s"'%e)
        try:
            instance = HyperModel(self.model,'TT')
            out_TT = np.power(10,-instance.HyperRestore(inputs))
            output = np.c_[output,out_TT]
            columns.append('output_TT')
        except Exception as e:
            logging.warning('Could not find the TT model due to "%s"'%e)
        try:
            instance = HyperModel(self.model,'HToZA')
            out_HToZA = np.power(10,-instance.HyperRestore(inputs))
            output = np.c_[output,out_HToZA]
            columns.append('output_HToZA')
        except Exception as e:
            logging.warning('Could not find the HToZA model due to "%s"'%e)
        try:
            instance = HyperModel(self.model,'class')
            out_class = instance.HyperRestore(inputs)
            output = np.c_[output,out_class]
            columns.extend(['Prob_DNN_DY','Prob_DNN_HToZA','Prob_DNN_TT'])
        except Exception as e:
            logging.warning('Could not find the classification model due to "%s"'%e)


        # From numpy output array to df #
        output_df = pd.DataFrame(output,columns=columns,index=data.index)

        # Make full df #
        full_df = pd.concat([data,output_df],axis=1)
        if self.is_signal:
            logging.info("Signal case : Recoupling of the data")
            full_df = Recoupler(full_df)
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

         
    def OutputNewData(self,input_dir,list_sample,path_output):
        """
            Given a model, produce the output 
            The Network has never seen this data !
        """
        # Loop over datasets #
        for f in list_sample: 
            name = os.path.basename(f)
            full_path = os.path.join(input_dir,f)
            logging.info('Looking at %s'%name)

            # Get the data #
            variables = parameters.inputs+parameters.outputs+parameters.other_variables
            data = Tree2Pandas(input_file=full_path,
                               variables=variables,
                               weight=parameters.weights,
                               reweight_to_cross_section=False)
            if data.shape[0]==0:
                continue # Avoids empty trees
            self.OutputFromTraining(data=data,path_output=path_output,output_name=name)



        


   
    







