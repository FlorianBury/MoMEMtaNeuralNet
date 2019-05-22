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
from NeuralNet import HyperModel
from import_tree import Tree2Pandas

import ROOT
from ROOT import TFile, TH1F, TH2F, TCanvas, gROOT, TGraph2D, gPad, TObject
import CMS_lumi
import tdrstyle


gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = 2000#[ROOT.kPrint, ROOT.kInfo]#, kWarning, kError, kBreak, kSysError, kFatal;

class LikelihoodMap():
    def __init__(self,name,xmin,ymin,xmax,ymax,N):
        self.xmin  = xmin
        self.ymin  = ymin
        self.xmax  = xmax
        self.ymax  = ymax
        self.N     = N    
        self.name  = name
        self.model = HyperModel(name,'HToZA')
        # Make the grid #
        self._make_grid()
        # Prepare output #
        self.Z = np.zeros(N**2)
        # Make directory output #
        self.path_output = os.path.join('PDF',self.name)
        if not os.path.exists(self.path_output):
            os.makedirs(self.path_output)

    def _make_grid(self):
        x = np.linspace(self.xmin,self.xmax,self.N)
        y = np.linspace(self.ymin,self.ymax,self.N)
        X,Y = np.meshgrid(x,y)
        self.mA = X.flatten()
        self.mH = Y.flatten()

    def AddEvent(self,event):
        inputs = np.c_[np.tile(event,(self.N**2,1)),self.mH,self.mA]
        outputs = self.model.HyperRestore(inputs)
        self.Z += outputs.reshape(-1,)

    def MakeGraph(self,title):
        self.title = title.replace('.root','')
        if title.find('DY')!=-1:
            title = 'Drell-Yann events'
        elif title.find('TT')!=-1:
            title = r't\bar{t} events'
        else:
            mH_value = re.findall(r'\d+', title)[2]
            mA_value = re.findall(r'\d+', title)[3]
            title = 'Signal events with M_{H} = %s GeV and M_{A} = %s GeV'%(mH_value,mA_value)

        graph = copy.deepcopy(TGraph2D(self.N**2,self.mA,self.mH,self.Z))
        graph.SetTitle('Log-Likelihood : %s;M_{A} [GeV]; M_{H} [GeV]; -\sum_{i=1}^{n} log(L)'%(title))
        graph.SetNpx(1000)
        graph.SetNpy(1000)

        self.graph = graph
        self._saveGraph()

    def _saveGraph(self):
        full_name = self.path_output+"/likelihood.root"
        if os.path.exists(full_name):
            root_file = TFile(full_name,"update")
            self.graph.Write(self.title,TObject.kOverwrite)
            logging.info("New Graph saved in %s"%full_name)
        else:
            root_file = TFile(full_name,"recreate")
            self.graph.Write(self.title)
            logging.info("Graph replaced in %s"%full_name)
            

def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='From given set of root files, make different histograms in a root file')
    parser.add_argument('-m','--model', action='store', required=True, type=str, default='',
                  help='NN model to be used')
    parser.add_argument('-f','--file', action='store', required=False, type=str, default='',
                  help='File (fulle path) to be used')
    parser.add_argument('-n','--number', action='store', required=False, type=int, default=0,
                  help='Number of events to build the likelihood map')
    parser.add_argument('--max', action='store', required=False, type=int, default=1000,
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
        path_root = os.path.join('PDF',opt.model,'likelihood.root')
        path_pdf  = os.path.join('PDF',opt.model,'likelihood.pdf')
        f = TFile(path_root)
        canvas = TCanvas()
        canvas.Print(path_pdf+'[')
        for i, (key,obj) in enumerate(getall(f)):
            c1 = TCanvas()
            c1.SetGrid()
            logging.info('Processing %s'%key)
            hist = obj.GetHistogram()
            hist.SetContour(100)
            hist.Draw('colz') 
            c1.SetTopMargin(0.1)
            c1.SetBottomMargin(0.12)
            c1.SetLeftMargin(0.12)
            c1.SetRightMargin(0.18)
            hist.GetXaxis().SetTitleOffset(1.3)
            hist.GetYaxis().SetTitleOffset(1.3)
            hist.GetZaxis().SetTitleOffset(1.5)
            c1.Print(path_pdf,'Title:'+key.replace('.root','').replace('/',''))
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

    events = Tree2Pandas(input_file=opt.file, variables=parameters, n=opt.number).values

    # Instantiate the map #
    likelihood = LikelihoodMap(name = opt.model,
                               xmin = 0,
                               ymin = 0,
                               xmax = opt.max,
                               ymax = opt.max,
                               N    = 100)

    # Loop over events #
    manager = enlighten.get_manager()
    pbar = manager.counter(total=opt.number, desc='Progress', unit='Event')
    for i in range(events.shape[0]):
        likelihood.AddEvent(events[i,:]) 
        pbar.update()
    manager.stop()

    # Make and print map #
    likelihood.MakeGraph(title=os.path.basename(opt.file))


    


if __name__ == "__main__":
    main()   
