#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"

void separate_invalids(const char* dir, TString name){
    /* Paths */
    TString full_name = gSystem->ConcatFileName(dir,name);
    //TString valid_path = "/nfs/scratch/fynu/fbury/MoMEMta_output/valid_weights/";
    TString valid_path = "/nfs/scratch/fynu/fbury/MoMEMta_output/signal_weights_valid/";
    //TString invalid_DY_path = "/nfs/scratch/fynu/fbury/MoMEMta_output/invalid_DY_weights/";
    //TString invalid_TT_path = "/nfs/scratch/fynu/fbury/MoMEMta_output/invalid_TT_weights/";
    
    /* Open tree */
    TFile *f = TFile::Open(full_name);
    TTree *tree = (TTree*)f->Get("tree");

    /* Generate new trees and files */
    TFile *valid_file = new TFile(valid_path+name, "RECREATE");
    TTree *valid_tree = tree->CloneTree(0);
    
    //TFile *invalid_DY_file = new TFile(invalid_DY_path+name, "RECREATE");
    //TTree *invalid_DY_tree = tree->CloneTree(0);

    //TFile *invalid_TT_file = new TFile(invalid_TT_path+name, "RECREATE");
    //TTree *invalid_TT_tree = tree->CloneTree(0);

    auto N = tree->GetEntries();
    
    /* Branch Address */
    //double w_DY, w_DY_err;
    //double w_TT, w_TT_err;
    //tree->SetBranchAddress( "weight_DY" , &w_DY );
    //tree->SetBranchAddress( "weight_DY_err" , &w_DY_err );
    //tree->SetBranchAddress( "weight_TT" , &w_TT );
    //tree->SetBranchAddress( "weight_TT_err" , &w_TT_err );
    std::vector<double> weight_HToZA;
    std::vector<double> weight_HToZA_err;
    for (int i=0; i<23 ; i++){
        weight_HToZA.push_back(0);
        weight_HToZA_err.push_back(0);
    }

    tree->SetBranchAddress( "weight_HToZA_mH_200_mA_50" , &(weight_HToZA[0]) );
    tree->SetBranchAddress( "weight_HToZA_mH_200_mA_100" , &(weight_HToZA[1]) );
    tree->SetBranchAddress( "weight_HToZA_mH_250_mA_50" , &(weight_HToZA[2]) );
    tree->SetBranchAddress( "weight_HToZA_mH_250_mA_100" , &(weight_HToZA[3]) );
    tree->SetBranchAddress( "weight_HToZA_mH_300_mA_50" , &(weight_HToZA[4]) );
    tree->SetBranchAddress( "weight_HToZA_mH_300_mA_100" , &(weight_HToZA[5]) );
    tree->SetBranchAddress( "weight_HToZA_mH_300_mA_200" , &(weight_HToZA[6]) );
    tree->SetBranchAddress( "weight_HToZA_mH_500_mA_50" , &(weight_HToZA[7]) );
    tree->SetBranchAddress( "weight_HToZA_mH_500_mA_100" , &(weight_HToZA[8]) );
    tree->SetBranchAddress( "weight_HToZA_mH_500_mA_200" , &(weight_HToZA[9]) );
    tree->SetBranchAddress( "weight_HToZA_mH_500_mA_300" , &(weight_HToZA[10]) );
    tree->SetBranchAddress( "weight_HToZA_mH_500_mA_400" , &(weight_HToZA[11]) );
    tree->SetBranchAddress( "weight_HToZA_mH_650_mA_50" , &(weight_HToZA[12]) );
    tree->SetBranchAddress( "weight_HToZA_mH_800_mA_50" , &(weight_HToZA[13]) );
    tree->SetBranchAddress( "weight_HToZA_mH_800_mA_100" , &(weight_HToZA[14]) );
    tree->SetBranchAddress( "weight_HToZA_mH_800_mA_200" , &(weight_HToZA[15]) );
    tree->SetBranchAddress( "weight_HToZA_mH_800_mA_400" , &(weight_HToZA[16]) );
    tree->SetBranchAddress( "weight_HToZA_mH_800_mA_700" , &(weight_HToZA[17]) );
    tree->SetBranchAddress( "weight_HToZA_mH_1000_mA_50" , &(weight_HToZA[18]) );
    tree->SetBranchAddress( "weight_HToZA_mH_1000_mA_200" , &(weight_HToZA[19]) );
    tree->SetBranchAddress( "weight_HToZA_mH_1000_mA_500" , &(weight_HToZA[20]) );
    tree->SetBranchAddress( "weight_HToZA_mH_2000_mA_1000" , &(weight_HToZA[21]) );
    tree->SetBranchAddress( "weight_HToZA_mH_3000_mA_2000" , &(weight_HToZA[22]) );

    tree->SetBranchAddress( "weight_HToZA_mH_200_mA_50_err" , &(weight_HToZA_err[0]) );
    tree->SetBranchAddress( "weight_HToZA_mH_200_mA_100_err" , &(weight_HToZA_err[1]) );
    tree->SetBranchAddress( "weight_HToZA_mH_250_mA_50_err" , &(weight_HToZA_err[2]) );
    tree->SetBranchAddress( "weight_HToZA_mH_250_mA_100_err" , &(weight_HToZA_err[3]) );
    tree->SetBranchAddress( "weight_HToZA_mH_300_mA_50_err" , &(weight_HToZA_err[4]) );
    tree->SetBranchAddress( "weight_HToZA_mH_300_mA_100_err" , &(weight_HToZA_err[5]) );
    tree->SetBranchAddress( "weight_HToZA_mH_300_mA_200_err" , &(weight_HToZA_err[6]) );
    tree->SetBranchAddress( "weight_HToZA_mH_500_mA_50_err" , &(weight_HToZA_err[7]) );
    tree->SetBranchAddress( "weight_HToZA_mH_500_mA_100_err" , &(weight_HToZA_err[8]) );
    tree->SetBranchAddress( "weight_HToZA_mH_500_mA_200_err" , &(weight_HToZA_err[9]) );
    tree->SetBranchAddress( "weight_HToZA_mH_500_mA_300_err" , &(weight_HToZA_err[10]) );
    tree->SetBranchAddress( "weight_HToZA_mH_500_mA_400_err" , &(weight_HToZA_err[11]) );
    tree->SetBranchAddress( "weight_HToZA_mH_650_mA_50_err" , &(weight_HToZA_err[12]) );
    tree->SetBranchAddress( "weight_HToZA_mH_800_mA_50_err" , &(weight_HToZA_err[13]) );
    tree->SetBranchAddress( "weight_HToZA_mH_800_mA_100_err" , &(weight_HToZA_err[14]) );
    tree->SetBranchAddress( "weight_HToZA_mH_800_mA_200_err" , &(weight_HToZA_err[15]) );
    tree->SetBranchAddress( "weight_HToZA_mH_800_mA_400_err" , &(weight_HToZA_err[16]) );
    tree->SetBranchAddress( "weight_HToZA_mH_800_mA_700_err" , &(weight_HToZA_err[17]) );
    tree->SetBranchAddress( "weight_HToZA_mH_1000_mA_50_err" , &(weight_HToZA_err[18]) );
    tree->SetBranchAddress( "weight_HToZA_mH_1000_mA_200_err" , &(weight_HToZA_err[19]) );
    tree->SetBranchAddress( "weight_HToZA_mH_1000_mA_500_err" , &(weight_HToZA_err[20]) );
    tree->SetBranchAddress( "weight_HToZA_mH_2000_mA_1000_err" , &(weight_HToZA_err[21]) );
    tree->SetBranchAddress( "weight_HToZA_mH_3000_mA_2000_err" , &(weight_HToZA_err[22]) );


    /* Filling loop */
    bool valid = true;
    for(int i=0 ; i<N ; i++){
        valid = true;
        tree->GetEntry(i);
        //if (w_DY<w_DY_err) 
        //    invalid_DY_tree->Fill();
        //else if (w_TT<w_TT_err)
        //    invalid_TT_tree->Fill(); 
        //else
        //    valid_tree->Fill();
        //std::cout<<i<<"  "<<int(N/100)<<"  "<<i%(int(N/100))<<std::endl;
        for (int j=0 ; j<weight_HToZA.size() ; j++){
            if (weight_HToZA[j]<weight_HToZA_err[j])     
                valid = false;
        }
        if (valid)
            valid_tree->Fill();
        if (i%(int(N/100))==0)
            std::cout<<"Status : "<<float(i)/N*100<<"%"<<std::endl;
    }
    
    /* Write trees */
    valid_file->Write();
    //invalid_DY_file->Write();
   // invalid_TT_file->Write();

    /* Cross section and event_weight_sum */
    TFile input(full_name);
    TObject* cs = input.Get("cross_section");
    TObject* ws = input.Get("event_weight_sum");

    valid_file->cd();
    cs->Write();
    ws->Write();

//    invalid_DY_file->cd();
//    cs->Write();
//    ws->Write();
//
//    invalid_TT_file->cd();
//    cs->Write();
//    ws->Write();
//
    input.Close();
    valid_file->Close();
    //invalid_DY_file->Close();
    //invalid_TT_file->Close();

}
    
