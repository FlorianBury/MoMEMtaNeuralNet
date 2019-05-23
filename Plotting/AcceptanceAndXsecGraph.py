import os
import sys
import re
import argparse
import glob
import logging
import copy
sys.path.insert(0,'/home/ucl/cp3/fbury/.local/lib/python3.6/site-packages')
import numpy as np
import math
import enlighten

sys.path.append('/home/ucl/cp3/fbury/scratch/CMSSW_7_1_20_patch2/src/cp3_llbb/Calculators42HDM/python/') # needed to improt Calc2HDM
from Calc2HDM import Calc2HDM

import ROOT
from ROOT import TFile,  gROOT, TGraph2D, TCanvas
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
    parser.add_argument('--xsec', action='store_true', required=False, default=False,
            help='Compute the cross-sections and produce graphs')
    parser.add_argument('--acceptance', action='store_true', required=False, default=False,
            help='Compute the acceptance and produce graph')
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
    # Cross section and Branching Ratio graphs #
    #############################################################################################
    if opt.xsec:
        # Alexia's PhD thesis parameters
        sqrts = 13000
        tb = 1.5
        cba = 0.01
        mh = 125
        sba = math.sqrt(1 - pow(cba, 2)) 
        workdir = '/home/ucl/cp3/fbury/scratch/CMSSW_7_1_20_patch2/src/cp3_llbb/Calculators42HDM/'
        outputFile = os.path.join(workdir,"out.dat")


        # Make grid #
        xy = np.linspace(0,opt.max,opt.bins) 
        mA,mH = np.meshgrid(xy,xy)
        upper = np.logical_and(np.greater(mH,mA),np.greater(mH,mh))
            # Ensure that mH > mh
            # Ensure that mH > mA
        mA = mA[upper].flatten().astype(int)
        mH = mH[upper].flatten().astype(int)
        N = mA.shape[0]
        # Bug in Sushi -> if both mH and mA have decimals the computation of Xsec fails

        # Randomize mA and mH (launch multiple)
        index = np.arange(N)
        np.random.shuffle(index)
        mA = mA[index]
        mH = mH[index]

        # Initialize TGraph2D #
        graph_Xsec     = TGraph2D(N)
        graph_BR_HtoZA = TGraph2D(N)
        graph_BR_Atobb = TGraph2D(N)
        graph_BR_Ztoll = TGraph2D(N)

        # Get the cross sections #

        instance = Calc2HDM(mode = 'H',
                            sqrts = sqrts,
                            type = 2,
                            tb = tb,
                            m12 = 0,
                            mh = mh,
                            mH = 0,
                            mA = 0,
                            mhc = 0,
                            sba = sba,
                            outputFile = outputFile,
                            muR = 1.,
                            muF = 1.,
                            workdir = workdir)
        instance.setpdf('NNPDF30_lo_as_0130_nf_4')


        manager = enlighten.get_manager()
        pbar = manager.counter(total=N, desc='Progress', unit='Point')
        for i in range(N):
            print ('-'*80)
            print ('MH = %0.2f, MA = %0.2f'%(mH[i], mA[i]))
            mhc = max(mH[i], mA[i])
            m12 = math.sqrt(pow(mhc, 2) * tb / (1 + pow(tb, 2)))
            # change the masses #
            instance.setmA(mA[i])
            instance.setmH(mH[i])
            instance.setmHc(mhc)
            instance.setm12(m12)

            # Get BR #
            instance.computeBR()
            # Get Xsec #
            try:
                xsec, _, _, _ = instance.getXsecFromSusHi()
                print ('Xsec      : ',xsec)
            except Exception as e:
                print ('Exception "%s" -> Xsec put to 0'%e)
                xsec = 0
            # Record values #
            print ('H->ZA     : ',instance.HtoZABR)
            print ('A->bb     : ',instance.AtobbBR)
            print ('Z->ll     : ',3.3658 * 2 / 100)
            print ('Xsec x BR : ',xsec*instance.HtoZABR*instance.AtobbBR*3.3658 * 2 / 100)

            graph_Xsec.SetPoint(i,mA[i],mH[i],xsec)
            graph_BR_HtoZA.SetPoint(i,mA[i],mH[i],instance.HtoZABR)
            graph_BR_Atobb.SetPoint(i,mA[i],mH[i],instance.AtobbBR)
            graph_BR_Ztoll.SetPoint(i,mA[i],mH[i],3.3658 * 2 / 100)

            # Update loading bar #
            pbar.update()
        manager.stop()

        graph_Xsec.SetNpx(500)
        graph_Xsec.SetNpy(500)
        graph_BR_HtoZA.SetNpx(500)
        graph_BR_HtoZA.SetNpy(500)
        graph_BR_Atobb.SetNpx(500)
        graph_BR_Atobb.SetNpy(500)
        graph_BR_Ztoll.SetNpx(500)
        graph_BR_Ztoll.SetNpy(500)

        graph_Xsec.SetTitle('Cross-section map; MA [GeV] ; MH [GeV] ; Xsec [pb]')
        graph_BR_HtoZA.SetTitle('Branching ratio H #rightarrow ZA map; MA [GeV] ; MH [GeV] ; BR(HtoZA)')
        graph_BR_Atobb.SetTitle('Branching ratio A #rightarrow bb map; MA [GeV] ; MH [GeV] ; BR(Atobb)')
        graph_BR_Ztoll.SetTitle('Branching ratio Z #rightarrow ll map; MA [GeV] ; MH [GeV] ; BR(Ztoll)')

        name = 'XsecMap.root'
        root_file = TFile(name,"recreate")
        graph_Xsec.Write('Xsec')
        graph_BR_HtoZA.Write('BR_HtoZA')
        graph_BR_Atobb.Write('BR_Atobb')
        graph_BR_Ztoll.Write('BR_Ztoll')


    #############################################################################################
    # Acceptance graphs #
    #############################################################################################
    if opt.acceptance:
        path_to_207_signal_files = "/nfs/scratch/fynu/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/skimmed_for_Florian_2019_all207signals/slurm/output/"
        path_to_23_signal_files = "/nfs/user/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/skimmedPlots_for_Florian/slurm/output/"
        files_207 = glob.glob(os.path.join(path_to_207_signal_files,'HToZA*root'))
        files_23 = glob.glob(os.path.join(path_to_23_signal_files,'HToZA*root'))
        files = files_207 + files_23
        graph_acc = TGraph2D(len(files))
        for i,f in enumerate(files):
            name = os.path.basename(f)
            if not name.startswith('HToZA'):
                continue
            print ( name)
            file_handle = TFile.Open(f)
            p = re.compile(r'\d+[p]\d+')
            if len(p.findall(name))==0:
                mH = float(re.findall(r'\d+', filename)[2])
                mA = float(re.findall(r'\d+', filename)[3])
            else:
                mH = float(p.findall(name)[0].replace('p','.'))
                mA = float(p.findall(name)[1].replace('p','.'))
            print ( mH, mA)

            tree = file_handle.Get('t') 
            weight_sum = file_handle.Get('event_weight_sum').GetVal()  
            N = tree.GetEntries()           
            print (N,weight_sum,N/weight_sum)
            graph_acc.SetPoint(i,mA,mH,N/weight_sum)
        sys.exit()
        name = 'AcceptanceMap.root'
        root_file = TFile(name,"recreate")
        graph_acc.Write('Acceptance')
       
if __name__ == "__main__":
    main() 
