############################################################
####################### DY weights #########################
############################################################

MEM_weight_DY:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_DY)
  weight: ''
  name: MEM_weight_DY
  cut: '' 
  bins: 60
  xmin: 15
  xmax: 30
  title: ''
  xlabel: -log_{10}(DY weight MoMEMta)
  ylabel: events

DNN_weight_DY:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_DY)
  weight: ''
  name: DNN_weight_DY
  cut: ''
  bins: 60
  xmin: 15
  xmax: 30
  title: ''
  xlabel: -log_{10}(DY weight DNN)
  ylabel: events

############################################################
####################### TT weights #########################
############################################################

MEM_weight_TT:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_TT)
  weight: ''
  name: MEM_weight_TT
  cut: ''
  bins: 50
  xmin: 15
  xmax: 40
  title: ''
  xlabel: -log_{10}(t#bar{t} weight MoMEMta)
  ylabel: events


DNN_weight_TT:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_TT)
  weight: ''
  name: DNN_weight_TT
  cut: ''
  bins: 50
  xmin: 15
  xmax: 40
  title: ''
  xlabel: -log_{10}(t#bar{t} weight DNN)
  ylabel: events

############################################################
##################### Dicriminant  #########################
############################################################

Discriminant_MEM:
  filename: 
  tree: tree
  variable: weight_TT/(weight_TT+weight_DY)
  weight: ''
  name: MEM_Discriminant
  cut: '' 
  bins: 50
  xmin: 0
  xmax: 1
  title: ''
  xlabel: Discriminant from MoMEMta weights
  ylabel: events

Discriminant_DNN:
  filename: 
  tree: tree
  variable: output_TT/(output_TT+output_DY)
  weight: ''
  name: DNN_Discriminant
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: ''
  xlabel: Discriminant from DNN weights
  ylabel: events

