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

from Classes import Plot_TH1, Plot_TH2, Plot_Ratio_TH1, Plot_ROC, LoopPlotOnCanvas, MakeROCPlot

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
    INPUT_VALID = os.path.join(INPUT_DIR,'NNOutput',opt.model,'valid_weights')
    INPUT_INVALID = os.path.join(INPUT_DIR,'NNOutput',opt.model,'invalid_{}_weights')

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
    logging.info('Starting Plotting the valid weights')
    f_valid =  glob.glob(INPUT_VALID+'/*.root')

    if len(f_valid) == 0:
        logging.error('Could not find the valid weights at %s'%(INPUT_VALID))

    # Start ROC curve #
    instance_ROC_MEM = Plot_ROC('weight_TT','weight_DY','total_weight','MEM')
    instance_ROC_DNN = Plot_ROC('output_TT','output_DY','total_weight','DNN')
    # Loop over files #
    for f in f_valid:
        filename = f.replace(INPUT_VALID+'/','').replace('.root','')
        logging.info('Processing valid weights from %s'%(filename))
        
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

        # If DY or TT, add to ROC #
        if os.path.basename(f).startswith('DY'):
            try:
                instance_ROC_MEM.AddToROC(f,'tree','DY')
                instance_ROC_DNN.AddToROC(f,'tree','DY')
            except Exception as e:
                logging.warning('Could not plot ROC due to "%s"'%(e))
        elif os.path.basename(f).startswith('TT'):
            try:
                instance_ROC_MEM.AddToROC(f,'tree','TT')
                instance_ROC_DNN.AddToROC(f,'tree','TT')
            except Exception as e:
                logging.warning('Could not plot ROC due to "%s"'%(e))

         
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

    try:
        instance_ROC_MEM.ProcessROC()
        instance_ROC_DNN.ProcessROC()
        MakeROCPlot([instance_ROC_MEM],os.path.join(OUTPUT_PDF,'ROC_MEM'))
        MakeROCPlot([instance_ROC_DNN],os.path.join(OUTPUT_PDF,'ROC_DNN'))
        MakeROCPlot([instance_ROC_MEM,instance_ROC_DNN],os.path.join(OUTPUT_PDF,'ROC_MEM_vs_DNN'))
    except:
        logging.warning('Could not process ROC')
    
    ####################################### INVALID #############################################
    invalid_cat = ['DY','TT']


    # Loop over invalid categories #
    for cat in invalid_cat:
        f_inv = glob.glob(INPUT_INVALID.format(cat)+'/*.root')
        temp_list = []
        if len(f_inv) == 0:
            logging.error('Could not find the invalid weights at %s'%(INPUT_VALID.format(cat)))
        # Start ROC curve #
        instance_ROC_MEM = Plot_ROC('weight_TT','weight_DY','total_weight','Invalid {} MEM'.format(cat),"weight_{0}>weight_{0}_err".format(cat))
        instance_ROC_DNN = Plot_ROC('output_TT','output_DY','total_weight','Invalid {} DNN'.format(cat),"weight_{0}>weight_{0}_err".format(cat))

        # Loop over files over one category #
        for f in f_inv:
            filename = f.replace(INPUT_INVALID.format(cat)+'/','').replace('_invalid_{}.root'.format(cat),'')
            logging.info('Processing invalid %s weights from %s'%(cat,filename))

            # If DY or TT, add to ROC #
            if os.path.basename(f).startswith('DY'):
                try:
                    instance_ROC_MEM.AddToROC(f,'tree','DY')
                    instance_ROC_DNN.AddToROC(f,'tree','DY')
                except:
                    logging.warning('Could not add DY to ROC')
            elif os.path.basename(f).startswith('TT'):
                try:
                    instance_ROC_MEM.AddToROC(f,'tree','TT')
                    instance_ROC_DNN.AddToROC(f,'tree','TT')
                except:
                    logging.warning('Could not add TT to ROC')


             # Particularize TH1 Ratio YAML file #
            with open('TH1Ratio.yml.tpl') as tpl_handle:
                tpl = tpl_handle.read()
                tpl = tpl.format(file=f, name=filename, cut="'weight_{0}>weight_{0}_err'".format(cat),category='Invalid {}'.format(cat))
                with open(OUTPUT_YAML+'/TH1Ratio_INV_{}_'.format(cat)+filename+'.yml', 'w') as out_yml:
                    out_yml.write(tpl)

            with open('TH2.yml.tpl') as tpl_handle:
                tpl = tpl_handle.read()
                tpl = tpl.format(file=f, name=filename, cut="'weight_{0}>weight_{0}_err'".format(cat),category='Invalid {}'.format(cat))
                with open(OUTPUT_YAML+'/TH2_INV_{}_'.format(cat)+filename+'.yml', 'w') as out_yml:
                    out_yml.write(tpl)

            # Parse and load YAML file #
            with open(OUTPUT_YAML+'/TH1Ratio_INV_{}_'.format(cat)+filename+'.yml', 'r') as stream:
                config_TH1_ratio = yaml.load(stream) # Dict of dicts 
            with open(OUTPUT_YAML+'/TH2_INV_{}_'.format(cat)+filename+'.yml', 'r') as stream:
                config_TH2 = yaml.load(stream) # Dict of dicts 
             
            # Create list of histo # 
            for name,dict_histo in config_TH1_ratio.items():
                try:
                    logging.info('\tPlot %s'%(name))
                    instance = Plot_Ratio_TH1(**dict_histo)
                    instance.MakeHisto()
                    temp_list.append(instance)
                except Exception as e:
                    logging.warning('Could not plot %s due to "%s"'%(name,e))
            for name,dict_histo in config_TH2.items():
                try:
                    logging.info('\tPlot %s'%(name))
                    instance = Plot_TH2(**dict_histo)
                    instance.MakeHisto()
                    temp_list.append(instance)
                except Exception as e:
                    logging.warning('Could not plot %s due to "%s"'%(name,e))

        # Make and save ROC #
        try:
            instance_ROC_MEM.ProcessROC()
            instance_ROC_DNN.ProcessROC()
            MakeROCPlot([instance_ROC_MEM],os.path.join(OUTPUT_PDF,'Invalid_{}_ROC_MEM'.format(cat)))
            MakeROCPlot([instance_ROC_DNN],os.path.join(OUTPUT_PDF,'Invalid_{}_ROC_DNN'.format(cat)))
            MakeROCPlot([instance_ROC_MEM,instance_ROC_DNN],os.path.join(OUTPUT_PDF,'Invalid_{}_ROC_MEM_vs_DNN'.format(cat)))
        except:
            logging.warning('Could not process ROC')
    
        # Append in list #
        list_histo_invalid.append(temp_list)

    #############################################################################################
    # Save histograms #
    #############################################################################################
    LoopPlotOnCanvas(os.path.join(OUTPUT_PDF,opt.model+'_valid'),list_histo_valid)
    for i,cat in enumerate(invalid_cat):
        LoopPlotOnCanvas(os.path.join(OUTPUT_PDF,opt.model+'_invalid_{}'.format(cat)),list_histo_invalid[i])
    logging.info("All Canvas have been printed")

        
        
        



if __name__ == "__main__":
    main()   
