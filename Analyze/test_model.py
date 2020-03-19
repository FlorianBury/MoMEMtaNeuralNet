import sys
import os
import numpy as np
import pickle
from keras.models import model_from_json

sys.path.append(os.path.abspath('..'))
from preprocessing import PreprocessLayer

class TestModel:
    def __init__(self,basemodel,preprocess_layer=False):
        self.basemodel = basemodel
        self.preprocess_layer = preprocess_layer
        self.custom_objects = {"PreprocessLayer":PreprocessLayer} if preprocess_layer else {}

        self.load_model()

    def load_model(self):
        with open(self.basemodel+'.json','r') as f:
            loaded_model_json = f.read()
        self.model = model_from_json(loaded_model_json,custom_objects = self.custom_objects)
        self.model.load_weights(self.basemodel+".h5")
        if not self.preprocess_layer:
            with open(self.basemodel+'.pkl', 'rb') as handle:
                self.scaler = pickle.load(handle)

    def process(self,inputs):
        if len(inputs.shape) == 1: # turn vector into matrix
            inputs = inputs.reshape(1,-1)

        if not self.preprocess_layer:
            inputs = self.scaler.transform(inputs)

        outputs = self.model.predict(inputs)
        return outputs

