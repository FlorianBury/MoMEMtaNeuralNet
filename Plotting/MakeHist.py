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

from Classes import Plot_TH1, Plot_TH2, Plot_Ratio_TH1#, PlotOnCanvas

gROOT.SetBatch(True)

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
    INPUT_INVALID_DY = os.path.join(INPUT_DIR,'NNOutput',opt.model,'invalid_DY_weights')
    INPUT_INVALID_TT = os.path.join(INPUT_DIR,'NNOutput',opt.model,'invalid_TT_weights')

    # List that will gather the root ZA_plotter_allhistos #
    list_histo = []

    #############################################################################################
    # Valid weights output #
    #############################################################################################
    logging.info('Starting Plotting the valid weights')
    f_valid =  glob.glob(INPUT_VALID+'/*.root')

    if len(f_valid) == 0:
        logging.error('Could not find the valid weights at %s'%(INPUT_VALID))
        sys.exit(1)

    # Loop over files #
    for f in f_valid:
        filename = f.replace(INPUT_VALID+'/','').replace('.root','')
        logging.info('Processing %s'%(filename))
        
        # Particularize TH1 YAML file #
        with open('TH1.yml.tpl') as tpl_handle:
            tpl = tpl_handle.read()
            tpl = tpl.format(file=f, name=filename)
            with open('TH1_'+filename+'.yml', 'w') as out_yml:
                out_yml.write(tpl)

         # Particularize TH1 YAML file #
        with open('TH1Ratio.yml.tpl') as tpl_handle:
            tpl = tpl_handle.read()
            tpl = tpl.format(file=f, name=filename)
            with open('TH1Ratio_'+filename+'.yml', 'w') as out_yml:
                out_yml.write(tpl)

        # Particularize TH2 YAML file #
        with open('TH2.yml.tpl') as tpl_handle:
            tpl = tpl_handle.read()
            tpl = tpl.format(file=f, name=filename)
            with open('TH2_'+filename+'.yml', 'w') as out_yml:
                out_yml.write(tpl)
        
        # Parse and load YAML file #
        with open('TH1_'+filename+'.yml', 'r') as stream:
            config_TH1 = yaml.load(stream) # Dict of dicts 
        with open('TH1Ratio_'+filename+'.yml', 'r') as stream:
            config_TH1_ratio = yaml.load(stream) # Dict of dicts 
        with open('TH2_'+filename+'.yml', 'r') as stream:
            config_TH2 = yaml.load(stream) # Dict of dicts 
         
        
        for name,dict_histo in config_TH1.items():
            logging.info('\tPlot %s'%(name))
            instance = Plot_TH1(**dict_histo)
            instance.ReturnHisto()
            list_histo.append(instance)

        for name,dict_histo in config_TH1_ratio.items():
            logging.info('\tPlot %s'%(name))
            instance = Plot_Ratio_TH1(**dict_histo)
            instance.ReturnHisto()
            list_histo.append(instance)

        for name,dict_histo in config_TH2.items():
            logging.info('\tPlot %s'%(name))
            instance = Plot_TH2(**dict_histo)
            instance.ReturnHisto()
            list_histo.append(instance)
    #############################################################################################
    # Save histograms #
    #############################################################################################
    # Save to root file #
    f_root = TFile(opt.model+".root", "recreate")
    for idx,inst in enumerate(list_histo,1):
            # inst is a class object -> inst.histo = TH1/TH2
            if idx==1:
                c2 = TCanvas()
                c2.Print(opt.model+'.pdf[')
                inst.PlotOnCanvas(pdf_name=opt.model+'.pdf')
            elif idx==len(list_histo):
                inst.PlotOnCanvas(pdf_name=opt.model+'.pdf')
                c2 = TCanvas()
                c2.Print(opt.model+'.pdf]')
            else:
                inst.PlotOnCanvas(pdf_name=opt.model+'.pdf')

            #for h in inst.histo:
            #    print (type(h))
            #inst.histo.Write()


        
        
        



if __name__ == "__main__":
    main()   
