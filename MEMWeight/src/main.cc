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
    TChain chain("tree");
    //string INPUT_DIR = "/nfs/scratch/fynu/asaggio/CMSSW_8_0_30/src/cp3_llbb/ZATools/factories_ZA/fourVectors_withMETphi_for_Florian/slurm/output/";
    string INPUT_DIR = "/home/ucl/cp3/fbury/scratch/MoMEMta_output/invalid_TT_weights/";
    string file = INPUT_DIR+FLAGS_input;
    LOG(info)<<"Directory : "+INPUT_DIR;
    LOG(info)<<"Using file : "+FLAGS_input; 
    bool USE_RECOMPUTE = true;
    LOG(info)<<"Weights recomputation is enabled";

    chain.Add(file.c_str());
    TTreeReader myReader(&chain);

    // TODO : Initial Files -> LorentzVectorE, output LorentzeVector
    TTreeReaderValue<LorentzVector> lep_plus_p4E(myReader, "lep1_p4");
    TTreeReaderValue<LorentzVector> lep_minus_p4E(myReader, "lep2_p4");
    TTreeReaderValue<LorentzVector> jet1_p4E(myReader, "jet1_p4");
    TTreeReaderValue<LorentzVector> jet2_p4E(myReader, "jet2_p4");
    // TODO : either float or doubles
    TTreeReaderValue<double> t_w(myReader, "total_weight");
    TTreeReaderValue<double> e_w(myReader,  "event_weight");
    TTreeReaderValue<double> jjm(myReader, "jj_M");
    TTreeReaderValue<double> lljjm(myReader, "lljj_M");
    TTreeReaderValue<double> llm(myReader, "ll_M");
    TTreeReaderValue<double> m_pt(myReader, "met_pt");
    TTreeReaderValue<double> m_phi(myReader, "met_phi");
    TTreeReaderValue<double> l1c(myReader, "lep1_charge");
    TTreeReaderValue<double> l2c(myReader, "lep2_charge");

    //TTreeReaderValue<double> MET_phi(myReader, "MET_phi");
    //TTreeReaderValue<int> leading_lep_PID(myReader, "leadLepPID");

    /*
     * Define output TTree, which will be a clone of the input tree,
     * with the addition of the weights we're computing (including uncertainty and computation time)
     */
    TFile *output = TFile::Open(FLAGS_output.c_str(), "recreate");
    TTree* out_tree = new TTree("tree", "tree");
    LorentzVector lep1_p4,lep2_p4,jet1_p4,jet2_p4;
    double total_weight,event_weight,jj_M,lljj_M,ll_M,met_pt,met_phi,lep1_charge,lep2_charge;
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

    double weight_TT, weight_TT_err,weight_DY, weight_DY_err, weight_DY_time, weight_TT_time;
    out_tree->Branch("weight_TT", &weight_TT);
    out_tree->Branch("weight_TT_err", &weight_TT_err);
    out_tree->Branch("weight_DY", &weight_DY);
    out_tree->Branch("weight_DY_err", &weight_DY_err);
    out_tree->Branch("weight_DY_time", &weight_DY_time);
    out_tree->Branch("weight_TT_time", &weight_TT_time);


    /*
     * Prepare MoMEMta to compute the weights
     */

    // Construct the ConfigurationReader from the Lua file
    LOG(info) << "Reading configuration files from '" << FLAGS_confs_dir << "'";
    //ConfigurationReader configuration_TTbar(FLAGS_confs_dir + "TTbar_FullyLeptonic.lua");
    //ConfigurationReader configuration_DY(FLAGS_confs_dir + "dy_to_ll_simple.lua");

    // Instantiate MoMEMta using a **frozen** configuration
    //MoMEMta TTbar_weight(configuration_TTbar.freeze());
    //MoMEMta DY_weight(configuration_DY.freeze());
    
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
    while (myReader.Next()) {
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
        LOG(info) << "Event " << myReader.GetCurrentEntry();

        // TT weights
        bool failed_TT = false;
        int n_start_TT = 20000;
        weight_TT_time = 0;
        LOG(debug)<<"Starting TT weight computation";
        do {
            int rand_num = rand()%1000;
            failed_TT = false;
            LOG(info)<<"Random number for seed : "<<rand_num;
            LOG(info)<<"Starting eval : "<<n_start_TT<<"\tMax eval : "<<n_start_TT*20;
            if (n_start_TT>=2000000)
                break;

            ParameterSet lua_parameters;
            lua_parameters.set("random", rand_num);
            lua_parameters.set("n_start_TT", n_start_TT);
            lua_parameters.set("max_eval", n_start_TT*20);
            
            ConfigurationReader configuration_TTbar(FLAGS_confs_dir + "TTbar_FullyLeptonic.lua",lua_parameters);

            // Instantiate MoMEMta using a **frozen** configuration
            MoMEMta TTbar_weight(configuration_TTbar.freeze());


           // Retrieve the weight and uncertainty for TT
            auto start_time_TT = system_clock::now();
            std::vector<std::pair<double, double>> TTbar_weights = TTbar_weight.computeWeights({lep_minus, lep_plus, bjet1, bjet2},met_p4);
            auto end_time_TT = system_clock::now();

            weight_TT = TTbar_weights.back().first;
            weight_TT_err = TTbar_weights.back().second;
            weight_TT_time += std::chrono::duration_cast<milliseconds>(end_time_TT - start_time_TT).count();

            LOG(info)<<" -> TT result: " << weight_TT << " +- " << weight_TT_err;
            LOG(info) << "Weight computed in " << weight_TT_time << "ms";

            // If weights did not converge 
            if (USE_RECOMPUTE == true and weight_TT<weight_TT_err){ 
                LOG(warning) << "TT weights dit not converge, will increase precision";
                failed_TT = true;
                n_start_TT += 200000;
            }
        }
        while (failed_TT);


        // DY weights 
        LOG(debug)<<"Starting DY weight computation";
    
        bool failed_DY = false;
        int n_start_DY = 20000;
        weight_DY_time = 0;
        do {
            int rand_num = rand()%1000;
            failed_DY = false;
            LOG(info)<<"Random number for seed : "<<rand_num;
            LOG(info)<<"Starting eval : "<<n_start_DY<<"\tMax eval : "<<n_start_DY*20;
            if (n_start_DY>=2000000)
                break;

            ParameterSet lua_parameters;
            lua_parameters.set("random", rand_num);
            lua_parameters.set("n_start_DY", n_start_DY);
            lua_parameters.set("max_eval", n_start_DY*20);
            
            ConfigurationReader configuration_DY(FLAGS_confs_dir + "dy_to_ll_simple.lua",lua_parameters);

            // Instantiate MoMEMta using a **frozen** configuration
            MoMEMta DY_weight(configuration_DY.freeze());

            // Retrieve the weight and uncertainty for DY
            auto start_time_DY = system_clock::now();
            std::vector<std::pair<double, double>> DY_weights = DY_weight.computeWeights({lep_minus, lep_plus, bjet1, bjet2, isr});
            auto end_time_DY = system_clock::now();

            weight_DY = DY_weights.back().first;
            weight_DY_err = DY_weights.back().second;
            weight_DY_time += std::chrono::duration_cast<milliseconds>(end_time_DY - start_time_DY).count();

            LOG(info)<<" -> DY result: " << weight_DY << " +- " << weight_DY_err;
            LOG(info) << "Weight computed in " << weight_DY_time << "ms";
            // If weights did not converge 
            if (USE_RECOMPUTE == true && weight_DY<weight_DY_err){ 
                LOG(warning) << "DY weights dit not converge, will increase precision";
                failed_DY = true;
                n_start_DY += 200000;
            }
 
       }
        while (failed_DY);

        // Other values in branches
        total_weight = *t_w;
        event_weight = *e_w;
        jj_M = *jjm;
        lljj_M = *lljjm;
        ll_M = *llm;
        met_pt = *m_pt;
        met_phi = *m_phi;
        lep1_charge = *l1c;
        lep2_charge = *l2c;
    
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
