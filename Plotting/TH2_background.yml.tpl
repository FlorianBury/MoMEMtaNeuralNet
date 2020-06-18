############################################################
####################### DY weights #########################
############################################################

MEM_vs_DNN_weight_DY:
  filename: 
  tree: tree
  variablex: -TMath::Log10(weight_DY)
  variabley: -TMath::Log10(output_DY) 
  weight: ''
  name: MEM_vs_DNN_weight_DY
  cut: ''
  binsx: 60
  xmin: 15
  xmax: 30
  binsy: 60
  ymin: 15
  ymax: 30
  title: ''
  xlabel: -log_{10}(DY weight from MEM)
  ylabel: -log_{10}(DY weight from DNN)
  zlabel: events
  option : 'colz'
  logz : True

############################################################
####################### TT weights #########################
############################################################

MEM_vs_DNN_weight_TT:
  filename: 
  tree: tree
  variablex: -TMath::Log10(weight_TT)
  variabley: -TMath::Log10(output_TT)
  weight: ''
  name: MEM_vs_DNN_weight_TT
  cut: ''
  binsx: 50
  xmin: 15
  xmax: 40
  binsy: 50
  ymin: 15
  ymax: 40
  title: ''
  xlabel: -log_{10}(t#bar{t} weight from MEM)
  ylabel: -log_{10}(t#bar{t} weight from DNN)
  zlabel: events
  option : 'colz'
  logz : True

