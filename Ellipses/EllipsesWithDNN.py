import os
import sys
import re
import argparse
import glob
import logging
import copy
import numpy as np
import pandas as pd
import enlighten

from Processing import ProcessDNN ,ProcessEllipse, ProcessROC

def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='Uses the ellipse selection with the DNN output')
    parser.add_argument('-m','--model', action='store', required=True, type=str, default='',
                  help='NN model to be used')
    parser.add_argument('-f','--file', action='store', required=False, type=str, default='',
                  help='File (full path) to be used')
    parser.add_argument('--DNN', action='store_true', required=False, default=False,
            help='Wether to apply the DNN regression and classification')
    parser.add_argument('--ellipse', action='store_true', required=False, default=False,
            help='Wether to apply the ellipse classification')
    parser.add_argument('--ROC', action='store_true', required=False, default=False,
            help='Wether to apply the ROC curve')
    parser.add_argument('--HToZA', action='store_true', required=False, default=False,
            help='Compute the signal weights (combined with DNN option)')
    parser.add_argument('--DY', action='store_true', required=False, default=False,
            help='Compute the DY weights (combined with DNN option)')
    parser.add_argument('--TT', action='store_true', required=False, default=False,
            help='Compute the TT weights (combined with DNN option)')
    parser.add_argument('--force_DNN', action='store_true', required=False, default=False,
            help='Force the reprocessing byt the DNN and recreation of the save')
    parser.add_argument('--force_ellipse', action='store_true', required=False, default=False,
            help='Force the reprocessing byt the DNN and recreation of the save')
    parser.add_argument('--start', action='store', required=False, type=int,
                  help='Where to start in the tree')
    parser.add_argument('--end', action='store', required=False, type=int, 
                  help='Where to end in the tree')

    opt = parser.parse_args() 


    #############################################################################################
    # Get the files #
    #############################################################################################
    path_to_signal = '/nfs/scratch/fynu/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/skimmed_for_Florian_2019_all207signals/slurm/output/'
    path_to_background = '/nfs/scratch/fynu/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/skimmed_for_Florian_2019_backgrounds/slurm/output/'
    path_save = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/EllipsesOutput/'

    list_HToZA = glob.glob(os.path.join(path_to_signal,opt.file))
    list_DY    = glob.glob(os.path.join(path_to_background,'DY*.root')) 
    list_TT    = glob.glob(os.path.join(path_to_background,'TT*.root')) 
    if opt.file != '':
        p = re.compile(r'\d+[p]\d+')
        mH = float(p.findall(opt.file)[0].replace('p','.'))
        mA = float(p.findall(opt.file)[1].replace('p','.'))
    else:
        mH = 0
        mA = 0

    # Lists of parameters #
    list_inputs = [
                    'lep1_p4.Pt()',
                    'lep1_p4.Eta()',
                    'lep2_p4.Pt()', 
                    'lep2_p4.Eta()', 
                    'lep2_p4.Phi()-lep1_p4.Phi()', 
                    'jet1_p4.Pt()',
                    'jet1_p4.Eta()', 
                    'jet1_p4.Phi()-lep1_p4.Phi()',
                    'jet2_p4.Pt()',  
                    'jet2_p4.Eta()',
                    'jet2_p4.Phi()-lep1_p4.Phi()',
                    'met_pt',
                    'met_phi-lep1_p4.Phi()',
                  ]
    list_other = [
                    'll_M',
                    'jj_M',
                    'lljj_M',
                    'total_weight',
                 ]
    cuts = 'met_pt<80 && ll_M>70 && ll_M<110'
    sigmas = [0.5,1,1.5,2,2.5,3,3.5,4]

    # Instantiate #
    DY = None
    TT = None
    HToZA = None
    if opt.start is not None and opt.end is not None:
        supp_str = '_%d_%d'%(opt.start,opt.end)
    else:
        supp_str = ''
    if opt.DNN:
        if opt.DY:
            DY = ProcessDNN(model_name=opt.model,
                        list_inputs=list_inputs,
                        label='DY',
                        list_files = list_DY,
                        variables = list_inputs+list_other,
                        cuts = cuts,
                        save_path = os.path.join(path_save,'DY'+supp_str+'.root'),
                        mH = mH,
                        mA = mA,
                        force = opt.force_DNN,
                        path_signal = path_to_signal,
                        start = opt.start,
                        end = opt.end,
                        do_all_masses= True)            
        if opt.TT:
            TT = ProcessDNN(model_name=opt.model,
                        list_inputs=list_inputs,
                        label='TT',
                        list_files = list_TT,
                        variables = list_inputs+list_other,
                        cuts = cuts,
                        save_path = os.path.join(path_save,'TT'+supp_str+'.root'),
                        mH = mH,
                        mA = mA,
                        force = opt.force_DNN,
                        path_signal = path_to_signal,
                        start = opt.start,
                        end = opt.end,
                        do_all_masses= True)            
        if opt.HToZA:
            HToZA = ProcessDNN(model_name=opt.model,
                        list_inputs=list_inputs,
                        label='HToZA',
                        list_files = list_HToZA,
                        variables = list_inputs+list_other,
                        cuts = cuts,
                        save_path = os.path.join(path_save,os.path.basename(opt.file)),
                        force = opt.force_DNN,
                        path_signal = path_to_signal,
                        mH = mH,
                        mA = mA,
                        start = opt.start,
                        end = opt.end)            

    # Instantiate ellipse # 
    if opt.ellipse and opt.file != '':
        ellipse = ProcessEllipse(
                          inst_DY = DY,
                          inst_TT = TT,
                          inst_HToZA = HToZA, 
                          path_json = 'fullEllipseParamWindowFit_ElEl.json',
                          mA = mA,
                          mH = mH,
                          sigmas = sigmas,
                          save_path = os.path.join(path_save,'Processed_'+os.path.basename(opt.file)),
                          force = opt.force_ellipse)            

    # Instantiate ROC # 
    if opt.ROC:
        ROC = ProcessROC(ellipse,mH=mH,mA=mA)
                
              

if __name__ == "__main__":
    main()   
