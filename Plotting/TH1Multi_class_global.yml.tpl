##################### HToZA MEM weights ########################

MEM_Multi_Prob:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
    - Prob_MEM_TT/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
    - Prob_MEM_HToZA/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
  list_color:
    - 601
    - 633
    - 418
  list_legend:
    - P(Drell-Yann)
    - P(t\bar{t})
    - P(H\rightarrow ZA)
  list_cut : '1'

##################### HToZA DNN weights ########################

DNN_Multi_Prob:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
    - Prob_DNN_TT/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
    - Prob_DNN_HToZA/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
  list_color:
    - 601
    - 633
    - 418
  list_legend:
    - P(Drell-Yann)
    - P(t\bar{t})
    - P(H\rightarrow ZA)
  list_cut : '1'
##################### HToZA DNN+MEM weights ########################

Multi_Prob:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
    - Prob_DNN_DY/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA) 
    - Prob_MEM_TT/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA) 
    - Prob_DNN_TT/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA) 
    - Prob_MEM_HToZA/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA) 
    - Prob_DNN_HToZA/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA) 
  list_color:
    - 602
    - 861
    - 634
    - 628
    - 418
    - 412
  list_legend:
    - P(Drell-Yann) from MEM
    - P(Drell-Yann) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrow ZA) from MEM
    - P(H\rightarrow ZA) from DNN
  list_cut : '1'

