#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"

void root_split(TString path_root, int sep){
    /* Paths */
    TString path1 = path_root+"1.root";
    TString path2 = path_root+"2.root";
    path_root += ".root";
    /* Open tree */
    TFile *f = TFile::Open(path_root);
    TTree *tree = (TTree*)f->Get("tree");

    /* Generate new trees and files */
    TFile *file1 = new TFile(path1, "RECREATE");
    TTree *tree1 = tree->CloneTree(0);
    TFile *file2 = new TFile(path2, "RECREATE");
    TTree *tree2 = tree->CloneTree(0);
    
    auto N = tree->GetEntries();

    /* Get objects */
    TObject* cs = f->Get("cross_section");
    TObject* ws = f->Get("event_weight_sum");

    double w_DY;
    tree->SetBranchAddress( "weight_DY" , &w_DY );
    
    /* Filling loop */
    for(int i=0 ; i<N ; i++){
        tree->GetEntry(i);
        if (i<sep){
            tree1->Fill();
        }
        else{
            tree2->Fill();
        }
        if (i%(int(N/100))==0)
            std::cout<<"Status : "<<float(i)/N*100<<"%"<<std::endl;
    }
    
    /* Write trees */
    tree1->Write();
    tree2->Write();
    std::cout<<"First tree size  : "<<tree1->GetEntry()<<std::endl;
    std::cout<<"Second tree size : "<<tree2->GetEntry()<<std::endl;

    /* Add objects to files */
    file1->cd();
    cs->Write();
    ws->Write();
    file1->Close();
 
    file2->cd();
    cs->Write();
    ws->Write();
    file2->Close();
    
    delete f;


}
    
