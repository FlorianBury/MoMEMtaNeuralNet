import os
import sys
import argparse
import glob
import logging
import copy
import yaml

import ROOT
from ROOT import TFile, TH1F, TH2F, TCanvas, gROOT
import CMS_lumi
import tdrstyle

import Classes
from Classes import Plot_TH1, Plot_TH2, Plot_Ratio_TH1, Plot_Stack_TH1, Plot_ROC, LoopPlotOnCanvas, MakeROCPlot, ProcessYAML

gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = 2000#[ROOT.kPrint, ROOT.kInfo]#, kWarning, kError, kBreak, kSysError, kFatal;

def main():
    #############################################################################################
    # Options #
    #############################################################################################
    parser = argparse.ArgumentParser(description='From given set of root files, make different histograms in a root file')
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
    # Select samples #
    #############################################################################################
    INPUT_DIR = os.path.join('/home/ucl/cp3/fbury/scratch/MoMEMta_output/NNOutput',opt.model)
    logging.info('Taking inputs from %s'%INPUT_DIR)
    
    # For each directory, puth the path in dictn the value is the list of histograms #
    class Plots():
        def __init__(self,name,override_params):
            self.name = name                            # Name of the subdir
            self.path = os.path.join(INPUT_DIR,name)    # Full path to files
            self.override_params = override_params      # Parameters to override in the configs
            self.list_histo = []                        # List of histograms to be filled

    list_plots = [
                    Plots(name = 'valid_weights',
                          override_params = {}),
                    Plots(name = 'invalid_DY_weights',
                          override_params = {}),
                    Plots(name = 'invalid_TT_weights',
                          override_params = {}),
                    Plots(name = 'interpolation_weights',
                          override_params = {}),
                 ]

    # Select template #
    class Template:
        def __init__(self,tpl,class_name):
            self.tpl = tpl                          # Template ".yml.tpl" to be used
            self.class_name = class_name            # Name of one of the class below to use

    templates = [
                    #Template(tpl = 'TH1_background.yml.tpl',
                    #         class_name = 'Plot_TH1'),
                    #Template(tpl = 'TH1_signal.yml.tpl',
                    #         class_name = 'Plot_TH1'),
                    #Template(tpl = 'TH1Ratio_background.yml.tpl',
                    #         class_name = 'Plot_Ratio_TH1'),
                    Template(tpl = 'TH1Ratio_signal.yml.tpl',
                             class_name = 'Plot_Ratio_TH1'),
                    Template(tpl = 'TH1Ratio_interpolation.yml.tpl',
                             class_name = 'Plot_Ratio_TH1'),
                    #Template(tpl = 'TH1Stack_signal.yml.tpl',
                    #         class_name = 'Plot_Stack_TH1)',
                    #Template(tpl = 'TH2_background.yml.tpl',
                    #         class_name = 'Plot_TH2'),
                    #Template(tpl = 'TH2_signal.yml.tpl',
                    #         class_name = 'Plot_TH2'),
                ] 

    # Make the output dir #
    OUTPUT_PDF = os.path.join(os.getcwd(),'PDF',opt.model)
    if not os.path.exists(OUTPUT_PDF):
        os.makedirs(OUTPUT_PDF)

    #############################################################################################
    # Loop over the different paths #
    #############################################################################################
    # Loop over the files #
    for obj in list_plots:
        logging.info('Starting Plotting from %s subdir'%obj.name)
        files = glob.glob(obj.path+'/*.root')

        if len(files) == 0:
            logging.error('Could not find %s at %s'%(obj.name,obj.path))

        # Start ROC curve #
        instance_ROC_MEM = Plot_ROC('weight_TT','weight_DY','total_weight','MEM')
        instance_ROC_DNN = Plot_ROC('output_TT','output_DY','total_weight','DNN')
        # Loop over files #
        for f in files:
            fullname = f.replace(obj.path+'/','').replace('.root','')
            logging.info('Processing weights from %s'%(fullname+'.root'))
            if fullname.startswith('DY'):
                filename = 'Drell-Yann'
            elif fullname.startswith('TT'):
                filename = 't#bar{t}'
            elif fullname.startswith('HToZA'):
                filename = 'Signal'

            # If DY or TT, add to ROC #
            if os.path.basename(f).startswith('DY'):
                try:
                    instance_ROC_MEM.AddToROC(f,'tree','DY')
                    instance_ROC_DNN.AddToROC(f,'tree','DY')
                except Exception as e:
                    logging.warning('Could not compute ROC due to "%s"'%(e))
            elif os.path.basename(f).startswith('TT'):
                try:
                    instance_ROC_MEM.AddToROC(f,'tree','TT')
                    instance_ROC_DNN.AddToROC(f,'tree','TT')
                except Exception as e:
                    logging.warning('Could not compute ROC due to "%s"'%(e))

            # Loop over the templates #
            for template in templates: 
                logging.debug('Template "%s" -> Class "%s"'%(template.tpl, template.class_name))
                list_config = [] # Will contain the dictionaries of parameters
                YAML = ProcessYAML(template.tpl) # Contain the ProcessYAML objects
                params = {**{'filename':f,'title':filename},**obj.override_params}
                # Get the list of configs #
                YAML.Particularize(fullname)
                YAML.Override(params)
                # loop over the configs #
                for name,config in YAML.config.items():
                    try:
                        class_ = getattr(Classes, template.class_name)
                        logging.info('\tPlot %s'%(name))
                        instance = class_(**config)
                        instance.MakeHisto()
                        obj.list_histo.append(instance)
                    except Exception as e:
                        logging.warning('Could not plot %s due to "%s"'%(name,e))

            #for name,dict_histo in config_TH1_stack.items():
            #    if not os.path.basename(f).startswith('HToZA'):
            #        continue
            #    if not isinstance(dict_histo,dict):
            #        continue
            #    dict_histo['list_cut'] = config_TH1_stack['list_cut']
            #    dict_histo['list_legend'] = config_TH1_stack['list_legend']
            #    dict_histo['list_color'] = config_TH1_stack['list_color']
            #    try:
            #        logging.info('\tPlot %s'%(name))
            #        instance = Plot_Stack_TH1(**dict_histo)
            #        instance.MakeHisto()
            #        list_histo_valid.append(instance)
            #    except Exception as e:
            #        logging.warning('Could not plot %s due to "%s"'%(name,e))
        try:
            instance_ROC_MEM.ProcessROC()
            instance_ROC_DNN.ProcessROC()
            MakeROCPlot([instance_ROC_MEM],os.path.join(OUTPUT_PDF,obj.name+' ROC_MEM'))
            MakeROCPlot([instance_ROC_DNN],os.path.join(OUTPUT_PDF,obj.name+' ROC_DNN'))
            MakeROCPlot([instance_ROC_MEM,instance_ROC_DNN],os.path.join(OUTPUT_PDF,obj.name+' ROC_MEM_vs_DNN'))
        except Exception as e:
            logging.warning('Could not process ROC due to "%s"'%e)
    
    ####################################### INVALID #############################################
