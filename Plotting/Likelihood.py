import os
import sys
import re
import argparse
import math
import glob
import logging
import copy
import numpy as np
import enlighten

sys.path.insert(0,"..") # We need our own version of talos
                        # If we import our modules after the version is sites-package, our version is ignored
#from NeuralNet import HyperModel
from import_tree import Tree2Pandas
from preprocessing import PreprocessLayer
from talos import Restore

import ROOT
from ROOT import TFile, TH1F, TH2F, TCanvas, gROOT, TGraph2D, gPad, TObject, gStyle, TPaveText
import CMS_lumi
import tdrstyle

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
ROOT.gErrorIgnoreLevel = 2000#[ROOT.kPrint, ROOT.kInfo]#, kWarning, kError, kBreak, kSysError, kFatal;

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
# PYPLOT STYLE # 
SMALL_SIZE = 24 
MEDIUM_SIZE = 28 
BIGGER_SIZE = 32 
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels  
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels 
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels 
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize  
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title 

class LikelihoodMap():
    def __init__(self,name,xmin,ymin,xmax,ymax,N,normalize=False):
        self.xmin  = xmin
        self.ymin  = ymin
        self.xmax  = xmax
        self.ymax  = ymax
        self.N     = N    
        self.name  = name
        self.normalize = normalize # Xsec*BR*Acc
        self.nevents = 0 # count the number of events
        custom_objects =  {'PreprocessLayer': PreprocessLayer}
        self.model = Restore(os.path.join('/home/users/f/b/fbury/MoMEMtaNeuralNet/model/',name+'_HToZA.zip'),custom_objects=custom_objects).model
        #self.model = HyperModel(name,'HToZA')
        # Make directory output #
        self.path_output = os.path.join('/home/ucl/cp3/fbury/MoMEMtaNeuralNet/Plotting/PDF',self.name)
        if not os.path.exists(self.path_output):
            os.makedirs(self.path_output)
        # Get the normalization #
        if self.normalize:
            self._importGraphs()
        # Make the grid #
        self._make_grid()
        # Prepare output #
        self.Z = np.zeros(self.N) # N has chnaged because of unphysical phase space point

        ################################################
        # L(x_i|alpha)       = \prod_i 1/sigma_vis W(x_i|alpha)
        # -ln (L(x_i|alpha)) = \sum_i [ -ln(W(x_i|alpha)) + ln(sigma_vis) ]
        #                    = \sum_i [ output_DNN ] + n*ln(sigma_vis)


    def _make_grid(self):
        x = np.linspace(self.xmin,self.xmax,self.N)
        y = np.linspace(self.ymin,self.ymax,self.N)
        X,Y = np.meshgrid(x,y)
        mA = X.flatten()
        mH = Y.flatten()
        mh = 125
        mZ = 90
        # Unphysical phase-space points #
        condition1 = np.greater(mH,mA) 
        condition2 = np.greater(mH,mh) 
        condition3 = np.greater(np.subtract(mH,mA),mZ)
        #upper = np.logical_and(condition1,condition2)
        upper = np.logical_and(np.logical_and(condition1,condition2),condition3)
        # Ensure that mH > mh
        # Ensure that mH > mA
        # Ensure that mH-mA > mZ 
        self.mA = mA[upper]
        self.mH = mH[upper]
        self.N = self.mA.shape[0]

        # Normalisation with xsec visible #
        self.norm = np.ones(self.N)
        if self.normalize:
            logging.info('Normalization enabled')
            for i in range(0,self.N):
                 self.norm[i] *= self.acc.Interpolate(self.mA[i],self.mH[i])
                 #self.norm[i] *= self.xsec.Interpolate(self.mA[i],self.mH[i])
                 self.norm[i] *= self.BR_HtoZA.Interpolate(self.mA[i],self.mH[i])
                 #self.norm[i] *= self.BR_Atobb.Interpolate(self.mA[i],self.mH[i])
                 self.norm[i] *= 3.3658 * 2 / 100 # Z-> e+e- + Z-> mu+mu-
                 self.norm[i] *= 1e-12 # Xsec in pb
        # Get log(normalization) #
        self.norm = np.log10(self.norm) # if normalize == False => norm =1 => log(norm)=0 (thus not used)
        # phase space points non physical(xsec=0) -> will produce -inf 

    def AddEvent(self,event):
        # Get the -log(weight) #
        inputs = np.c_[np.tile(event,(self.N,1)),self.mH,self.mA]
        #outputs = self.model.HyperRestore(inputs)
        outputs = self.model.predict(inputs,batch_size=512)
        self.Z += outputs.reshape(-1,)
        self.nevents += 1
        
    def MakeGraph(self,title,suffix):
        self.legend_title = title.replace('.root','').replace('-','_')
        self.suffix = suffix
        if title.find('DY')!=-1:
            title = 'Drell-Yan events'
        elif title.find('TT')!=-1:
            title = r't\bar{t} events'
        else:
            mH_value = re.findall(r'\d+', title)[2]
            mA_value = re.findall(r'\d+', title)[3]
            title = 'Signal events with M_{H} = %s GeV and M_{A} = %s GeV'%(mH_value,mA_value)

        # Normalize #
        if self.normalize:
            self.Z += self.nevents*self.norm
            title += ' [Normalized]'
            self.legend_title += '_norm'

        # Divide by total entries #
        self.Z /= self.nevents # Divide by N
        self.Z *= 2 # Because -2 log L
        
        # check for invalids (nan of inf) might be coming from log10 #
        invalid_entries = np.logical_or(np.isinf(self.Z),np.isnan(self.Z))
        max_Z = np.amax(self.Z[np.invert(invalid_entries)])
        min_Z = np.amin(self.Z[np.invert(invalid_entries)])
        self.Z[invalid_entries] = 0 # removes non physical points 

        # Generate graph #
        graph = TGraph2D(self.N)
        print ('Generating TGraph2D')
        manager = enlighten.get_manager()
        pbar = manager.counter(total=self.N, desc='Progress', unit='Point')
        for i in range(self.N):
            graph.SetPoint(i,self.mA[i],self.mH[i],self.Z[i])
            pbar.update()
        manager.stop()

        #graph = copy.deepcopy(TGraph2D(self.N,self.mA,self.mH,self.Z))
        graph.SetTitle('Log-Likelihood : %s;M_{A} [GeV]; M_{H} [GeV]; -2log L'%(title))
        graph.SetMaximum(max_Z)
        graph.SetMinimum(min_Z)
        graph.SetNpx(1000)
        graph.SetNpy(1000)

        # Save graph #
        self.graph = graph
        self._saveGraph()

    def _saveGraph(self):
        full_name = self.path_output+'/likelihood_'+self.suffix+'.root'
        if os.path.exists(full_name):
            root_file = TFile(full_name,"update")
            self.graph.Write(self.legend_title,TObject.kOverwrite)
            logging.info("New Graph saved in %s"%full_name)
        else:
            root_file = TFile(full_name,"recreate")
            self.graph.Write(self.legend_title)
            logging.info("Graph replaced in %s"%full_name)

    def _importGraphs(self):
        # import the TGraphs 2D #
        path_graphs = '/home/users/f/b/fbury/MoMEMtaNeuralNet/Plotting/'
        file_xsec = TFile.Open(os.path.join(path_graphs,'XsecMap_full.root'))
        file_acc = TFile.Open(os.path.join(path_graphs,'AcceptanceMap_full.root'))

        try: # Deepcopy necessary to avoid seg fault
            self.xsec = copy.deepcopy(file_xsec.Get('Xsec'))
            self.BR_HtoZA = copy.deepcopy(file_xsec.Get('BR_HtoZA'))
            self.BR_Atobb = copy.deepcopy(file_xsec.Get('BR_Atobb'))
            self.BR_Ztoll = copy.deepcopy(file_xsec.Get('BR_Ztoll'))
            self.acc = copy.deepcopy(file_acc.Get('Acceptance'))
        except:
            self.normalize = False
            logging.warning ('Could not load the Objects -> normalization off')

        if not isinstance(self.xsec,ROOT.TGraph2D):
            self.normalize = False
            logging.warning ('Xsec is %s and not TGraph2D -> normalization off'%type(self.xsec))
        if not isinstance(self.BR_HtoZA,ROOT.TGraph2D):
            self.normalize = False
            logging.warning ('BR_HtoZA is %s and not TGraph2D -> normalization off'%type(self.BR_HtoZA))
        if not isinstance(self.BR_Atobb,ROOT.TGraph2D):
            self.normalize = False
            logging.warning ('BR_Atobb is %s and not TGraph2D -> normalization off'%type(self.BR_Atobb))
        if not isinstance(self.BR_Ztoll,ROOT.TGraph2D):
            self.normalize = False
            logging.warning ('BR_Ztoll is %s and not TGraph2D -> normalization off'%type(self.BR_Ztoll))
        if not isinstance(self.acc,ROOT.TGraph2D):
            self.normalize = False
            logging.warning ('Acceptance is %s and not TGraph2D -> normalization off'%type(self.acc))

