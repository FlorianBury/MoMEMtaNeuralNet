import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from ROOT import TGraph2D, TCanvas, gPad, TH2F, gStyle

gStyle.SetOptStat(0)

mH = np.array([200,200,250,250,300,300,300,500,500,500,500,500,650,800,800,800,800,800,1000,1000,1000,2000,3000])
mA = np.array([50,100,50,100,50,100,200,50,100,200,300,400,50,50,100,200,400,700,50,200,500,1000,2000])
AUC_MEM = np.array([0.90107,0.89736,0.90640,0.87296,0.92959,0.90424,0.85102,0.97537,0.97514,0.97068,0.94650,0.90751,0.95916,0.93991,0.96377,0.98120,0.99205,0.97595,0.92522,0.97245,0.99472,0.99782,0.99816])
AUC_DNN = np.array([0.90729,0.90475,0.90596,0.87725,0.93349,0.90674,0.85802,0.97674,0.97644,0.97210,0.94923,0.90743,0.96152,0.93995,0.96559,0.98142,0.99210,0.97635,0.92650,0.97343,0.99470,0.99726,0.99729])
#mH = np.array([200,200,250,250,300,300,300,500,500,500,500,500,650,800,800,800,800,800,1000,1000,1000])
#mA = np.array([50,100,50,100,50,100,200,50,100,200,300,400,50,50,100,200,400,700,50,200,500])
#AUC_MEM = np.array([0.90107,0.89736,0.90640,0.87296,0.92959,0.90424,0.85102,0.97537,0.97514,0.97068,0.94650,0.90751,0.95916,0.93991,0.96377,0.98120,0.99205,0.97595,0.92522,0.97245,0.99472])
#AUC_DNN = np.array([0.90729,0.90475,0.90596,0.87725,0.93349,0.90674,0.85802,0.97674,0.97644,0.97210,0.94923,0.90743,0.96152,0.93995,0.96559,0.98142,0.99210,0.97635,0.92650,0.97343,0.99470])

N = mA.shape[0]

graph_DNN = TGraph2D(N)
graph_MEM = TGraph2D(N)
for i in range(0,N):
    graph_MEM.SetPoint(i,mA[i],mH[i],AUC_MEM[i])
    graph_DNN.SetPoint(i,mA[i],mH[i],AUC_DNN[i])

graph_MEM.SetNpx(500)
graph_MEM.SetNpy(500)
graph_DNN.SetNpx(500)
graph_DNN.SetNpy(500)

canvas = TCanvas('c1','c1',1600,700)
canvas.Divide(2,1,0.005)

canvas.cd(1)
gPad.SetRightMargin(0.2)
gPad.SetLeftMargin(0.12)
base_hist = TH2F('','',500,50,850,500,200,1000)
graph_MEM.SetHistogram(base_hist)
graph_MEM.SetMinimum(np.amin(AUC_MEM))
graph_MEM.SetMaximum(np.amax(AUC_MEM))
graph_MEM.Draw("colz")
graph_MEM.SetTitle("AUC score from MEM weights;M_{A} [GeV];M_{H} [GeV];AUC")

    
canvas.cd(2)
gPad.SetRightMargin(0.2)
gPad.SetLeftMargin(0.12)
base_hist = TH2F('','',500,50,850,500,200,1000)
graph_DNN.SetHistogram(base_hist)
graph_DNN.SetMinimum(np.amin(AUC_DNN))
graph_DNN.SetMaximum(np.amax(AUC_DNN))
graph_DNN.Draw("colz")
graph_DNN.SetTitle("AUC score from DNN weights;M_{A} [GeV];M_{H} [GeV];AUC")

canvas.Print('AUC.pdf')