#    invalid_cat = ['DY','TT']
#
#
#    # Loop over invalid categories #
#    for cat in invalid_cat:
#        f_inv = glob.glob(INPUT_INVALID.format(cat)+'/*.root')
#        temp_list = []
#        if len(f_inv) == 0:
#            logging.error('Could not find the invalid weights at %s'%(INPUT_VALID.format(cat)))
#        # Start ROC curve #
#        if cat == 'DY':
#            title_cat = r'Drell-Yann'
#        elif cat == 'TT':
#            title_cat = r'$t\bar{t}$'
#        instance_ROC_MEM = Plot_ROC('weight_TT','weight_DY','total_weight','MEM',"weight_{0}>weight_{0}_err".format(cat))
#        instance_ROC_DNN = Plot_ROC('output_TT','output_DY','total_weight','DNN',"weight_{0}>weight_{0}_err".format(cat))
#
#        # Loop over files over one category #
#        for f in f_inv:
#            filename = f.replace(INPUT_INVALID.format(cat)+'/','').replace('_invalid_{}.root'.format(cat),'')
#            logging.info('Processing invalid %s weights from %s'%(cat,filename))
#            # Esthetic printing #
#            if filename.startswith('DY'):
#                filename = 'Drell-Yann'
#            elif filename.startswith('TT'):
#                filename = 't#bar{t}'
#            elif filename.startswith('HToZA'):
#                filename = 'Signal'
#
#            # If DY or TT, add to ROC #
#            if os.path.basename(f).startswith('DY'):
#                try:
#                    instance_ROC_MEM.AddToROC(f,'tree','DY')
#                    instance_ROC_DNN.AddToROC(f,'tree','DY')
#                except:
#                    logging.warning('Could not add DY to ROC')
#            elif os.path.basename(f).startswith('TT'):
#                try:
#                    instance_ROC_MEM.AddToROC(f,'tree','TT')
#                    instance_ROC_DNN.AddToROC(f,'tree','TT')
#                except:
#                    logging.warning('Could not add TT to ROC')
#            # Particularize TH1 YAML file #
#            with open('TH1.yml.tpl') as tpl_handle:
#                tpl = tpl_handle.read()
#                tpl = tpl.format(file=f, name=filename, cut="'weight_{0}>weight_{0}_err'".format(cat),category='')
#                with open(OUTPUT_YAML+'/TH1_INV_{}_'.format(cat)+filename+'.yml', 'w') as out_yml:
#                    out_yml.write(tpl)
#
#             # Particularize TH1 Ratio YAML file #
#            with open('TH1Ratio.yml.tpl') as tpl_handle:
#                tpl = tpl_handle.read()
#                tpl = tpl.format(file=f, name=filename, cut="'weight_{0}>weight_{0}_err'".format(cat),category='')
#                with open(OUTPUT_YAML+'/TH1Ratio_INV_{}_'.format(cat)+filename+'.yml', 'w') as out_yml:
#                    out_yml.write(tpl)
#
#            with open('TH2.yml.tpl') as tpl_handle:
#                tpl = tpl_handle.read()
#                tpl = tpl.format(file=f, name=filename, cut="'weight_{0}>weight_{0}_err'".format(cat),category='')
#                with open(OUTPUT_YAML+'/TH2_INV_{}_'.format(cat)+filename+'.yml', 'w') as out_yml:
#                    out_yml.write(tpl)
#
#            # Parse and load YAML file #
#            with open(OUTPUT_YAML+'/TH1_INV_{}_'.format(cat)+filename+'.yml', 'r') as stream:
#                config_TH1 = yaml.load(stream) # Dict of dicts 
#            with open(OUTPUT_YAML+'/TH1Ratio_INV_{}_'.format(cat)+filename+'.yml', 'r') as stream:
#                config_TH1_ratio = yaml.load(stream) # Dict of dicts 
#            with open(OUTPUT_YAML+'/TH2_INV_{}_'.format(cat)+filename+'.yml', 'r') as stream:
#                config_TH2 = yaml.load(stream) # Dict of dicts 
#             
#            # Create list of histo # 
#            for name,dict_histo in config_TH1.items():
#                try:
#                    logging.info('\tPlot %s'%(name))
#                    instance = Plot_TH1(**dict_histo)
#                    instance.MakeHisto()
#                    temp_list.append(instance)
#                except Exception as e:
#                    logging.warning('Could not plot %s due to "%s"'%(name,e))
#
#            for name,dict_histo in config_TH1_ratio.items():
#                try:
#                    logging.info('\tPlot %s'%(name))
#                    instance = Plot_Ratio_TH1(**dict_histo)
#                    instance.MakeHisto()
#                    temp_list.append(instance)
#                except Exception as e:
#                    logging.warning('Could not plot %s due to "%s"'%(name,e))
#            for name,dict_histo in config_TH2.items():
#                try:
#                    logging.info('\tPlot %s'%(name))
#                    instance = Plot_TH2(**dict_histo)
#                    instance.MakeHisto()
#                    temp_list.append(instance)
#                except Exception as e:
#                    logging.warning('Could not plot %s due to "%s"'%(name,e))
#
#        # Make and save ROC #
#        try:
#            instance_ROC_MEM.ProcessROC()
#            instance_ROC_DNN.ProcessROC()
#            MakeROCPlot([instance_ROC_MEM],os.path.join(OUTPUT_PDF,'Invalid_{}_ROC_MEM'.format(title_cat)))
#            MakeROCPlot([instance_ROC_DNN],os.path.join(OUTPUT_PDF,'Invalid_{}_ROC_DNN'.format(title_cat)))
#            MakeROCPlot([instance_ROC_MEM,instance_ROC_DNN],os.path.join(OUTPUT_PDF,'Invalid_{}_ROC_MEM_vs_DNN'.format(title_cat)))
#        except:
#            logging.warning('Could not process ROC')
#    
#        # Append in list #
#        list_histo_invalid.append(temp_list)
#
    #############################################################################################
    # Save histograms #
    #############################################################################################
    for obj in list_plots:
        PDF_name = os.path.join(OUTPUT_PDF,obj.name) 
        LoopPlotOnCanvas(PDF_name,obj.list_histo)
    logging.info("All Canvas have been printed")

        
        
        



if __name__ == "__main__":
    main()   
