##################### Prob Signal ########################

MEM_ratio_DNN_Prob_signal:
  filename: 
  tree: tree
  variable1: Prob_MEM_signal
  variable2: Prob_DNN_signal
  weight: total_weight
  name: MEM_ratio_DNN_Prob_signal
  cut: '' 
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Ratio MEM/DNN Probability(Signal)'
  xlabel: Probability(Drell-Yann)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

