#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"

void split_Ntree(const char* dir, TString name, std::vector<float> relcut){
    /* Will cut the given tree in several N trees 
        eg : relcut = std<float> [0.1,0.7,0.9], tree size = =N
        -> tree with [0,0.1[*N
        -> tree with [0.1,0.7[*N
        -> tree with [0.7,0.9[*N
        -> tree with [0.9,1]*N
    */
    for (int i = 0 ; i<relcut.size() ; i++){
        if (i>0 && relcut[i]<relcut[i-1]){
            std::cout<<"[ERROR] Not increasing relative cuts"<<std::endl;
            return;
        }
    }
    
    /* Paths */
    TString full_name = gSystem->ConcatFileName(dir,name);
    std::vector<TString> paths;
    for (int i = 0 ; i<relcut.size()+1 ; i++){
        std::string s = "/path"+std::to_string(i)+"/";
        TString a_path = gSystem->ConcatFileName(dir,s.c_str());
        gSystem->Exec("mkdir "+a_path);
        paths.push_back(a_path);
    }
    
    /* Open tree */
    TFile *f = TFile::Open(full_name);
    TTree *tree = (TTree*)f->Get("tree");

    /* Generate new trees and files */
    std::vector<TFile*> files;
    std::vector<TTree*> trees;
    for (auto & path : paths){
        files.push_back(new TFile(path+name, "RECREATE"));
        trees.push_back(tree->CloneTree(0));
    }

    auto N = tree->GetEntries();
    
    /* Filling loop */
    for(int i=0 ; i<N ; i++){ // Loop over entries
        tree->GetEntry(i);
        /* Check for first cut */
        if (i < relcut[0]*N){
            trees[0]->Fill();
        /* Check for last cut */
        } else if (i >= relcut[relcut.size()-1]*N){
            trees[relcut.size()]->Fill();
        /* Check other cuts */
        } else{
            for (int j=1 ; j<relcut.size() ; ++j){ 
                if (i>=relcut[j-1]*N && i<relcut[j]*N) 
                    trees[j]->Fill();   
            }
        }
        if (i%(int(N/100))==0)
            std::cout<<"Status : "<<float(i)/N*100<<"%"<<std::endl;
    }
    
    /* Write trees */
    std::vector<TFile*>::iterator iter;
    for(iter = files.begin() ; iter != files.end(); ++iter) {
        (*iter)->Write();
        (*iter)->Close();
    }
}
    
