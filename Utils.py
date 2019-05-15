import os
import sys
import glob
import argparse
import shutil
from operator import add
import zipfile
import pandas
import pprint

##################################################################################################
##########################                 GetEntries                   ##########################
##################################################################################################
def GetEntries(f,cut=''):
    """ Count the entries in a file, with or without a cut """
    from ROOT import TFile
    file_handle = TFile.Open(f)                                                                                                                                                                
    tree = file_handle.Get('tree') 
    if cut=='':
        return tree.GetEntries()
    else:
        player = tree.GetPlayer()
        return [player.GetEntries(cut),tree.GetEntries()]

##################################################################################################
##########################                 ListEntries                  ##########################
##################################################################################################
def ListEntries(path,part=[''],cut=''):
    """ Given a path, count the entries of all the files that match part, with or without cuts """
    if cut=='':
        N_tot = 0
    else:
        N_tot = [0,0]
    for f in glob.glob(path+'/*'):
        skip = False
        filename = f.replace(path,'').replace('root','')
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

##################################################################################################
##########################                 CopyZip                      ##########################
##################################################################################################

def CopyZip(path_in,path_out):
    """ Copy the zip content from path_in to path_out (useful when changin the name of an archive because it changes the names internally)"""
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


##################################################################################################
##########################                 CountVariables               ##########################
##################################################################################################
def CountVariables(path_files,var, part=[''],cut='',is_time_in_ms=False):
    """
        Loops over all the files in path_files,
        Find all the branches that match var (can be multiple),
        Add all the values of the event with the given variables (if they pass the cut)
        Returns the total value, variable by variable
    """
    from ROOT import TFile
    from root_numpy import tree2array
    var_dict = {}

    files = glob.glob(os.path.join(path_files,'*.root'))
    if len(files)==0:
        print ('No files in %s matching %s have been found'%(path_files,part))

    for f in files:
        filename = f.replace(path_files,'').replace('root','')
        skip = False 
        for p in part:
            if filename.find(p)==-1: # Could not find part of name
                skip = True
        if skip:
            continue

        print ('\t Looking at %s'%(filename))
        # Get the branch names #
        name_list = []
        root_file = TFile.Open(f)
        tree = root_file.Get("tree")
        br = tree.GetListOfBranches().Clone()
        for b in br: # Loop over branch objetcs
            name_list.append(b.GetName())

        # Only keep the ones that contain var #
        var_list = [k for k in name_list if var in k]
        for vl in var_list: # Save the branch names in the dict
            if not vl in var_dict:
                var_dict[vl] = 0

        # Get the numpy array from this tree, then pandas #
        data = tree2array(tree,branches=var_list,selection=cut)
        data = pandas.DataFrame(data)
        for name, values in data.iteritems():
            var_dict[name] += values.sum()

    # Print the results #
    total_var = 0
    print ('')
    for k,v in var_dict.items():
        if is_time_in_ms:
            print (("Branch : %s "%k).ljust(50,'.'),' Value : ',convert_time(v))        
        else:
            print (("Branch : %s "%k).ljust(50,'.'),' Value : %f'%v)        
        total_var += v
    print ('-'*80)
    if is_time_in_ms:
        print ('Total for all variables '.ljust(50,'.'),' Value : ',convert_time(total_var))
    else:
        print ('Total for all variables '.ljust(50,'.'),' Value : %f'%total_var)
    print ('')
    print ('')
    
        
def convert_time(time):
    seconds=(time/1000)%60
    seconds = int(seconds)
    minutes=(time/(1000*60))%60
    minutes = int(minutes)
    hours=(time/(1000*60*60))%24
    days = (time/(1000*60*60*24))

    return ("%6dd:%2dh:%2dm:%2ds" % (days, hours, minutes, seconds))

