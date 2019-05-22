############################################################
####################### DY weights #########################
############################################################

MEM_vs_DNN_weight_DY:
  filename: 
  tree: tree
  variablex: -TMath::Log10(weight_DY)
  variabley: -TMath::Log10(output_DY) 
  weight: total_weight
  name: MEM_vs_DNN_weight_DY
  cut: ''
  binsx: 100
  xmin: 15
  xmax: 45
  binsy: 100
  ymin: 15
  ymax: 45
  title: '{} sample : MEM vs DNN weight DY'
  xlabel: -log_{10}(weight from MEM)
  ylabel: -log_{10}(weight from DNN)
  zlabel: Events
  option : 'colz'

############################################################
####################### TT weights #########################
############################################################

MEM_vs_DNN_weight_TT:
  filename: 
  tree: tree
  variablex: -TMath::Log10(weight_TT)
  variabley: -TMath::Log10(output_TT)
  weight: total_weight
  name: MEM_vs_DNN_weight_TT
  cut: ''
  binsx: 100
  xmin: 15
  xmax: 45
  binsy: 100
  ymin: 15
  ymax: 45
  title: '{} sample : MEM vs DNN weight TT'
  xlabel: -log_{10}(weight from MEM)
  ylabel: -log_{10}(weight from DNN)
  zlabel: Events
  option : 'colz'

