import sys
import logging
import os
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def PlotScans(data,path):
    logging.debug('Data from csv')
    logging.debug(data)
    sns.set(rc={'figure.figsize':(16,9)})

    # Parameters barplot #
    g = sns.relplot(x="hidden_layers",
                y="eval_error",
                col="first_neuron",
                hue="activation",
                style="activation",
                data=data);
    g.set(yscale="log");
    g.set(ylim=(0.1, None))
    plt.savefig(os.path.join(path,'barplot_neuron_hidden_activation.png'))

    g = sns.relplot(x="hidden_layers",
                y="eval_error",
                hue="output_activation",
                style="output_activation",
                data=data);
    g.set(yscale="log");
    g.set(ylim=(0.1, None))
    plt.savefig(os.path.join(path,'barplot_hidden_last_activation.png'))
   #plt.show()

    g = sns.relplot(x="l2",
                y="eval_error",
                col='dropout',
                data=data);
    g.set(yscale="log");
    g.set(ylim=(0.1, None))
    plt.savefig(os.path.join(path,'l2_dropout.png'))


    # Lr batch catplot #
    g = sns.catplot(x="lr", 
                y="eval_error",
                hue="batch_size",
                kind="swarm",
                data=data);
    g.set(ylim=(0.1, None))
    g.set(yscale="log");
    #plt.show()
    plt.savefig(os.path.join(path,'cat_plot_lr_batch.png'))
    
    # Pairplot #
    sns.pairplot(data=data, 
                 hue="hidden_layers");
    plt.savefig(os.path.join(path,'pairplot_hidden.png'))
    
    # LMplot # 
    sns.lmplot(x="val_loss",
               y="loss", 
               col="hidden_layers",
               hue="first_neuron",
               data=data);
    plt.savefig(os.path.join(path,'reg_loss.png'))                                                                                                                                               

    sns.kdeplot(data.lr, data.batch_size , cmap="Blues", shade=True, shade_lowest=True);
    plt.savefig(os.path.join(path,'kde_lr_batch.png'))                                                                                                                                               

    # joinplot eval_erro val_loss #
    g = sns.lmplot(x='eval_error', y='val_loss',
                   truncate=True, height=5, data=data)
    plt.savefig(os.path.join(path,'eval_error_vs_val_loss.png'))
    


