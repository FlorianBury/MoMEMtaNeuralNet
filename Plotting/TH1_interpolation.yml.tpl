############################################################
################# interpolation weights ####################
############################################################

MEM_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_HToZA_mH_600_mA_250)
  weight: ''
  name: MEM_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err' 
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(H#rightarrowZA weight MoMEMta | M_{A} = 250 GeV , M_{H} = 600 GeV)
  ylabel: events

DNN_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_HToZA_mH_600_mA_250)
  weight: ''
  name: DNN_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err' 
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(H#rightarrowZA weight DNN | M_{A} = 250 GeV , M_{H} = 600 GeV)
  ylabel: events

inter_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(inter_HToZA_mH_600_mA_250)
  weight: ''
  name: inter_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err' 
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(H#rightarrowZA weight interpolation| M_{A} = 250 GeV , M_{H} = 600 GeV)
  ylabel: events


invalid_MEM_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_HToZA_mH_600_mA_250)
  weight: ''
  name: MEM_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250<=weight_HToZA_mH_600_mA_250_err' 
  bins: 50
  xmin: 15
  xmax: 60 
  title: '' 
  xlabel: -log_{10}(H#rightarrowZA invalid weight MoMEMta | M_{A} = 250 GeV , M_{H} = 600 GeV)
  ylabel: events

invalid_DNN_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_HToZA_mH_600_mA_250)
  weight: ''
  name: DNN_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250<=weight_HToZA_mH_600_mA_250_err' 
  bins: 50
  xmin: 15
  xmax: 60
  title: '' 
  xlabel: -log_{10}(H#rightarrowZA invalid weights DNN | M_{A} = 250 GeV , M_{H} = 600 GeV)
  ylabel: events

invalid_inter_weight_HToZA_mH_600_mA_250:
  filename: 
  tree: tree
  variable: -TMath::Log10(inter_HToZA_mH_600_mA_250)
  weight: ''
  name: inter_weight_HToZA_mH_600_mA_250
  cut: 'weight_HToZA_mH_600_mA_250<=weight_HToZA_mH_600_mA_250_err' 
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(H#rightarrowZA invalid weights interpolation| M_{A} = 250 GeV , M_{H} = 600 GeV)
  ylabel: events


