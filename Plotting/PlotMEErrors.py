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
            'GPU_6x200_elu_500epochs' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_6x200_elu_500epochs_batchNorm/ME_generator_weights/All.root',
            'GPU_8x500_elu_200epochs' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_8x500_elu_200epochs_withBatchNorm/ME_generator_weights/All.root',
            'GPU_10x200_elu_300epochs' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_10x200_elu_300epochs_batchNorm/ME_generator_weights/All.root',
            'GPU_10x200_elu_1000epochs' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_10x200_elu_1000epochs_batchNorm/ME_generator_output_weights/All.root',
            'GPU_10x200_elu_300epochs Curriculum Learning' : '/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput/GPU_10x200_elu_300epochs_batchNorm_CLHard200EpochsThenEasy200Epochs/ME_generator_output_weights/All.root'
                         }
        self.graph_dict = {}

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
        for name,filepath in self.path_dict.items():
            print ("Looking at file %s (name %s)"%(filepath,name))
            h = self.makeErrorHist(filepath)
            self.graph_dict[name] = copy.deepcopy(self.makeErrorGraph(h))

    def makePlot(self):
        tdrstyle.setTDRStyle()
        C = ROOT.TCanvas("C","C",800,600)
        legend = ROOT.TLegend(0.5,0.2,0.8,0.7)
        legend.SetHeader("Legend","C")                      
        C.cd()
        print ("makePlot")
        for i,(name,graph) in enumerate(self.graph_dict.items()):
            print (name)
            legend.AddEntry(graph,name,"l")
            graph.SetLineColor(i+2) 
            graph.SetLineWidth(2) 
            if i == 0:
                graph.SetTitle("Error graph;Error in orders of magnitude;Fraction of events")
                graph.Draw()
            else:
                graph.Draw("same")

        legend.Draw()
        C.Draw()
        #input("Type to exit")
        C.Print("errorPlot.png")
            
if __name__ == '__main__':
    instance = errorPlots()
    instance.loopOverFiles()
    instance.makePlot()
