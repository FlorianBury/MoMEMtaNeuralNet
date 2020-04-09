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
            'GPU 10x200 (Px,Py,Pz,E)' : ('/nfs/scratch/fynu/fbury/MoMEMta_output/NNOutput/GPU_10x200_elu_300epochs_batchNorm_v2/ME_generator_output_weights/All.root',602),
            'GPU 10x200 (Pt,Eta,Phi)' : ('/nfs/scratch/fynu/fbury/MoMEMta_output/NNOutput/GPU_10x200_elu_300epochs_batchNorm_newvar_v2/ME_generator_output_weights/All.root',634),
            'GPU 10x200 (Pt,Eta,Phi + SP + IM)' : ('/nfs/scratch/fynu/fbury/MoMEMta_output/NNOutput/GPU_10x200_elu_300epochs_batchNorm_newvar2_v2/ME_generator_output_weights/All.root',418),
            'GPU 10x200 (Pt + SP + IM)' : ('/nfs/scratch/fynu/fbury/MoMEMta_output/NNOutput/GPU_10x200_elu_300epochs_batchNorm_newvar3_v2/ME_generator_output_weights/All.root',799),
                         }
        self.mg = ROOT.TMultiGraph()
        self.dict_hist = {}

    def makeErrorGraph(self,h):   
        graph = ROOT.TGraph(int(h.GetNbinsX()))
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
        t.Draw("abs(log10(MEPdf)-log10(output_ME))>>h(1000,0,3)")
        h = copy.deepcopy(ROOT.gROOT.FindObject("h"))
        f.Close()

        return h

    def loopOverFiles(self):
        for name,(filepath,color) in self.path_dict.items():
            print ("Looking at file %s (name %s)"%(filepath,name))
            h = self.makeErrorHist(filepath)
            h.SetLineWidth(2)
            h.SetLineColor(color)
            self.dict_hist[name] = h

            g = self.makeErrorGraph(h)
            g.SetLineColor(color)
            g.SetLineWidth(2)
            g.SetTitle(name)
            self.mg.Add(g)

    def makePlot(self):
        C = ROOT.TCanvas("C","C",800,600)
        C.cd()
        C.SetGrid()
        self.mg.SetTitle("Error graph;Error in orders of magnitude (|log_{10}(ME^{True})-log_{10}(ME^{DNN})|);Fraction of events")
        self.mg.Draw("AL")

        legend = C.BuildLegend(0.4,0.15,0.85,0.6,"Legend","")
        legend.Draw()
        C.Print("errorPlot.png")

        C.Clear()
        C.cd()
        legend.SetY1NDC(0.45);
        legend.SetY2NDC(0.85);
        hmax = max([h.GetMaximum() for h in self.dict_hist.values()])
        for i, (name,h) in enumerate(self.dict_hist.items()):
            h.SetMaximum(hmax*1.1)
            h.SetStats(0)
            if i == 0:
                h.SetTitle("Log difference between True ME and DNN regression;|log_{10}(ME^{True})-log_{10}(ME^{DNN})|;Events")
                h.Draw()
            else:   
                h.Draw("sames")
        legend.Draw()
        C.Print("logdiff.png")
            
if __name__ == '__main__':
    instance = errorPlots()
    instance.loopOverFiles()
    instance.makePlot()
