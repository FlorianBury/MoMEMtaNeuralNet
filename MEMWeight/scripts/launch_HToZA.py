import os
import sys
import glob
import runpy
from ROOT import TFile,TTree

def run_script(script_name,*args):
    _argv = sys.argv[:]
    sys.argv = list(args)
    execfile(script_name)
    sys.argv = _argv

INPUT_DIR = '/nfs/scratch/fynu/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/fourVectors_withMETphi_for_Florian/slurm/output/'

for file in glob.glob(INPUT_DIR+'*.root'):
    filename = file.replace(INPUT_DIR,'')
    if filename.startswith('HToZA'):
        continue
    else:
        pass

    name = filename[:27]
    
    f = TFile.Open(file)
    t = f.Get("t")
    max_events = t.GetEntries()
    print (filename)
    print (max_events)
    #run_script('submit_on_slurm.py',name,filename,max_events)
    #runpy.run_path('submit_on_slurm.py')
    
