import os
import sys
import re
import json
import glob
import logging
import copy
import numpy as np
import pandas as pd
import enlighten
import psutil
import time
from sklearn import metrics
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from root_numpy import array2root

sys.path.insert(0,"..") # We need our own version of talos
                        # If we import our modules after the version is sites-package, our version is ignored
from NeuralNet import HyperModel
from import_tree import Tree2Pandas
from cutWindow import massWindow
from signal_coupling import Repeater, Transposer, Decoupler, Recoupler
from Utils import ListBranches

# PYPLOT STYLE # 
SMALL_SIZE = 10
MEDIUM_SIZE = 20 
BIGGER_SIZE = 24
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes 
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels 
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels 
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title


#################################################################################################
# ProcessDNN #
#################################################################################################
class ProcessDNN:
    def __init__(self,model_name,list_inputs,label,list_files,variables,path_signal,start=0,end=-1,cuts=None,save_path=None,force=False,mH=None,mA=None,do_all_masses=False):
        self.label = label              # For printing purposes
        self.model_name = model_name    
        # Name of the DNN model (same with disctinction for categories : 
        #       model_+ [DY,TT,HToZA,class]
        self.list_inputs = list_inputs  # inputs of the DNN
        self.list_files = list_files    # List of files to apply the DNN and ellipse later
        self.variables = variables      # Variables to be extracted from tree
        self.cuts = cuts                # Cuts to apply
        self.save_path = save_path      # Wether to look for a save
        self.force = force              # Wether to force the processing and erase the save
        self.path_signal = path_signal  # Path to (new) signal samples to get masses
        self.do_all_masses = do_all_masses
        self.mH = mH
        self.mA = mA
        self.start = start
        self.end = end

        self.p = psutil.Process(os.getpid())
        print ('[MEMORY] current pid : ',os.getpid())

        print ('Extracting data for %s sample'%self.label)
        # Check if save exists #
        if force: print ('Careful, will replace the save')
        save_exists = False if force else os.path.exists(self.save_path) 
            
        # Process #
        if save_exists:
            self._recoverFromROOT()
        else:
            self._getMasses()
            self._memoryUsage()
            self._getData()
            self._memoryUsage()
            self._produceWeights()
            self._memoryUsage()
            self._produceGlobalProbabilities()
            self._memoryUsage()
            self._produceParamProbabilities()
            self._memoryUsage()
            self._removeUselessBranches()
            self._memoryUsage()
            self._saveAsROOT()

    def _getMasses(self):
        if self.do_all_masses:
            self.new_masses = np.empty((0,2)) 
            p = re.compile(r'\d+[p]\d+')
            for f in glob.glob(os.path.join(self.path_signal,'*root')):
                name = os.path.basename(f)
                arr = np.array([[float(p.findall(name)[0].replace('p','.')) , float(p.findall(name)[1].replace('p','.'))]])
                self.new_masses = np.append(self.new_masses,arr,axis=0)  
        else:
            self.new_masses = np.array([[self.mH,self.mA]])
            
        self.old_masses = np.array([[200,50],
                            [200,100],
                            [250,50],
                            [250,100],
                            [300,50],
                            [300,100],
                            [300,200],
                            [500,50],
                            [500,100],
                            [500,200],
                            [500,300],
                            [500,400],
                            [650,50],
                            [800,50],
                            [800,100],
                            [800,200],
                            [800,400],
                            [800,700],
                            [1000,50],
                            [1000,200],
                            [1000,500],
                            [2000,1000],
                            [3000,2000]])
    def _memoryUsage(self):
        print ('[MEMORY] Current memory usage : %0.3f GB'%(self.p.memory_info().rss/(1024**3)))

    def _getData(self):
        data = []
        manager = enlighten.get_manager()
        pbar = manager.counter(total=len(self.list_files), desc='Progress', unit='File')
        for f in self.list_files:
            df = Tree2Pandas(input_file = f, 
                             variables = self.variables, 
                             cut = self.cuts,
                             reweight_to_cross_section=True, 
                             n = self.end,
                             start = self.start,
                             tree_name='t')
            self._memoryUsage()
            data.append(df)
            pbar.update()
        manager.stop()
        self.data = pd.concat(data, axis=0)
        self.size = self.data.shape[0]
        print ('Sample size : %d'%(self.size))
        if self.size == 0:
            sys.exit('Empty tree')
 
    def _produceWeights(self):
        """
        Careful, weights will be in -log10 !
        """
        print ('Producing weights for %s sample'%self.label)
        # Initialize DNN model #
        model_DY = HyperModel(self.model_name,'DY')
        model_TT = HyperModel(self.model_name,'TT')
        model_HToZA = HyperModel(self.model_name,'HToZA')

        self._memoryUsage()
        inputs = self.data[self.list_inputs].values
        # Background weights #
        start_time = time.time()
        weight_DY = model_DY.HyperRestore(inputs,batch_size=512,verbose=1)
        print("--- %0.5f seconds ---" % ((time.time() - start_time)*1000))
        print ('...... DY weights done')
        self._memoryUsage()
        start_time = time.time()
        weight_TT = model_TT.HyperRestore(inputs,batch_size=512,verbose=1)
        print("--- %0.5f seconds ---" % ((time.time() - start_time)*1000))
        print ('...... TT weights done')
        self.weight_names = ['weight_DY','weight_TT']
        self._memoryUsage()

        # Signal weights #
        masses = np.concatenate((self.old_masses,self.new_masses),axis=0)
        self.weight_names.extend(['weight_old_mH_%0.2f_mA_%0.2f'%(self.old_masses[i,0],self.old_masses[i,1]) for i in range(self.old_masses.shape[0])])
        self.weight_names.extend(['weight_new_mH_%0.2f_mA_%0.2f'%(self.new_masses[i,0],self.new_masses[i,1]) for i in range(self.new_masses.shape[0])])
        print ('...... Decoupling signal inputs')
        inputs = Repeater(inputs,masses.shape[0])
        inputs = np.c_[inputs,np.tile(masses,(self.size,1))]
        self._memoryUsage()
        print ('...... Processing signal inputs')
        start_time = time.time()
        weight_HToZA = model_HToZA.HyperRestore(inputs,batch_size=512,verbose=1)
        print("--- %0.5f seconds ---" % ((time.time() - start_time)*1000))
        self._memoryUsage()
        print ('...... Recoupling signal inputs')
        weight_HToZA = Transposer(weight_HToZA,masses.shape[0])
        print ('...... HToZA weights done')
        self._memoryUsage()

        # Make into DF #
        weights = np.c_[weight_DY,weight_TT,weight_HToZA]
        weights = pd.DataFrame(weights)
        weights.columns = self.weight_names
        weights = weights.reset_index(drop=True)
        self.data = self.data.reset_index(drop=True)
        self.data = pd.concat([self.data,weights],axis=1)
        print ('...... Concatenation done')

        self._memoryUsage()
        # Remove the useless DF #
        del inputs
        del weights

    def _produceGlobalProbabilities(self):
        print ('Producing global probabilities for %s sample'%self.label)
        self._memoryUsage()
        # Initialize DNN model #
        model_class = HyperModel(self.model_name,'class_global')
        # List of inputs (only old masses weights and backgrounds) #
        weight_names = ['weight_DY','weight_TT']
        weight_names += ['weight_old_mH_%0.2f_mA_%0.2f'%(self.old_masses[i,0],self.old_masses[i,1]) for i in range(self.old_masses.shape[0])]
        # Get probs #
        start_time = time.time()
        probs = model_class.HyperRestore(self.data[weight_names].values,batch_size=512,verbose=1)
        print("--- %0.5f seconds ---" % ((time.time() - start_time)*1000))
        print ('...... Classification probabilities done')
        self._memoryUsage()
        # Save in DF #
        self.prob_names = ['Prob_global_DY','Prob_global_HToZA','Prob_global_TT']
        probs = pd.DataFrame(probs)
        probs.columns = self.prob_names
        self.data = pd.concat([self.data,probs],axis=1)
        print ('...... Concatenation done')
        self._memoryUsage()
        del probs

    def _produceParamProbabilities(self):
        print ('Producing parameteric probabilities for %s sample'%self.label)
        self._memoryUsage()
        # Initialize DNN model #
        model_class = HyperModel(self.model_name,'class_param')
        df_list = []
        # Iterate over mass points to use as parameters #
        for i in range(self.new_masses.shape[0]):
            mH = self.new_masses[i,0]
            mA = self.new_masses[i,1]
            print ('Processing mass point : mH = %0.2f, mA = %0.2f (%d/%d)'%(mH,mA,i,self.new_masses.shape[0]))
            masses_repeated = np.tile(self.new_masses[i,:],(self.data.shape[0],1))
            weight_names = ['weight_DY','weight_TT','weight_new_mH_%0.2f_mA_%0.2f'%(mH,mA)]
            weight_values = self.data[weight_names].values
            inputs = np.c_[weight_values,masses_repeated]
            start_time = time.time()
            probs = model_class.HyperRestore(inputs,batch_size=512,verbose=1)
            print("--- %0.5f seconds ---" % ((time.time() - start_time)*1000))
            probs_names = ['Prob_param_%s_mH_%0.2f_mA_%0.2f'%(t,mH,mA) for t in ['DY','HToZA','TT']]
            probs = pd.DataFrame(probs,columns=probs_names)
            df_list.append(probs)
            self._memoryUsage()
        print ('...... Classification probabilities done')
        for df in df_list:
            self.data = pd.concat((self.data,df),axis=1)
        print ('...... Concatenation done')
        self._memoryUsage()

        del df_list
        del probs
        del inputs

    def _removeUselessBranches(self):
        for li in self.list_inputs+self.weight_names:
            del self.data[li]

    def _saveAsROOT(self):
        output = self.data.to_records(index=False,column_dtypes='float64')
        output.dtype.names = [(name.replace('.','p').replace('(','').replace(')','').replace('-','_minus_').replace('*','_times_')) for name in output.dtype.names] # root_numpy issues
        array2root(output,self.save_path,mode='recreate') 
        print('Output saved as : '+self.save_path)

    def _recoverFromROOT(self):
        branches = ['ll_M',
                    'jj_M',
                    'lljj_M',
                    'total_weight',
                    'Prob_global_HToZA',
                    ('Prob_param_HToZA_mH_%0.2f_mA_%0.2f'%(self.mH,self.mA)).replace('.','p')]
 
        #list_variables = ListBranches(self.save_path)
        #self.data = Tree2Pandas(input_file=self.save_path,variables=list_variables)
        self.data = Tree2Pandas(input_file=self.save_path,variables=branches)
        self.size = self.data.shape[0]
        print ('Output recovered from : '+self.save_path)
        print ('\tSample size : %d'%self.size)
        self._memoryUsage()

       
