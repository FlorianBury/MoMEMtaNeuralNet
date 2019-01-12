import os
import sys
import glob

from ROOT import TFile

def GetEntries(f):
    file_handle = TFile.Open(f)                                                                                                                                                                
    tree = file_handle.Get('tree') 
    return tree.GetEntries()

def ListEntries(path,part=['']):
    N_tot =0
    for root, dirs, files in os.walk(path):
        N = 0
        sub_root = False
        for f in glob.glob(root+'/*.root'):
            skip = False
            if f.replace(root,'').find('output')!=-1:
                sub_root = True
            if not sub_root:
                for p in part:
                    if f.replace(root,'').find(p)==-1:
                        skip = True
            if skip:
                continue
            if sub_root:
                N += GetEntries(f)
            else:
                print (f.replace(root,'').ljust(50,'.')+('  %d'%(tree.GetEntries())).ljust(9,' ')+' entries')
                N_tot += GetEntries(f)

        sub_root_name = os.path.basename(os.path.dirname(root))
        if sub_root:
            ski= False
            for p in part:
                if sub_root_name.find(p)==-1:
                    skip = True
            if skip:
                continue
            print (('Path : %s '%(sub_root_name)).ljust(70,'.')+('  %d'%(N)).ljust(9,' ')+' entries')    
            N_tot += N

    print ('--> Total size of all trees %d'%(N_tot))




if __name__=='__main__':
    print ('Path used : %s'%(sys.argv[1]))
    if len(sys.argv)==2:
        ListEntries(path=sys.argv[1])
    if len(sys.argv)>2:
        ListEntries(path=sys.argv[1],part=sys.argv[2:])

