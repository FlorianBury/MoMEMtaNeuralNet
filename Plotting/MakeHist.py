import os
import sys
import argparse
import glob
import logging
import copy
import yaml

import ROOT
from ROOT import TFile, TH1F, TH2F, TCanvas, gROOT
import CMS_lumi
import tdrstyle

import Classes
from Classes import Plot_TH1, Plot_TH2, Plot_Ratio_TH1, Plot_Multi_TH1, Plot_ROC, LoopPlotOnCanvas, MakeROCPlot, ProcessYAML, Plot_Multi_ROC, MakeMultiROCPlot

gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = 2000#[ROOT.kPrint, ROOT.kInfo]#, kWarning, kError, kBreak, kSysError, kFatal;

def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='From given set of root files, make different histograms in a root file')
    parser.add_argument('-m','--model', action='store', required=True, type=str, default='',
                  help='NN model to be used')
    parser.add_argument('--ROC',action='store_true',default=False,
                  help='Whether to compute the ROCs')
    parser.add_argument('-v','--verbose', action='store_true', required=False, default=False,
            help='Show DEGUG logging')
    opt = parser.parse_args() 

    # Logging #
    if opt.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s') 
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    #############################################################################################
    # Select samples #
    #############################################################################################
    INPUT_DIR = os.path.join('/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput',opt.model)
    logging.info('Taking inputs from %s'%INPUT_DIR)
    
    # For each directory, puth the path in dictn the value is the list of histograms #
    class Plots():
        def __init__(self,name,override_params):
            self.name = name                            # Name of the subdir
            self.path = os.path.join(INPUT_DIR,name)    # Full path to files
            self.override_params = override_params      # Parameters to override in the configs
            self.list_histo = []                        # List of histograms to be filled

    list_plots = [
                    #Plots(name = 'valid_weights_DY_TT',
                    #      override_params = {}),
                    #Plots(name = 'valid_weights_HToZA',
                    #      override_params = {}),
                    #Plots(name = 'valid_weights_class',
                    #      override_params = {}),
                    Plots(name = 'valid_weights_binary',
                          override_params = {}),
                    #Plots(name = 'invalid_DY_weights',
                    #      override_params = {}),
                    #Plots(name = 'invalid_TT_weights',
                    #      override_params = {}),
                    #Plots(name = 'JEC_weights',
                    #      override_params = {}),
                    #Plots(name = 'interpolation_weights',
                    #      override_params = {}),
                    #Plots(name = 'classification_weights',
                    #        override_params = {}),
                    #Plots(name = 'delaunay',
                    #      override_params = {}),
                 ]

    # Select template #
    class Template:
        def __init__(self,tpl,class_name):
            self.tpl = tpl                          # Template ".yml.tpl" to be used
            self.class_name = class_name            # Name of one of the class below to use

    templates = [
                    ############       TH1       ##############
                    #Template(tpl = 'TH1_background.yml.tpl',
                    #         class_name = 'Plot_TH1'),
                    #Template(tpl = 'TH1_signal.yml.tpl',
                    #         class_name = 'Plot_TH1'),
                    #Template(tpl = 'TH1_interpolation.yml.tpl',
                    #          class_name = 'Plot_TH1'),
                    #Template(tpl = 'TH1_class.yml.tpl',
                    #         class_name = 'Plot_TH1'),
                    Template(tpl = 'TH1_binary.yml.tpl',
                             class_name = 'Plot_TH1'),

                    #########       TH1 Ratio       ###########
                    #Template(tpl = 'TH1Ratio_background.yml.tpl',
                    #         class_name = 'Plot_Ratio_TH1'),
                    #Template(tpl = 'TH1Ratio_signal.yml.tpl',
                    #         class_name = 'Plot_Ratio_TH1'),
                    #Template(tpl = 'TH1Ratio_interpolation.yml.tpl',
                    #         class_name = 'Plot_Ratio_TH1'),
                    #Template(tpl = 'TH1Ratio_class.yml.tpl',
                    #         class_name = 'Plot_Ratio_TH1'),
                    Template(tpl = 'TH1Ratio_binary.yml.tpl',
                             class_name = 'Plot_Ratio_TH1'),

                    #########       TH1 Multi       ###########
                    #Template(tpl = 'TH1Multi_signal.yml.tpl',
                    #         class_name = 'Plot_Multi_TH1'),
                    #Template(tpl = 'TH1Multi_class.yml.tpl',
                    #         class_name = 'Plot_Multi_TH1'),
                    Template(tpl = 'TH1Multi_binary.yml.tpl',
                             class_name = 'Plot_Multi_TH1'),
                    #Template(tpl = 'TH1Multi_interpolation.yml.tpl',
                    #         class_name = 'Plot_Multi_TH1'),

                    ############       TH2       ##############
                    #Template(tpl = 'TH2_background.yml.tpl',
                    #         class_name = 'Plot_TH2'),
                    #Template(tpl = 'TH2_signal.yml.tpl',
                    #         class_name = 'Plot_TH2'),
                    #Template(tpl = 'TH2_class.yml.tpl',
                    #         class_name = 'Plot_TH2'),
                ] 

    # Make the output dir #
    OUTPUT_PDF = os.path.join(os.getcwd(),'PDF',opt.model)
    if not os.path.exists(OUTPUT_PDF):
        os.makedirs(OUTPUT_PDF)

    #############################################################################################
    # Loop over the different paths #
    #############################################################################################
    # Loop over the files #
    for obj in list_plots:
        logging.info('Starting Plotting from %s subdir'%obj.name)
        files = glob.glob(obj.path+'/*.root')

        if len(files) == 0:
            logging.error('Could not find %s at %s'%(obj.name,obj.path))

        # Start ROC curve #
        instance_ROC_MEM = Plot_ROC(variable = ['weight_TT/(weight_TT+weight_DY)'],
                                    weight = 'total_weight',
                                    title = 'MEM')
        instance_ROC_MEM = Plot_ROC(variable = ['output_TT/(output_TT+output_DY)'],
                                    weight = 'total_weight',
                                    title = 'DNN')
        instance_binary_ROC_MEM = Plot_ROC(variable = ['Prob_MEM_signal'],
                                           weight = 'total_weight',
                                           title = 'MEM')
        instance_binary_ROC_DNN = Plot_ROC(variable = ['Prob_DNN_signal'],
                                           weight = 'total_weight',
                                           title = 'DNN')
        instance_ROC_Multi_MEM = Plot_Multi_ROC(
                            classes = ['DY','HToZA','TT'],
                            labels = ['P(Drell-Yann)',r'P(Signal H$\rightarrow ZA))$',r'P($t\bar{t}$)'],
                            colors = ['navy','green','darkred'],
                            weight = 'total_weight',
                            title = 'MEM')
        instance_ROC_Multi_DNN = Plot_Multi_ROC(        
                            classes = ['DY','HToZA','TT'],
                            labels = ['P(Drell-Yann)',r'P(Signal H$\rightarrow ZA))$',r'P($t\bar{t}$)'],
                            colors = ['dodgerblue','lawngreen','red'],
                            weight = 'total_weight',
                            title = 'DNN')

        list_ROC_MEM = ['Prob_MEM_DY','Prob_MEM_HToZA','Prob_MEM_TT']
        list_ROC_DNN = ['Prob_DNN_DY','Prob_DNN_HToZA','Prob_DNN_TT']

        # Loop over files #
        for f in files:
            fullname = f.replace(obj.path+'/','').replace('.root','')
            logging.info('Processing weights from %s'%(fullname+'.root'))
            if fullname.startswith('DY'):
                filename = 'Drell-Yann'
            elif fullname.startswith('TT'):
                filename = 't#bar{t}'
            elif fullname.startswith('HToZA'):
                filename = 'Signal'

            ##############  ROC section ################ 
            if opt.ROC:
                if os.path.basename(f).startswith('DY'):
                    logging.info('\tAdded to ROC as DY')
                    #try:
                    #    instance_ROC_MEM.AddToROC(f,'tree',0)
                    #    instance_ROC_DNN.AddToROC(f,'tree',0)
                    #except Exception as e:
                    #    logging.warning('Could not compute ROC due to "%s"'%(e))
                    try:
                        instance_binary_ROC_MEM.AddToROC(f,'tree',0)
                        instance_binary_ROC_DNN.AddToROC(f,'tree',0)
                    except Exception as e:
                        logging.warning('Could not compute binary ROC due to "%s"'%(e))
                    #try:
                    #    instance_ROC_Multi_MEM.AddToROC(f,'tree',list_ROC_MEM,'DY')
                    #    instance_ROC_Multi_DNN.AddToROC(f,'tree',list_ROC_DNN,'DY')
                    #except Exception as e:
                    #    logging.warning('Could not compute Multi ROC due to "%s"'%(e))
                elif os.path.basename(f).startswith('TT'):
                    logging.info('\tAdded to ROC as TT')
                    #try:
                    #    instance_ROC_MEM.AddToROC(f,'tree',1)
                    #    instance_ROC_DNN.AddToROC(f,'tree',1)
                    #except Exception as e:
                    #    logging.warning('Could not compute ROC due to "%s"'%(e))
                    try:
                        instance_binary_ROC_MEM.AddToROC(f,'tree',0)
                        instance_binary_ROC_DNN.AddToROC(f,'tree',0)
                    except Exception as e:
                        logging.warning('Could not compute binary ROC due to "%s"'%(e))
                    #try:
                    #    instance_ROC_Multi_MEM.AddToROC(f,'tree',list_ROC_MEM,'TT')
                    #    instance_ROC_Multi_DNN.AddToROC(f,'tree',list_ROC_DNN,'TT')
                    #except Exception as e:
                    #    logging.warning('Could not compute Multi ROC due to "%s"'%(e))
                elif os.path.basename(f).startswith('HToZA'):
                    logging.info('\tAdded to ROC as HToZA')
                    try:
                        instance_binary_ROC_MEM.AddToROC(f,'tree',1)
                        instance_binary_ROC_DNN.AddToROC(f,'tree',1)
                    except Exception as e:
                        logging.warning('Could not compute binary ROC due to "%s"'%(e))
                    #try:
                    #    instance_ROC_Multi_MEM.AddToROC(f,'tree',list_ROC_MEM,'HToZA')
                    #    instance_ROC_Multi_DNN.AddToROC(f,'tree',list_ROC_DNN,'HToZA')
                    #except Exception as e:
                    #    logging.warning('Could not compute Multi ROC due to "%s"'%(e))

            ##############  HIST section ################ 
            # Loop over the templates #
            for template in templates: 
                logging.debug('Template "%s" -> Class "%s"'%(template.tpl, template.class_name))
                list_config = [] # Will contain the dictionaries of parameters
                YAML = ProcessYAML(template.tpl) # Contain the ProcessYAML objects
                params = {**{'filename':f,'title':filename},**obj.override_params}
                # Get the list of configs #
                YAML.Particularize(fullname)
                YAML.Override(params)
                # loop over the configs #
                for name,config in YAML.config.items():
                    try:
                        class_ = getattr(Classes, template.class_name)
                        logging.info('\tPlot %s'%(name))
                        instance = class_(**config)
                        instance.MakeHisto()
                        obj.list_histo.append(instance)
                    except Exception as e:
                            logging.warning('Could not plot %s due to "%s"'%(name,e))
        if opt.ROC:
            #try:
            #    instance_ROC_MEM.ProcessROC()
            #    instance_ROC_DNN.ProcessROC()
            #    instance_binary_ROC_MEM.ProcessROC()
            #    instance_binary_ROC_DNN.ProcessROC()
            #    MakeROCPlot([instance_ROC_MEM],os.path.join(OUTPUT_PDF,obj.name+'_ROC_MEM'),'ROC MEM')
            #    MakeROCPlot([instance_ROC_DNN],os.path.join(OUTPUT_PDF,obj.name+'_ROC_DNN'),'ROC DNN')
            #    MakeROCPlot([instance_ROC_MEM,instance_ROC_DNN],os.path.join(OUTPUT_PDF,obj.name+'_ROC_MEM_vs_DNN'),'ROC MEM vs DNN')
            #except Exception as e:
            #    logging.warning('Could not process ROC due to "%s"'%e)
            try:
                instance_binary_ROC_MEM.ProcessROC()
                instance_binary_ROC_DNN.ProcessROC()
                MakeROCPlot([instance_binary_ROC_MEM],os.path.join(OUTPUT_PDF,obj.name+'_binary_ROC_MEM'),'ROC MEM')
                MakeROCPlot([instance_binary_ROC_DNN],os.path.join(OUTPUT_PDF,obj.name+'_binary_ROC_DNN'),'ROC DNN')
                MakeROCPlot([instance_binary_ROC_MEM,instance_binary_ROC_DNN],os.path.join(OUTPUT_PDF,obj.name+'_binary_ROC_MEM_vs_DNN'),'ROC MEM vs DNN')
            except Exception as e:
                logging.warning('Could not process binary ROC due to "%s"'%e)

            #try:
            #    instance_ROC_Multi_MEM.ProcessROC()
            #    instance_ROC_Multi_DNN.ProcessROC()
            #    MakeMultiROCPlot([instance_ROC_Multi_MEM],os.path.join(OUTPUT_PDF,obj.name+'_MULTI_ROC_MEM'),'Classification ROC MEM')
            #    MakeMultiROCPlot([instance_ROC_Multi_DNN],os.path.join(OUTPUT_PDF,obj.name+'_MULTI_ROC_DNN'),'Classification ROC DNN')
            #    MakeMultiROCPlot([instance_ROC_Multi_MEM,instance_ROC_Multi_DNN],os.path.join(OUTPUT_PDF,obj.name+'_MULTI_ROC_MEM_vs_DNN'),'Classification ROC MEM vs DNN')
            #except Exception as e:
            #    logging.warning('Could not process Multi ROC due to "%s"'%e)

    #############################################################################################
    # Save histograms #
    #############################################################################################
    for obj in list_plots:
        PDF_name = os.path.join(OUTPUT_PDF,obj.name) 
        LoopPlotOnCanvas(PDF_name,obj.list_histo)
    logging.info("All Canvas have been printed")

        
        
        



if __name__ == "__main__":
    main()   
