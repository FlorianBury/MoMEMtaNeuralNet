############################################################
################ interpolation weights #####################
############################################################

MEM_ratio_DNN_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_600_mA_250)
  variable2: -TMath::Log10(output_HToZA_mH_600_mA_250)
  weight: total_weight
  name: MEM_ratio_DNN_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err' 
  bins: 100
  xmin: 15
  xmax: 45
  title: '{} sample : Ratio MEM/DNN weight signal ( M_{{H}} = 600 GeV, M_{{A}}  = 250 GeV) '
  xlabel: -log_{10}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

invalid_MEM_ratio_DNN_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_600_mA_250)
  variable2: -TMath::Log10(output_HToZA_mH_600_mA_250)
  weight: total_weight
  name: MEM_ratio_DNN_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250<=weight_HToZA_mH_600_mA_250_err' 
  bins: 100
  xmin: 15
  xmax: 60
  title: '{} sample (invalid weights) : Ratio MEM/DNN weight signal ( M_{{H}} = 600 GeV, M_{{A}}  = 250 GeV) '
  xlabel: -log_{10}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

