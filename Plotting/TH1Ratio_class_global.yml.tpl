##################### Prob DY ########################

MEM_ratio_DNN_Prob_DY:
  filename: 
  tree: tree
  variable1: Prob_MEM_DY
  variable2: Prob_DNN_DY
  weight: total_weight
  name: MEM_ratio_DNN_Prob_DY
  cut: '' 
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Ratio MEM/DNN Probability(Drell-Yann)'
  xlabel: Probability(Drell-Yann)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

##################### Prob TT ########################

MEM_ratio_DNN_Prob_TT:
  filename: 
  tree: tree
  variable1: Prob_MEM_TT  
  variable2: Prob_DNN_TT  
  weight: total_weight
  name: MEM_ratio_DNN_Prob_TT
  cut: '' 
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Ratio MEM/DNN Probability(t#bar{{t}})'
  xlabel: Probability(t#bar{t})
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

#################### Prob HToZA #######################

MEM_ratio_DNN_Prob_HToZA:
  filename: 
  tree: tree
  variable1: Prob_MEM_HToZA  
  variable2: Prob_DNN_HToZA
  weight: total_weight
  name: MEM_ratio_DNN_Prob_HToZA
  cut: '' 
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Ratio MEM/DNN Probability(signal)'
  xlabel: Probability(H#rightarrow ZA)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

