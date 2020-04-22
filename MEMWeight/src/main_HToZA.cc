/*
 *  MoMEMta: a modular implementation of the Matrix Element Method
 *  Copyright (C) 2016  Universite catholique de Louvain (UCL), Belgium
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include <signal.h>
#include <cstdlib>
#include <algorithm>
#include <memory>
#include <string>

#include <gflags/gflags.h>

#include <momemta/ConfigurationReader.h>
#include <momemta/Logging.h>
#include <momemta/MoMEMta.h>
#include <momemta/Unused.h>

#include <chrono>
#include <memory>

// ROOT
#include <TFile.h>
#include <TTree.h>
#include <TParameter.h>
#include <TChain.h>
#include <TTreeReader.h>
#include <TTreeReaderArray.h>
#include <TTreeReaderValue.h>

#include <Math/PtEtaPhiM4D.h>
#include <Math/LorentzVector.h>


using namespace std;
using namespace std::chrono;

using LorentzVectorE = ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiE4D<float>>;

/*
 * Example executable file loading an input sample of events,
 * computing weights using MoMEMta in the fully-leptonic ttbar hypothesis,
 * and saving these weights along with a copy of the event content in an output file.
 */

void normalizeInput(LorentzVector& p4) {
    if (p4.M() > 0)
        return;

    // Increase the energy until M is positive
    p4.SetE(p4.P());
    while (p4.M2() < 0) {
        double delta = p4.E() * 1e-5;
        p4.SetE(p4.E() + delta);
    };
}

// Command line => gflags
DEFINE_string(output, "output.root", "Name of the output file containing the weights");
DEFINE_uint64(from, 0, "First entry to process");
DEFINE_uint64(to, 0, "Last entry to process. If 0, process all the inputs");
DEFINE_bool(verbose, false, "Enable verbose mode");
DEFINE_string(confs_dir, CONFS_DIRECTORY, "Directory containing configurations");
DEFINE_string(input, "input.root", "Name of the input file of the tree");

