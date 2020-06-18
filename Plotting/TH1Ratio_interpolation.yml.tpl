############################################################
################ interpolation weights #####################
############################################################

MEM_ratio_DNN_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_600_mA_250)
  variable2: -TMath::Log10(output_HToZA_mH_600_mA_250)
  weight: ''
  name: MEM_ratio_DNN_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err' 
  bins: 50
  xmin: 15
  xmax: 40
  title: ''
  xlabel: -log_{10}(H#rightarrowZA weight | M_{A} = 250 GeV , M_{H} = 600 GeV)
  ylabel: events
  legend1: 'MEM'
  legend2: 'DNN' 

invalid_MEM_ratio_DNN_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_600_mA_250)
  variable2: -TMath::Log10(output_HToZA_mH_600_mA_250)
  weight: ''
  name: MEM_ratio_DNN_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250<=weight_HToZA_mH_600_mA_250_err' 
  bins: 50
  xmin: 15
  xmax: 40
  title: ''
  xlabel: -log_{10}(H#rightarrowZA invalid weight | M_{A} = 250 GeV , M_{H} = 600 GeV)
  ylabel: events
  legend1: 'MEM'
  legend2: 'DNN' 