#################################################################################################
# ProcessEllipse #
#################################################################################################
class ProcessEllipse:
    def __init__(self,inst_DY,inst_TT,inst_HToZA,path_json,mA,mH,sigmas,save_path,force=False):
        self.inst_DY = inst_DY          # Process DNN instance for DY sample
        self.inst_TT = inst_TT          # Process DNN instance for TT sample 
        self.inst_HToZA = inst_HToZA    # Process DNN instance for HToZA sample 
        self.list_inst = [self.inst_DY,self.inst_TT,self.inst_HToZA] # List of instances
        self.path_json = path_json                      # Path to get the ellipse config
        self.window = massWindow(self.path_json)        # 
        self.mA = mA
        self.mH = mH
        self.save_path = save_path      # Wether to look for a save
        self.force = force              # Wether to force the processing and erase the save

        self.p = psutil.Process(os.getpid())
        print ('[MEMORY] current pid : ',os.getpid())

        print ('Beginning the ellipse computation')
        # Check if save exists #
        if force: print ('Careful, will replace the save')
        save_exists = False if force else os.path.exists(self.save_path) 
    
        self.sigmas = sigmas
        self.sigmas_columns = [('sigma_%0.1f'%s).replace('.','p') for s in self.sigmas]

        if save_exists:
            self._recoverFromROOT()
        else:
            self._getCenter()
            self._insideEllipses()
            self._makeTargets()
            self._concatenate()
            self._saveAsROOT()

    def _memoryUsage(self):
        print ('[MEMORY] Current memory usage : %0.3f GB'%(self.p.memory_info().rss/(1024**3)))

    def _getCenter(self):
        with open(self.path_json) as json_file:
            data_json = json.load(json_file)
        center = ()
        for (mbb, mllbb, a, b, theta, mA, mH) in data_json:
            if mA == self.mA and mH == self.mH:
                self.center = (mbb,mllbb)
        if len(self.center)==0:
            sys.exit('Could not find mA = %0.2f and mH = %0.2f in config file'%(self.mA,self.mH))


    def _insideEllipses(self):
        self._memoryUsage()
        for inst in self.list_inst:
            print ('Computing ellipses for %s sample'%inst.label)
            manager = enlighten.get_manager()
            pbar = manager.counter(total=len(self.sigmas)*inst.size, desc='Progress', unit='Events %s'%inst.label)
            list_inside = []
            for idx,sigma in enumerate(self.sigmas):
                print ('....... Counting ellipse with sigma = %0.1f'%sigma)
                inside = np.zeros(inst.size)
                for i in range(inst.size):
                    masspoint = inst.data.iloc[i,:][['jj_M','lljj_M']]
                    check = self.window.isInWindow(self.center,sigma,masspoint)
                    if check : inside[i] = 1
                    pbar.update()
                inside = pd.DataFrame(inside) 
                inside.columns = [self.sigmas_columns[idx]]
                list_inside.append(inside)
                self._memoryUsage()
            print ('....... Concatenating the results into a single DF')
            manager.stop()
            for inside in list_inside:
                inst.data = pd.concat([inst.data,inside],axis=1)
            self._memoryUsage()

    def _makeTargets(self):
        self.inst_DY.data = pd.concat([self.inst_DY.data,pd.DataFrame(np.zeros(self.inst_DY.size),columns=['target'])],axis=1) 
        self.inst_TT.data = pd.concat([self.inst_TT.data,pd.DataFrame(np.zeros(self.inst_TT.size),columns=['target'])],axis=1) 
        self.inst_HToZA.data = pd.concat([self.inst_HToZA.data,pd.DataFrame(np.ones(self.inst_HToZA.size),columns=['target'])],axis=1) 

    def _concatenate(self):
        df = []
        print ('Concatenating the different samples')
        for inst in self.list_inst:
            df.append(inst.data)
        df = pd.concat(df,axis=0)
        self.data = df
        print ('...... Concatenation done')
        self._memoryUsage()
        del df
        del self.list_inst
       
    def _saveAsROOT(self):
        output = self.data.to_records(index=False,column_dtypes='float64')
        output.dtype.names = [(name.replace('.','p').replace('(','').replace(')','').replace('-','_minus_').replace('*','_times_')) for name in output.dtype.names] # root_numpy issues
        array2root(output,self.save_path,mode='recreate') 
        print('Output saved as : '+self.save_path)
    def _recoverFromROOT(self):
        list_variables = ListBranches(self.save_path)
        self.data = Tree2Pandas(input_file=self.save_path,variables=list_variables)
        print ('Output recovered from : '+self.save_path)
        print ('\tSample size : %d'%self.data.shape[0])
        

