############################################################
####################### DY weights #########################
############################################################

MEM_DNN_weight_DY:
  filename: 
  tree: tree
  weight: ''
  name: MEM_DNN_weight_DY
  bins: 50
  xmin: 15
  xmax: 40
  xlabel: -log_{10}(DY weight)
  ylabel: events
  title: ''
  list_color:
    - 600
    - 632
  list_variable:
    - -TMath::Log10(weight_DY)
    - -TMath::Log10(output_DY)
  list_cut: 'weight_DY_err < weight_DY' 
  list_legend:
    - 'MoMEMta'
    - 'DNN'
  legend_pos:
    - 0.60
    - 0.80
    - 0.93
    - 0.93

############################################################
####################### TT weights #########################
############################################################
MEM_DNN_weight_TT:
  filename: 
  tree: tree
  weight: ''
  name: MEM_DNN_weight_TT
  bins: 60
  xmin: 20
  xmax: 50
  xlabel: -log_{10}(t#bar{t} weight)
  ylabel: events
  title: ''
  list_color:
    - 600
    - 632
  list_variable:
    - -TMath::Log10(weight_TT)
    - -TMath::Log10(output_TT)
  list_cut: 'weight_TT_err < weight_TT' 
  list_legend:
    - 'MoMEMta'
    - 'DNN'
  legend_pos:
    - 0.60
    - 0.80
    - 0.93
    - 0.93
