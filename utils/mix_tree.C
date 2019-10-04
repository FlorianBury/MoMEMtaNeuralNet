#include <vector>
#include <iostream>

#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"
#include "TString.h"
#include "TRandom3.h"

void mix_tree(const char* dir){
    /* Get list of files */
    void* dirp = gSystem->OpenDirectory(dir);
    TString ext = ".root";
    TString str;
    const char* entry;
    std::vector<TString> filenames;
    while((entry = (char*)gSystem->GetDirEntry(dirp))) {
        str = entry;
        if(str.EndsWith(ext)){
            filenames.push_back(gSystem->ConcatFileName(dir, entry));
        }
    }

    /* TFile and TTree */ 
    std::vector<TFile*> files;
    std::vector<TTree*> trees;
    std::vector<int> sizes;
    std::vector<float> probs;
    std::vector<int> counters;
    int N_tot = 0;
    for (auto & filename : filenames){
        TFile *f = TFile::Open(filename);
        TTree *tree = (TTree*)f->Get("tree");
        
        files.push_back(f);
        trees.push_back(tree);
        sizes.push_back(tree->GetEntries());
        counters.push_back(0);
        N_tot += tree->GetEntries();
    }
    for (auto & size: sizes){
        probs.push_back(float(size)/float(N_tot));
    }

    for (int j = 0 ; j<filenames.size(); ++j)
        std::cout<<"Filename : "<<filenames[j]<<" -> Prob = N/N_tot = "<<sizes[j]<<" /  "<<N_tot<<" = "<<probs[j]<<std::endl; 

    /* Branch for checking */ 
    double MEPdf; 
    for (auto & tree:trees)
        tree->SetBranchAddress( "MEPdf" , &MEPdf);

    /* Generate the mixed tree */
    TFile *mix_file = new TFile(gSystem->ConcatFileName(dir, "MixTree.root"), "RECREATE");
    TTree *mix_tree = trees[0]->CloneTree(0); 
    int i = 0; 
    TRandom3 rndm;
    while (i<N_tot){
        /* Randomly select one of the file */
        int index  = int(rndm.Uniform(0,filenames.size()));
        /* Check if can take from it, with probablity */
        float prob = probs[index];
        float test = rndm.Rndm();
        /* If passed with probability prob, check if tree has not been exhausted */
        if (test < prob){
            /* Check if entries remaining in tree */
            if (counters[index]>sizes[index]){ // If all entries have been used
                continue;
            }
            /* Get entry from tree if passed the selection */
            trees[index]->GetEntry(counters[index]);     
            /* Fill mix tree */
            mix_tree->Fill();
            /* Iterate counter of taken tree */
            counters[index]++;
            /* Iterate mix tree counter */
            i++;
            if (i%(int(N_tot/100))==0){
                std::cout<<"Status : "<<float(i)/N_tot*100<<"%"<<std::endl;
            }
        }
    }
    
    /* Write files and close */
    mix_file->Write();
    mix_file->Close();
    std::vector<TFile*>::iterator iter;
    for(iter = files.begin() ; iter != files.end(); ++iter) {
        (*iter)->Close();
    }
        
    


//    for (int i = 0 ; i<relcut.size() ; i++){
//        if (i>0 && relcut[i]<relcut[i-1]){
//            std::cout<<"[ERROR] Not increasing relative cuts"<<std::endl;
//            return;
//        }
//    }
//    
//    /* Paths */
//    TString full_name = gSystem->ConcatFileName(dir,name);
//    std::vector<TString> paths;
//    for (int i = 0 ; i<relcut.size()+1 ; i++){
//        std::string s = "/path"+std::to_string(i)+"/";
//        TString a_path = gSystem->ConcatFileName(dir,s.c_str());
//        gSystem->Exec("mkdir "+a_path);
//        paths.push_back(a_path);
//    }
//    
//    /* Open tree */
//
//    /* Generate new trees and files */
//    auto N = tree->GetEntries();
//    
//    /* Filling loop */
//    for(int i=0 ; i<N ; i++){ // Loop over entries
//        tree->GetEntry(i);
//        /* Check for first cut */
//        if (i < relcut[0]*N){
//            trees[0]->Fill();
//        /* Check for last cut */
//        } else if (i >= relcut[relcut.size()-1]*N){
//            trees[relcut.size()]->Fill();
//        /* Check other cuts */
//        } else{
//            for (int j=1 ; j<relcut.size() ; ++j){ 
//                if (i>=relcut[j-1]*N && i<relcut[j]*N) 
//                    trees[j]->Fill();   
//            }
//        }
//    }
//    
}
    
