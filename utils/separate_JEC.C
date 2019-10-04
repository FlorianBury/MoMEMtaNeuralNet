#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"

void separate_invalids(const char* dir, TString name){
    /* Paths */
    TString full_name = gSystem->ConcatFileName(dir,name);
    TString JEC_path = gSystem->ConcatFileName(dir,"/split_JEC/");
    TString NoJEC_path = gSystem->ConcatFileName(dir,"/split_NoJEC/");
    
    /* Open tree */
    TFile *f = TFile::Open(full_name);
    TTree *tree = (TTree*)f->Get("tree");

    /* Generate new trees and files */
    TFile *JEC_file = new TFile(JEC_path+name, "RECREATE");
    TTree *JEC_tree = tree->CloneTree(0);
    
    TFile *NoJEC_file = new TFile(NoJEC_path+name, "RECREATE");
    TTree *NoJEC_tree = tree->CloneTree(0);

    auto N = tree->GetEntries();
    
    /* Branch Address */
    double is_JEC; 
    tree->SetBranchAddress( "is_JEC" , &is_JEC);

    /* Filling loop */
    bool valid = true;
    for(int i=0 ; i<N ; i++){
        valid = true;
        tree->GetEntry(i);
        if (is_JEC == 1) JEC_tree->Fill();
        else NoJEC_tree->Fill();
        if (i%(int(N/100))==0)
            std::cout<<"Status : "<<float(i)/N*100<<"%"<<std::endl;
    }
    
    /* Write trees */
    JEC_file->Write();
    NoJEC_file->Write();

    JEC_file->Close();
    NoJEC_file->Close();
}
    
