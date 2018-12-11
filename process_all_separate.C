#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"

void separate_invalids(const char* dir, TString name);

void process_all_separate(){
    /* Loads macro */
    //gInterpreter->AddIncludePath("/home/ucl/cp3/fbury/MoMEMta/");
    //gROOT->ProcessLine(".L separate_invalids.C");
    //gROOT->LoadMacro("separate_invalids.C");

    /* Defines paths */
    const char *path_to_file = "/nfs/scratch/fynu/fbury/MoMEMta_output/slurm/";
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
    
void separate_invalids(const char* dir, TString name){
    /* Paths */
    TString full_name = gSystem->ConcatFileName(dir,name);
    TString valid_path = "/nfs/scratch/fynu/fbury/MoMEMta_output/valid_weights/";
    TString invalid_DY_path = "/nfs/scratch/fynu/fbury/MoMEMta_output/invalid_DY_weights/";
    TString invalid_TT_path = "/nfs/scratch/fynu/fbury/MoMEMta_output/invalid_TT_weights/";
    
    /* Open tree */
    TFile *f = TFile::Open(full_name);
    TTree *tree = (TTree*)f->Get("tree");

    /* Generate new trees and files */
    TFile *valid_file = new TFile(valid_path+name, "RECREATE");
    TTree *valid_tree = tree->CloneTree(0);
    
    TFile *invalid_DY_file = new TFile(invalid_DY_path+name, "RECREATE");
    TTree *invalid_DY_tree = tree->CloneTree(0);

    TFile *invalid_TT_file = new TFile(invalid_TT_path+name, "RECREATE");
    TTree *invalid_TT_tree = tree->CloneTree(0);

    auto N = tree->GetEntries();
    
    /* Branch Address */
    double w_DY, w_DY_err;
    double w_TT, w_TT_err;
    tree->SetBranchAddress( "weight_DY" , &w_DY );
    tree->SetBranchAddress( "weight_DY_err" , &w_DY_err );
    tree->SetBranchAddress( "weight_TT" , &w_TT );
    tree->SetBranchAddress( "weight_TT_err" , &w_TT_err );

    /* Filling loop */
    for(int i=0 ; i<N ; i++){
        tree->GetEntry(i);
        if (w_DY<w_DY_err) 
            invalid_DY_tree->Fill();
        else if (w_TT<w_TT_err)
            invalid_TT_tree->Fill(); 
        else
            valid_tree->Fill();
        //std::cout<<i<<"  "<<int(N/100)<<"  "<<i%(int(N/100))<<std::endl;
        if (i%(int(N/100))==0)
            std::cout<<"Status : "<<int(float(i)/N*100)<<"%"<<std::endl;
    }
    
    /* Write trees */
    valid_file->Write();
    invalid_DY_file->Write();
    invalid_TT_file->Write();
}
 
