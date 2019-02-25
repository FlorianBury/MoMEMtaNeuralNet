#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"

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
        if (w_DY<=w_DY_err) 
            invalid_DY_tree->Fill();
        else if (w_TT<=w_TT_err)
            invalid_TT_tree->Fill(); 
        else
            valid_tree->Fill();
        if (i%(int(N/100))==0)
            std::cout<<"Status : "<<float(i)/N*100<<"%"<<std::endl;
    }
    
    /* Write trees */
    valid_file->Write();
    invalid_DY_file->Write();
    invalid_TT_file->Write();


}
    
