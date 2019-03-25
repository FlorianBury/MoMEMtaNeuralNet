function append(t1, t2)
    for i = 1, #t2 do
        t1[#t1 + 1] = t2[i]
    end

    return t1
end

function copy_and_append(t1, t2)
    local t3 = {}

    append(t3, t1)
    append(t3, t2)

    return t3
end

-- Order convention : e+ e- b bbar
-- Reco particles : input::particles/1
-- Gen particles, depends on what you do

-- Available parameters : https://github.com/MoMEMta/MoMEMta/blob/master/core/src/MoMEMta.cc#L141
-- If "relative accuracy" is reached stop launching points unless "min_eval" point have been launched,
-- if after "max_eval" points have been launched stop launching even if we do not have reahced accuracy.
-- "n_start" : Vegas works by iterations will launch n_start point by n_start point and refine the grid at each step
-- n_increase allow to launch more points at each iteration
-- NB : all the point that have been launched are used to compute the intergal
cuba = {
    seed = random,
    relative_accuracy = 0.01,
    verbosity = 3,
    max_eval = max_eval,
    n_start = n_start_HToZA
}

-- NB: to be defined in the .cc is matrix_element_prefix

--inputs as will be feed to the blocks and ME
local neg_lepton = declare_input("lepton1")
local pos_lepton = declare_input("lepton2")
local bjet1 = declare_input("bjet1")
local bjet2 = declare_input("bjet2")


USE_TF = true
USE_PERM = true -- carefull if you use TF binned in eta and the permutations, jet1 tf is applied to jet2

baseDirME = "/home/ucl/cp3/fbury/MoMEMtaNeuralNet/MEMWeight/MatrixElements/HToZA_"..tostring(math.floor(mH)).."_"..tostring(math.floor(mA))
baseDirTF = "/home/ucl/cp3/brfranco/scratch/framework/MIS_prod_data/CMSSW_7_6_5/src/cp3_llbb/HHTools/histFactory_hh/"
TFFile = baseDirTF .. "tf_genCut0_noRecoCut_lljjorbb_Oct18/condor/output/allTT_smoothed_notPutToZero.root"
parameters = {
    energy = 13000.,
    top_mass = 173.,
    top_width = 1.491500,
    W_mass = 80.419002,
    W_width = 2.047600,
    Z_mass = 91.1876,
    Z_width = 2.49,
    H_mass = 250.,--mH,
    H_width = 1.,
    A_mass = 100.,--mA,
    A_width = 1.,
    lep1_me_index = 1,
    lep1TFFile = TFFile,
    lep1TFName = "ERecMinEGenVSEGen_el_matchedToAfterFSR_allEta_Norm_hh_llmetjj_HWWleptons_nobtag_csv",
    lep2_me_index = 2,
    lep2TFFile = TFFile,
    lep2TFName = "ERecMinEGenVSEGen_el_matchedToAfterFSR_allEta_Norm_hh_llmetjj_HWWleptons_nobtag_csv",
    jet1TFFile = TFFile,
    jet1TFName = "ERecMinEGenVSEGen_bjet_matchedToAfterFSR_allEta_Norm_hh_llmetjj_HWWleptons_nobtag_csv",
    jet2TFFile = TFFile,
    jet2TFName = "ERecMinEGenVSEGen_bjet_matchedToAfterFSR_allEta_Norm_hh_llmetjj_HWWleptons_nobtag_csv",
    matrix_element = "HToZA_"..tostring(math.floor(mH)).."_"..tostring(math.floor(mA)).."_2HDM4MG5_may15_P1_Sigma_2HDM4MG5_may15_uux_bbxepem", 
    matrix_element_parameters = baseDirME .. "/Cards/param_card.dat",
    export_graph_as = "HToZA_"..tostring(math.floor(mH)).."_"..tostring(math.floor(mA)).."_computing_graph.dot"
}
matrix_element_lib = baseDirME .. "/build/libme_HToZA_"..tostring(math.floor(mH)).."_"..tostring(math.floor(mA))..".so"
load_modules(matrix_element_lib)

if USE_PERM then
    -- Permute b and bbar
    -- ME va etre moyenné sur les permutations --> effectuer les permutations uniquement si il y a une différence (sinon == *2/2) e.g. pas pour H--> bbbar
    add_reco_permutations(bjet1, bjet2) 
end

if USE_TF then
    -- Fix gen energy of the two leptons according to their transfer function
    BinnedTransferFunctionOnEnergy.tf_neg_lepton = {
        ps_point = add_dimension(),
        reco_particle = neg_lepton.reco_p4,
        file = parameter('lep1TFFile'),
        th2_name = parameter('lep1TFName'),
    }
    BinnedTransferFunctionOnEnergy.tf_pos_lepton = {
        ps_point = add_dimension(),
        reco_particle = pos_lepton.reco_p4,
        file = parameter('lep2TFFile'),
        th2_name = parameter('lep2TFName'),
    }
    
    --GaussianTransferFunctionOnEnergy.tf_neg_lepton = {
    --    ps_point = add_dimension(),
    --    reco_particle = neg_lepton.reco_p4,
    --    sigma = 0.02,
    --    sigma_range = 5.,
    --} 
    neg_lepton.set_gen_p4("tf_neg_lepton::output")
    pos_lepton.set_gen_p4("tf_pos_lepton::output")
    -- Pos_lepton comes from the evaluator later

    --BinnedTransferFunctionOnEnergy.tf_bjet2 = {
    --    ps_point = add_dimension(),
    --    reco_particle = bjet2.reco_p4,
    --    file = parameter('jet2TFFile'),
    --    th2_name = parameter('jet2TFName'),
    --}
    --GaussianTransferFunctionOnEnergy.tf_bjet2 = {
    --    ps_point = add_dimension(),
    --    reco_particle = bjet2.reco_p4,
    --    sigma = 0.15,
    --    sigma_range = 5.,
    --}
    --bjet2.set_gen_p4("tf_bjet2::output");
    -- bjet1 comes from the evaluator later


    -- Flatter for the H, A and Z resoncances
    --NarrowWidthApproximation.flatter_H = {
    --    mass = parameter('H_mass'),
    --    width = parameter('H_width')
    --    
    --}
    --NarrowWidthApproximation.flatter_A = {
    --    mass = parameter('A_mass'),
    --    width = parameter('A_width')
    --} 
    --BreitWignerGenerator.flatter_Z = {
    --    ps_point = add_dimension(),
    --    mass = parameter('Z_mass'),
    --    width = parameter('Z_width')
    --}


    ------------------ OPTION 1 ----------------------------
    --SecondaryBlockCD.sb_cd_A = { -- SB of the decay of A
    --    s12 = 'flatter_A::s',
    --    p1 = bjet1.gen_p4,   -- "invisible"
    --    p2 = bjet2.gen_p4   -- "visible", both at gen level
    --}
    --Looper.looper_sb_cd_A = {
    --    solutions = 'sb_cd_A::solutions',
    --    path = Path("blockb","looper_blockb")
    --}
    --SecondaryBlockCD.sb_cd_Z = { -- SB of the decay of Z
    --    s12 = 'flatter_Z::s',
    --    p1 = neg_lepton.gen_p4,   -- "invisible"
    --    p2 = pos_lepton.gen_p4   -- "visible", both at gen level
    --}
    --Looper.looper_sb_cd_Z = {
    --    solutions = 'sb_cd_Z::solutions',
    --    path = Path("blockb","looper_blockb")
    --}
    --VectorLinearCombinator.A_p4 = {
    --    inputs = {bjet1.gen_p4, bjet2.gen_p4},
    --    coefficients = {1., 1.}
    --}
    --VectorLinearCombinator.Z_p4 = {
    --    inputs = {neg_lepton.gen_p4, pos_lepton.gen_p4},
    --    coefficients = {1., 1.}
    --}

    --BlockB.blockb = {
    --    s12 = 'flatter_H::s',
    --    p2 = 'A_p4::output',
    --    pT_is_met = true,
    --}
    --Looper.looper_blockb = {
    --    solutions = "blockb::solutions",
    --    path = Path("boost","HToZA","integrand")    
    --}

    ------------------ OPTION 2 ----------------------------
    --StandardPhaseSpace.phaseSpaceOut = {
    --    particles = {'tf_neg_lepton::output', 'tf_bjet2::output'}
    --}

    --SecondaryBlockCD.sb_cd = {
    --    s12 = 'flatter_Z::s',
    --    p1 = pos_lepton.reco_p4,   -- "invisible" (no TF so reco level)
    --    p2 = neg_lepton.gen_p4   -- "visible" (TF so gen level)
    --}
    --Looper.looper_sb_cd = {
    --    solutions = 'sb_cd::solutions',
    --    path = Path("tfEval_pos_lepton","blockb","looper_blockb")
    --}
    --pos_lepton.set_gen_p4("looper_sb_cd::particles/1")

    --BinnedTransferFunctionOnEnergyEvaluator.tfEval_pos_lepton = {
    --    reco_particle = pos_lepton.reco_p4,
    --    gen_particle = pos_lepton.gen_p4, 
    --    file = parameter('lep2TFFile'),
    --    th2_name = parameter('lep2TFName'),
    --}
 
    ----VectorLinearCombinator.Z_p4 = {
    ----    inputs = {neg_lepton.gen_p4, pos_lepton.gen_p4},
    ----    coefficients = {1., 1.}
    ----}

    --BlockB.blockb = {
    --    s12 = 'flatter_A::s',
    --    p2 = bjet2.gen_p4,
    --    branches = {neg_lepton.gen_p4,pos_lepton.gen_p4}
    --}
    --    
    --Looper.looper_blockb = {
    --    solutions = "blockb::solutions",
    --    path = Path("tfEval_bjet1","boost","HToZA","integrand")    
    --}

    --bjet1.set_gen_p4("looper_blockb::particles/1")

    --BinnedTransferFunctionOnEnergyEvaluator.tfEval_bjet1 = {
    --    reco_particle = bjet1.reco_p4,
    --    gen_particle = bjet1.gen_p4, 
    --    file = parameter('jet1TFFile'),
    --    th2_name = parameter('jet1TFName'),
    --}
    ------------------ OPTION 3 ----------------------------
    --StandardPhaseSpace.phaseSpaceOut = {
    --    particles = {'tf_neg_lepton::output', 'tf_bjet2::output'}
    --}

    --SecondaryBlockCD.sb_cd = {
    --    s12 = 'flatter_Z::s',
    --    p1 = pos_lepton.reco_p4,   -- "invisible" (no TF so reco level)
    --    p2 = neg_lepton.gen_p4   -- "visible" (TF so gen level)
    --}
    --Looper.looper_sb_cd = {
    --    solutions = 'sb_cd::solutions',
    --    path = Path("tfEval_pos_lepton","Z_p4","blockc","looper_blockc")
    --}
    --pos_lepton.set_gen_p4("looper_sb_cd::particles/1")

    --BinnedTransferFunctionOnEnergyEvaluator.tfEval_pos_lepton = {
    --    reco_particle = pos_lepton.reco_p4,
    --    gen_particle = pos_lepton.gen_p4, 
    --    file = parameter('lep2TFFile'),
    --    th2_name = parameter('lep2TFName'),
    --}
 
    --VectorLinearCombinator.Z_p4 = {
    --    inputs = {neg_lepton.gen_p4, pos_lepton.gen_p4},
    --    coefficients = {1., 1.}
    --}

    --BlockC.blockc = {
    --    s12 = 'flatter_A::s',
    --    s123 = 'flatter_H::s',
    --    p2 = bjet2.gen_p4,
    --    p3 = 'Z_p4::output'
    --}
    -- 
    --Looper.looper_blockc = {
    --   solutions = "blockc::solutions",
    --   path = Path("tfEval_bjet1","boost","HToZA","integrand")    
    --}

    --bjet1.set_gen_p4("looper_blockc::particles/1")

    --BinnedTransferFunctionOnEnergyEvaluator.tfEval_bjet1 = {
    --    reco_particle = bjet1.reco_p4,
    --    gen_particle = bjet1.gen_p4, 
    --    file = parameter('jet1TFFile'),
    --    th2_name = parameter('jet1TFName'),
    --}
    ------------------ OPTION 4 ----------------------------
    --StandardPhaseSpace.phaseSpaceOut = {
    --    particles = {'tf_neg_lepton::output', 'tf_bjet2::output'}
    --}

    --BlockF.blockf = {
    --    q1 = add_dimension(),
    --    q2 = add_dimension(),
    --    s13 = 'flatter_A::s',
    --    s24 = 'flatter_Z::s',
    --    p3 = bjet2.gen_p4,
    --    p4 = neg_lepton.gen_p4 ,
    --    --m1 = 100.,
    --    --m2 = 100.,
    --}
    --Looper.looper_blockf = {
    --   solutions = "blockf::solutions",
    --   path = Path("tfEval_bjet1","tfEval_pos_lepton","boost","HToZA","integrand")    
    --}

    --bjet1.set_gen_p4("looper_blockf::particles/1")
    --pos_lepton.set_gen_p4("looper_blockf::particles/2")
    --BinnedTransferFunctionOnEnergyEvaluator.tfEval_pos_lepton = {
    --    reco_particle = pos_lepton.reco_p4,
    --    gen_particle = pos_lepton.gen_p4, 
    --    file = parameter('lep2TFFile'),
    --    th2_name = parameter('lep2TFName'),
    --}
    -- BinnedTransferFunctionOnEnergyEvaluator.tfEval_bjet1 = {
    --    reco_particle = bjet1.reco_p4,
    --    gen_particle = bjet1.gen_p4, 
    --    file = parameter('jet1TFFile'),
    --    th2_name = parameter('jet1TFName'),
    --}
    --GaussianTransferFunctionOnEnergyEvaluator.tfEval_pos_lepton = {
    --    reco_particle = pos_lepton.reco_p4,
    --    gen_particle = pos_lepton.gen_p4, 
    --}
    -- GaussianTransferFunctionOnEnergyEvaluator.tfEval_bjet1 = {
    --    reco_particle = bjet1.reco_p4,
    --    gen_particle = bjet1.gen_p4, 
    --}
    ------------------ OPTION 5 ----------------------------
    StandardPhaseSpace.phaseSpaceOut = {
        particles = {'tf_neg_lepton::output', 'tf_pos_lepton::output'}
    }
    BlockA.blocka = {
        p1 = bjet1.reco_p4,
        p2 = bjet2.reco_p4,
        branches = {neg_lepton.gen_p4,pos_lepton.gen_p4}
    }
    Looper.looper_blocka = {
       solutions = "blocka::solutions",
       path = Path("tfEval_bjet1","tfEval_bjet2","boost","HToZA","integrand")    
    }
    bjet1.set_gen_p4("looper_blocka::particles/1")
    bjet2.set_gen_p4("looper_blocka::particles/2")
    BinnedTransferFunctionOnEnergyEvaluator.tfEval_bjet1 = {
        reco_particle = bjet1.reco_p4,
        gen_particle = bjet1.gen_p4, 
        file = parameter('jet1TFFile'),
        th2_name = parameter('jet1TFName'),
    }
    BinnedTransferFunctionOnEnergyEvaluator.tfEval_bjet2 = {
        reco_particle = bjet2.reco_p4,
        gen_particle = bjet2.gen_p4, 
        file = parameter('jet2TFFile'),
        th2_name = parameter('jet2TFName'),
    }


    genParticles = {
        bjet1.gen_p4,
        bjet2.gen_p4,
        pos_lepton.gen_p4,
        neg_lepton.gen_p4,
        }
    
else 
    genParticles = {
        bjet1.reco_p4,
        bjet2.reco_p4,
        pos_lepton.reco_p4,
        neg_lepton.reco_p4,
        }
    -- Compute the phase space density for observed particles not concerned by the change of variable : here lepton on which we evaluate the TF 
    -- The TF jacobian just account for dp/dE to go from |p| to E, not the phase space volume, the other blocks give the whole product of jacobian and phase space volume to go from one param to another
    StandardPhaseSpace.phaseSpaceOut = {
        particles = genParticles
    }
end


BuildInitialState.boost = {
    do_transverse_boost = true,
    particles = genParticles
}
--P4Printer.printparton2 = {
--    input = 'boost::partons/2'
--}

jacobians = {'phaseSpaceOut::phase_space'}

if USE_TF then
    --append(jacobians, {'tf_neg_lepton::TF_times_jacobian', 'looper_sb_cd_A::jacobian','looper_sb_cd_Z::jacobian','looper_blockb::jacobian', 'tf_pos_lepton::TF_times_jacobian', 'tf_neg_lepton::TF_times_jacobian', 'tf_bjet1::TF_times_jacobian', 'tf_bjet2::TF_times_jacobian','flatter_H::jacobian','flatter_A::jacobian','flatter_Z::jacobian'}) --OPTION 1 -- 
    --append(jacobians, {'looper_sb_cd::jacobian','looper_blockb::jacobian', 'tfEval_pos_lepton::TF', 'tfEval_bjet1::TF', 'tf_neg_lepton::TF_times_jacobian', 'tf_bjet2::TF_times_jacobian','flatter_A::jacobian','flatter_Z::jacobian'})-- OPTION 2 --
    --append(jacobians, {'looper_sb_cd::jacobian','looper_blockc::jacobian', 'tfEval_pos_lepton::TF', 'tfEval_bjet1::TF', 'tf_neg_lepton::TF_times_jacobian', 'tf_bjet2::TF_times_jacobian','flatter_A::jacobian','flatter_Z::jacobian','flatter_H::jacobian'})-- OPTION 3 --
    --append(jacobians, {'looper_blockf::jacobian', 'tfEval_pos_lepton::TF', 'tfEval_bjet1::TF', 'tf_neg_lepton::TF_times_jacobian', 'tf_bjet2::TF_times_jacobian','flatter_A::jacobian','flatter_Z::jacobian'}) -- OPTION 4 --
    append(jacobians, {'looper_blocka::jacobian', 'tfEval_bjet1::TF', 'tfEval_bjet2::TF', 'tf_neg_lepton::TF_times_jacobian', 'tf_pos_lepton::TF_times_jacobian'})-- OPTION 5 --
end

MatrixElement.HToZA = {
  pdf = 'CT10nlo',
  pdf_scale = parameter('H_mass'),

  matrix_element = parameter('matrix_element'),
  matrix_element_parameters = {
      card = parameter('matrix_element_parameters'),
  },

  initialState = 'boost::partons',

  particles = {
    inputs = genParticles,
    ids = {
      {
        pdg_id =  5,
        me_index = 1,
      },

      {
        pdg_id = -5,
        me_index = 2,
      },

      {
        pdg_id = -13,
        me_index = 3,
      },

      {
        pdg_id = 13,
        me_index = 4,
      }
    }
  },

  jacobians = jacobians
}

DoubleLooperSummer.integrand = {
    input = "HToZA::output"
}

integrand("integrand::sum")
