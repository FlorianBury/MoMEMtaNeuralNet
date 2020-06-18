############################################################
#################### MEM probability #######################
############################################################

MEM_prob_DY:
  filename: 
  tree: tree
  variable: Prob_MEM_DY/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
  weight: ''
  name: Prob_MEM_DY
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '' 
  xlabel: P(DY)
  ylabel: events

MEM_prob_TT:
  filename: 
  tree: tree
  variable: Prob_MEM_TT/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
  weight: ''
  name: Prob_MEM_TT
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '' 
  xlabel: P(TT)
  ylabel: events

MEM_prob_HToZA:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
  weight: ''
  name: Prob_MEM_HToZA
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: ''
  xlabel: P(H \rightarrow ZA)
  ylabel: events

############################################################
#################### DNN probability #######################
############################################################

DNN_prob_DY:
  filename: 
  tree: tree
  variable: Prob_DNN_DY/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
  weight: ''
  name: Prob_DNN_DY
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '' 
  xlabel: P(DY)
  ylabel: events

DNN_prob_TT:
  filename: 
  tree: tree
  variable: Prob_DNN_TT/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
  weight: ''
  name: Prob_DNN_TT
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '' 
  xlabel: P(TT)
  ylabel: events

DNN_prob_HToZA:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
  weight: ''
  name: Prob_DNN_HToZA
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '' 
  xlabel: P(H#rightarrow ZA)
  ylabel: events

