############################################################
####################### DY weights #########################
############################################################

MEM_ratio_DNN_weight_DY:
  filename: 
  tree: tree
  variable1: -TMath::Log10(weight_DY)
  variable2: -TMath::Log10(output_DY)
  weight: total_weight
  name: MEM_ratio_DNN_weight_DY
  cut: '' 
  bins: 100
  xmin: 15
  xmax: 45
  title: '{} sample : Ratio MEM/DNN weight Drell-Yann'
  xlabel: -log_{10}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

############################################################
####################### TT weights #########################
############################################################

MEM_ratio_DNN_weight_TT:
  filename: 
  tree: tree
  variable1: -TMath::Log10(weight_TT)
  variable2: -TMath::Log10(output_TT)
  weight: total_weight
  name: MEM_ratio_DNN_weight_TT
  cut: '' 
  bins: 100
  xmin: 15
  xmax: 45
  title: '{} sample : Ratio MEM/DNN weight t#bar{{t}}'
  xlabel: -log_{10}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

############################################################
##################### Dicriminant  #########################
############################################################

Discriminant_ratio:
  filename: 
  tree: tree
  variable1: weight_TT/(weight_TT+weight_DY)
  variable2: output_TT/(output_TT+output_DY)
  weight: total_weight
  name: Discriminant_Ratio
  cut: '' 
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Discriminant Ratio'
  xlabel: Discriminant
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

