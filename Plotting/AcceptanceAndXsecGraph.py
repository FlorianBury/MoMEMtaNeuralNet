import os
import sys
import re
import argparse
import glob
import logging
import copy
import numpy as np
import math
import enlighten

sys.path.append('/home/ucl/cp3/fbury/scratch/CMSSW_7_1_20_patch2/src/cp3_llbb/Calculators42HDM/python/') # needed to improt Calc2HDM
from Calc2HDM import Calc2HDM

import ROOT
from ROOT import TFile,  gROOT, TGraph2D
import CMS_lumi
import tdrstyle


gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = 2000#[ROOT.kPrint, ROOT.kInfo]#, kWarning, kError, kBreak, kSysError, kFatal;
       

def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='Built the acceptance and cross-section graph to be used later in the likelihood')
    parser.add_argument('--bins', action='store', required=True, type=int, 
                  help='Numebr of bins in each axis of the graph')
    parser.add_argument('--max', action='store', required=True, type=int,
                  help='Maximum values for mA and mH in the graph')
    parser.add_argument('--PDF', action='store_true', required=False, default=False,
            help='Produce PDF from the root file')
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
    # Acceptance and Cross section graphs #
    #############################################################################################
    # Make grid #
    xy = np.linspace(0,opt.max,opt.bins) 
    mA,mH = np.meshgrid(xy,xy)
    upper = np.greater(mH,mA)
    mA = mA[upper]
    mH = mH[upper]
    N = mA.shape[0]


    # Alexia's PhD thesis parameters
    sqrts = 13000
    tb = 1.5
    cba = 0.01
    sba = math.sqrt(1 - pow(cba, 2)) 
    outputFile = "out.dat"

    # Get the cross sections #
    Xseco = np.zeros(mA.shape[0])
    BR_HtoZA = np.zeros(mA.shape[0])
    BR_Atobb = np.zeros(mA.shape[0])
    BR_Ztobb = np.ones(mA.shape[0])*3.3658 * 2 / 100. # no taus

    manager = enlighten.get_manager()
    pbar = manager.counter(total=N, desc='Progress', unit='Point')
    for i in range(N):
        mhc = max(mH[i], mA[i])
        instance = Calc2HDM(mode = 'H',
                            sqrts = sqrts,
                            type = 2,
                            tb = tb,
                            m12 = math.sqrt(pow(mhc, 2) * tb / (1 + pow(tb, 2))),
                            mh = 125,
                            mH = mH[i],
                            mA = mA[i],
                            mhc = mhc,
                            sba = sba,
                            outputFile = outputFile,
                            muR = 1.,
                            muF = 1.,
                            workdir = '/home/ucl/cp3/fbury/scratch/CMSSW_7_1_20_patch2/src/cp3_llbb/Calculators42HDM/')
        instance.setpdf('NNPDF30_lo_as_0130_nf_4')
        instance.computeBR()
        print (instance.HtoZABR)
        print (instance.AtobbBR)
        xsec, err_integration, err_muRm, err_muRp = instance.getXsecFromSusHi()
        print (xsec, err_integration, err_muRm, err_muRp)
        pbar.update()
        sys.exit()

    manager.stop()

   
if __name__ == "__main__":
    main() 
