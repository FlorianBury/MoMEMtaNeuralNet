import os
import sys
import argparse
import glob
import logging
import copy

import ROOT
from ROOT import TFile, TH1F, gROOT, TRatioPlot
#gROOT.Macro( os.path.abspath( 'rootlogon.C'))
#gROOT.LoadMacro("Divide2hists1D.C")

def MakeLabels(hist):
    try:
        hist.GetXaxis().SetTitle("-log(weights)")
        hist.GetYaxis().SetTitle("Occurences")
    except AttributeError:
        pass


def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='From given set of root files, make different histograms in a root file')
    #parser.add_argument('-t','--type', action='store', required=True, type=str, default='',
    #              help='Type fo file to use (HToZA, DY or TT)')
    parser.add_argument('-m','--model', action='store', required=True, type=str, default='',
                  help='NN model to be used')
    parser.add_argument('-v','--verbose', action='store_true', required=False, default=False,
            help='Show DEGUG logging')
    opt = parser.parse_args() 

    #if opt.type != "HToZA" and opt.type != "DY" and opt.type != "TT":
    #    sys.exit('Incorrect type')

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
    INPUT_VALID = os.path.join(INPUT_DIR,'valid_weights')
    INPUT_INVALID_DY = os.path.join(INPUT_DIR,'invalid_DY_weights')
    INPUT_INVALID_TT = os.path.join(INPUT_DIR,'invalid_TT_weights')
    INPUT_MODEL = os.path.join(INPUT_DIR,'NNOutput',opt.model)

    # generate Root files #
    f_root = TFile(opt.model+".root", "recreate")

    #############################################################################################
    # Valid weights output #
    #############################################################################################
    logging.info('Starting Plotting the valid weights')
    list_hist = []
    for f in glob.glob(INPUT_MODEL+'/*.root'):
        # Except invalids #
        filename = f.replace(INPUT_MODEL,'')
        if filename.find('invalid')!=-1:
            continue
        logging.info('Processing %s'%(filename))
        # Get root file #
        file_handle = TFile.Open(f)
        tree = file_handle.Get('tree')

        # Save the hist #
        tree.Draw("MEM_weight_DY>>MEM_weight_DY_"+filename+"(100,10,40)","","goff")    
        MEM_weight_DY = gROOT.FindObject("MEM_weight_DY_"+filename)
        tree.Draw("MEM_weight_TT>>MEM_weight_TT_"+filename+"(100,10,40)","","goff")    
        MEM_weight_TT = gROOT.FindObject("MEM_weight_TT_"+filename)
        tree.Draw("output_DY>>NN_weight_DY_"+filename+"(100,10,40)","","goff")    
        NN_weight_DY = gROOT.FindObject("NN_weight_DY_"+filename)
        tree.Draw("output_TT>>NN_weight_TT_"+filename+"(100,10,40)","","goff")    
        NN_weight_TT = gROOT.FindObject("NN_weight_TT_"+filename)

        # Ratiplot #
        ratio_DY = TRatioPlot(MEM_weight_DY,NN_weight_DY)
        #ratio_DY.SetTitle('Ratio DY')
        ratio_TT = TRatioPlot(MEM_weight_TT,NN_weight_TT)
        #ratio_TT.SetTitle('Ratio TT')

        # Append to list #
        list_hist.append(copy.deepcopy(MEM_weight_DY)) # copy because hist is destroyed when leaving file 
        list_hist.append(copy.deepcopy(MEM_weight_TT)) 
        list_hist.append(copy.deepcopy(NN_weight_DY))
        list_hist.append(copy.deepcopy(NN_weight_TT)) 
        list_hist.append(copy.deepcopy(ratio_DY)) 
        list_hist.append(copy.deepcopy(ratio_TT)) 


    # Save to root file #
    f_root = TFile(opt.model+".root", "recreate")
    for hist in list_hist:
        MakeLabels(hist)
        hist.Write()
            

    

        
        
        



if __name__ == "__main__":
    main()   