#################################################################################################
# FindSigma #
#################################################################################################

def FindSigma(x,y,frac):
    from scipy.optimize import curve_fit
    def f(x,a,b,c):
        return a*x**2+b*x+c
    # Find minimum index #
    idxmin = np.argmin(y)
    # Select part of the data for the fit in the middle #
    N = x.shape[0]
    selection = np.arange(max(idxmin-round(N*frac),0),min(idxmin+round(N*frac),N))

    x = x[selection]
    y = y[selection]
    # Fit with the polnym #
    popt, pcov = curve_fit(f, x, y)
    print (popt)
    # Get coefficients #
    a = popt[0]
    b = popt[1]
    c = popt[2]
    # Find minimum #
    xmin = -b/(2*a)
    ymin = f(xmin,*popt)
    print ('Xmin = ',xmin)
    print ('Ymin = ',ymin)
    # Find x1, x2 such that f(x) = 1 #
    #discriminant  = b**2-4*a*1000/2
    discriminant  = 4*a*1
    x1 = (-b-math.sqrt(discriminant))/(2*a)
    x2 = (-b+math.sqrt(discriminant))/(2*a)
    print ('Resolution = ',abs(x1-x2))
    return abs(x1-x2),x,f(x,*popt)

#################################################################################################
# MakeProfile #
#################################################################################################

