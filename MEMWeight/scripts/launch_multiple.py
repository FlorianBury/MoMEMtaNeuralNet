import os
import sys
import glob
import runpy
from ROOT import TFile,TTree

INPUT_DIR = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/invalid_TT_weights/'
# TODO : replace INPUT_DIR in main.cc !!!
tag = '_invalid_TT'

for filename in glob.glob(INPUT_DIR+'*.root'):
    name = filename.replace(INPUT_DIR,'')
    
    f = TFile.Open(filename)
    t = f.Get("tree")
    max_events = t.GetEntries()
    print (filename,' -> Entries',str(max_events))

    if max_events==0:
        print ('WARNING -> empty file')
        continue
    # launch submit #
    launch = input ('Can I launch ? (y/n)')
    if launch == 'y': 
        os.system("python submit_on_slurm.py -n {} -i {} -m {}".format(name.replace('.root','')+tag,name,max_events))

