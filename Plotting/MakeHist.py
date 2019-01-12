import os
import sys
import argparse
import glob
import logging
import copy

import ROOT
from ROOT import TFile, TH1F, TH2F, TCanvas, gROOT
import CMS_lumi, tdrstyle


def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='From given set of root files, make different histograms in a root file')
    #parser.add_argument('-t','--type', action='store', required=True, type=str, default='',
    #              help='Type fo file to use (HToZA, DY or TT)')
    parser.add_argument('-m','--model', action='store', required=True, type=str, default='',
                  help='NN model to be used')
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
    # Get files #
    #############################################################################################
    INPUT_DIR = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/'
    INPUT_VALID = os.path.join(INPUT_DIR,'valid_weights')
    INPUT_INVALID_DY = os.path.join(INPUT_DIR,'invalid_DY_weights')
    INPUT_INVALID_TT = os.path.join(INPUT_DIR,'invalid_TT_weights')
    INPUT_MODEL = os.path.join(INPUT_DIR,'NNOutput',opt.model)

    # generate Root files #
    f_root = TFile(opt.model+".root", "recreate")

    #############################################################################################
    # Class definition #
    #############################################################################################
    class Plot_TH1:
        def __init__(self,filename,tree,variable,cut,name,bins,xmin,xmax,title,xlabel,ylabel):
            self.filename = filename
            self.tree = tree
            self.variable = variable
            self.cut = cut
            self.name = name
            self.bins = bins
            self.xmin = xmin
            self.xmax = xmax
            self.title = title
            self.xlabel = xlabel
            self.ylabel = ylabel
    
        def ReturnHisto(self):
            file_handle = TFile.Open(self.filename)
            tree = file_handle.Get(self.tree)
            tree.Draw(self.variable+'>>'+self.name+'('+str(self.bins)+','+str(self.xmin)+','+str(self.xmax)+')',self.cut,"goff")    
            histo = gROOT.FindObject(self.name)
            histo.SetTitle(self.title+';'+self.xlabel+';'+self.ylabel)
            return copy.copy(histo)

    class Plot_TH2:
        def __init__(self,filename,tree,variable1,variable2,cut,name,binsx,binsy,xmin,xmax,ymin,ymax,title,xlabel,ylabel,zlabel):
            self.filename = filename
            self.tree = tree
            self.variable = variable
            self.variable1 = variable1
            self.variable2 = variable2
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
        def ReturnHisto(self):
            file_handle = TFile.Open(self.filename)
            tree = file_handle.Get(self.tree)
            tree.Draw(self.variable1+':'+self.variable2+'>>'+self.name+'('+str(self.bins)+','+str(self.xmin)+','+str(self.xmax)+')',self.cut,"goff")    
            histo = gROOT.FindObject(self.name)
            histo.SetTitle(self.title+';'+self.xlabel+';'+self.ylabel)
            return copy.copy(histo)

    
        def ReturnHisto(self):
            file_handle = TFile.Open(self.filename)
            tree = file_handle.Get(self.tree)
            tree.Draw(self.variable+'>>'+self.name+'('+str(self.bins)+','+str(self.xmin)+','+str(self.xmax)+')',self.cut,"goff")    
            histo = gROOT.FindObject(self.name)
            histo.SetTitle(self.title+';'+self.xlabel+';'+self.ylabel)
            return copy.copy(histo)




    def PlotOnCanvas(histo,pdf_name,first=False,last=False):
        tdrstyle.setTDRStyle() 

        canvas = TCanvas("c1", "c1", 800, 600)
        histo.SetTitleOffset(1.4,'xyz')
        histo.Draw()

        if first:
            canvas.SaveAs(pdf_name+'[')
        elif last:
            canvas.SaveAs(pdf_name+']')
        else:
            canvas.SaveAs(pdf_name)
    

            
        #return copy.deepcopy(canvas)



    #############################################################################################
    # Valid weights output #
    #############################################################################################
    logging.info('Starting Plotting the valid weights')
    list_histo = []
    list_canvas = []
    f_valid =  glob.glob(INPUT_MODEL+'/*.root')
    if len(f_valid) == 0:
        logging.error('Could not find the valid weights at %s'%(INPUT_MODEL+'/*.root'))
        sys.exit(1)
    for f in f_valid:
        # Except invalids #
        filename = f.replace(INPUT_MODEL+'/','').replace('.root','')
        if filename.find('invalid')!=-1:
            logging.debug('\tNot looking at %s'%(filename))
            continue
        logging.info('Processing %s'%(filename))

        # Initialize variables #
        MEM_weight_TT =  {'filename'    : f,
                          'tree'        : 'tree',
                          'variable'    : 'MEM_weight_DY',
                          'cut'         : '',
                          'name'        : filename+'_sample_MEM_weight_DY',
                          'bins'        : 100,
                          'xmin'        : 10,
                          'xmax'        : 40,
                          'title'       : filename+' sample : MEM weight DY',
                          'xlabel'      : '-log_{10}(weight)',
                          'ylabel'      : 'Occurences'
                         }
        MEM_weight_DY =  {'filename'    : f,
                          'tree'        : 'tree',
                          'variable'    : 'MEM_weight_TT',
                          'cut'         : '',
                          'name'        : filename+'_sample_MEM_weight_TT',
                          'bins'        : 100,
                          'xmin'        : 10,
                          'xmax'        : 40,
                          'title'       : filename+' sample : MEM weight TT',
                          'xlabel'      : '-log_{10}(weight)',
                          'ylabel'      : 'Occurences'
                         }
        DNN_weight_DY =  {'filename'    : f,
                          'tree'        : 'tree',
                          'variable'    : 'output_DY',
                          'cut'         : '',
                          'name'        : filename+'_sample_DNN_weight_DY',
                          'bins'        : 100,
                          'xmin'        : 10,
                          'xmax'        : 40,
                          'title'       : filename+' sample : DNN weight DY',
                          'xlabel'      : '-log_{10}(weight)',
                          'ylabel'      : 'Occurences'
                         }
        DNN_weight_TT  =  {'filename'    : f,
                          'tree'        : 'tree',
                          'variable'    : 'output_TT',
                          'cut'         : '',
                          'name'        : filename+'_sample_DNN_weight_TT',
                          'bins'        : 100,
                          'xmin'        : 10,
                          'xmax'        : 40,
                          'title'       : filename+' sample : DNN weight TT',
                          'xlabel'      : '-log_{10}(weight)',
                          'ylabel'      : 'Occurences'
                         }

        list_histo.append(Plot_TH1(**MEM_weight_DY).ReturnHisto())
        list_histo.append(Plot_TH1(**MEM_weight_TT).ReturnHisto())
        list_histo.append(Plot_TH1(**DNN_weight_DY).ReturnHisto())
        list_histo.append(Plot_TH1(**DNN_weight_TT).ReturnHisto())
        #list_canvas.append(Plot_TH1(**MEM_weight_TT).PlotOnCanvas())
        #list_canvas.append(Plot_TH1(**MEM_weight_DY).PlotOnCanvas())
        #list_canvas.append(Plot_TH1(**DNN_weight_TT).PlotOnCanvas())
        #list_canvas.append(Plot_TH1(**DNN_weight_DY).PlotOnCanvas())
                            

        # TH2D #
        #tree.Draw("output_DY:MEM_weight_DY>>"+filename+"_sample_MEM_vs_NN_weight_DY(100,0,40,100,0,40)","","goff")    
        #MEM_vs_NN_weight_DY = gROOT.FindObject(filename+"_sample_MEM_vs_NN_weight_DY")
        #tree.Draw("output_TT:MEM_weight_TT>>"+filename+"_sample_MEM_vs_NN_weight_TT(100,0,40,100,0,40)","","goff")    
        #MEM_vs_NN_weight_TT = gROOT.FindObject(filename+"_sample_MEM_vs_NN_weight_TT")


        # Ratiplot #
        #ratio_DY = TRatioPlot(MEM_weight_DY,NN_weight_DY)
        #ratio_DY.SetTitle('Ratio DY')
        #ratio_TT = TRatioPlot(MEM_weight_TT,NN_weight_TT)
        #ratio_TT.SetTitle('Ratio TT')



    #############################################################################################
    # Save histograms #
    #############################################################################################
    # Save to root file #
    f_root = TFile(opt.model+".root", "recreate")
    for idx,histo in enumerate(list_histo,1):
        if idx ==1:
            PlotOnCanvas(histo,opt.model+'.pdf',first=True)
        elif idx ==len(list_histo):
            PlotOnCanvas(histo,opt.model+'.pdf',last=True)
        else:
            PlotOnCanvas(histo,opt.model+'.pdf')

        histo.Write()

    #c2 = TCanvas('c2','c2',800,600)
    #c2.SaveAs(opt.model+'.pdf[')
    #for i,canvas in enumerate(list_canvas,1):
    #    if i==1:
    #        canvas.SaveAs(opt.model+'.pdf',first=True)
    #    elif i==len(list_canvas):
    #        canvas.SaveAs(opt.model+'.pdf',last=True)
    #    else:
    #        canvas.SaveAs(opt.model+'.pdf')
    #c2.SaveAs(opt.model+'.pdf]')

            

    

        
        
        



if __name__ == "__main__":
    main()   
