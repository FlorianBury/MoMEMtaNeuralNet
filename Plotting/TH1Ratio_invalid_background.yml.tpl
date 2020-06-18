############################################################
####################### DY weights #########################
############################################################

MEM_ratio_DNN_weight_DY:
  filename: 
  tree: tree
  variable1: -TMath::Log10(weight_DY)
  variable2: -TMath::Log10(output_DY)
  weight: ''
  name: MEM_ratio_DNN_weight_DY
  cut: 'weight_DY_err < weight_DY' 
  bins: 50
  xmin: 15
  xmax: 40
  title: ''
  xlabel: -log_{10}(DY weight)
  ylabel: events
  legend1: 'MoMEMta'
  legend2: 'DNN' 

############################################################
####################### TT weights #########################
############################################################

MEM_ratio_DNN_weight_TT:
  filename: 
  tree: tree
  variable1: -TMath::Log10(weight_TT)
  variable2: -TMath::Log10(output_TT)
  weight: ''
  name: MEM_ratio_DNN_weight_TT
  cut: 'weight_TT_err < weight_TT' 
  bins: 60
  xmin: 20
  xmax: 50
  title: ''
  xlabel: -log_{10}(t#bar{t} weight)
  ylabel: events
  legend1: 'MoMEMta'
  legend2: 'DNN' 

############################################################
##################### Dicriminant  #########################
############################################################

Discriminant_ratio:
  filename: 
  tree: tree
  variable1: weight_TT/(weight_TT+weight_DY)
  variable2: output_TT/(output_TT+output_DY)
  weight: ''
  name: Discriminant_Ratio
  cut: '' 
  bins: 50
  xmin: 0
  xmax: 1
  title: ''
  xlabel: Discriminant
  ylabel: events
  legend1: 'MoMEMta'
  legend2: 'DNN' 

