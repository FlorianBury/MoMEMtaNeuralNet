##################### HToZA MEM weights ########################

MEM_Multi_Prob:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob
  bins: 50
  xmin: 0
  xmax: 1
  title: '' 
  xlabel: Classification probability
  ylabel: events
  legend_pos:
    - 0.30
    - 0.60
    - 0.70
    - 0.92
  list_variable:
    - Prob_MEM_DY/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
    - Prob_MEM_TT/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
    - Prob_MEM_HToZA/(Prob_MEM_DY+Prob_MEM_TT+Prob_MEM_HToZA)
  list_color:
    - 601
    - 633
    - 418
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrow ZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob
  bins: 50
  xmin: 0
  xmax: 1
  title: '' 
  xlabel: Classification probability
  ylabel: events
  legend_pos:
    - 0.30
    - 0.60
    - 0.80
    - 0.92
  list_variable:
    - Prob_DNN_DY/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
    - Prob_DNN_TT/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
    - Prob_DNN_HToZA/(Prob_DNN_DY+Prob_DNN_TT+Prob_DNN_HToZA)
  list_color:
    - 601
    - 633
    - 418
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrow ZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN+MEM weights ########################

Multi_Prob:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob
  bins: 50
  xmin: 0
  xmax: 1
  title: '' 
  xlabel: Classification probability
  ylabel: events
  legend_pos:
    - 0.30
    - 0.60
    - 0.80
    - 0.92
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
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MoMEMta
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MoMEMta
    - P(t\bar{t}) from DNN
    - P(H\rightarrow ZA) from MoMEMta
    - P(H\rightarrow ZA) from DNN
  list_cut : '1'
  logy: True

