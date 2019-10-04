#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"
#include <string>
#include <separate_invalids.C>


void process_all_separate(){
    /* Loads macro */
    //gInterpreter->AddIncludePath("/home/ucl/cp3/fbury/MoMEMta/");
    //gROOT->ProcessLine(".L separate_invalids.C");
    //gROOT->LoadMacro("separate_invalids.C");

    /* Defines paths */
    const char *path_to_file = "/nfs/scratch/fynu/fbury/MoMEMta_output/classification_weights/";
    char* dir = gSystem->ExpandPathName(path_to_file);
    void* dirp = gSystem->OpenDirectory(dir);

    /* Get array of filenames */
    char* entry;
    const char* filename[100];
    Int_t n = 0;
    TString str;

    while((entry = (char*)gSystem->GetDirEntry(dirp))) {
        str = entry;
        if(str.EndsWith(".root"))
            filename[n++] = entry;
    }

    /* Apply separation of the root files */
    for (Int_t i = 0; i < n; i++){
        Printf("file -> %s", gSystem->ConcatFileName(dir,filename[i]));   
        separate_invalids(dir,filename[i]);
    }
}
   
