import os
import sys
import copy
import ROOT

import tdrstyle
        
ROOT.gStyle.SetOptStat(True)
ROOT.gROOT.SetBatch(True)

class errorPlots:
    def __init__(self):
        self.path_dict = {
            'GPU 6x200 500 epochs' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_6x200_elu_500epochs_batchNorm/ME_generator_weights/All.root',
            'GPU 8x500 300 epochs' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_8x500_elu_300epochs_withBatchNorm/ME_generator_weights/All.root',
            'GPU 8x500 200 epochs (reweighted)' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_8x500_elu_200epochs_batchNorm_weighted/ME_generator_weights/All.root',
            'GPU 6x200 200 epochs (reweighted clip 100)' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_6x200_elu_200epochs_batchNorm_weightedClip100/ME_generator_weights/All.root',
            'GPU 6x200 200 epochs (reweighted clip 10)' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_6x200_elu_200epochs_batchNorm_weightedClip10/ME_generator_weights/All.root',
            'GPU 10x200 1000 epochs' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_10x200_elu_1000epochs_batchNorm/ME_generator_output_weights/All.root',
            'GPU 10x200 2x200 epochs (4-momentas) CL (hard->easy)' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_10x200_elu_300epochs_batchNorm_CLHard200EpochsThenEasy200Epochs/ME_generator_output_weights/All.root',
            #'GPU_10x200_elu_300epochs_batchNorm_newvar' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_10x200_elu_300epochs_batchNorm_newvar/ME_generator_output_weights/All.root',
            'GPU 10x200 1000 epochs (Pt,Eta,Phi)' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_10x200_elu_1000epochs_batchNorm_newvar/ME_generator_output_weights/All.root',
            'GPU_10x200 200 epochs (Pt,Eta,Phi + SP + IM)' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_10x200_elu_200epochs_batchNorm_newvar2/ME_generator_output_weights/All.root',
                         }
        self.mg = ROOT.TMultiGraph()

    def makeErrorGraph(self,h):   
        graph = ROOT.TGraph(int(h.GetEntries()))
        for i in range(1,h.GetNbinsX()+1):
            cont = 0
            for j in range(1,i+1):
                cont += h.GetBinContent(j)
            cont /= h.GetEntries()
            graph.SetPoint(i-1,h.GetBinLowEdge(i),cont)
        return graph

    def makeErrorHist(self,filepath):   
        f = ROOT.TFile(filepath)
        t = f.Get("tree")
        t.Draw("abs(log10(MEPdf)-log10(output_ME))>>h(1000,0,5)")
        h = copy.deepcopy(ROOT.gROOT.FindObject("h"))
        f.Close()

        return h

    def loopOverFiles(self):
        for i,(name,filepath) in enumerate(self.path_dict.items()):
            print ("Looking at file %s (name %s)"%(filepath,name))
            h = self.makeErrorHist(filepath)
            g = self.makeErrorGraph(h)
            g.SetLineColor(i+1)
            g.SetLineWidth(2)
            g.SetTitle(name)
            self.mg.Add(g)

    def makePlot(self):
        #tdrstyle.setTDRStyle()
        C = ROOT.TCanvas("C","C",800,600)
        C.cd()
        C.SetGrid()
        self.mg.SetTitle("Error graph;Error in orders of magnitude (|log_{10}(ME^{True})-log_{10}(ME^{DNN})|);Fraction of events")
        self.mg.Draw("AL")

        legend = C.BuildLegend(0.4,0.15,0.85,0.6,"Legend","" )
        #legend.SetBorderSize(0)
        #legend.SetFillStyle(1)
        legend.Draw()
        #C.Draw()
        #input("Type to exit")
        C.Print("errorPlot.png")
            
if __name__ == '__main__':
    instance = errorPlots()
    instance.loopOverFiles()
    instance.makePlot()
