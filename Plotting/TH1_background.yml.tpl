############################################################
####################### DY weights #########################
############################################################

MEM_weight_DY:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_DY)
  weight: total_weight
  name: MEM_weight_DY
  cut: '' 
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : MEM weight DY'
  xlabel: -log_{10}(weight)
  ylabel: Events

DNN_weight_DY:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_DY)
  weight: total_weight
  name: DNN_weight_DY
  cut: ''
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : DNN weight DY'
  xlabel: -log_{10}(weight)
  ylabel: Events

############################################################
####################### TT weights #########################
############################################################

MEM_weight_TT:
  filename: 
  tree: tree
  variable: -TMath::Log10(weight_TT)
  weight: total_weight
  name: MEM_weight_TT
  cut: ''
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : MEM weight TT'
  xlabel: -log_{10}(weight)
  ylabel: Events


DNN_weight_TT:
  filename: 
  tree: tree
  variable: -TMath::Log10(output_TT)
  weight: total_weight
  name: DNN_weight_TT
  cut: ''
  bins: 150
  xmin: 15
  xmax: 45
  title: '{} sample : DNN weight TT'
  xlabel: -log_{10}(weight)
  ylabel: Events

############################################################
##################### Dicriminant  #########################
############################################################

Discriminant_MEM:
  filename: 
  tree: tree
  variable: weight_TT/(weight_TT+weight_DY)
  weight: total_weight
  name: MEM_Discriminant
  cut: '' 
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : MEM Discriminant '
  xlabel: Discriminant
  ylabel: Events

Discriminant_DNN:
  filename: 
  tree: tree
  variable: output_TT/(output_TT+output_DY)
  weight: total_weight
  name: DNN_Discriminant
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DNN Discriminant '
  xlabel: Discriminant
  ylabel: Events

