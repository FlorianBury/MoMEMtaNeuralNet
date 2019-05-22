############################################################
################# interpolation weights ####################
############################################################

MEM_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_HToZA_mH_600_mA_250)
  weight: total_weight
  name: MEM_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err' 
  bins: 60
  xmin: 15
  xmax: 45
  title: '{} sample : MEM weight HToZA ( M_{{H}} = 600 GeV, M_{{A}} = 250 GeV) '
  xlabel: -log_{10}(weight)
  ylabel: Events

DNN_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_HToZA_mH_600_mA_250)
  weight: total_weight
  name: DNN_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err' 
  bins: 60
  xmin: 15
  xmax: 45
  title: '{} sample : DNN weight HToZA ( M_{{H}} = 600 GeV, M_{{A}} = 250 GeV) '
  xlabel: -log_{10}(weight)
  ylabel: Events

inter_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(inter_HToZA_mH_600_mA_250)
  weight: total_weight
  name: inter_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err' 
  bins: 60
  xmin: 15
  xmax: 45
  title: '{} sample : Interpolation weight HToZA ( M_{{H}} = 600 GeV, M_{{A}} = 250 GeV) '
  xlabel: -log_{10}(weight)
  ylabel: Events


invalid_MEM_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_HToZA_mH_600_mA_250)
  weight: total_weight
  name: MEM_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250<=weight_HToZA_mH_600_mA_250_err' 
  bins: 60
  xmin: 15
  xmax: 60 
  title: '{} sample (invalid weights) : MEM weight HToZA ( M_{{H}} = 600 GeV, M_{{A}} = 250 GeV) '
  xlabel: -log_{10}(weight)
  ylabel: Events

invalid_DNN_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_HToZA_mH_600_mA_250)
  weight: total_weight
  name: DNN_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250<=weight_HToZA_mH_600_mA_250_err' 
  bins: 60
  xmin: 15
  xmax: 60
  title: '{} sample (invalid weights) : DNN weight HToZA ( M_{{H}} = 600 GeV, M_{{A}} = 250 GeV) '
  xlabel: -log_{10}(weight)
  ylabel: Events

invalid_inter_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(inter_HToZA_mH_600_mA_250)
  weight: total_weight
  name: inter_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250<=weight_HToZA_mH_600_mA_250_err' 
  bins: 60
  xmin: 15
  xmax: 45
  title: '{} sample (invalid weoghts) : Interpolation weight HToZA ( M_{{H}} = 600 GeV, M_{{A}} = 250 GeV) '
  xlabel: -log_{10}(weight)
  ylabel: Events


