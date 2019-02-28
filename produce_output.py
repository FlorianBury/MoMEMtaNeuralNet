import os
import copy
import logging
import numpy as np
from root_numpy import array2root

from NeuralNet import HyperModel
from import_tree import Tree2Numpy
import parameters


class ProduceOutput:
    def __init__(self,model,scaler,dtype_base):
        self.model = model              # Model of the NeuralNet
        self.scaler = scaler            # Scaler to preprocess the inputs
        self.dtype_base = dtype_base    # dtype for array2root

    def OutputFromTraining(self,inputs_scaled,outputs_scaled,other,tag,path_output):
        """
            Get the output of the model from the test set
            This is data separated from the training
        """
        # De-preprocess inputs and outputs to save in file #
        inputs_unscaled = inputs_scaled*self.scaler.scale_+self.scaler.mean_ # undo preprocess
        outputs_unscaled = np.power(10,-outputs_scaled)

        # Concatenate output #
        full_out = np.c_[inputs_unscaled,outputs_unscaled,other] # without NN output
        dtype = copy.deepcopy(self.dtype_base)

        # Get Model Output #

        #try:
        instance = HyperModel(self.model)
        out = np.asarray(instance.HyperRestore(inputs_scaled))[:,:,0].transpose() # Tensor list -> np vector
        out = np.power(10,-out) # Back to real weights
        full_out = np.c_[full_out,out]
        dtype.append(('output_DY','float64'))
        dtype.append(('output_TT','float64'))
        #except Exception as e:
        #    logging.warning('Could not find the model due to "%s"'%e)

        full_out.dtype = dtype
        full_out_name = os.path.join(path_output,tag+'.root')
        array2root(full_out,full_out_name,mode='recreate')
        logging.info('Output saved as : '+full_out_name)
         

    def OutputNewData(self,input_dir,list_sample,path_output,cut):
        """
            Given a model, produce the output 
            The Network has never seen this data !
        """
        # Loop over datasets #
        for f in list_sample: 
            name = os.path.basename(f)
            full_path = os.path.join(input_dir,f)
            logging.info('\tLooking at %s'%name)

            # Get the data #
            variables = parameters.inputs+parameters.outputs+parameters.other_variables
            
            data, weight = Tree2Numpy(input_file=full_path,variables=variables,weight=parameters.weights[0],reweight_to_cross_section=True,cut=cut)
            if data.shape[0]==0:
                continue # Avoids empty trees
           
            # Split and Pre-process #
            NIn = len(parameters.inputs)
            NOut = len(parameters.outputs)
            
            inputs_unscaled = data[:,:NIn]
            inputs_scaled = self.scaler.transform(inputs_unscaled)  
            outputs = data[:,NIn:NIn+NOut]
            other = np.c_[data[:,NIn+NOut:],weight]

            # Concatenate full_out #
            full_out = np.c_[inputs_unscaled,outputs,other]
            dtype = copy.deepcopy(self.dtype_base)

            # Get Model output #
            try:
                instance = HyperModel(self.model)
                out = np.asarray(instance.HyperRestore(inputs_scaled))[:,:,0].transpose() # Tensor list -> np vector
                out = np.power(10,-out) # Back to real weights
                full_out = np.c_[full_out,out]
                dtype.append(('output_DY','float64'))
                dtype.append(('output_TT','float64'))
            except Exception as e:
                logging.warning('Could not find the model due to "%s"'%e)

            # Save to Root file # 
            full_out.dtype = dtype
            output_name = os.path.join(path_output,name)
            array2root(full_out,output_name,mode='recreate')
            logging.info('Output saved as : '+output_name)


