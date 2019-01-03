import sys
import os
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def PlotScans(data,path):
    #print (data)
    sns.set(rc={'figure.figsize':(16,9)})

    sns.relplot(x="hidden_layers",
                y="val_loss",
                col="first_neuron",
                hue="activation",
                style="activation",
                data=data);
    plt.savefig(os.path.join(path,'barplot_neuron_hidden_activation.png'))

    sns.relplot(x="hidden_layers",
                y="val_loss",
                hue="output_activation",
                style="output_activation",
                data=data);
    plt.savefig(os.path.join(path,'barplot_hidden_last_activation.png'))
   #plt.show()

    sns.catplot(x="lr", 
                y="val_loss",
                hue="batch_size",
                kind="swarm",
                data=data);
    #plt.show()
    
    plt.savefig(os.path.join(path,'cat_plot_lr_batch.png'))

    sns.pairplot(data=data, 
                 hue="hidden_layers");
    plt.savefig(os.path.join(path,'pairplot_hidden.png'))
    
    sns.jointplot(x="lr", y="batch_size", data=data);
    plt.savefig(os.path.join(path,'joint_lr_batch.png'))                                                                                                                                               

    sns.lmplot(x="val_loss",
               y="loss", 
               col="hidden_layers",
               hue="first_neuron",
               data=data);
    plt.savefig(os.path.join(path,'reg_loss.png'))                                                                                                                                               

    sns.kdeplot(data.lr, data.batch_size , cmap="Blues", shade=True, shade_lowest=True);
    plt.savefig(os.path.join(path,'kde_lr_batch.png'))                                                                                                                                               

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data['lr'], data['batch_size'], data['val_loss'], c='skyblue', s=60)
    ax.view_init(30, 185)
    plt.savefig(os.path.join(path,'lr_batch_val_loss.png'))
