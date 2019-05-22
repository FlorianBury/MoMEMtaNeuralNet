##################### Prob DY ########################

Prob_DY_MEM_vs_DNN:
  filename: 
  tree: tree
  variablex: Prob_MEM_DY
  variabley: Prob_DNN_DY
  weight: total_weight
  name: Prob_DY_MEM_vs_DNN 
  cut: ''
  binsx: 50
  xmin: 0
  xmax: 1
  binsy: 50
  ymin: 0
  ymax: 1
  title: '{} sample : MEM vs DNN Probability(Drell-Yann)'
  xlabel: Probability(Drell-Yann|MEM)
  ylabel: Probability(Drell-Yann|DNN)
  zlabel: Events
  option : 'prof'

##################### Prob TT ########################

Prob_TT_MEM_vs_DNN:
  filename: 
  tree: tree
  variablex: Prob_MEM_TT
  variabley: Prob_DNN_TT
  weight: total_weight
  name: Prob_TT_MEM_vs_DNN 
  cut: ''
  binsx: 50
  xmin: 0
  xmax: 1
  binsy: 50
  ymin: 0
  ymax: 1
  title: '{} sample : MEM vs DNN Probability(t#bar{{t}})'
  xlabel: Probability(t#bar{t}|MEM)
  ylabel: Probability(t#bar{t}|DNN)
  zlabel: Events
  option : 'prof'

#################### Prob HToZA #######################

Prob_HToZA_MEM_vs_DNN:
  filename: 
  tree: tree
  variablex: Prob_MEM_HToZA
  variabley: Prob_DNN_HToZA
  weight: total_weight
  name: Prob_HToZA_MEM_vs_DNN 
  cut: ''
  binsx: 50
  xmin: 0
  xmax: 1
  binsy: 50
  ymin: 0
  ymax: 1
  title: '{} sample : MEM vs DNN Probability(Signal)'
  xlabel: Probability(H#rightarrow ZA|MEM)
  ylabel: Probability(H#rightarrow ZA|DNN)
  zlabel: Events
  option : 'prof'

