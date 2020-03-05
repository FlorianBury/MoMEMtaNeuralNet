#include <iostream>
#include <TSystem.h>

void makeWeights(std::string root_file, float cutoff=-1.){
    gStyle->SetOptStat(0);

    TH1F* h;
    TFile* f_hist = new TFile("hist.root","UPDATE");
    //if(gSystem->AccessPathName(hist_path.c_str())){
    if (f_hist->IsZombie()){
        std::cout<<"File does not exist, will create the histogram"<<std::endl;
        TFile* f_root = new TFile(root_file.c_str(),"READ");
        TTree* t = (TTree*)f_root->Get("tree");
        t->Draw("-log10(MEPdf)>>h(1000,0,15");
        h = (TH1F*)gROOT->FindObject("h");
        h->SetName("h");
        h->SetDirectory(0);
        f_hist->cd();
        h->Write();
        f_hist->Write();
        f_hist->Close();
        f_root->Close(); 
    }
    else{
        std::cout<<"File exists, will get the histogram"<<std::endl;
        h = (TH1F*)f_hist->Get("h");
        h->SetDirectory(0);
        f_hist->Close(); 
    }
    TH1F* h_weights = new TH1F("weights","weights",1000,0,15);
    /* Fill weights hist */
    for (int b = 1 ; b <= h->GetNbinsX() ; ++b){
        auto val = h->GetBinContent(b);
        if (val>0){
            h_weights->SetBinContent(b,h->GetMaximum()/val);    
            if(cutoff != -1. && h->GetMaximum()/val > cutoff)
                h_weights->SetBinContent(b,cutoff);
        }
        else{
            h_weights->SetBinContent(b,1);
            std::cout<<"Missing "<<b<<" -> "<<val<<std::endl;
        }
    }

    /* Check if the sum of weights is indeed uniform */
    int N = 1000000; // Number of sampling of hist 
    std::vector<float> binValues(1000,0.);
    for (int i = 0 ; i<N ; i++){
        auto val = h->GetRandom();
        auto bin = h_weights->FindBin(val);
        auto w = h_weights->GetBinContent(bin);
        binValues[bin] += w;
    }
    TH1F* h_test = new TH1F("testUniform","test uniform",1000,0,15);
    for (int i = 0 ; i<binValues.size() ; i++){
        h_test->SetBinContent(i,binValues[i]);
    }


    /* Plots */
    TCanvas* C = new TCanvas("C","C",1600,600);
    C->Divide(3,1);

    auto pad1 = C->cd(1);
    h->SetTitle("Neural network target;-log_{10}(ME x PDF)");
    h->Draw();
    
    auto pad2 = C->cd(2);
    pad2->SetLogy();
    h_weights->SetTitle("Learning weights;-log_{10}(ME x PDF)");
    h_weights->Draw();
    
    auto pad3 = C->cd(3);
    pad3->SetLogy();
    h_test->SetTitle("Sum of weights;-log_{10}(ME x PDF)");
    h_test->Draw();

    TCanvas* C1 = new TCanvas();
    //C1->SetLogy();
    h_weights->Draw();

    /* Save weight histgram */
    TFile* f_weights= new TFile("weights.root","RECREATE");
    h_weights->Write();
    f_weights->Write();
    f_weights->Close();

}


