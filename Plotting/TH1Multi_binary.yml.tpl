##################### Signal DNN+MEM weights ########################

Multi_Prob:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Binary classification probabilities'
  xlabel: Probability
  ylabel: events
  list_variable:
    - Prob_MEM_signal
    - Prob_DNN_signal
  list_color:
    - 602
    - 861
  list_legend:
    - P(Signal) from MEM
    - P(Signal) from DNN
  list_cut : '1'

