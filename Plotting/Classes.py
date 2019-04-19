import os
import sys
import glob
import copy
import logging
from array import array

import ROOT
from ROOT import TFile, TH1F, TH2F, TCanvas, gROOT, TGaxis, TPad, TLegend, TImage

from sklearn import metrics
import matplotlib.pyplot as plt

# ROOT STYLE #
import CMS_lumi
import tdrstyle

 # PYPLOT STYLE #
SMALL_SIZE = 16
MEDIUM_SIZE = 20
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title

#################################################################################################
""" Class definitions """
#################################################################################################

#####################################     Plot_TH1      #########################################
class Plot_TH1:
    def __init__(self,filename,tree,variable,weight,cut,name,bins,xmin,xmax,title,xlabel,ylabel):
        self.filename = filename
        self.tree = tree
        self.variable = variable
        self.weight = weight
        self.cut = cut
        self.name = name
        self.bins = bins
        self.xmin = xmin
        self.xmax = xmax
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def MakeHisto(self):
        file_handle = TFile.Open(self.filename)
        tree = file_handle.Get(self.tree)
        tree.Draw(self.variable+'>>'+self.name+'('+str(self.bins)+','+str(self.xmin)+','+str(self.xmax)+')',self.cut,"goff")    
        histo = gROOT.FindObject(self.name)
        histo.SetTitle(self.title+';'+self.xlabel+';'+self.ylabel)
        self.histo = copy.deepcopy(histo)

    def PlotOnCanvas(self,pdf_name):
        tdrstyle.setTDRStyle() 
        canvas = TCanvas("c1", "c1", 800, 600)
        self.histo.SetTitleOffset(1.4,'xyz')
        self.histo.SetMinimum(0)
        self.histo.SetLineWidth(2)

        self.histo.Draw()

        canvas.Print(pdf_name,'Title:'+self.title)
        canvas.Close()



####################################      Plot_TH2       ########################################
class Plot_TH2:
    def __init__(self,filename,tree,variablex,variabley,weight,cut,name,binsx,binsy,xmin,xmax,ymin,ymax,title,xlabel,ylabel,zlabel,option):
        self.filename = filename
        self.tree = tree
        self.variablex = variablex
        self.variabley = variabley
        self.weight = weight
        self.cut = cut
        self.name = name
        self.binsx = binsx
        self.binsy = binsy
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.zlabel = zlabel
        self.option = option

    def MakeHisto(self):
        file_handle = TFile.Open(self.filename)
        tree = file_handle.Get(self.tree)
        tree.Draw(self.variabley+':'+self.variablex+'>>'+self.name+'('+str(self.binsx)+','+str(self.xmin)+','+str(self.xmax)+','+str(self.binsx)+','+str(self.xmin)+','+str(self.xmax)+')',self.cut,"goff "+self.option)    
        self.histo = copy.deepcopy(gROOT.FindObject(self.name))
        self.histo.SetTitle(self.title+';'+self.xlabel+';'+self.ylabel+';'+self.zlabel)
        self.histo.SetMinimum(0)

    def PlotOnCanvas(self,pdf_name):
        tdrstyle.setTDRStyle() 
        canvas = TCanvas("c1", "c1", 800, 600)
        self.histo.SetTitleOffset(1.4,'xyz')
        canvas.SetRightMargin(0.2)
        self.histo.Draw()

        canvas.Print(pdf_name,'Title:'+self.title)
        canvas.Close()