#################################################################################################
# ProcessROC#
#################################################################################################
class ProcessROC:
    def __init__(self,inst_ellipse,mH,mA):
        self.inst_ellipse = inst_ellipse
        self.mH = mH
        self.mA = mA
        self.path_ROC = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/Ellipses/ROC/'

        if self.inst_ellipse.data.shape[0] == 0:
            sys.exit('Empty tree')

        self._getFPRAndTPR()
        self._makeROC()

    def _getFPRAndTPR(self):
        prob_param = ('Prob_param_HToZA_mH_%0.2f_mA_%0.2f'%(self.mH,self.mA)).replace('.','p')

        self.scores = {}
        # Loop over the ellipses #
        print ('Process the ellipse with the DNN')
        for i in range(len(self.inst_ellipse.sigmas)):
            print ('....... Processing ellipse with sigma = %0.1f'%self.inst_ellipse.sigmas[i])
            # Select the columns #
            selection = [prob_param,'target','Prob_global_HToZA','total_weight',('sigma_%0.1f'%self.inst_ellipse.sigmas[i]).replace('.','p')]
            #Select subDF #
            df = copy.deepcopy(self.inst_ellipse.data[selection])

            # Get ellipses FPR and TPR #
            idx_ell_in = df[self.inst_ellipse.sigmas_columns[i]]==1
            idx_ell_out = np.invert(idx_ell_in)
            tp_ell = np.sum(np.logical_and(idx_ell_in,df['target']==1)*1)
            tn_ell = np.sum(np.logical_and(idx_ell_out,df['target']==0)*1)
            fp_ell = np.sum(np.logical_and(idx_ell_in,df['target']==0)*1)
            fn_ell = np.sum(np.logical_and(idx_ell_out,df['target']==1)*1)
            tpr_ell = tp_ell/(tp_ell+fn_ell)
            fpr_ell = fp_ell/(fp_ell+tn_ell)

            # loop over DNN cuts #
            cuts = np.linspace(0,1,10000)
            tpr_global = []
            fpr_global = []
            tpr_param = []
            fpr_param = []
            for c in range(cuts.shape[0]):
                # What is in or out #
                idx_in_global = np.logical_and(df['Prob_global_HToZA']>cuts[c],idx_ell_in)
                idx_out_global = np.invert(idx_in_global) 
                idx_in_param = np.logical_and(df[prob_param]>cuts[c],idx_ell_in)
                idx_out_param = np.invert(idx_in_param) 
                
                # Get the FPR and TPr #
                tp_global = np.sum(np.logical_and(idx_in_global,df['target']==1)*1)
                tn_global = np.sum(np.logical_and(idx_out_global,df['target']==0)*1)
                fp_global = np.sum(np.logical_and(idx_in_global,df['target']==0)*1)
                fn_global = np.sum(np.logical_and(idx_out_global,df['target']==1)*1)
                tp_param = np.sum(np.logical_and(idx_in_param,df['target']==1)*1)
                tn_param = np.sum(np.logical_and(idx_out_param,df['target']==0)*1)
                fp_param = np.sum(np.logical_and(idx_in_param,df['target']==0)*1)
                fn_param = np.sum(np.logical_and(idx_out_param,df['target']==1)*1)
                tpr_global.append(tp_global/(tp_global+fn_global))
                fpr_global.append(fp_global/(fp_global+tn_global))
                tpr_param.append(tp_param/(tp_param+fn_param))
                fpr_param.append(fp_param/(fp_param+tn_param))

            self.scores[(self.inst_ellipse.sigmas[i],tpr_ell,fpr_ell)] = np.c_[tpr_global,fpr_global,tpr_param,fpr_param]
            del df

        # Get the fpr and tpr for the DNN alone #
        self.fpr_DNN_global, self.tpr_DNN_global, thresholds = metrics.roc_curve(self.inst_ellipse.data['target'], self.inst_ellipse.data['Prob_global_HToZA'])
        self.fpr_DNN_param, self.tpr_DNN_param, thresholds = metrics.roc_curve(self.inst_ellipse.data['target'], self.inst_ellipse.data[prob_param])


    def _makeROC(self):
        # Make figure #
        fig = plt.figure(figsize=(16,9))
        ax = fig.add_subplot(111)
        plt.subplots_adjust(left=0.06, bottom=0.1, right=0.95, top=0.9)
        color= iter(cm.rainbow(np.linspace(0,1,len(self.scores))))
        print ('Starting the ROC section')
        # Get the roc curve for ellipses #
        list_tpr_ell = [e[1] for e in self.scores.keys()]
        list_fpr_ell = [e[2] for e in self.scores.keys()]
        # Loop over ellipses #
        legend_ell = []
        legend_DNN_global = []
        legend_DNN_param = []
        for key,val in self.scores.items():
            # Unpack 
            sigma, tpr_ell, fpr_ell = key
            tpr_global = val[:,0]
            fpr_global = val[:,1]
            tpr_param = val[:,2]
            fpr_param = val[:,3]
            print ('....... Processing sigma %0.1f'%sigma)
            # plot #
            c = next(color)
            ax.scatter(tpr_ell,fpr_ell,marker='X',s=100,color=c,label=r'Ellipse : %0.1f $\rho$'%sigma)
            ax.plot(tpr_global,fpr_global,color=c,linestyle='-',label=r'Global + ellipse (%0.1f $\rho$)'%sigma)
            ax.plot(tpr_param,fpr_param,color=c,linestyle='--',label=r'Parametric + ellipse (%0.1f $\rho)$'%sigma)
        ax.plot(list_tpr_ell,list_fpr_ell,color='k',linestyle=':',label='ROC ellipses')
        ax.plot(self.tpr_DNN_global,self.fpr_DNN_global,color='k',linestyle='-',label='ROC global DNN')
        ax.plot(self.tpr_DNN_param,self.fpr_DNN_param,color='k',linestyle='--',label='ROC parametric DNN')

        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width*0.55, box.height])
        handles, labels = ax.get_legend_handles_labels()
        labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
        handles = list(handles)
        labels = list(labels)
        ell_handles =     [handles[-3]] + handles[:len(self.scores)]
        global_handles =  [handles[-2]] + handles[len(self.scores):2*len(self.scores)]
        param_handles =   [handles[-1]] + handles[2*len(self.scores):3*len(self.scores)]
        ell_labels =      [labels[-3]] + labels[:len(self.scores)]
        global_labels =   [labels[-2]] + labels[len(self.scores):2*len(self.scores)]
        param_labels =    [labels[-1]] + labels[2*len(self.scores):3*len(self.scores)]
        handles = ell_handles+global_handles+param_handles
        labels = ell_labels+global_labels+param_labels
        legend = ax.legend(handles, labels,loc='upper left',bbox_to_anchor=(1.02, 1,0.70,0),fancybox=False,labelspacing=2.5,shadow=True,ncol=3,prop={'size': 11},frameon=False)

        #ax.set_yscale('symlog', linthreshy=0.001)
        ax.set_yscale('log')
        ax.set_xlim([0, 1])
        ax.set_ylim([0.0001, 1])
        ax.set_xlabel('Signal selection efficiency')
        ax.set_ylabel('Background selection efficiency')
        plt.suptitle('ROC curve : $M_{H}$ = %0.2f GeV and $M_{A}$ = %0.2f GeV'%(self.inst_ellipse.mH,self.inst_ellipse.mA))
        plt.grid(b=True,which='both',axis='both')
        roc_name = os.path.join(self.path_ROC,('ROC_mH_%0.2f_mA_%0.2f'%(self.inst_ellipse.mH,self.inst_ellipse.mA)).replace('.','p')+'.png')
        fig.savefig(roc_name)
        print ('ROC curve saved as %s'%roc_name)
     
