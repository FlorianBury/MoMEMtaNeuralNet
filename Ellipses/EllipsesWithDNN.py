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

from Sample import Sample ,Ellipse

def main():
    # Get the files #
    path_to_signal = '/nfs/scratch/fynu/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/skimmed_for_Florian_2019_all207signals/slurm/output/'
    path_to_background = '/nfs/scratch/fynu/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/skimmed_for_Florian_2019_backgrounds/slurm/output/'
    list_HToZA = glob.glob(os.path.join(path_to_signal,'HToZA*.root')) 
    list_DY    = glob.glob(os.path.join(path_to_background,'DY*.root')) 
    list_TT    = glob.glob(os.path.join(path_to_background,'TT*.root')) 

    # Lists of parameters #
    list_inputs = [
                    'lep1_p4.Pt()',
                    'lep1_p4.Eta()',
                    'lep2_p4.Pt()', 
                    'lep2_p4.Eta()', 
                    'lep2_p4.Phi() - lep1_p4.Phi()', 
                    'jet1_p4.Pt()',
                    'jet1_p4.Eta()', 
                    'jet1_p4.Phi() - lep1_p4.Phi()',
                    'jet2_p4.Pt()',  
                    'jet2_p4.Eta()',
                    'jet2_p4.Phi() - lep1_p4.Phi()',
                    'met_pt',
                    'met_phi - lep1_p4.Phi()',
                  ]
    list_other = [
                    'll_M',
                    'jj_M',
                    'lljj_M',
                    'total_weight',
                 ]
    cuts = 'met_pt<80 && ll_M>70 && ll_M<110'

    # Instantiate #

    DY = Sample(model_name='BestModel',
                list_inputs=list_inputs,
                label='DY',
                list_files = list_DY,
                variables = list_inputs+list_other,
                cuts = cuts)            

    #TT = Sample(model_name='BestModel',
    #            list_inputs=list_inputs,
    #            label='TT',
    #            list_files = list_TT,
    #            variables = list_inputs+list_other,
    #            cuts = cuts)            

    #HToZA = Sample(model_name='BestModel',
    #            list_inputs=list_inputs,
    #            label='HToZA',
    #            list_files = list_HToZA,
    #            variables = list_inputs+list_other,
    #            cuts = cuts)            
    
    # Instantiate ellipse # 
    #DY = None
    TT = None
    HToZA = None
    ellipse = Ellipse(inst_DY = DY,
                      inst_TT = TT,
                      inst_HToZA = HToZA, 
                      path_json = 'fullEllipseParamWindowFit_ElEl.json',
                      mA = 47.08,
                      mH = 609.21,
                     )
                      


                
              

if __name__ == "__main__":
    main()   
