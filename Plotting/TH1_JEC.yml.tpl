############################################################
#####################    With JEC   ########################
############################################################

MEM_weight_DY_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_DY_JEC)
  weight: ''
  name:  MEM_weight_DY_JEC
  cut: '1'
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(DY weight MoMEMta)
  ylabel: events

MEM_weight_TT_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_TT_JEC)
  weight: ''
  name:  MEM_weight_DY_JEC
  cut: '1'
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(t#bar{t} weight MoMEMta)
  ylabel: events

DNN_output_DY_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_DY_JEC)
  weight: ''
  name:  DNN_output_DY_JEC
  cut: '1'
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(DY weight DNN)
  ylabel: events

DNN_output_TT_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_TT_JEC)
  weight: ''
  name:  DNN_output_DY_JEC
  cut: '1'
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(t#bar{t} weight DNN)
  ylabel: events

############################################################
#####################  Without JEC  ########################
############################################################

MEM_weight_DY_no_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_DY)
  weight: ''
  name:  MEM_weight_DY_no_JEC
  cut: '1'
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(DY weight MoMEMta)
  ylabel: events

MEM_weight_TT_no_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_TT)
  weight: ''
  name:  MEM_weight_DY_no_JEC
  cut: '1'
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(t#bar{t} weight MoMEMta)
  ylabel: events

DNN_output_DY_no_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_DY)
  weight: ''
  name:  DNN_output_DY_no_JEC
  cut: '1'
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(DY weight DNN)
  ylabel: events

DNN_output_TT_no_JEC:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_TT)
  weight: ''
  name:  DNN_output_DY_no_JEC
  cut: '1'
  bins: 50
  xmin: 15
  xmax: 40
  title: '' 
  xlabel: -log_{10}(t#bar{t} weight DNN)
  ylabel: events

