#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"

void split_2tree(const char* dir, TString name, float relcut){
    if (relcut>1 || relcut<0){
        std::cout<<"relcut must be between 0 and 1"<<std::endl;
        return;
    }
    
    /* Paths */
    TString full_name = gSystem->ConcatFileName(dir,name);
    TString path1 = gSystem->ConcatFileName(dir,"/path1/");
    TString path2 = gSystem->ConcatFileName(dir,"/path2/");
    gSystem->Exec("mkdir "+path1);
    gSystem->Exec("mkdir "+path2);
    
    /* Open tree */
    TFile *f = TFile::Open(full_name);
    TTree *tree = (TTree*)f->Get("tree");

    /* Generate new trees and files */
    TFile *file1 = new TFile(path1+name, "RECREATE");
    TTree *tree1 = tree->CloneTree(0);
    
    TFile *file2 = new TFile(path2+name, "RECREATE");
    TTree *tree2 = tree->CloneTree(0);

    auto N = tree->GetEntries();
    
    /* Filling loop */
    for(int i=0 ; i<N ; i++){
        tree->GetEntry(i);
        if (i < relcut*N)
            tree1->Fill();
        else 
            tree2->Fill();
        if (i%(int(N/100))==0)
            std::cout<<"Status : "<<float(i)/N*100<<"%"<<std::endl;
    }
    
    /* Write trees */
    file1->Write();
    file2->Write();

    file1->Close();
    file2->Close();
}
    
