import os
import sys
import re
import argparse
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
from ROOT import TFile, TH1F, TH2F, TCanvas, gROOT, TGraph2D, gPad, TObject, gStyle
import CMS_lumi
import tdrstyle


gROOT.SetBatch(True)
gStyle.SetOptStat(0)
ROOT.gErrorIgnoreLevel = 2000#[ROOT.kPrint, ROOT.kInfo]#, kWarning, kError, kBreak, kSysError, kFatal;

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
        self.norm = np.ones(self.mA.shape[0])
        if self.normalize:
            logging.info('Normalization enabled')
            for i in range(0,self.mH.shape[0]):
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
        self.legend_title = title.replace('.root','')
        self.suffix = suffix
        if title.find('DY')!=-1:
            title = 'Drell-Yann events'
        elif title.find('TT')!=-1:
            title = r't\bar{t} events'
        else:
            mH_value = re.findall(r'\d+', title)[2]
            mA_value = re.findall(r'\d+', title)[3]
            title = 'Signal events with M_{H} = %s GeV and M_{A} = %s GeV'%(mH_value,mA_value)

        # Normalize #
        if self.normalize:
            save_Z = copy.deepcopy(self.Z)
            self.Z += self.nevents*self.norm
            title += ' [Normalized]'
            self.legend_title += ' [Normalized]'
        
        # check for invalids (nan of inf) might be coming from log10 #
        invalid_entries = np.logical_or(np.isinf(self.Z),np.isnan(self.Z))
        max_Z = np.amax(self.Z[np.invert(invalid_entries)])
        min_Z = np.amin(self.Z[np.invert(invalid_entries)])
        self.Z[invalid_entries] = 0 # removes non physical points 

        # Generate graph #
        graph = copy.deepcopy(TGraph2D(self.N,self.mA,self.mH,self.Z))
        graph.SetTitle('Log-Likelihood : %s;M_{A} [GeV]; M_{H} [GeV]; -log(L)'%(title))
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
            

def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='From given set of root files, make different histograms in a root file')
    parser.add_argument('-m','--model', action='store', required=True, type=str, default='',
                  help='NN model to be used')
    parser.add_argument('-f','--file', action='store', required=False, type=str, default='',
                  help='File (full path) to be used')
    parser.add_argument('--mA',action='store', required=False, type=str, default='',
                  help='Print as PDf only some of the mass config')
    parser.add_argument('--mH',action='store', required=False, type=str, default='',
                  help='Print as PDf only some of the mass config')
    parser.add_argument('-n','--number', action='store', required=False, type=int, default=0,
                  help='Number of events to build the likelihood map')
    parser.add_argument('--xmax', action='store', required=False, type=int, default=1500,
                  help='Maximum values for mA in the graph')
    parser.add_argument('--ymax', action='store', required=False, type=int, default=1500,
                  help='Maximum values for mH in the graph')
    parser.add_argument('--xmin', action='store', required=False, type=int, default=0,
                  help='Minimum values for mA in the graph')
    parser.add_argument('--ymin', action='store', required=False, type=int, default=0,
                  help='Minimum values for mH in the graph')
    parser.add_argument('--zmin', action='store', required=False, type=int, default=0,
                  help='Minimum values for z axis in the graph')
    parser.add_argument('--zmax', action='store', required=False, type=int, default=None,
                  help='Maximum values for z axis in the graph')
    parser.add_argument('--bins', action='store', required=False, type=int, default=100,
                  help='Bins in both the graph axes')
    parser.add_argument('--suffix', action='store', required=False, type=str, default='',
                  help='Suffix to be added to output name (likelihood_suffix.pdf/.root), default to empty string')
    parser.add_argument('--PDF', action='store_true', required=False, default=False,
            help='Produce PDF from the root file')
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

    def findMinMaxInRange(hist,xmin,xmax,ymin,ymax):
        zmin = 1000000
        zmax = 0
        for x in range(hist.GetXaxis().FindBin(xmin),hist.GetXaxis().FindBin(xmax)+1):
            for y in range(hist.GetYaxis().FindBin(ymin),hist.GetYaxis().FindBin(ymax)):
                content = hist.GetBin(x,y)
                if content > zmax: zmax = content
                if content < zmin: zmin = content
                #print (x,y,num,hist.GetXaxis().GetBinLowEdge(num),hist.GetYaxis().GetBinLowEdge(num))
        print (zmin,zmax)
        return zmin,zmax

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
            canvas = TCanvas()
            canvas.Print(path_pdf+'[')
        graphs = [(key,obj) for (key,obj) in getall(f)]
        graphs = sorted(graphs, key=lambda tup: tup[0]) # Sort according to name
        for  i,(key,obj) in enumerate(graphs):
            if key.find(opt.mA)==-1 or key.find(opt.mH)==-1:
                continue
            logging.info('Processing %s'%key)

            if key.find('DY')!=-1:
                title = 'DY'
            elif key.find('TT')!=-1:
                title = 'TT'
            else:
                mH_value = int(re.findall(r'\d+', key)[2])
                mA_value = int(re.findall(r'\d+', key)[3])
                title = 'HToZATo2L2B_mH_%d_mA_%d'%(mH_value,mA_value)

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
                    c1 = TCanvas()
                    c1.SetGrid()
                    base_hist = TH2F('','',opt.bins,opt.xmin,opt.xmax,opt.bins,opt.ymin,opt.ymax) 
                    obj.SetHistogram(base_hist)
                    hist = obj.GetHistogram()
                    hist.SetContour(1000)
                    hist.GetXaxis().SetRangeUser(opt.xmin,opt.xmax)
                    hist.GetYaxis().SetRangeUser(opt.ymin,opt.ymax)
                    hist.SetMinimum(opt.zmin)
                    amax = hist.GetMaximum() if opt.zmax is None else opt.zmax 
                    hist.SetMaximum(amax)
                    hist.Draw('colz') 
                    c1.SetTopMargin(0.1)
                    c1.SetBottomMargin(0.12)
                    c1.SetLeftMargin(0.12)
                    c1.SetRightMargin(0.18)
                    hist.GetXaxis().SetTitleOffset(1.3)
                    hist.GetYaxis().SetTitleOffset(1.3)
                    hist.GetZaxis().SetTitleOffset(1.5)
                    hist.SetTitle(obj.GetTitle())
                    c1.Print(path_pdf,'Title:'+key.replace('.root','').replace('/',''))
            except Exception as e:
                logging.critical('Could not save %s due to error "%s"'%(key,e))
        if opt.PDF:
            canvas.Print(path_pdf) 
            canvas.Print(path_pdf+']') 
            logging.info('PDF saved as %s'%path_pdf)

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

    # Instantiate the map #
    likelihood = LikelihoodMap(name = opt.model,
                               xmin = opt.xmin,
                               ymin = opt.xmax,
                               xmax = opt.xmax,
                               ymax = opt.ymax,
                               N    = 100,
                               normalize=opt.norm)

    # Loop over events #
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