def MakeProfile(graph,mH,mA,N,path,step=10,slices=10):
    """
    Make the profile in both axes (mH and mA as variables) with several values ont the other axis
    graph       = TGraph2D to be used for the profile
    mH          = masses of H
    mA          = masses of A
    N           = number of points for interpolation
    path        = output path as string
    step        = step as increment in the parameters
    slices      = number of different values in each plot
    """
    # Get the profile along mA #
    x = np.linspace(mA*0.85,mA*1.15,N)
    mH_slice = np.linspace(mH-round(slices/2)*step,mH+round(slices/2)*step,slices if slices%2==1 else slices+1)
    out_x = np.zeros((N,mH_slice.shape[0])) # columns = mH values

    print ('Computing the curves for mA')
    # Interpolate at fixed mH #
    for j in range(mH_slice.shape[0]): # Loop across mH values
        for i in range(N): # Loop over axis
            out_x[i,j] = graph.Interpolate(x[i],mH_slice[j])
            if out_x[i,j] == 0: # avoid artifacts
                out_x[i,j] = out_x[i-1,j]
    out_x[:,:] -= np.amin(out_x[:,:]) # shift at 0

    # Get the slices along mH #
    y = np.linspace(mH*0.90,mH*1.10,N)
    mA_slice = np.linspace(mA-round(slices/2)*step,mA+round(slices/2)*step,slices if slices%2==1 else slices+1)
    out_y = np.zeros((N,mA_slice.shape[0])) # columns = mA values

    print ('Computing the curves for mH')
    # Interpolate at fixed mA #
    for j in range(mA_slice.shape[0]): # Loop across mA values
        for i in range(N): # Loop over axis
            out_y[i,j] = graph.Interpolate(mA_slice[j],y[i])
            if out_y[i,j] == 0:   # avoid artifacts
                out_y[i,j] = out_y[i-1,j]
    out_y[:,:] -= np.amin(out_y[:,:]) # shift at 0

    # Get envelope #
    print ('Getting the envelopes')
    envelope_mA = np.zeros(N)
    envelope_mH = np.zeros(N)
    for i in range(N):
        envelope_mA[i] = np.amin(out_x[i,:])
        envelope_mH[i] = np.amin(out_y[i,:])

    # Plot #
    fig = plt.figure(figsize=(25,12))
    plt.subplots_adjust(left=0.08, bottom=0.1, right=0.95, top=0.85, wspace=0.18, hspace=None)
    ax1 = fig.add_subplot(121) 
    ax2 = fig.add_subplot(122) 

    color = iter(cm.seismic(np.linspace(0,1,mA_slice.shape[0])))
    print ('Plotting mA')
    # Loop over curves # 
    for j in range(mH_slice.shape[0]): # Loop across mH values
        # Find resolution at 1sigma #
        print ((' Slice mH = %d GeV '%(mH_slice[j])).center(50,'-'))
        c=next(color)
        try:
            res,x_fit,y_fit = FindSigma(x,out_x[:,j],frac=0.25)
            ax1.plot(x_fit,y_fit,color=c,linestyle='--')
        except Exception as e:
            print ('[ERROR] : %s'%e)
            res = 0
        # Plot
        if mH_slice[j] == mH:
            c = 'darkgreen'
        ax1.plot(x,out_x[:,j],label='$M_{H}$ = %d GeV (Resolution = %0.2f GeV)'%(mH_slice[j],res),color=c)
    # Plot and resolution of envelope #
    try:
        res_envelope_mA, x_fit_envelope_mA, y_fit_envelope_mA, = FindSigma(x,envelope_mA,frac=0.25) 
        ax1.plot(x,envelope_mA,label='Envelope (Resolution = %0.2f GeV)'%(res_envelope_mA),color='k')
        ax1.plot(x_fit_envelope_mA,y_fit_envelope_mA,color='k',linestyle='--')
    except Exception as e:
        print ('[ERROR] : %s'%e)

    ax1.legend(loc='upper right',prop={'size': 14})
    ax1.set_ylim(0)
    ax1.set_xlabel('$M_{A}$')
    ax1.set_ylabel('-2log L')
    ax1.set_title('Profile likelihood in $M_{A}$')

    color = iter(cm.seismic(np.linspace(0,1,mA_slice.shape[0])))
    print ('Plotting mH')
    for j in range(mA_slice.shape[0]): # Loop across mA values
        c=next(color)
        # Find resolution at 1sigma #
        print ((' Slice mA = %d GeV '%(mA_slice[j])).center(50,'-'))
        try:
            res,x_fit,y_fit = FindSigma(y,out_y[:,j],frac=0.30)
            ax2.plot(x_fit,y_fit,color=c,linestyle='--')
        except Exception as e:
            print ('[ERROR] : %s'%e)
            res = 0
        # Plot #
        if mA_slice[j] == mA:
            c = 'darkgreen'
        ax2.plot(y,out_y[:,j],label='$M_{A}$ = %d GeV (Resolution = %0.2f GeV)'%(mA_slice[j],res),color=c)
    # Plot and resolution of envelope #
    try:
        res_envelope_mH, x_fit_envelope_mH, y_fit_envelope_mH, = FindSigma(y,envelope_mH,frac=0.30) 
        ax2.plot(y,envelope_mH,label='Envelope (Resolution = %0.2f GeV)'%(res_envelope_mH),color='k')
        ax2.plot(x_fit_envelope_mH,y_fit_envelope_mH,color='k',linestyle='--')
    except Exception as e:
        print ('[ERROR] : %s'%e)
 
    ax2.legend(loc='upper right',prop={'size': 14})
    ax2.set_ylim(0)
    ax2.set_xlabel('$M_{H}$')
    ax2.set_ylabel('-2log L')
    ax2.set_title('Profile likelihood in $M_{H}$')

    fig.suptitle('Profile likelihood for events with $M_{H}$ = %d GeV and $M_{A}$ = %d GeV'%(mH,mA))

    name = os.path.join(path,'profile_likelihood_mH_%d_mA_%d.png'%(mH,mA))
    fig.savefig(name)
    print ('Figure saved as %s'%name)


            

