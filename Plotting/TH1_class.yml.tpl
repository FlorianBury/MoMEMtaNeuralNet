############################################################
#################### MEM probability #######################
############################################################

MEM_prob_DY:
  filename: 
  tree: tree
  variable: Prob_MEM_DY/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
  weight: total_weight
  name: Prob_MEM_DY
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT:
  filename: 
  tree: tree
  variable: Prob_MEM_TT/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
  weight: total_weight
  name: Prob_MEM_TT
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
  weight: total_weight
  name: Prob_MEM_HToZA
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events

############################################################
#################### DNN probability #######################
############################################################

DNN_prob_DY:
  filename: 
  tree: tree
  variable: Prob_DNN_DY/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
  weight: total_weight
  name: Prob_DNN_DY
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT:
  filename: 
  tree: tree
  variable: Prob_DNN_TT/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
  weight: total_weight
  name: Prob_DNN_TT
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
  weight: total_weight
  name: Prob_DNN_HToZA
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events