##################################################################################################
##########################                 ListBranches                 ##########################
##################################################################################################
def ListBranches(rootfile):
    from ROOT import TFile
    name_list = []
    root_file = TFile.Open(rootfile)
    tree = root_file.Get("tree")
    br = tree.GetListOfBranches().Clone()
    for b in br: # Loop over branch objetcs
        name_list.append(b.GetName())
    print ('Branches from %s'%rootfile)
    for l in name_list:
        print ('\t%s'%l)
    return name_list

##################################################################################################
##########################                 AppendTree                   ##########################
##################################################################################################
def AppendTree(rootfile1,rootfile2,branches):
    """
    Append the branches of rootfile2 to rootfile1
    All the common branches must be identical
    """
    # Get the arrays #
    import root_numpy
    import pandas as pd
    data1 = pd.DataFrame(root_numpy.root2array(rootfile1,'tree',branches=ListBranches(rootfile1)))
    # Check that the requested branches are in rootfile2 #
    list_branches2 = ListBranches(rootfile2)
    for b in branches:
        if not b in list_branches2:
            print ('Branch %s not present in file %s'%(b,rootfile2))
    data2 = pd.DataFrame(root_numpy.root2array(rootfile2,'tree',branches=branches))
    if data1.shape[0] != data2.shape[0]:
        sys.exit('The two files do not have the same number of events')
    print ('Number of branches in first file : %d'%data1.shape[1])
    print ('Number of branches in second file to append : %d'%data2.shape[1])

    # Concatenate them #
    all_df = pd.concat((data1,data2),axis=1)
    all_data  = all_df.to_records(index=False,column_dtypes='float64')
    
    # Save them #
    root_numpy.array2root(all_data,rootfile1,mode='recreate')

##################################################################################################
##########################                 Main                         ##########################
##################################################################################################

if __name__=='__main__':
    parser = argparse.ArgumentParser('Several useful tools in the context of MoMEMtaNeuralNet')
    countArgs = parser.add_argument_group('Count tree events in multiple root files')
    countArgs.add_argument('-p','--path', action='store', required=False, help='Path for the count')
    countArgs.add_argument('-i','--input', action='append', nargs='+', required=False, help='List of strings that must be contained in the filename')
    countArgs.add_argument('-c','--cut', action='store', default='', type=str, required=False, help='Cuts to be applied')
    zipArgs = parser.add_argument_group('Concatenate zip files (also modifying names of files inside the archive')
    zipArgs.add_argument('-z','--zip', action='append', nargs=2, required=False, help='path to input .zip + path to output .zip')
    CountVar = parser.add_argument_group('Counts the sum of variables in all files')
    CountVar.add_argument('-v','--variable', action='store', required=False, type=str, help='Partial name of the branches to include in the count (--path must have been provided)')
    CountVar.add_argument('-l','--list', action='store', required=False, type=str, help='Lists all the branches of a given file')
    zipArgs.add_argument('-a','--append', action='append', nargs='+', required=False, help='Name of first root file + Name of second root file + list of branches to be taen from second and appended to first')

    args = parser.parse_args()
    if args.path is not None:
        if args.input is not None:
            if args.variable is not None:
                CountVariables(args.path,args.variable,is_time_in_ms=True,part=args.input[0])
            ListEntries(path=args.path,part=args.input[0],cut=args.cut)
        else:
            if args.variable is not None:
                CountVariables(args.path,args.variable,is_time_in_ms=True)
            ListEntries(path=args.path,cut=args.cut)

    if args.zip is not None:
        CopyZip(args.zip[0][0],args.zip[0][1])

    if args.list is not None:
        _ = ListBranches(args.list)

    if args.append is not None:
        if len(args.append[0])<=2:
            print ('Not enough arguments to append')
        else:
            file1 = args.append[0][0]
            file2 = args.append[0][1]
            branches = args.append[0][2:]
            print ('File to be appended : %s'%file1)
            print ('File to be append   : %s'%file2)
            print ('Branches to append :')
            for b in branches:
                print ('..... %s'%b)
            AppendTree(file1,file2,branches)


