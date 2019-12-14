#include <vector>
#include <iostream>

#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"
#include "TString.h"
#include "TRandom3.h"
#include "TLorentzVector.h"

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

    /* SetBranchAddress */
    double MEPdf; 
    TLorentzVector* init1_p4;
    TLorentzVector* init2_p4;
    TLorentzVector* positron_p4;
    TLorentzVector* neutrino_p4;
    TLorentzVector* bjet_p4;
    TLorentzVector* electron_p4;
    TLorentzVector* antineutrino_p4;
    TLorentzVector* antibjet_p4;
    for (auto & tree:trees){
        tree->SetBranchAddress( "MEPdf" , &MEPdf);
        tree->SetBranchAddress( "init1_p4" , &init1_p4);
        tree->SetBranchAddress( "init2_p4" , &init2_p4);
        tree->SetBranchAddress( "positron_p4" , &positron_p4);
        tree->SetBranchAddress( "neutrino_p4" , &neutrino_p4);
        tree->SetBranchAddress( "bjet_p4" , &bjet_p4);
        tree->SetBranchAddress( "electron_p4" , &electron_p4);
        tree->SetBranchAddress( "antineutrino_p4" , &antineutrino_p4);
        tree->SetBranchAddress( "antibjet_p4" , &antibjet_p4);
    }// Need to that for all branches otherwise they will be repeated 

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
}
    
