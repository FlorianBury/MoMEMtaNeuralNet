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

from Classes import *

gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = 2000#[ROOT.kPrint, ROOT.kInfo]#, kWarning, kError, kBreak, kSysError, kFatal;

def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='From given set of root files, make different histograms in a root file')
    parser.add_argument('-m','--model', action='store', required=True, type=str, default='',
                  help='NN model to be used')
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
    # Get files #
    #############################################################################################
    INPUT_DIR = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/'
    INPUT_VALID = os.path.join(INPUT_DIR,'Classifier',opt.model)

    OUTPUT_PDF = os.path.join(os.getcwd(),'PDF',opt.model)
    OUTPUT_YAML= os.path.join(os.getcwd(),'YAML')
    if not os.path.exists(OUTPUT_PDF):
        os.makedirs(OUTPUT_PDF)
    if not os.path.exists(OUTPUT_YAML):
        os.makedirs(OUTPUT_YAML)

    # List that will gather the root ZA_plotter_allhistos #
    list_histo_valid = []
    list_histo_invalid = []


    ######################################## VALID ##############################################
    logging.info('Starting Plotting')
    f_valid =  glob.glob(INPUT_VALID+'/*.root')

    if len(f_valid) == 0:
        logging.error('Could not find the weights at %s'%(INPUT_VALID))

    # ROC curve instantiation #
    # Careful ! Classes as alphabetic order
    instance_ROC_MEM = Plot_Multi_ROC(['DY','HToZA','TT'],'total_weight','MEM')
    instance_ROC_DNN = Plot_Multi_ROC(['DY','HToZA','TT'],'total_weight','DNN')

    # Loop over files #
    for f in f_valid:
        filename = f.replace(INPUT_VALID+'/','').replace('.root','')
        logging.info('Processing from %s'%(filename))
        
        # Particularize TH1 YAML file #
        with open('TH1.yml.tpl') as tpl_handle:
            tpl = tpl_handle.read()
            tpl = tpl.format(file=f, name=filename, cut="''",category='')
            with open(OUTPUT_YAML+'/TH1_'+filename+'.yml', 'w') as out_yml:
                out_yml.write(tpl)

         # Particularize TH1 Ratio YAML file #
        with open('TH1Ratio.yml.tpl') as tpl_handle:
            tpl = tpl_handle.read()
            tpl = tpl.format(file=f, name=filename, cut="''",category='')
            with open(OUTPUT_YAML+'/TH1Ratio_'+filename+'.yml', 'w') as out_yml:
                out_yml.write(tpl)

        # Particularize TH2 YAML file #
        with open('TH2.yml.tpl') as tpl_handle:
            tpl = tpl_handle.read()
            tpl = tpl.format(file=f, name=filename, cut="''",category='')
            with open(OUTPUT_YAML+'/TH2_'+filename+'.yml', 'w') as out_yml:
                out_yml.write(tpl)
        
        # Parse and load YAML file #
        with open(OUTPUT_YAML+'/TH1_'+filename+'.yml', 'r') as stream:
            config_TH1 = yaml.load(stream) # Dict of dicts 
        with open(OUTPUT_YAML+'/TH1Ratio_'+filename+'.yml', 'r') as stream:
            config_TH1_ratio = yaml.load(stream) # Dict of dicts 
        with open(OUTPUT_YAML+'/TH2_'+filename+'.yml', 'r') as stream:
            config_TH2 = yaml.load(stream) # Dict of dicts 

        # Create list of histo # 
        for name,dict_histo in config_TH1.items():
            try:
                logging.info('\tPlot %s'%(name))
                instance = Plot_TH1(**dict_histo)
                instance.MakeHisto()
                list_histo_valid.append(instance)
            except Exception as e:
                logging.warning('Could not plot %s due to "%s"'%(name,e))

        for name,dict_histo in config_TH1_ratio.items():
            try:
                logging.info('\tPlot %s'%(name))
                instance = Plot_Ratio_TH1(**dict_histo)
                instance.MakeHisto()
                list_histo_valid.append(instance)
            except Exception as e:
                logging.warning('Could not plot %s due to "%s"'%(name,e))

        for name,dict_histo in config_TH2.items():
            try:
                logging.info('\tPlot %s'%(name))
                instance = Plot_TH2(**dict_histo)
                instance.MakeHisto()
                list_histo_valid.append(instance)
            except Exception as e:
                logging.warning('Could not plot %s due to "%s"'%(name,e))

        # Add to ROC #
        list_ROC_MEM = ['prob_MEM_DY','prob_MEM_HToZA','prob_MEM_TT']
        list_ROC_DNN = ['prob_DNN_DY','prob_DNN_HToZA','prob_DNN_TT']
        # Must follow the alphabetic order 
        if os.path.basename(f).startswith('HToZA'):
            logging.info('\tAdded to ROC as HToZA')
            try:
                instance_ROC_MEM.AddToROC(f,'tree',list_ROC_MEM,'HToZA')
                instance_ROC_DNN.AddToROC(f,'tree',list_ROC_DNN,'HToZA')
            except Exception as e:
                logging.warning('Could not plot ROC due to "%s"'%(e))
        if os.path.basename(f).startswith('DY'):
            logging.info('\tAdded to ROC as DY')
            try:
                instance_ROC_MEM.AddToROC(f,'tree',list_ROC_MEM,'DY')
                instance_ROC_DNN.AddToROC(f,'tree',list_ROC_DNN,'DY')
            except Exception as e:
                logging.warning('Could not plot ROC due to "%s"'%(e))

        if os.path.basename(f).startswith('TT'):
            logging.info('\tAdded to ROC as TT')
            try:
                instance_ROC_MEM.AddToROC(f,'tree',list_ROC_MEM,'TT')
                instance_ROC_DNN.AddToROC(f,'tree',list_ROC_DNN,'TT')
            except Exception as e:
                logging.warning('Could not plot ROC due to "%s"'%(e))

    # Make ROC curves #
    #try:
    logging.info('Processing ROC curve for MEM') 
    instance_ROC_MEM.ProcessROC()
    logging.info('Processing ROC curve for DNN') 
    instance_ROC_DNN.ProcessROC()
    MakeMultiROCPlot([instance_ROC_MEM],os.path.join(OUTPUT_PDF,'MULTI_ROC_MEM'))
    MakeMultiROCPlot([instance_ROC_DNN],os.path.join(OUTPUT_PDF,'MULTI_ROC_DNN'))
    MakeMultiROCPlot([instance_ROC_MEM,instance_ROC_DNN],os.path.join(OUTPUT_PDF,'MULTI_ROC_MEM_vs_DNN'))
    #except Exception as e:
    #    logging.warning('Could not process ROC due to "%s"'%e)    



    #############################################################################################
    # Save histograms #
    #############################################################################################
    LoopPlotOnCanvas(os.path.join(OUTPUT_PDF,opt.model),list_histo_valid)
    logging.info("All Canvas have been printed")

        
        
        



if __name__ == "__main__":
    main()   
