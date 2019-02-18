import os
import sys
import glob
import argparse
import shutil
from operator import add
import zipfile


def GetEntries(f,cut=''):
    from ROOT import TFile
    file_handle = TFile.Open(f)                                                                                                                                                                
    tree = file_handle.Get('tree') 
    if cut=='':
        return tree.GetEntries()
    else:
        player = tree.GetPlayer()
        return [player.GetEntries(cut),tree.GetEntries()]

def ListEntries(path,part=[''],cut=''):
    if cut=='':
        N_tot = 0
    else:
        N_tot = [0,0]
    for f in glob.glob(path+'/*'):
        skip = False
        filename = f.replace(path,'')
        for p in part:
            if filename.find(p)==-1: # Could not find part of name
                skip = True
        if skip:
            continue

        # If dir, get all the root files in it and add number of entries #
        if os.path.isdir(f):
            if cut=='':
                N = 0
            else:
                N = [0,0]
            for root, dirs, files in os.walk(f):
                for rf in files:
                    if rf.endswith('.root'):
                        #N = N+GetEntries(os.path.join(root,rf),cut)
                        if cut=='':
                            N += GetEntries(os.path.join(root,rf))
                        else:
                            N = list( map(add, N, GetEntries(os.path.join(root,rf),cut)) )
        # If root files, get N directly #
        if os.path.isfile(f) and f.endswith('.root'):
            N = GetEntries(f,cut)
        
        if cut=='':
            print (('Object : %s '%(filename)).ljust(70,'.')+('  %d'%(N)).ljust(9,' ')+' entries')    
            N_tot += N
        elif cut!='' and N[1]!=0:
            print (('Object : %s '%(filename)).ljust(70,'.')+('  %d cut / %d total = %0.2f%%'%(N[0],N[1],(N[0]*100/N[1]))).ljust(9,' ')+' entries')    
            N_tot = list( map(add, N_tot, N) )

    print ('-'*120)
    if cut=='':
            print ('All folder : '+('  %d'%(N_tot)).ljust(9,' ')+' entries')    
    else:
        print ('All folder : '+('  %d cut / %d total = %0.2f%%'%(N_tot[0],N_tot[1],(N_tot[0]*100/N_tot[1]))).ljust(9,' ')+' entries')    

def CopyZip(path_in,path_out):
    if not path_in.endswith('.zip') or not path_out.endswith('.zip'):
        sys.exit('You forgot .zip at the end of the file')
    # Split paths #
    dir_in = os.path.dirname(path_in)
    name_in = os.path.basename(path_in)
    dir_out = os.path.dirname(path_out)
    name_out = os.path.basename(path_out)
    # Unzip in tmp dir #
    with zipfile.ZipFile(path_in,"r") as zip_ref:
        tmp_dir = os.path.join(dir_in,'tmp_'+name_in.replace('.zip',''))
        zip_ref.extractall(tmp_dir)
    # Loop over the tmp dir  and rename each file accordint to desired output #
    for f in glob.glob(tmp_dir+'/*'):
        base_f = os.path.basename(f)
        dir_f = os.path.dirname(f)
        new_base = base_f.replace(name_in.replace('.zip',''),name_out.replace('.zip',''))
        os.rename(f,os.path.join(dir_f,new_base))
    # Zip in new file #
    with zipfile.ZipFile(os.path.join(tmp_dir,name_out),"w") as zip_ref:
        for f in glob.glob(tmp_dir+'/*'):
            if f.endswith('.zip'):
                continue # Avoids including the zip file itself
            zip_ref.write(f,os.path.basename(f))
    # Move new zip to dit_out #
    shutil.move(os.path.join(tmp_dir,name_out),path_out)
    # Clean tmp dir #
    shutil.rmtree(tmp_dir)


if __name__=='__main__':
    parser = argparse.ArgumentParser('Several useful tools in the context of MoMEMtaNeuralNet')
    countArgs = parser.add_argument_group('Count tree events in multiple root files')
    countArgs.add_argument('-p','--path', action='store', required=False, help='Path for the count')
    countArgs.add_argument('-i','--input', action='append', nargs='+', required=False, help='List of strings that must be contained')
    countArgs.add_argument('-c','--cut', action='store', default='', type=str, required=False, help='Cuts to be applied')
    zipArgs = parser.add_argument_group('Concatenate zip files (also modifying names of file sinside the archive')
    zipArgs.add_argument('-z','--zip', action='append', nargs=2, required=False, help='path to input .zip + path to output .zip')

    args = parser.parse_args()
    if args.path is not None:
        if args.input is not None:
            ListEntries(path=args.path,part=args.input[0],cut=args.cut)
        else:
            ListEntries(path=args.path,cut=args.cut)

    if args.zip is not None:
        CopyZip(args.zip[0][0],args.zip[0][1])


