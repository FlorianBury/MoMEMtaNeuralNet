############################################################
#################### MEM probability #######################
############################################################

MEM_prob_signal:
  filename: 
  tree: tree
  variable: Prob_MEM_signal
  weight: ''
  name: MEM_prob_signal 
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights'
  xlabel: P(Signal)
  ylabel: events

############################################################
#################### DNN probability #######################
############################################################

DNN_prob_signal:
  filename: 
  tree: tree
  variable: Prob_DNN_signal
  weight: ''
  name: DNN_prob_signal 
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights'
  xlabel: P(Signal)
  ylabel: events