int main(int argc, char** argv) {

    gflags::ParseCommandLineFlags(&argc, &argv, true);

    if (FLAGS_verbose)
        logging::set_level(logging::level::debug);
    else
        logging::set_level(logging::level::info);

    using std::swap;

    /*
     * Load events from input file, retrieve reconstructed particles and MET
     */
    TChain chain("t");
    //string INPUT_DIR = "/nfs/scratch/fynu/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/skimmed_for_Florian_2019_backgrounds/slurm/output/";
    string INPUT_DIR = "/home/ucl/cp3/fbury/scratch/HToZA_Analysis/backgrounds/";
    //string INPUT_DIR = "/home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/";
    string file = INPUT_DIR+FLAGS_input;
    LOG(info)<<"Directory : "+INPUT_DIR;
    LOG(info)<<"Using file : "+FLAGS_input; 

    bool USE_JEC = false;

    if (USE_JEC)
        LOG(warning)<<"Jet Energy Correction is enabled";

    chain.Add(file.c_str());
    TTreeReader myReader(&chain);

    // TODO : Initial Files -> LorentzVectorE, output LorentzeVector
    TTreeReaderValue<LorentzVectorE> lep_plus_p4E(myReader, "lep1_p4");
    TTreeReaderValue<LorentzVectorE> lep_minus_p4E(myReader, "lep2_p4");
    TTreeReaderValue<LorentzVectorE> jet1_p4E(myReader, "jet1_p4");
    TTreeReaderValue<LorentzVectorE> jet2_p4E(myReader, "jet2_p4");
    // TODO : either float or doubles
    TTreeReaderValue<float> t_w(myReader, "total_weight");
    TTreeReaderValue<float> jjm(myReader, "jj_M");
    TTreeReaderValue<float> lljjm(myReader, "lljj_M");
    TTreeReaderValue<float> llm(myReader, "ll_M");
    TTreeReaderValue<float> m_pt(myReader, "met_pt");
    TTreeReaderValue<float> m_phi(myReader, "met_phi");
    TTreeReaderValue<float> l1c(myReader, "lep1_charge");
    TTreeReaderValue<float> l2c(myReader, "lep2_charge");

    TTreeReaderValue<double> w_200_50(myReader, "weight_HToZA_mH_200_mA_50");
    TTreeReaderValue<double> w_200_50_e(myReader, "weight_HToZA_mH_200_mA_50_err");
    TTreeReaderValue<double> w_200_50_t(myReader, "weight_HToZA_mH_200_mA_50_time");
    TTreeReaderValue<double> w_200_100(myReader, "weight_HToZA_mH_200_mA_100");
    TTreeReaderValue<double> w_200_100_e(myReader, "weight_HToZA_mH_200_mA_100_err");
    TTreeReaderValue<double> w_200_100_t(myReader, "weight_HToZA_mH_200_mA_100_time");
    TTreeReaderValue<double> w_250_50(myReader, "weight_HToZA_mH_250_mA_50");
    TTreeReaderValue<double> w_250_50_e(myReader, "weight_HToZA_mH_250_mA_50_err");
    TTreeReaderValue<double> w_250_50_t(myReader, "weight_HToZA_mH_250_mA_50_time");
    TTreeReaderValue<double> w_250_100(myReader, "weight_HToZA_mH_250_mA_100");
    TTreeReaderValue<double> w_250_100_e(myReader, "weight_HToZA_mH_250_mA_100_err");
    TTreeReaderValue<double> w_250_100_t(myReader, "weight_HToZA_mH_250_mA_100_time");
    TTreeReaderValue<double> w_300_50(myReader, "weight_HToZA_mH_300_mA_50");
    TTreeReaderValue<double> w_300_50_e(myReader, "weight_HToZA_mH_300_mA_50_err");
    TTreeReaderValue<double> w_300_50_t(myReader, "weight_HToZA_mH_300_mA_50_time");
    TTreeReaderValue<double> w_300_100(myReader, "weight_HToZA_mH_300_mA_100");
    TTreeReaderValue<double> w_300_100_e(myReader, "weight_HToZA_mH_300_mA_100_err");
    TTreeReaderValue<double> w_300_100_t(myReader, "weight_HToZA_mH_300_mA_100_time");
    TTreeReaderValue<double> w_300_200(myReader, "weight_HToZA_mH_300_mA_200");
    TTreeReaderValue<double> w_300_200_e(myReader, "weight_HToZA_mH_300_mA_200_err");
    TTreeReaderValue<double> w_300_200_t(myReader, "weight_HToZA_mH_300_mA_200_time");
    TTreeReaderValue<double> w_500_50(myReader, "weight_HToZA_mH_500_mA_50");
    TTreeReaderValue<double> w_500_50_e(myReader, "weight_HToZA_mH_500_mA_50_err");
    TTreeReaderValue<double> w_500_50_t(myReader, "weight_HToZA_mH_500_mA_50_time");
    TTreeReaderValue<double> w_500_100(myReader, "weight_HToZA_mH_500_mA_100");
    TTreeReaderValue<double> w_500_100_e(myReader, "weight_HToZA_mH_500_mA_100_err");
    TTreeReaderValue<double> w_500_100_t(myReader, "weight_HToZA_mH_500_mA_100_time");
    TTreeReaderValue<double> w_500_200(myReader, "weight_HToZA_mH_500_mA_200");
    TTreeReaderValue<double> w_500_200_e(myReader, "weight_HToZA_mH_500_mA_200_err");
    TTreeReaderValue<double> w_500_200_t(myReader, "weight_HToZA_mH_500_mA_200_time");
    TTreeReaderValue<double> w_500_300(myReader, "weight_HToZA_mH_500_mA_300");
    TTreeReaderValue<double> w_500_300_e(myReader, "weight_HToZA_mH_500_mA_300_err");
    TTreeReaderValue<double> w_500_300_t(myReader, "weight_HToZA_mH_500_mA_300_time");
    TTreeReaderValue<double> w_500_400(myReader, "weight_HToZA_mH_500_mA_400");
    TTreeReaderValue<double> w_500_400_e(myReader, "weight_HToZA_mH_500_mA_400_err");
    TTreeReaderValue<double> w_500_400_t(myReader, "weight_HToZA_mH_500_mA_400_time");
    TTreeReaderValue<double> w_650_50(myReader, "weight_HToZA_mH_650_mA_50");
    TTreeReaderValue<double> w_650_50_e(myReader, "weight_HToZA_mH_650_mA_50_err");
    TTreeReaderValue<double> w_650_50_t(myReader, "weight_HToZA_mH_650_mA_50_time");
    TTreeReaderValue<double> w_800_50(myReader, "weight_HToZA_mH_800_mA_50");
    TTreeReaderValue<double> w_800_50_e(myReader, "weight_HToZA_mH_800_mA_50_err");
    TTreeReaderValue<double> w_800_50_t(myReader, "weight_HToZA_mH_800_mA_50_time");
    TTreeReaderValue<double> w_800_100(myReader, "weight_HToZA_mH_800_mA_100");
    TTreeReaderValue<double> w_800_100_e(myReader, "weight_HToZA_mH_800_mA_100_err");
    TTreeReaderValue<double> w_800_100_t(myReader, "weight_HToZA_mH_800_mA_100_time");
    TTreeReaderValue<double> w_800_200(myReader, "weight_HToZA_mH_800_mA_200");
    TTreeReaderValue<double> w_800_200_e(myReader, "weight_HToZA_mH_800_mA_200_err");
    TTreeReaderValue<double> w_800_200_t(myReader, "weight_HToZA_mH_800_mA_200_time");
    TTreeReaderValue<double> w_800_400(myReader, "weight_HToZA_mH_800_mA_400");
    TTreeReaderValue<double> w_800_400_e(myReader, "weight_HToZA_mH_800_mA_400_err");
    TTreeReaderValue<double> w_800_400_t(myReader, "weight_HToZA_mH_800_mA_400_time");
    TTreeReaderValue<double> w_800_700(myReader, "weight_HToZA_mH_800_mA_700");
    TTreeReaderValue<double> w_800_700_e(myReader, "weight_HToZA_mH_800_mA_700_err");
    TTreeReaderValue<double> w_800_700_t(myReader, "weight_HToZA_mH_800_mA_700_time");
    TTreeReaderValue<double> w_1000_50(myReader, "weight_HToZA_mH_1000_mA_50");
    TTreeReaderValue<double> w_1000_50_e(myReader, "weight_HToZA_mH_1000_mA_50_err");
    TTreeReaderValue<double> w_1000_50_t(myReader, "weight_HToZA_mH_1000_mA_50_time");
    TTreeReaderValue<double> w_1000_200(myReader, "weight_HToZA_mH_1000_mA_200");
    TTreeReaderValue<double> w_1000_200_e(myReader, "weight_HToZA_mH_1000_mA_200_err");
    TTreeReaderValue<double> w_1000_200_t(myReader, "weight_HToZA_mH_1000_mA_200_time");
    TTreeReaderValue<double> w_1000_500(myReader, "weight_HToZA_mH_1000_mA_500");
    TTreeReaderValue<double> w_1000_500_e(myReader, "weight_HToZA_mH_1000_mA_500_err");
    TTreeReaderValue<double> w_1000_500_t(myReader, "weight_HToZA_mH_1000_mA_500_time");
    TTreeReaderValue<double> w_2000_1000(myReader, "weight_HToZA_mH_2000_mA_1000");
    TTreeReaderValue<double> w_2000_1000_e(myReader, "weight_HToZA_mH_2000_mA_1000_err");
    TTreeReaderValue<double> w_2000_1000_t(myReader, "weight_HToZA_mH_2000_mA_1000_time");
    TTreeReaderValue<double> w_3000_2000(myReader, "weight_HToZA_mH_3000_mA_2000");
    TTreeReaderValue<double> w_3000_2000_e(myReader, "weight_HToZA_mH_3000_mA_2000_err");
    TTreeReaderValue<double> w_3000_2000_t(myReader, "weight_HToZA_mH_3000_mA_2000_time");

    /*
     * Define output TTree, which will be a clone of the input tree,
     * with the addition of the weights we're computing (including uncertainty and computation time)
     */
    TFile *output = TFile::Open(FLAGS_output.c_str(), "recreate");
    TTree* out_tree = new TTree("tree", "tree");
    LorentzVector lep1_p4,lep2_p4,jet1_p4,jet2_p4;
    float total_weight,event_weight,jj_M,lljj_M,ll_M,met_pt,met_phi,lep1_charge,lep2_charge;
    out_tree->Branch("lep1_p4", &lep1_p4);
    out_tree->Branch("lep2_p4", &lep2_p4);
    out_tree->Branch("jet1_p4", &jet1_p4);
    out_tree->Branch("jet2_p4", &jet2_p4);
    out_tree->Branch("total_weight", &total_weight);
    out_tree->Branch("event_weight", &event_weight);
    out_tree->Branch("jj_M", &jj_M);
    out_tree->Branch("lljj_M", &lljj_M);
    out_tree->Branch("ll_M", &ll_M);
    out_tree->Branch("met_pt", &met_pt);
    out_tree->Branch("met_phi", &met_phi);
    out_tree->Branch("lep1_charge", &lep1_charge);
    out_tree->Branch("lep2_charge", &lep2_charge);

    double weight_HToZA_mH_200_mA_50, weight_HToZA_mH_200_mA_50_err, weight_HToZA_mH_200_mA_50_time;
    double weight_HToZA_mH_200_mA_100, weight_HToZA_mH_200_mA_100_err, weight_HToZA_mH_200_mA_100_time;
    double weight_HToZA_mH_250_mA_50, weight_HToZA_mH_250_mA_50_err, weight_HToZA_mH_250_mA_50_time;
    double weight_HToZA_mH_250_mA_100, weight_HToZA_mH_250_mA_100_err, weight_HToZA_mH_250_mA_100_time;
    double weight_HToZA_mH_300_mA_50, weight_HToZA_mH_300_mA_50_err, weight_HToZA_mH_300_mA_50_time;
    double weight_HToZA_mH_300_mA_100, weight_HToZA_mH_300_mA_100_err, weight_HToZA_mH_300_mA_100_time;
    double weight_HToZA_mH_300_mA_200, weight_HToZA_mH_300_mA_200_err, weight_HToZA_mH_300_mA_200_time;
    double weight_HToZA_mH_500_mA_50, weight_HToZA_mH_500_mA_50_err, weight_HToZA_mH_500_mA_50_time;
    double weight_HToZA_mH_500_mA_100, weight_HToZA_mH_500_mA_100_err, weight_HToZA_mH_500_mA_100_time;
    double weight_HToZA_mH_500_mA_200, weight_HToZA_mH_500_mA_200_err, weight_HToZA_mH_500_mA_200_time;
    double weight_HToZA_mH_500_mA_300, weight_HToZA_mH_500_mA_300_err, weight_HToZA_mH_500_mA_300_time;
    double weight_HToZA_mH_500_mA_400, weight_HToZA_mH_500_mA_400_err, weight_HToZA_mH_500_mA_400_time;
    double weight_HToZA_mH_650_mA_50, weight_HToZA_mH_650_mA_50_err, weight_HToZA_mH_650_mA_50_time;
    double weight_HToZA_mH_800_mA_50, weight_HToZA_mH_800_mA_50_err, weight_HToZA_mH_800_mA_50_time;
    double weight_HToZA_mH_800_mA_100, weight_HToZA_mH_800_mA_100_err, weight_HToZA_mH_800_mA_100_time;
    double weight_HToZA_mH_800_mA_200, weight_HToZA_mH_800_mA_200_err, weight_HToZA_mH_800_mA_200_time;
    double weight_HToZA_mH_800_mA_400, weight_HToZA_mH_800_mA_400_err, weight_HToZA_mH_800_mA_400_time;
    double weight_HToZA_mH_800_mA_700, weight_HToZA_mH_800_mA_700_err, weight_HToZA_mH_800_mA_700_time;
    double weight_HToZA_mH_1000_mA_50, weight_HToZA_mH_1000_mA_50_err, weight_HToZA_mH_1000_mA_50_time;
    double weight_HToZA_mH_1000_mA_200, weight_HToZA_mH_1000_mA_200_err, weight_HToZA_mH_1000_mA_200_time;
    double weight_HToZA_mH_1000_mA_500, weight_HToZA_mH_1000_mA_500_err, weight_HToZA_mH_1000_mA_500_time;
    double weight_HToZA_mH_2000_mA_1000, weight_HToZA_mH_2000_mA_1000_err, weight_HToZA_mH_2000_mA_1000_time;
    double weight_HToZA_mH_3000_mA_2000, weight_HToZA_mH_3000_mA_2000_err, weight_HToZA_mH_3000_mA_2000_time;

    out_tree->Branch("weight_HToZA_mH_200_mA_50",&weight_HToZA_mH_200_mA_50);
    out_tree->Branch("weight_HToZA_mH_200_mA_50_err",&weight_HToZA_mH_200_mA_50_err);
    out_tree->Branch("weight_HToZA_mH_200_mA_50_time",&weight_HToZA_mH_200_mA_50_time);
    out_tree->Branch("weight_HToZA_mH_200_mA_100",&weight_HToZA_mH_200_mA_100);
    out_tree->Branch("weight_HToZA_mH_200_mA_100_err",&weight_HToZA_mH_200_mA_100_err);
    out_tree->Branch("weight_HToZA_mH_200_mA_100_time",&weight_HToZA_mH_200_mA_100_time);
    out_tree->Branch("weight_HToZA_mH_250_mA_50",&weight_HToZA_mH_250_mA_50);
    out_tree->Branch("weight_HToZA_mH_250_mA_50_err",&weight_HToZA_mH_250_mA_50_err);
    out_tree->Branch("weight_HToZA_mH_250_mA_50_time",&weight_HToZA_mH_250_mA_50_time);
    out_tree->Branch("weight_HToZA_mH_250_mA_100",&weight_HToZA_mH_250_mA_100);
    out_tree->Branch("weight_HToZA_mH_250_mA_100_err",&weight_HToZA_mH_250_mA_100_err);
    out_tree->Branch("weight_HToZA_mH_250_mA_100_time",&weight_HToZA_mH_250_mA_100_time);
    out_tree->Branch("weight_HToZA_mH_300_mA_50",&weight_HToZA_mH_300_mA_50);
    out_tree->Branch("weight_HToZA_mH_300_mA_50_err",&weight_HToZA_mH_300_mA_50_err);
    out_tree->Branch("weight_HToZA_mH_300_mA_50_time",&weight_HToZA_mH_300_mA_50_time);
    out_tree->Branch("weight_HToZA_mH_300_mA_100",&weight_HToZA_mH_300_mA_100);
    out_tree->Branch("weight_HToZA_mH_300_mA_100_err",&weight_HToZA_mH_300_mA_100_err);
    out_tree->Branch("weight_HToZA_mH_300_mA_100_time",&weight_HToZA_mH_300_mA_100_time);
    out_tree->Branch("weight_HToZA_mH_300_mA_200",&weight_HToZA_mH_300_mA_200);
    out_tree->Branch("weight_HToZA_mH_300_mA_200_err",&weight_HToZA_mH_300_mA_200_err);
    out_tree->Branch("weight_HToZA_mH_300_mA_200_time",&weight_HToZA_mH_300_mA_200_time);
    out_tree->Branch("weight_HToZA_mH_500_mA_50",&weight_HToZA_mH_500_mA_50);
    out_tree->Branch("weight_HToZA_mH_500_mA_50_err",&weight_HToZA_mH_500_mA_50_err);
    out_tree->Branch("weight_HToZA_mH_500_mA_50_time",&weight_HToZA_mH_500_mA_50_time);
    out_tree->Branch("weight_HToZA_mH_500_mA_100",&weight_HToZA_mH_500_mA_100);
    out_tree->Branch("weight_HToZA_mH_500_mA_100_err",&weight_HToZA_mH_500_mA_100_err);
    out_tree->Branch("weight_HToZA_mH_500_mA_100_time",&weight_HToZA_mH_500_mA_100_time);
    out_tree->Branch("weight_HToZA_mH_500_mA_200",&weight_HToZA_mH_500_mA_200);
    out_tree->Branch("weight_HToZA_mH_500_mA_200_err",&weight_HToZA_mH_500_mA_200_err);
    out_tree->Branch("weight_HToZA_mH_500_mA_200_time",&weight_HToZA_mH_500_mA_200_time);
    out_tree->Branch("weight_HToZA_mH_500_mA_300",&weight_HToZA_mH_500_mA_300);
    out_tree->Branch("weight_HToZA_mH_500_mA_300_err",&weight_HToZA_mH_500_mA_300_err);
    out_tree->Branch("weight_HToZA_mH_500_mA_300_time",&weight_HToZA_mH_500_mA_300_time);
    out_tree->Branch("weight_HToZA_mH_500_mA_400",&weight_HToZA_mH_500_mA_400);
    out_tree->Branch("weight_HToZA_mH_500_mA_400_err",&weight_HToZA_mH_500_mA_400_err);
    out_tree->Branch("weight_HToZA_mH_500_mA_400_time",&weight_HToZA_mH_500_mA_400_time);
    out_tree->Branch("weight_HToZA_mH_650_mA_50",&weight_HToZA_mH_650_mA_50);
    out_tree->Branch("weight_HToZA_mH_650_mA_50_err",&weight_HToZA_mH_650_mA_50_err);
    out_tree->Branch("weight_HToZA_mH_650_mA_50_time",&weight_HToZA_mH_650_mA_50_time);
    out_tree->Branch("weight_HToZA_mH_800_mA_50",&weight_HToZA_mH_800_mA_50);
    out_tree->Branch("weight_HToZA_mH_800_mA_50_err",&weight_HToZA_mH_800_mA_50_err);
    out_tree->Branch("weight_HToZA_mH_800_mA_50_time",&weight_HToZA_mH_800_mA_50_time);
    out_tree->Branch("weight_HToZA_mH_800_mA_100",&weight_HToZA_mH_800_mA_100);
    out_tree->Branch("weight_HToZA_mH_800_mA_100_err",&weight_HToZA_mH_800_mA_100_err);
    out_tree->Branch("weight_HToZA_mH_800_mA_100_time",&weight_HToZA_mH_800_mA_100_time);
    out_tree->Branch("weight_HToZA_mH_800_mA_200",&weight_HToZA_mH_800_mA_200);
    out_tree->Branch("weight_HToZA_mH_800_mA_200_err",&weight_HToZA_mH_800_mA_200_err);
    out_tree->Branch("weight_HToZA_mH_800_mA_200_time",&weight_HToZA_mH_800_mA_200_time);
    out_tree->Branch("weight_HToZA_mH_800_mA_400",&weight_HToZA_mH_800_mA_400);
    out_tree->Branch("weight_HToZA_mH_800_mA_400_err",&weight_HToZA_mH_800_mA_400_err);
    out_tree->Branch("weight_HToZA_mH_800_mA_400_time",&weight_HToZA_mH_800_mA_400_time);
    out_tree->Branch("weight_HToZA_mH_800_mA_700",&weight_HToZA_mH_800_mA_700);
    out_tree->Branch("weight_HToZA_mH_800_mA_700_err",&weight_HToZA_mH_800_mA_700_err);
    out_tree->Branch("weight_HToZA_mH_800_mA_700_time",&weight_HToZA_mH_800_mA_700_time);
    out_tree->Branch("weight_HToZA_mH_1000_mA_50",&weight_HToZA_mH_1000_mA_50);
    out_tree->Branch("weight_HToZA_mH_1000_mA_50_err",&weight_HToZA_mH_1000_mA_50_err);
    out_tree->Branch("weight_HToZA_mH_1000_mA_50_time",&weight_HToZA_mH_1000_mA_50_time);
    out_tree->Branch("weight_HToZA_mH_1000_mA_200",&weight_HToZA_mH_1000_mA_200);
    out_tree->Branch("weight_HToZA_mH_1000_mA_200_err",&weight_HToZA_mH_1000_mA_200_err);
    out_tree->Branch("weight_HToZA_mH_1000_mA_200_time",&weight_HToZA_mH_1000_mA_200_time);
    out_tree->Branch("weight_HToZA_mH_1000_mA_500",&weight_HToZA_mH_1000_mA_500);
    out_tree->Branch("weight_HToZA_mH_1000_mA_500_err",&weight_HToZA_mH_1000_mA_500_err);
    out_tree->Branch("weight_HToZA_mH_1000_mA_500_time",&weight_HToZA_mH_1000_mA_500_time);
    out_tree->Branch("weight_HToZA_mH_2000_mA_1000",&weight_HToZA_mH_2000_mA_1000);
    out_tree->Branch("weight_HToZA_mH_2000_mA_1000_err",&weight_HToZA_mH_2000_mA_1000_err);
    out_tree->Branch("weight_HToZA_mH_2000_mA_1000_time",&weight_HToZA_mH_2000_mA_1000_time);
    out_tree->Branch("weight_HToZA_mH_3000_mA_2000",&weight_HToZA_mH_3000_mA_2000);
    out_tree->Branch("weight_HToZA_mH_3000_mA_2000_err",&weight_HToZA_mH_3000_mA_2000_err);
    out_tree->Branch("weight_HToZA_mH_3000_mA_2000_time",&weight_HToZA_mH_3000_mA_2000_time);

    bool is_JEC;
    if (USE_JEC==true){
        out_tree->Branch("is_JEC", &is_JEC);
    }


    /* Generate map for the HToZA config */
    std::map<std::pair<double,double>,double> weight;
    std::map<std::pair<double,double>,double> err;
    std::map<std::pair<double,double>,double> time;
    weight[std::make_pair(200,50)] = 0;    err[std::make_pair(200,50)] = 0;    time[std::make_pair(200,50)] = 0;
    weight[std::make_pair(200,100)] = 0;   err[std::make_pair(200,100)] = 0;   time[std::make_pair(200,100)] = 0;
    weight[std::make_pair(250,50)] = 0;    err[std::make_pair(250,50)] = 0;    time[std::make_pair(250,50)] = 0;
    weight[std::make_pair(250,100)] = 0;   err[std::make_pair(250,100)] = 0;   time[std::make_pair(250,100)] = 0;
    weight[std::make_pair(300,50)] = 0;    err[std::make_pair(300,50)] = 0;    time[std::make_pair(300,50)] = 0;
    weight[std::make_pair(300,100)] = 0;   err[std::make_pair(300,100)] = 0;   time[std::make_pair(300,100)] = 0;
    weight[std::make_pair(300,200)] = 0;   err[std::make_pair(300,200)] = 0;   time[std::make_pair(300,200)] = 0;
    weight[std::make_pair(500,50)] = 0;    err[std::make_pair(500,50)] = 0;    time[std::make_pair(500,50)] = 0;
    weight[std::make_pair(500,100)] = 0;   err[std::make_pair(500,100)] = 0;   time[std::make_pair(500,100)] = 0;
    weight[std::make_pair(500,200)] = 0;   err[std::make_pair(500,200)] = 0;   time[std::make_pair(500,200)] = 0;
    weight[std::make_pair(500,300)] = 0;   err[std::make_pair(500,300)] = 0;   time[std::make_pair(500,300)] = 0;
    weight[std::make_pair(500,400)] = 0;   err[std::make_pair(500,400)] = 0;   time[std::make_pair(500,400)] = 0;
    weight[std::make_pair(600,250)] = 0;   err[std::make_pair(600,250)] = 0;   time[std::make_pair(600,250)] = 0;
    weight[std::make_pair(650,50)] = 0;    err[std::make_pair(650,50)] = 0;    time[std::make_pair(650,50)] = 0;
    weight[std::make_pair(800,50)] = 0;    err[std::make_pair(800,50)] = 0;    time[std::make_pair(800,50)] = 0;
    weight[std::make_pair(800,100)] = 0;   err[std::make_pair(800,100)] = 0;   time[std::make_pair(800,100)] = 0;
    weight[std::make_pair(800,200)] = 0;   err[std::make_pair(800,200)] = 0;   time[std::make_pair(800,200)] = 0;
    weight[std::make_pair(800,400)] = 0;   err[std::make_pair(800,400)] = 0;   time[std::make_pair(800,400)] = 0;
    weight[std::make_pair(800,700)] = 0;   err[std::make_pair(800,700)] = 0;   time[std::make_pair(800,700)] = 0;
    weight[std::make_pair(1000,50)] = 0;   err[std::make_pair(1000,50)] = 0;   time[std::make_pair(1000,50)] = 0;
    weight[std::make_pair(1000,200)] = 0;  err[std::make_pair(1000,200)] = 0;  time[std::make_pair(1000,200)] = 0;
    weight[std::make_pair(1000,500)] = 0;  err[std::make_pair(1000,500)] = 0;  time[std::make_pair(1000,500)] = 0;
    weight[std::make_pair(2000,1000)] = 0; err[std::make_pair(2000,1000)] = 0; time[std::make_pair(2000,1000)] = 0;
    weight[std::make_pair(3000,2000)] = 0; err[std::make_pair(3000,2000)] = 0; time[std::make_pair(3000,2000)] = 0;
    for (auto const& x : weight){
        std::string name;
        name.append("weight_HToZA_mH_");
        name.append(std::to_string(int(x.first.first)));
        name.append("_mA_");
        name.append(std::to_string(int(x.first.second)));
        out_tree->Branch(name.c_str(), &(weight[x.first]));
    } 
    for (auto const& x : err){
        std::string name;
        name.append("weight_HToZA_mH_");
        name.append(std::to_string(int(x.first.first)));
        name.append("_mA_");
        name.append(std::to_string(int(x.first.second)));
        name.append("_err");
        out_tree->Branch(name.c_str(), &(err[x.first]));
    } 
    for (auto const& x : time){
        std::string name;
        name.append("weight_HToZA_mH_");
        name.append(std::to_string(int(x.first.first)));
        name.append("_mA_");
        name.append(std::to_string(int(x.first.second)));
        name.append("_time");
        out_tree->Branch(name.c_str(), &(time[x.first]));
    }  



    /*
     * Prepare MoMEMta to compute the weights
     */

    // Construct the ConfigurationReader from the Lua file
    LOG(info) << "Reading configuration files from '" << FLAGS_confs_dir << "'";

    int rand_num = rand()%1000;
    int n_start  = 20000;
    int max_eval = 1000000;
    ParameterSet lua_parameters;
    lua_parameters.set("random", rand_num);
    lua_parameters.set("n_start", n_start);
    lua_parameters.set("max_eval", max_eval);
    LOG(info)<<"Random number for seed : "<<rand_num;
    LOG(info)<<"Starting eval : "<<n_start<<"\tMax eval : "<<max_eval;

    // To and From parameters
    size_t to = 0;
    if (FLAGS_to > 0)
        to = FLAGS_to;
    else
        to = chain.GetEntries();

    size_t from = 0;
    if (FLAGS_from > 0)
        from = std::max(from, FLAGS_from);

    if (from >= to) {
        LOG(fatal) << "First entry to process is greater than the total number of entries (" << from << " >= " << to << ")";
        abort();
    }

    myReader.SetEntriesRange(from, to);

    size_t selected = 0;
    LOG(info) << "Processing " << to - from << " entries, from " << from << " to " << to;

    /*
     * Loop over all input events
     */
    bool JEC_apply = false; // wether to redo the event with the JEC
    bool last_entry = false; // to get the last entry done again with JEC

    while (myReader.Next()) {
        if (USE_JEC && JEC_apply && !last_entry)
            myReader.SetEntry(myReader.GetCurrentEntry()-1); // redo the same event with JEC

        LOG(info) << "=====================================================================";
        LOG(info) << "Processing entry " << myReader.GetCurrentEntry() << " up to " << to;
        selected++;
        /*
         * Prepare the LorentzVectors passed to MoMEMta:
         * In the input file they are written in the PtEtaPhiM<float> basis,
         * while MoMEMta expects PxPyPzE<double>, so we have to perform this change of basis:
         *
         * We define here Particles, allowing MoMEMta to correctly map the inputs to the configuration file.
         * The string identifier used here must be the same as used to declare the inputs in the config file
         */
        lep1_p4 = LorentzVector { lep_plus_p4E->Px(), lep_plus_p4E->Py(), lep_plus_p4E->Pz(), lep_plus_p4E->E() };
        lep2_p4 = LorentzVector { lep_minus_p4E->Px(), lep_minus_p4E->Py(), lep_minus_p4E->Pz(), lep_minus_p4E->E() };
        jet1_p4 = LorentzVector { jet1_p4E->Px(), jet1_p4E->Py(), jet1_p4E->Pz(), jet1_p4E->E() };
        jet2_p4 = LorentzVector { jet2_p4E->Px(), jet2_p4E->Py(), jet2_p4E->Pz(), jet2_p4E->E() };
        LorentzVectorE met_p4E { *m_pt, 0, *m_phi, *m_pt };
        LorentzVector met_p4 { met_p4E.Px(), met_p4E.Py(), met_p4E.Pz(), met_p4E.E() };
        momemta::Particle lep_plus("lepton1", lep1_p4);
        momemta::Particle lep_minus("lepton2", lep2_p4);
        momemta::Particle bjet1("bjet1", jet1_p4);
        momemta::Particle bjet2("bjet2", jet2_p4);
        LorentzVector isr_p4;
        isr_p4 = -(lep1_p4+lep2_p4+jet1_p4+jet2_p4);
        isr_p4.SetE(std::abs(isr_p4.E()));
        momemta::Particle isr ("isr", isr_p4);

        // JEC to bjets #
        if (USE_JEC==true){
            if (JEC_apply){
                LOG(info)<<"JEC has been applied";
                auto temp1 = LorentzVectorE {jet1_p4.Pt(),jet1_p4.Eta(),jet1_p4.Phi(),jet1_p4.M()};
                auto temp2 = LorentzVectorE {jet2_p4.Pt(),jet2_p4.Eta(),jet2_p4.Phi(),jet2_p4.M()};
                auto previous_Pt_1 = jet1_p4.Pt();
                auto previous_Pt_2 = jet2_p4.Pt();
                temp1.SetPt(jet1_p4.Pt()*1.1);
                temp2.SetPt(jet2_p4.Pt()*1.1);
                jet1_p4 = LorentzVector { temp1.Px(), temp1.Py(), temp1.Pz(), temp1.E() };
                jet2_p4 = LorentzVector { temp2.Px(), temp2.Py(), temp2.Pz(), temp2.E() };
                LOG(info)<<"Jet1 Pt : "<<previous_Pt_1<<" -> "<<jet1_p4.Pt();
                LOG(info)<<"Jet2 Pt : "<<previous_Pt_2<<" -> "<<jet2_p4.Pt();
                JEC_apply = false; // Will not repeat the event
            }   
            else{
                LOG(info)<<"JEC has not been applied";
                LOG(info)<<"Jet1 Pt : "<<jet1_p4.Pt();
                LOG(info)<<"Jet2 Pt : "<<jet2_p4.Pt();
                JEC_apply = true; // Will repeat the event and apply the JEC
            }
        }

        // Due to numerical instability, the mass can sometimes be negative. If it's the case, change the energy in order to be mass-positive
        normalizeInput(lep_plus.p4);
        normalizeInput(lep_minus.p4);
        normalizeInput(bjet1.p4);
        normalizeInput(bjet2.p4);
        normalizeInput(isr.p4);

        // Ensure the leptons are given in the correct order w.r.t their charge 
        if (*l1c < 0) // if first lepton is negatively charge, swap them
            swap(lep_plus, lep_minus);

        // Compute the weights!

        // HToZA weights 
        if (FLAGS_process == "HToZA"){
            LOG(info) << "---------------------------------------------------------------------";
            LOG(info)<<"Starting HToZA weight computation";

            for (auto & x : weight){
                auto mH = x.first.first;
                auto mA = x.first.second;
                auto key = x.first;
                LOG(info) << "\tMH = "<<std::to_string(mH)<<" MA = "<<std::to_string(mA);

                ParameterSet lua_parameters;
                lua_parameters.set("random", rand_num);
                lua_parameters.set("n_start", n_start);
                lua_parameters.set("max_eval", max_eval);
                lua_parameters.set("mH", mH);
                lua_parameters.set("mA", mA);

                ConfigurationReader configuration_HToZA(FLAGS_confs_dir + "htoza_llbb.lua",lua_parameters); // needs to be called here so that we can change the masses
                    // TODO : one instantiation per mass point

                // Instantiate MoMEMta using a **frozen** configuration
                MoMEMta HToZA_weight(configuration_HToZA.freeze());

                // Retrieve the weight and uncertainty for HToZA
                auto start_time_HToZA = system_clock::now();
                std::vector<std::pair<double, double>> HToZA_weights = HToZA_weight.computeWeights({lep_minus, lep_plus, bjet1, bjet2});
                auto end_time_HToZA = system_clock::now();

                weight[key] = HToZA_weights.back().first;
                err[key] = HToZA_weights.back().second;
                time[key] = std::chrono::duration_cast<milliseconds>(end_time_HToZA - start_time_HToZA).count();

                LOG(info)<<" -> HToZA result: " << HToZA_weights.back().first<< " +- " << HToZA_weights.back().second;
                LOG(info) << "Weight computed in " << std::chrono::duration_cast<milliseconds>(end_time_HToZA - start_time_HToZA).count()<< "ms";
            }
        }

        // Other values in branches
        total_weight = *t_w;
        //event_weight = *e_w;
        jj_M = *jjm;
        lljj_M = *lljjm;
        ll_M = *llm;
        met_pt = *m_pt;
        met_phi = *m_phi;
        lep1_charge = *l1c;
        lep2_charge = *l2c;

        weight_HToZA_mH_200_mA_50         = *w_200_50 ;
        weight_HToZA_mH_200_mA_50_err     = *w_200_50_e;
        weight_HToZA_mH_200_mA_50_time    = *w_200_50_t;
        weight_HToZA_mH_200_mA_100        = *w_200_100;
        weight_HToZA_mH_200_mA_100_err    = *w_200_100_e;
        weight_HToZA_mH_200_mA_100_time   = *w_200_100_t;
        weight_HToZA_mH_250_mA_50         = *w_250_50;
        weight_HToZA_mH_250_mA_50_err     = *w_250_50_e;
        weight_HToZA_mH_250_mA_50_time    = *w_250_50_t;
        weight_HToZA_mH_250_mA_100        = *w_250_100;
        weight_HToZA_mH_250_mA_100_err    = *w_250_100_e;
        weight_HToZA_mH_250_mA_100_time   = *w_250_100_t;
        weight_HToZA_mH_300_mA_50         = *w_300_50;
        weight_HToZA_mH_300_mA_50_err     = *w_300_50_e;
        weight_HToZA_mH_300_mA_50_time    = *w_300_50_t;
        weight_HToZA_mH_300_mA_100        = *w_300_100;
        weight_HToZA_mH_300_mA_100_err    = *w_300_100_e;
        weight_HToZA_mH_300_mA_100_time   = *w_300_100_t;
        weight_HToZA_mH_300_mA_200        = *w_300_200;
        weight_HToZA_mH_300_mA_200_err    = *w_300_200_e;
        weight_HToZA_mH_300_mA_200_time   = *w_300_200_t;
        weight_HToZA_mH_500_mA_50         = *w_500_50;
        weight_HToZA_mH_500_mA_50_err     = *w_500_50_e;
        weight_HToZA_mH_500_mA_50_time    = *w_500_50_t;
        weight_HToZA_mH_500_mA_100        = *w_500_100;
        weight_HToZA_mH_500_mA_100_err    = *w_500_100_e;
        weight_HToZA_mH_500_mA_100_time   = *w_500_100_t;
        weight_HToZA_mH_500_mA_200        = *w_500_200;
        weight_HToZA_mH_500_mA_200_err    = *w_500_200_e;
        weight_HToZA_mH_500_mA_200_time   = *w_500_200_t;
        weight_HToZA_mH_500_mA_300        = *w_500_300;
        weight_HToZA_mH_500_mA_300_err    = *w_500_300_e;
        weight_HToZA_mH_500_mA_300_time   = *w_500_300_t;
        weight_HToZA_mH_500_mA_400        = *w_500_400;
        weight_HToZA_mH_500_mA_400_err    = *w_500_400_e;
        weight_HToZA_mH_500_mA_400_time   = *w_500_400_t;
        weight_HToZA_mH_650_mA_50         = *w_650_50;
        weight_HToZA_mH_650_mA_50_err     = *w_650_50_e;
        weight_HToZA_mH_650_mA_50_time    = *w_650_50_t;
        weight_HToZA_mH_800_mA_50         = *w_800_50;
        weight_HToZA_mH_800_mA_50_err     = *w_800_50_e;
        weight_HToZA_mH_800_mA_50_time    = *w_800_50_t;
        weight_HToZA_mH_800_mA_100        = *w_800_100;
        weight_HToZA_mH_800_mA_100_err    = *w_800_100_e;
        weight_HToZA_mH_800_mA_100_time   = *w_800_100_t;
        weight_HToZA_mH_800_mA_200        = *w_800_200;
        weight_HToZA_mH_800_mA_200_err    = *w_800_200_e;
        weight_HToZA_mH_800_mA_200_time   = *w_800_200_t;
        weight_HToZA_mH_800_mA_400        = *w_800_400;
        weight_HToZA_mH_800_mA_400_err    = *w_800_400_e;
        weight_HToZA_mH_800_mA_400_time   = *w_800_400_t;
        weight_HToZA_mH_800_mA_700        = *w_800_700;
        weight_HToZA_mH_800_mA_700_err    = *w_800_700_e;
        weight_HToZA_mH_800_mA_700_time   = *w_800_700_t;
        weight_HToZA_mH_1000_mA_50        = *w_1000_50;
        weight_HToZA_mH_1000_mA_50_err    = *w_1000_50_e;
        weight_HToZA_mH_1000_mA_50_time   = *w_1000_50_t;
        weight_HToZA_mH_1000_mA_200       = *w_1000_200;
        weight_HToZA_mH_1000_mA_200_err   = *w_1000_200_e;
        weight_HToZA_mH_1000_mA_200_time  = *w_1000_200_t;
        weight_HToZA_mH_1000_mA_500       = *w_1000_500;
        weight_HToZA_mH_1000_mA_500_err   = *w_1000_500_e;
        weight_HToZA_mH_1000_mA_500_time  = *w_1000_500_t;
        weight_HToZA_mH_2000_mA_1000      = *w_2000_1000;
        weight_HToZA_mH_2000_mA_1000_err  = *w_2000_1000_e;
        weight_HToZA_mH_2000_mA_1000_time = *w_2000_1000_t;
        weight_HToZA_mH_3000_mA_2000      = *w_3000_2000;
        weight_HToZA_mH_3000_mA_2000_err  = *w_3000_2000_e;
        weight_HToZA_mH_3000_mA_2000_time = *w_3000_2000_t;


        if (USE_JEC){
            if (JEC_apply){
                is_JEC = false; 
                if (myReader.GetCurrentEntry() == to-1){
                    myReader.SetEntry(myReader.GetCurrentEntry()-1);
                    last_entry = true;
                }
            }
            else
                is_JEC = true;
        }

        LOG(debug) << "Filling tree...";
        out_tree->Fill();
        LOG(debug) << "Done, next event";
    }

    // Save our output TTree
    LOG(info) << "Processing done: " << selected << " selected events";

    output->cd();

    out_tree->Write();

    TFile input(file.c_str());
    TObject* cs = input.Get("cross_section");
    TObject* ws = input.Get("event_weight_sum");
    output->cd();
    cs->Write();
    ws->Write();
    input.Close();

    output->Close();

    delete output;

    return 0;
}