####################################    Plot_Ratio_TH1    ########################################
class Plot_Ratio_TH1:
    def __init__(self,filename,tree,variable1,variable2,weight,cut,name,bins,xmin,xmax,title,xlabel,ylabel,legend1,legend2):
        self.filename = filename
        self.tree = tree
        self.variable1 = variable1
        self.variable2 = variable2
        self.cut = cut
        self.weight = weight
        self.name = name
        self.bins = bins
        self.xmin = xmin
        self.xmax = xmax
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.legend1 = legend1
        self.legend2 = legend2

    def MakeHisto(self):
        instance1 = Plot_TH1(self.filename,self.tree,self.variable1,self.weight,self.cut,self.name,self.bins,self.xmin,self.xmax,self.title,self.xlabel,self.ylabel)
        instance2 = Plot_TH1(self.filename,self.tree,self.variable2,self.weight,self.cut,self.name,self.bins,self.xmin,self.xmax,self.title,self.xlabel,self.ylabel)
        instance1.MakeHisto()
        instance2.MakeHisto()

        self.histo1 = copy.deepcopy(instance1.histo)
        self.histo2 = copy.deepcopy(instance2.histo)

        ratio = self.histo1.Clone(self.name)
        ratio.Sumw2()
        ratio.Divide(self.histo2)

        self.ratio = copy.deepcopy(ratio)

    def PlotOnCanvas(self,pdf_name):
        #gROOT.SetBatch(False)
        #tdrstyle.setTDRStyle() 
        canvas = TCanvas("c1", "c1", 800, 600)
        pad1 = TPad("pad1", "pad1", 0, 0.0, 1, 1.0)
        pad1.SetBottomMargin(0.32)
        pad1.SetGridx()
        pad1.Draw()
        pad1.cd()
        self.histo1.SetStats(0)
        self.histo1.Draw()
        self.histo2.Draw("same")

        legend = TLegend(0.70,0.72,0.85,0.83)
        legend.SetHeader("Legend","C")
        legend.AddEntry(self.histo1,self.legend1,"l")
        legend.AddEntry(self.histo2,self.legend2,"l")
        legend.Draw()

        # Redraw axis to avoid clipping 0
        self.histo1.GetXaxis().SetLabelSize(0.)
        self.histo1.GetXaxis().SetTitle('')
        #self.histo1.GetYaxis().SetLabelSize(0.)
        #axis = TGaxis( -9, , -4.5, 20, 1000,10000,50510,"+L")
        axis = TGaxis(-9,-2.8,-9,2.8,0,10000,50510,"")
        axis.SetLabelFont(43)
        axis.SetLabelSize(15)
        axis.Draw("same")

        pad2 = TPad("pad2", "pad2", 0, 0.0, 1, 0.3)
        pad2.SetTopMargin(0)
        pad2.SetBottomMargin(0.4)
        pad2.SetGridx()
        pad2.Draw()
        pad2.cd() 

        self.ratio.SetLineColor(ROOT.kBlack)
        self.ratio.SetMinimum(0.5)
        self.ratio.SetMaximum(1.5)
        self.ratio.SetStats(0)
        self.ratio.SetMarkerStyle(21)
        self.ratio.Draw("ep")

        self.histo1.SetLineColor(ROOT.kBlue+1)
        self.histo1.SetLineWidth(2)
        max_y = max(self.histo1.GetMaximum(),self.histo2.GetMaximum())
        self.histo1.SetMaximum(max_y*1.1)
        self.histo1.GetYaxis().SetNdivisions(505)
        self.histo1.GetYaxis().SetTitleSize(20)
        self.histo1.GetYaxis().SetTitleFont(43)
        self.histo1.GetYaxis().SetTitleOffset(1.55)

        self.histo2.SetLineColor(ROOT.kRed)
        self.histo2.SetLineWidth(2)

        self.ratio.SetTitle("")

        self.ratio.GetYaxis().SetTitle("Ratio")
        self.ratio.GetYaxis().SetNdivisions(505)
        self.ratio.GetYaxis().SetTitleSize(20)
        self.ratio.GetYaxis().SetTitleFont(43)
        self.ratio.GetYaxis().SetTitleOffset(1.55)
        self.ratio.GetYaxis().SetLabelFont(43)
        self.ratio.GetYaxis().SetLabelSize(15)

        self.ratio.GetXaxis().SetNdivisions(510)
        self.ratio.GetXaxis().SetTitleSize(20)
        self.ratio.GetXaxis().SetTitleFont(43)
        self.ratio.GetXaxis().SetTitleOffset(4.)
        self.ratio.GetXaxis().SetLabelFont(43)
        self.ratio.GetXaxis().SetLabelSize(15)

        ROOT.SetOwnership(canvas, False)
        ROOT.SetOwnership(pad1, False)
        ROOT.SetOwnership(pad2, False)

        canvas.Print(pdf_name,'Title:'+self.title)
        canvas.Close()

####################################      Plot_ROC       ########################################
class Plot_ROC:
    def __init__(self,variable1,variable2,weight,title,cut=''):
        self.variable1 = variable1
        self.variable2 = variable2
        self.weight = weight
        self.cut = cut
        self.title = title
        self.output = []
        self.target = []

    def AddToROC(self,filename,tree,sample):
        file_handle = TFile.Open(filename)
        tree = file_handle.Get(tree)
        var1 = array('d',[0])
        var2 = array('d',[0])
        tree.SetBranchAddress( self.variable1, var1 )
        tree.SetBranchAddress( self.variable2, var2 )
        i = 0
        while tree.GetEntry(i):
            i += 1
            self.output.append(var1[0]/(var2[0]+var1[0]))

    
        if sample == 'DY':
            self.target.extend([0]*i)
        elif sample == 'TT':
            self.target.extend([1]*i)

    def ProcessROC(self):
        self.fpr, self.tpr, threshold = metrics.roc_curve(self.target,self.output)
        self.roc_auc = metrics.auc(self.fpr, self.tpr)


def MakeROCPlot(list_obj,name):
    # Generate figure #
    fig, ax = plt.subplots(1,figsize=(8,6))

    # Loop over plot objects #
    for i,obj in enumerate(list_obj):
        ax.plot(obj.tpr, obj.fpr, label = '%s AUC = %0.5f' % (obj.title,obj.roc_auc))
        ax.grid(True)
        #plt.title('ROC : %s'%obj.title)
    plt.legend(loc = 'upper left')
    #plt.yscale('symlog',linthreshy=0.0001)
    plt.plot([0, 1], [0, 1],'k--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.xlabel(r'Correct $t\bar{t}$ identification')
    plt.ylabel(r'Misidentification of DY as $t\bar{t}$')
    plt.suptitle(os.path.basename(name.replace('_',' ')))

    fig.savefig(name+'.png')

#################################################################################################
""" Function definitions """
#################################################################################################
def LoopPlotOnCanvas(pdf_name,list_histo):
    for idx,inst in enumerate(list_histo,1):
        # inst is a class object -> inst.histo = TH1/TH2
        # Open file #
        if idx==1:
            c2 = TCanvas()
            c2.Print(pdf_name+'.pdf[')
            c2.Close()
        # Print each plot #
        inst.PlotOnCanvas(pdf_name=pdf_name+'.pdf')
        # Close file #
        if idx==len(list_histo):
            c2 = TCanvas()
            c2.Print(pdf_name+'.pdf') # Otherwise last plot does not have title
            c2.Print(pdf_name+'.pdf]')
            c2.Close()
    logging.info('Plots saved at %s'%(pdf_name+'.pdf'))





    # Save to root file #
    #f_root = TFile(pdf_name+".root", "recreate")
            #inst.histo.Write()