def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='From given set of root files, make different histograms in a root file')
    parser.add_argument('-m','--model', action='store', required=True, type=str, default='',
                  help='NN model to be used')
    parser.add_argument('-f','--file', action='store', required=False, type=str, default='',
                  help='File (full path) to be used')
    parser.add_argument('--mA',action='store', required=False, type=int, default=0,
                  help='Print as PDf only some of the mass config')
    parser.add_argument('--mH',action='store', required=False, type=int, default=0,
                  help='Print as PDf only some of the mass config')
    parser.add_argument('-n','--number', action='store', required=False, type=int, default=0,
                  help='Number of events to build the likelihood map')
    parser.add_argument('--xmax', action='store', required=False, type=float, default=1500,
                  help='Maximum values for mA in the graph')
    parser.add_argument('--ymax', action='store', required=False, type=float, default=1500,
                  help='Maximum values for mH in the graph')
    parser.add_argument('--xmin', action='store', required=False, type=float, default=0,
                  help='Minimum values for mA in the graph')
    parser.add_argument('--ymin', action='store', required=False, type=float, default=0,
                  help='Minimum values for mH in the graph')
    parser.add_argument('--zmin', action='store', required=False, type=float, default=0,
                  help='Minimum values for z axis in the graph')
    parser.add_argument('--zmax', action='store', required=False, type=float, default=None,
                  help='Maximum values for z axis in the graph')
    parser.add_argument('--bins', action='store', required=False, type=int, default=100,
                  help='Bins in both the graph axes')
    parser.add_argument('--suffix', action='store', required=False, type=str, default='',
                  help='Suffix to be added to output name (likelihood_suffix.pdf/.root), default to empty string')
    parser.add_argument('--PDF', action='store_true', required=False, default=False,
            help='Produce PDF from the root file')
    parser.add_argument('--profile', action='store_true', required=False, default=False,
            help='Whether to make the profile likelihood starting from the TGraph2D')
    parser.add_argument('--zoom', action='store_true', required=False, default=False,
            help='Zoom the TGraph2D according to given boundaries')
    parser.add_argument('--norm', action='store_true', required=False, default=False,
            help='Use the normalization by the visible cross section')
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
    # Get objects in TFile #
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

    #############################################################################################
    # Profile Likelihood #
    #############################################################################################
    if opt.profile:
        # Path to graph #
        path_root = os.path.abspath(os.path.join('PDF',opt.model,'likelihood_'+opt.suffix+'.root')) 
        path_out = os.path.abspath(os.path.join('PDF',opt.model))
        # Load TGraph2D #
        f = TFile(path_root)
        graphs = [(key,obj) for (key,obj) in getall(f)]
        for  key,obj in graphs:
            if key.find('HToZA')==-1:
                continue
            mH_value = int(re.findall(r'\d+', key)[2])
            mA_value = int(re.findall(r'\d+', key)[3])
            
            if mH_value != opt.mH or mA_value != opt.mA:
                continue

            MakeProfile(graph = obj,
                      mH = mH_value,
                      mA = mA_value,
                      N = 10000,
                      path = path_out,
                      step = 5,
                      slices=10)
        sys.exit(0)

    #############################################################################################
    # Make PDF #
    #############################################################################################
    def ZoomHist(graph,bins,xmin,xmax,ymin,ymax):
        x = np.linspace(xmin,xmax,bins)
        y = np.linspace(ymin,ymax,bins)
        X,Y = np.meshgrid(x,y)
        X = X.ravel()
        Y = Y.ravel()
        valid = np.logical_and(np.greater_equal(Y,X),np.greater_equal(Y,125))
        X = X[valid]
        Y = Y[valid]
        N = X.shape[0]
        new_graph = TGraph2D(N)
        manager = enlighten.get_manager() 
        pbar = manager.counter(total=N, desc='Progress', unit='Point')
        for i in range(N):
            content  = graph.Interpolate(X[i],Y[i])
            if content != 0 or Y[i]>125:
                new_graph.SetPoint(i,X[i],Y[i],content)
            pbar.update()
        new_graph.SetTitle(graph.GetTitle())
        return copy.deepcopy(new_graph)


    if opt.PDF or opt.zoom:
        path_root = os.path.abspath(os.path.join('PDF',opt.model,'likelihood_'+opt.suffix+'.root'))
        path_pdf  = os.path.abspath(os.path.join('PDF',opt.model,'likelihood_'+opt.suffix+'.pdf'))
        path_zoom = os.path.abspath(os.path.join('PDF',opt.model,'likelihood_'+opt.suffix+'_zoom.root'))
        f = TFile(path_root)
        if opt.PDF:
            c1 = TCanvas('c1','c1',1100,900)
            c1.SetGrid()
            #canvas = TCanvas('canvas','canvas',900,900)
            #canvas.Print(path_pdf+'[')
            c1.Print(path_pdf+'[')
            c1.SetTopMargin(0.05)
            c1.SetBottomMargin(0.18)
            c1.SetLeftMargin(0.18)
            c1.SetRightMargin(0.2)
        graphs = [(key,obj) for (key,obj) in getall(f)]
        graphs = sorted(graphs, key=lambda tup: tup[0]) # Sort according to name
        for  i,(key,obj) in enumerate(graphs):
            mH_value = 0
            mA_value = 0
            if key.find('DY')!=-1:
                title = 'DY'
            elif key.find('TT')!=-1:
                title = 'TT'
            else:
                mH_value = int(re.findall(r'\d+', key)[2])
                mA_value = int(re.findall(r'\d+', key)[3])
                title = 'HToZATo2L2B_mH_%d_mA_%d'%(mH_value,mA_value)

            if (mH_value != opt.mH or mA_value != opt.mA) and opt.mA != 0 and opt.mH != 0:
                continue
            logging.info('Processing %s'%key)
            try:
                if opt.zoom:
                    new_graph = ZoomHist(obj,opt.bins,opt.xmin,opt.xmax,opt.ymin,opt.ymax) 
                    if os.path.exists(path_zoom):
                        root_file = TFile(path_zoom,"update")
                        new_graph.Write(title,TObject.kOverwrite)
                        logging.info("Zoomed Graph saved in %s"%path_zoom)
                    else:
                        root_file = TFile(path_zoom,"recreate")
                        new_graph.Write(title)
                        logging.info("Zoomed Graph replaced in %s"%path_zoom)


                if opt.PDF:
                    base_hist = TH2F('','',opt.bins,opt.xmin,opt.xmax,opt.bins,opt.ymin,opt.ymax) 
                    obj.SetHistogram(base_hist)
                    hist = obj.GetHistogram()
                    hist.SetContour(1000)
                    hist.GetXaxis().SetRangeUser(opt.xmin,opt.xmax)
                    hist.GetYaxis().SetRangeUser(opt.ymin,opt.ymax)
                    hist.SetMinimum(max(opt.zmin,hist.GetMinimum()))
                    amax = hist.GetMaximum() if opt.zmax is None else opt.zmax 
                    hist.SetMaximum(amax)
                    hist.SetTitle(";M_{A} [GeV];M_{H} [GeV];-2 log L")
                    hist.GetXaxis().SetTitleOffset(1.2)
                    hist.GetYaxis().SetTitleOffset(1.2)
                    hist.GetZaxis().SetTitleOffset(1.2)
                    hist.GetXaxis().SetLabelSize(0.04)
                    hist.GetYaxis().SetLabelSize(0.04)
                    hist.GetZaxis().SetLabelSize(0.04)
                    hist.GetXaxis().SetTitleSize(0.06)
                    hist.GetYaxis().SetTitleSize(0.06)
                    hist.GetZaxis().SetTitleSize(0.06)
                    hist.Draw('colz') 
                    text = TPaveText(.55,.2,.80,.4,'brNDC')
                    text.AddText("Events with")
                    text.AddText("M_{A} = %d GeV"%mA_value)
                    text.AddText("M_{H} = %d GeV"%mH_value)
                    text.SetTextColor(1)
                    text.SetFillStyle(4100)
                    text.Draw("same")


                    #hist.SetTitle(obj.GetTitle())
                    c1.Print(path_pdf,'Title:'+key.replace('.root','').replace('/',''))
            except Exception as e:
                logging.critical('Could not save %s due to error "%s"'%(key,e))
        if opt.PDF:
