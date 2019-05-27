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

from Sample import Sample

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

    list_signal_outputs = [
                            '-log10(weight_HToZA_mH_200_mA_50)',
                            '-log10(weight_HToZA_mH_200_mA_100)',
                            '-log10(weight_HToZA_mH_250_mA_50)',
                            '-log10(weight_HToZA_mH_250_mA_100)',
                            '-log10(weight_HToZA_mH_300_mA_50)',   
                            '-log10(weight_HToZA_mH_300_mA_100)', 
                            '-log10(weight_HToZA_mH_300_mA_200)',
                            '-log10(weight_HToZA_mH_500_mA_50)', 
                            '-log10(weight_HToZA_mH_500_mA_100)',
                            '-log10(weight_HToZA_mH_500_mA_200)', 
                            '-log10(weight_HToZA_mH_500_mA_300)', 
                            '-log10(weight_HToZA_mH_500_mA_400)', 
                            '-log10(weight_HToZA_mH_650_mA_50)',
                            '-log10(weight_HToZA_mH_800_mA_50)',
                            '-log10(weight_HToZA_mH_800_mA_100)',
                            '-log10(weight_HToZA_mH_800_mA_200)',
                            '-log10(weight_HToZA_mH_800_mA_400)',
                            '-log10(weight_HToZA_mH_800_mA_700)',
                            '-log10(weight_HToZA_mH_1000_mA_50)',  
                            '-log10(weight_HToZA_mH_1000_mA_200)',
                            '-log10(weight_HToZA_mH_1000_mA_500)', 
                            '-log10(weight_HToZA_mH_2000_mA_1000)',
                            '-log10(weight_HToZA_mH_3000_mA_2000)',
                          ]
   
    #HToZA = Sample('HToZA')
    #HToZA.GetData(list_HToZA)
    #print (HToZA.data)
    DY = Sample('DY')
    DY.GetData(list_DY,list_inputs+list_other,cuts)

    DY.ProduceWeights('BestModel',list_inputs,list_signal_outputs)

    #list_signal_outputs 
                
              

if __name__ == "__main__":
    main()   
