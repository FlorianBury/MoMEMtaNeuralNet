import os
import sys
import argparse
import glob
import logging
import copy
import numpy as np
import enlighten

sys.path.insert(0,"..") # We need our own version of talos
                        # If we import our modules after the version is sites-package our versionis ignored
from NeuralNet import HyperModel
from import_tree import Tree2Pandas
import parameters

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
        inputs = np.c_[np.tile(event,(self.N**2,1)),self.mA,self.mH]
        outputs = self.model.HyperRestore(inputs)
        self.Z += outputs.reshape(-1,)

    def MakeGraph(self,title):
        self.title = title.replace('.root','')
        graph = copy.deepcopy(TGraph2D(self.N**2,self.mA,self.mH,self.Z))

        graph.SetTitle('Log-Likelihood : %s;M_{A} [GeV]; M_{H} [GeV]; -\sum_{i=1}^{n} log(L)'%self.title)
        graph.GetXaxis().SetTitleOffset(1.3)
        graph.GetYaxis().SetTitleOffset(1.3)
        graph.GetZaxis().SetTitleOffset(3)
        graph.SetNpx(1000)
        graph.SetNpy(1000)

        self.graph = graph

    def SaveOnCanvas(self):
        canvas = TCanvas(self.title, self.title, 800, 600)
        self.graph.Draw("colz")

        full_name = self.path_output+"/likelihood.root"
        if os.path.exists(full_name):
            root_file = TFile(full_name,"update")
            canvas.Write("",TObject.kOverwrite)
        else:
            root_file = TFile(full_name,"recreate")
            canvas.Write()
            
        logging.info("Canvas saved as %s"%full_name)

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
            logging.info('Processing %s'%key)
            
            obj.SetTopMargin(0.1)
            obj.SetBottomMargin(0.15)
            obj.SetLeftMargin(0.15)
            obj.SetRightMargin(0.2)
            obj.Print(path_pdf,'Title:'+key.replace('.root','').replace('/',''))
        canvas.Print(path_pdf+']') 

        sys.exit()
    #############################################################################################
    # Make likelihood map #
    #############################################################################################
    # Get events from tree #
    events = Tree2Pandas(input_file=opt.file, variables=parameters.inputs, n=opt.number).values

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
    likelihood.SaveOnCanvas()


    


if __name__ == "__main__":
    main()   
