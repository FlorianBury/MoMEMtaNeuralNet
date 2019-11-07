############################################################
#####################    With JEC   ########################
############################################################

MEM_weight_DY_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_DY_JEC)
  weight: total_weight
  name:  MEM_weight_DY_JEC
  cut: '1'
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : MEM weight DY (with JEC)'
  xlabel: -log_{10}(weight)
  ylabel: Events

MEM_weight_TT_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_TT_JEC)
  weight: total_weight
  name:  MEM_weight_DY_JEC
  cut: '1'
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : MEM weight TT (with JEC)'
  xlabel: -log_{10}(weight)
  ylabel: Events

DNN_output_DY_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_DY_JEC)
  weight: total_weight
  name:  DNN_output_DY_JEC
  cut: '1'
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : DNN output DY (with JEC)'
  xlabel: -log_{10}(weight)
  ylabel: Events

DNN_output_TT_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_TT_JEC)
  weight: total_weight
  name:  DNN_output_DY_JEC
  cut: '1'
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : DNN output TT (with JEC)'
  xlabel: -log_{10}(weight)
  ylabel: Events

############################################################
#####################  Without JEC  ########################
############################################################

MEM_weight_DY_no_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_DY)
  weight: total_weight
  name:  MEM_weight_DY_no_JEC
  cut: '1'
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : MEM weight DY (without JEC)'
  xlabel: -log_{10}(weight)
  ylabel: Events

MEM_weight_TT_no_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_TT)
  weight: total_weight
  name:  MEM_weight_DY_no_JEC
  cut: '1'
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : MEM weight TT (without JEC)'
  xlabel: -log_{10}(weight)
  ylabel: Events

DNN_output_DY_no_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_DY)
  weight: total_weight
  name:  DNN_output_DY_no_JEC
  cut: '1'
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : DNN output DY (without JEC)'
  xlabel: -log_{10}(weight)
  ylabel: Events

DNN_output_TT_no_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_TT)
  weight: total_weight
  name:  DNN_output_DY_no_JEC
  cut: '1'
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : DNN output TT (without JEC)'
  xlabel: -log_{10}(weight)
  ylabel: Events

