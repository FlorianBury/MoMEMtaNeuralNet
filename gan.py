import os
import sys
import json
import logging
import enlighten
import warnings
import random
import string

import numpy as np

from keras.layers import Input, Dense, Reshape, Flatten, Dropout
from keras.losses import binary_crossentropy, mean_squared_error 
from keras.layers import BatchNormalization, Activation, merge, Concatenate
from keras.activations import relu,selu,elu, sigmoid, tanh
from keras.regularizers import l1,l2 
from keras.models import Sequential, Model, load_model, model_from_json
from keras.optimizers import Adam
from keras.callbacks import History

from talos.model.layers import hidden_layers

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt

import parameters

SMALL_SIZE = 16
MEDIUM_SIZE = 20
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title

def launch_GAN(x_train,y_train,x_val,y_val,params): # Needed for Talos
    # Instantiate #
    instance = GAN(x_train,y_train,x_val,y_val,params)
    # Launch the training #
    instance.train(epochs=params['epochs'],batch_size=params['batch_size'])
    # Make the plot of the History #
    instance.PlotHistory()
    return instance.history,instance.model_talos


class GAN(): # TODO : add weights
    def __init__(self,x_train,y_train,x_val,y_val,params):
        #self.x_train, self.x_val, self.y_train, self.y_val = train_test_split(x,y,test_size=0.3)
        self.x_train = x_train
        self.y_train = y_train
        self.x_val = x_val
        self.y_val = y_val
        self.path_generator = parameters.path_generator 
        self.path_classifier = parameters.path_classifier
        logging.info("Training set size : %0.f"%self.x_train.shape[0])
        logging.info("Validation set size : %0.f"%self.x_val.shape[0])
        self.history = History()
        self.history.on_train_begin()

        optimizer = Adam(lr=params['lr'])

        # Build and compile the discriminator
        self.discriminator = self.build_discriminator(params)
        self.discriminator.compile(loss=binary_crossentropy,
            optimizer=optimizer,
            metrics=['accuracy'])

        # Build the generator -> Compile in combined model
        self.generator_TT = self.build_generator('TT')
        self.generator_DY = self.build_generator('DY')

        # Build and compile the classifier middle stage
        self.classifier = self.build_classifier()
        self.classifier.compile(loss=binary_crossentropy,
            optimizer=optimizer,
            metrics=['accuracy'])


        # The generator takes 4-vectors and returns TT and DY weights
        IN = Input(shape=(self.x_train.shape[1],))
        OUT_DY = self.generator_DY(IN)
        OUT_TT = self.generator_TT(IN)
        OUT_GEN = Concatenate(axis=-1)([OUT_DY,OUT_TT])

        self.model_talos = Model(inputs=IN, outputs=[OUT_DY,OUT_TT]) # Model to be passed to Talos 


        # The classifier takes TT and DY weights and returns probabilities TT, DY and HToZA
        OUT_CLASS = self.classifier([OUT_GEN])

        # For the combined model we will only train the generator
        self.discriminator.trainable = False
        self.classifier.trainable = False # Used as a function
        # Do not compile after !!! (even though this removes a UserWarning)


        # The discriminator takes generated images as input and determines validity
        OUT_DIS = self.discriminator(OUT_CLASS)

        # The combined model  (stacked generator and discriminator)
        # Trains the generator to fool the discriminator
        self.combined = Model(IN,OUT_DIS)
        self.combined.compile(loss=binary_crossentropy, optimizer=optimizer)
        logging.info("Combined model")
        self.combined.summary()

        # Container for plotters #
        self.batch = []
        self.disc_loss = []
        self.disc_val_loss = []
        self.disc_acc = []
        self.disc_val_acc = []
        self.comb_loss = []
        self.comb_val_loss = []
        self.DY_loss = []
        self.TT_loss = []
        self.gen_loss = []
        self.DY_val_loss = []
        self.TT_val_loss = []
        self.gen_val_loss = []


    def build_generator(self,tag):
        with open(self.path_generator.format(tag)+'.json', 'r') as json_file:
            architecture = json.load(json_file)
        model = model_from_json(json.dumps(architecture))
        model.load_weights(self.path_generator.format(tag)+'.h5')
        logging.info("Generator for %s"%tag)
        model.summary()

        inputs = Input(shape=(self.x_train.shape[1],)) # Inputs : Pt,Eta,Phi +Met
        outputs = model(inputs)                        # Outputs : TT and DY weights

        return Model(inputs,outputs)

    def build_discriminator(self,params):

        IN = Input(shape=(3,))
        L1 = Dense(params['first_neuron'],
                       activation=params['activation'],
                       kernel_regularizer=l2(params['l2']))(IN)
        HIDDEN = hidden_layers(params,1,batch_normalization=True).API(L1)
        OUT = Dense(1,activation=params['output_activation'])(HIDDEN)
        logging.info("Discriminator")
        model = Model(IN,OUT)
        model.summary()

        return model
    def build_classifier(self):
        with open(self.path_classifier+'.json', 'r') as json_file:
            architecture = json.load(json_file)
        model = model_from_json(json.dumps(architecture))
        model.load_weights(self.path_classifier+'.h5')
        logging.info("Classifier")
        model.summary()

        inputs = Input(shape=(2,)) # We take 2 weights : TT and DY
        outputs = model(inputs)    # 3 outputs : P(TT), P(DY) and P(HToZA)

        return Model(inputs,outputs)
        

    def train(self, epochs, batch_size=128):

        # Split into subsets #
        indexes  = np.arange(0,self.x_train.shape[0])
        np.random.shuffle(indexes)
        list_subset = np.array_split(indexes,np.ceil(self.x_train.shape[0]/batch_size))
        n_batches = len(list_subset)

        for epoch in range(0,epochs):
            logging.info('-'*80)
            logging.info('Epoch %d'%epoch)

            # Setup progress bar
            manager = enlighten.get_manager()
            pbar = manager.counter(total=n_batches, desc='Progress', unit='Batch')
            for n,idx_sub in enumerate(list_subset):
                # ---------------------
                #  Train Discriminator
                # ---------------------
                # Adversarial ground truths
                valid = np.ones((idx_sub.shape[0], 1)) # Coming from MoMEMta
                fake = np.zeros((idx_sub.shape[0], 1)) # Coming from the DNN that fits MoMEMta
                # Select a random batch of inputs and generator targets
                inputs_train = self.x_train[idx_sub]
                gen_targets_train = self.y_train[idx_sub]

                # Select validation set #
                idx_val = np.random.randint(0, self.x_val.shape[0], idx_sub.shape[0])
                inputs_val = self.x_val[idx_val]
                gen_targets_val = self.y_val[idx_val]


                # Get generator output (aka the weights)
                gen_outputs_train_DY = self.generator_DY.predict(inputs_train)
                gen_outputs_train_TT = self.generator_TT.predict(inputs_train)
                gen_outputs_train = np.c_[gen_outputs_train_DY,gen_outputs_train_TT]

                gen_outputs_val_DY = self.generator_DY.predict(inputs_val)
                gen_outputs_val_TT = self.generator_TT.predict(inputs_val)
                gen_outputs_val = np.c_[gen_outputs_val_DY,gen_outputs_val_TT]

                # Evaluate generator #
                DY_loss = mean_squared_error(gen_targets_train[:,0],gen_outputs_train_DY)
                TT_loss = mean_squared_error(gen_targets_train[:,1],gen_outputs_train_TT)
                DY_val_loss = mean_squared_error(gen_targets_val[:,0],gen_outputs_val_DY)
                TT_val_loss = mean_squared_error(gen_targets_val[:,1],gen_outputs_val_TT)
                gen_loss = mean_squared_error(gen_targets_train,gen_outputs_train)
                gen_val_loss = mean_squared_error(gen_targets_val,gen_outputs_val)

                # Pass both generator values to classifier #
                class_targets_train = self.classifier.predict(gen_targets_train)
                class_outputs_train = self.classifier.predict(gen_outputs_train)

                class_targets_val = self.classifier.predict(gen_targets_val)
                class_outputs_val = self.classifier.predict(gen_outputs_val)

                # Train the discriminator
                with warnings.catch_warnings(): # avoids safety UserWarning from Keras
                    # Since we have weights not being updated (discriminator)
                    # https://github.com/eriklindernoren/Keras-GAN/issues/91
                    warnings.simplefilter("ignore")
                    d_loss_train_real = self.discriminator.train_on_batch(class_targets_train,valid)
                    d_loss_train_fake = self.discriminator.train_on_batch(class_outputs_train,fake)
                    d_loss_val_real = self.discriminator.test_on_batch(class_targets_val,valid)
                    d_loss_val_fake = self.discriminator.test_on_batch(class_outputs_val,fake)

                d_loss = 0.5 * np.add(d_loss_train_real, d_loss_train_fake)
                d_val_loss = 0.5 * np.add(d_loss_val_real, d_loss_val_fake)

                # ---------------------
                #  Train Generator
                # ---------------------
                # Train the generator (to have the discriminator label samples as valid)
                g_loss = self.combined.train_on_batch(inputs_train, valid)
                g_val_loss = self.combined.test_on_batch(inputs_val, valid)
                
                # Register in container #
                frac_epoch = float(n)/float(n_batches)+epoch
                self.batch.append(frac_epoch)

                self.disc_loss.append(d_loss[0])
                self.disc_val_loss.append(d_val_loss[0])
                self.disc_acc.append(100*d_loss[1])
                self.disc_val_acc.append(100*d_val_loss[1])

                self.comb_loss.append(g_loss)
                self.comb_val_loss.append(g_val_loss)
                self.DY_loss.append(DY_loss)
                self.DY_val_loss.append(DY_val_loss)
                self.TT_loss.append(TT_loss)
                self.TT_val_loss.append(TT_val_loss)

                # Append history #
                batch_log = {}
                batch_log['loss'] = g_loss
                batch_log['val_loss'] = g_val_loss
                batch_log['disc_loss'] = d_loss[0]
                batch_log['disc_val_loss'] = d_val_loss[0]
                batch_log['disc_acc'] = 100*d_loss[1]
                batch_log['disc_val_acc'] = 100*d_val_loss[1]
                batch_log['gen_loss'] = gen_loss
                batch_log['gen_val_loss'] = gen_val_loss
                batch_log['DY_loss'] = DY_loss
                batch_log['DY_val_loss'] = DY_val_loss
                batch_log['TT_loss'] = TT_loss
                batch_log['TT_val_loss'] = TT_val_loss

                self.history.on_epoch_end(frac_epoch,batch_log)

                # Plot the progress of the batch 
                logging.info(("Batch %d/%d"%(n+1,n_batches)).ljust(15,' ')+" D [loss: %.5f, val_loss : %.5f]    [ acc.: %.2f%%, val_acc.: %.2%%f]" % (d_loss[0], d_val_loss[0],100*d_loss[1], 100*d_val_loss[1]))

                logging.info(''.rjust(15,'.')+" G [loss: %.5f, val_loss : %.5f] DY [ loss: %.5f, val_loss: %.5f] TT [loss: %.5f, val_loss: %.5f]" % (g_loss,g_val_loss,DY_loss,DY_val_loss,TT_loss,TT_val_loss))
                pbar.update()

            # Stop progress bar #
            manager.stop()
            # Plot the progress of the epoch
            
            #g_loss = self.combined.test_on_batch(self.x_train, np.ones(self.x_train.shape[0]))
            #g_val_loss = self.combined.test_on_batch(self.x_val, np.ones(self.x_val.shape[0]))
            ## output of generator #
            #y_train_pred_DY = self.generator_DY.predict(self.x_train)
            #y_train_pred_TT = self.generator_TT.predict(self.x_train)
            #y_val_pred_DY = self.generator_DY.predict(self.x_val)
            #y_val_pred_TT = self.generator_TT.predict(self.x_val)
            ## Loss and val_loss of generator
            #loss_DY = mean_squared_error(self.y_train[:,0],y_train_pred_DY)
            #loss_TT = mean_squared_error(self.y_train[:,1],y_train_pred_TT)
            #val_loss_DY = mean_squared_error(self.y_val[:,0],y_val_pred_DY)
            #val_loss_TT = mean_squared_error(self.y_val[:,1],y_val_pred_TT)

            ## Record in containers #
            #self.epoch.append(epoch)
            #self.comb_loss.append(g_loss)
            #self.comb_val_loss.append(g_val_loss)
            #self.DY_loss.append(loss_DY)
            #self.TT_loss.append(loss_TT)
            #self.DY_val_loss.append(val_loss_DY)
            #self.TT_val_loss.append(val_loss_TT)

            # Log #


    def PlotHistory(self):
        try:
            fig,ax = plt.subplots(4,1,figsize=(9,16))
            fig.subplots_adjust(right=0.87, wspace = 0.3, hspace=0.4, left=0.1, bottom=0.05, top=0.92)
            fig.suptitle('Generative Adversarial Network')

            # Discriminator #
            ax_twin = ax[0].twinx()
            ax_twin.tick_params('y')
            line1 = ax[0].plot(self.batch,self.disc_acc,c='g',label='Accuracy [%]')
            line2 = ax[0].plot(self.batch,self.disc_val_acc,c='g',linestyle=':',label='Validation accuracy')
            line3 = ax_twin.plot(self.batch,self.disc_loss,c='r',label='Cross-entropy loss')
            line4 = ax_twin.plot(self.batch,self.disc_val_loss,c='r',linestyle=':',label='validation cross-entropy loss')
            ax[0].set_xlabel('Epochs')
            ax[0].set_ylabel('Accuracy')
            ax_twin.set_ylabel('Loss')
            ax[0].set_title('Disciminator')
            lines = line1+line2+line3+line4 # Because two plots on same legend
            labs = [l.get_label() for l in lines]
            ax[0].legend(lines, labs, loc='center right')

            # DY Network #
            ax[1].plot(self.batch,self.DY_loss,color='b',label='Generator DY loss')
            ax[1].plot(self.batch,self.DY_val_loss,color='b',linestyle=':',label='Generator DY val loss')
            ax[1].set_xlabel('Epochs')
            ax[1].set_ylabel('Loss')
            ax[1].set_title('DY Network')
            ax[1].legend(loc='upper right')

            # TT Network #
            ax[2].plot(self.batch,self.TT_loss,color='b',label='Generator TT loss')
            ax[2].plot(self.batch,self.TT_val_loss,color='b',linestyle=':',label='Generator TT val loss')
            ax[2].set_xlabel('Epochs')
            ax[2].set_ylabel('Loss')
            ax[2].set_title('TT Network')
            ax[2].legend(loc='upper right')

            # Combined Network #
            ax[3].plot(self.batch,self.comb_loss,color='b',label='GAN loss')
            ax[3].plot(self.batch,self.comb_val_loss,color='b',linestyle=':',label='GAN val loss')
            ax[3].set_xlabel('Epochs')
            ax[3].set_ylabel('Loss')
            ax[3].set_title('Combined Network')
            ax[3].legend(loc='upper right')

            
            rand_hash = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16)) # avoids overwritting
            png_name = 'GAN_%s.png'%rand_hash
            fig.savefig(png_name)
            logging.info('Curves saved as %s'%png_name)

        except Exception as e:
            logging.error(e)
        finally:
            np.save('self.batch',self.batch)
            np.save('self.disc_loss',self.disc_loss)
            np.save('self.disc_val_loss',self.disc_val_loss)
            np.save('self.disc_acc',self.disc_acc)
            np.save('self.disc_val_acc',self.disc_val_acc)
            np.save('self.comb_loss',self.comb_loss)
            np.save('self.comb_val_loss',self.comb_val_loss)
            np.save('self.gen_loss',self.gen_loss)
            np.save('self.gen_val_loss',self.gen_val_loss)
            np.save('self.DY_loss',self.DY_loss)
            np.save('self.DY_val_loss',self.DY_val_loss)
            np.save('self.TT_loss',self.TT_loss)
            np.save('self.TT_val_loss',self.TT_val_loss)