#            canvas.Print(path_pdf) 
#            canvas.Print(path_pdf+']') 
            logging.info('PDF saved as %s'%path_pdf)
            c1.Print(path_pdf+']') 

        sys.exit()
    #############################################################################################
    # Make likelihood map #
    #############################################################################################
    # Get events from tree #
    logging.info('Looking at file %s'%opt.file)
    variables  = [
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

    events = Tree2Pandas(input_file=opt.file, variables=variables, n=opt.number).values
    if events.shape[0] == 0:
        raise RuntimeError("Did you forget -n ?")

    # Instantiate the map #
    likelihood = LikelihoodMap(name = opt.model,
                               xmin = opt.xmin,
                               ymin = opt.ymin,
                               xmax = opt.xmax,
                               ymax = opt.ymax,
                               N    = 300,
                               normalize=opt.norm)

    # Loop over events #
    logging.info('Adding events')
    manager = enlighten.get_manager()
    pbar = manager.counter(total=opt.number, desc='Progress', unit='Event')
    for i in range(events.shape[0]):
        likelihood.AddEvent(events[i,:])
        pbar.update()
    manager.stop()

    # Make and print map #
    likelihood.MakeGraph(title=os.path.basename(opt.file),suffix=opt.suffix)


    


if __name__ == "__main__":
    main()   
