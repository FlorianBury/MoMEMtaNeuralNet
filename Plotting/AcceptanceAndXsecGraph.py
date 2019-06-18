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
from ROOT import TFile,  gROOT, TGraph2D, TCanvas, TH2F, gPad, gStyle
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
    parser.add_argument('--recover', action='store_true', required=False, default=False,
            help='Only use the already computed xsec files from Sushy')
    parser.add_argument('--acceptance', action='store_true', required=False, default=False,
            help='Compute the acceptance and produce graph')
    parser.add_argument('--combine', action='store_true', required=False, default=False,
            help='Combine the acceptance, xsec and BR to get the visible cross section')
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
    # Make grid #
    #############################################################################################
    xy = np.linspace(0,opt.max,opt.bins) 
    mA_plane,mH_plane = np.meshgrid(xy,xy)
    mh = 125
    mZ = 90
    condition1 = np.greater(mH_plane,mA_plane)
    condition2 = np.greater(mH_plane,mh)
    #condition3 = np.greater(np.subtract(mH_plane,mA_plane),mZ)
    #upper = np.logical_and(np.logical_and(condition1,condition2),condition3)
    upper = np.logical_and(condition1,condition2)
        # Ensure that mH > mh
        # Ensure that mH > mA
        # Ensure that mH-mA > mZ
    mA = mA_plane[upper].flatten().astype(int)
    mH = mH_plane[upper].flatten().astype(int)
    mA_plane = mA_plane.flatten()
    mH_plane = mH_plane.flatten()
    N = mA.shape[0]
    N_plane = mA_plane.shape[0]
    # Bug in Sushi -> if both mH and mA have decimals the computation of Xsec fails

    #############################################################################################
    # Make PDF #
    #############################################################################################
    def getall(d, basepath="/"):
        "Generator function to recurse into a ROOT file/dir and yield (path, obj) pairs"
        for key in d.GetListOfKeys():
            kname = key.GetName()
            if key.IsFolder():
                for i in getall(d.Get(kname), basepath+kname+'/'):
                    yield i
            else:
                yield basepath+kname, d.Get(kname)

    if opt.PDF:
        path_root = ['AcceptanceMap.root','XsecMap.root','VisibleXsecMap.root']

        path_pdf  = ['AcceptanceMap.pdf','XsecMap.pdf','VisibleXsecMap.pdf']
    
        for root,pdf in zip(path_root,path_pdf):
            f = TFile(root)
            canvas = TCanvas()
            canvas.Print(pdf+'[')
            for i, (key,obj) in enumerate(getall(f)):
                c1 = TCanvas()
                c1.SetGrid()
                logging.info('Processing %s'%key)
                base_hist = TH2F('','',opt.bins,0,opt.max,opt.bins,0,opt.max)
                obj.SetHistogram(base_hist)
                hist = obj.GetHistogram()
                hist.GetXaxis().SetRangeUser(0,opt.max)
                hist.GetYaxis().SetRangeUser(0,opt.max)
                hist.SetContour(opt.bins)
                hist.Draw('colz')
                gStyle.SetOptStat(0)
                c1.SetTopMargin(0.1)
                c1.SetBottomMargin(0.12)
                c1.SetLeftMargin(0.12)
                c1.SetRightMargin(0.18)
                hist.GetXaxis().SetTitleOffset(1.3)
                hist.GetYaxis().SetTitleOffset(1.3)
                hist.GetZaxis().SetTitleOffset(1.5)
                hist.SetTitle(obj.GetTitle())
                c1.Print(pdf,'Title:'+key.replace('.root','').replace('/',''))
            canvas.Print(pdf+']') 
            logging.info('PDF saved as %s'%pdf)

        sys.exit()
    #############################################################################################
    # Combine graph #
    #############################################################################################
    if opt.combine:
        # Load the graphs #
        file_xsec = TFile.Open('XsecMap.root')                                                                                                                                                     
        file_acc = TFile.Open('AcceptanceMap.root')                                                                                                                                                
        
        xsec = copy.deepcopy(file_xsec.Get('Xsec'))                                                                                                                                             
        BR_HtoZA = copy.deepcopy(file_xsec.Get('BR_HtoZA'))                                                                                                                                    
        BR_Atobb = copy.deepcopy(file_xsec.Get('BR_Atobb'))                                                                                                                                    
        BR_Ztoll = copy.deepcopy(file_xsec.Get('BR_Ztoll'))                                                                                                                                    
        acc = copy.deepcopy(file_acc.Get('Acceptance'))    

        # Make combined graph #
        comb_graph = TGraph2D(N)
        manager = enlighten.get_manager()
        pbar = manager.counter(total=N, desc='Progress', unit='Point')
        for i in range(N):
            m_A = mA[i]
            m_H = mH[i]
            XsecVis =  xsec.Interpolate(m_A,m_H)
            XsecVis *= BR_HtoZA.Interpolate(m_A,m_H)
            #XsecVis *= BR_Atobb.Interpolate(m_A,m_H)
            XsecVis *= 3.3658 * 2 / 100 #BR_Ztoll.Interpolate(m_A,m_H)
            XsecVis *= acc.Interpolate(m_A,m_H)
            comb_graph.SetPoint(i,m_A,m_H,XsecVis)
            pbar.update()
        manager.stop()
    
        comb_graph.SetTitle('Visible Cross-section; MA [GeV] ; MH [GeV] ; Xsec [pb]')
        comb_graph.SetNpx(500)
        comb_graph.SetNpy(500)
        name = 'VisibleXsecMap.root'
        root_file = TFile(name,"recreate")
        comb_graph.Write('Visible_XsecMap')
       

    #############################################################################################
    # Extrapolate graph #
    #############################################################################################
    def ExtrapolateGraph(graph,points):
        print ('Extrapolation')
        new_graph = TGraph2D(N_plane)
        # Extrapolation #
        from scipy.optimize import curve_fit

        def func(x,a,b,c,x0,y0,e1,e2):
            z = (a*(x[0]-x0)**2 + b*(x[1]-y0)**2 + c*(x[0]-x0)*(x[1]-y0))*np.exp(-x[0]/e1-x[1]/e2)
            return z.ravel()
        initial_guess = (-4e-6,-5e-7,9e-6,500,800,400,700) 
        popt, pcov = curve_fit(func, (points[:,0],points[:,1]), points[:,2], p0=initial_guess)
        print (popt)

        manager = enlighten.get_manager()
        pbar = manager.counter(total=N_plane, desc='Progress', unit='Point')
        for i in range(N_plane):
            pbar.update()
            m_A = mA_plane[i]
            m_H = mH_plane[i]
            if m_A>=m_H :#or m_H<=mh :#or m_H-m_A<mZ:
                new_graph.SetPoint(i,m_A,m_H,0)
                continue
            Z = func((m_A,m_H),*popt)
           # Truncation #
            if m_H>1000:
                Z = func((m_A,1000),*popt)
            if Z<=0.02:
                Z = 0.02
            if Z<=0.07 and m_H>400:
                    Z = 0.07
                
            new_graph.SetPoint(i,m_A,m_H,Z)
        manager.stop()
        return new_graph
    
    #############################################################################################
    # Cross section and Branching Ratio graphs #
    #############################################################################################
    if opt.recover:   
        save_dir = '/home/ucl/cp3/fbury/scratch/CMSSW_7_1_20_patch2/src/cp3_llbb/Calculators42HDM/Scan/*.out'
        files = glob.glob(save_dir)
        N_files = len(files)
        mA = []
        mH = []
        print ('Recovering the outputs from Sushi')
        manager = enlighten.get_manager()
        pbar = manager.counter(total=N_files, desc='Progress', unit='Files')
        for i,f in enumerate(files):
            ints = re.findall(r"\d+", os.path.basename(f))
            if int(ints[0])>1500 or int(ints[1])>1500:
                continue
            mH.append(int(ints[0]))
            mA.append(int(ints[1]))
            print ('\tMH = %d MA = %d'%(int(ints[1]),int(ints[0])))
        mA = np.asarray(mA)
        mH = np.asarray(mH)
        N = mA.shape[0]
        print ("Total configurations %d"%N)
        
    if opt.xsec:
        # Alexia's PhD thesis parameters
        sqrts = 13000
        tb = 1.5
        cba = 0.01
        mh = 125
        sba = math.sqrt(1 - pow(cba, 2)) 
        workdir = '/home/ucl/cp3/fbury/scratch/CMSSW_7_1_20_patch2/src/cp3_llbb/Calculators42HDM/'
        outputFile = os.path.join(workdir,"out.dat")

        # Randomize mA and mH (launch multiple)
        #index = np.arange(mA.shape[0])
        #np.random.shuffle(index)
        #mA = mA[index]
        #mH = mH[index]

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

        if os.path.exists('xsec_arr.npy') and os.path.exists('BR_HtoZA_arr.npy') and os.path.exists('BR_Atobb_arr.npy'):
            print ('Recovered npy files')
            xsec_arr = np.load('xsec_arr.npy')
            BR_HtoZA_arr = np.load('BR_HtoZA_arr.npy')
            BR_Atobb_arr = np.load('BR_Atobb_arr.npy')

            for i in range(xsec_arr.shape[0]):
                graph_Xsec.SetPoint(i,xsec_arr[i,0],xsec_arr[i,1],xsec_arr[i,2])
                graph_BR_HtoZA.SetPoint(i,BR_HtoZA_arr[i,0],BR_HtoZA_arr[i,1],BR_HtoZA_arr[i,2])
                graph_BR_Atobb.SetPoint(i,BR_Atobb_arr[i,0],BR_Atobb_arr[i,1],BR_Atobb_arr[i,2])
                graph_BR_Ztoll.SetPoint(i,BR_Atobb_arr[i,0],BR_Atobb_arr[i,1],3.3658 * 2 / 100)
                
        else:
            manager = enlighten.get_manager()
            pbar = manager.counter(total=N, desc='Progress', unit='Point')
            xsec_arr = []
            BR_HtoZA_arr = []
            BR_Atobb_arr = []       
            mH_arr = []
            mA_arr = []
            for i in range(N):
                print ('-'*80)
                print ('MH = %0.2f, MA = %0.2f'%(mH[i], mA[i]))
                mhc = max(mH[i], mA[i])
                m12 = math.sqrt(pow(mhc, 2) * tb / (1 + pow(tb, 2)))
                # change the masses #
                instance.setmA(int(mA[i]))
                instance.setmH(int(mH[i]))
                instance.setmHc(mhc)
                instance.setm12(m12)
                mH_arr.append(mH[i])
                mA_arr.append(mA[i])

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
                xsec_arr.append(xsec)
                BR_HtoZA_arr.append(instance.HtoZABR)
                BR_Atobb_arr.append(instance.AtobbBR)

                # Update loading bar #
                pbar.update()
            manager.stop()

            # Save numpy objects #
            xsec_arr = np.asarray(xsec_arr)
            BR_HtoZA_arr = np.asarray(BR_HtoZA_arr)
            BR_Atobb_arr = np.asarray(BR_Atobb_arr)
            mA_arr = np.asarray(mA_arr)
            mH_arr = np.asarray(mH_arr)
            np.save('xsec_arr',np.c_[mA_arr,mH_arr,xsec_arr])
            np.save('BR_HtoZA_arr',np.c_[mA_arr,mH_arr,BR_HtoZA_arr])
            np.save('BR_Atobb_arr',np.c_[mA_arr,mH_arr,BR_Atobb_arr])

        # Save graph #

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
        # Paths and files #
        path_to_207_signal_files = "/nfs/scratch/fynu/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/skimmed_for_Florian_2019_all207signals/slurm/output/"
        path_to_23_signal_files = "/nfs/user/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/skimmedPlots_for_Florian/slurm/output/"
        files_207 = glob.glob(os.path.join(path_to_207_signal_files,'HToZA*root'))
        #files_23 = glob.glob(os.path.join(path_to_23_signal_files,'HToZA*root'))
        files = files_207 

        # Initialize #
        points = np.empty((0,3))
        manager = enlighten.get_manager()
        pbar = manager.counter(total=len(files), desc='Progress', unit='Point')

        # Loop over mass points #
        for i,f in enumerate(files):
            name = os.path.basename(f)
            # check if signal #
            if not name.startswith('HToZA'):
                continue
            
            # Get the mA and mH #
            file_handle = TFile.Open(f)
            p = re.compile(r'\d+[p]\d+')
            if len(p.findall(name))==0:
                m_H = float(re.findall(r'\d+', name)[2])
                m_A = float(re.findall(r'\d+', name)[3])
            else:
                m_H = float(p.findall(name)[0].replace('p','.'))
                m_A = float(p.findall(name)[1].replace('p','.'))
            print ('Sample MH = %0.2f mA = %0.2f'%(m_H,m_A))

            # Get the ratio #
            tree = file_handle.Get('t') 
            weight_sum = file_handle.Get('event_weight_sum').GetVal()  
            N = tree.GetEntries()           
            ratio = N/weight_sum
            print ('\tRatio : %0.5f'%(ratio))

            # if seen before -> add #
            seen = False
            idx = i
            for j in range(points.shape[0]):
                if m_H == points[j,1] and m_A == points[j,0]:
                    idx = j # if seen before records that index, else keep i
                    seen = True

            # Records #
            if not seen :
                new_entry = np.array([m_A,m_H,0],ndmin=2)
                points = np.append(points,new_entry,axis=0) # add mA,mH to record
            points[idx,2] +=  ratio
            pbar.update()
        manager.stop()

        # Fill TGraph2D #
        graph_acc = TGraph2D(points.shape[0])
        for i in range(points.shape[0]):
            graph_acc.SetPoint(i,points[i,0],points[i,1],points[i,2])

        graph_acc.SetTitle('Acceptance; MA [GeV] ; MH [GeV] ; Ratio')
        graph_acc.SetNpx(500)
        graph_acc.SetNpy(500)

        extra_graph_acc = ExtrapolateGraph(graph_acc,points)
        extra_graph_acc.SetTitle('Acceptance; MA [GeV] ; MH [GeV] ; Ratio')
        extra_graph_acc.SetNpx(500)
        extra_graph_acc.SetNpy(500)
        np.save('points',points)

        name = 'AcceptanceMap.root'
        root_file = TFile(name,"recreate")
        graph_acc.Write('Acceptance_intra')
        extra_graph_acc.Write('Acceptance')
       
if __name__ == "__main__":
    main() 
