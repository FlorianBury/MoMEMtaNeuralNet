##################### MEM ########################

ROC_MEM:
  tree: tree
  classes:
    - DY
    - HToZA
    - TT
  prob_branches:
    - Prob_MEM_DY/(Prob_MEM_DY+Prob_MEM_HToZA+Prob_MEM_TT)
    - Prob_MEM_HToZA/(Prob_MEM_DY+Prob_MEM_HToZA+Prob_MEM_TT)
    - Prob_MEM_TT/(Prob_MEM_DY+Prob_MEM_HToZA+Prob_MEM_TT)
  labels:
    - P(Drell-Yann)
    - P(Signal $H\rightarrow ZA$)
    - P($t\bar{t}$)
  colors:
    - navy
    - green
    - darkred
  weight : total_weight
  title : MEM
  cut : ''
  selector :
    'TT' : 'TT'
    'DY' : 'DY'
    'HToZA': 'HToZA'
 
##################### DNN ########################
  
ROC_DNN:
  tree: tree
  classes:
    - DY
    - HToZA
    - TT
  prob_branches:
    - Prob_DNN_DY/(Prob_DNN_DY+Prob_DNN_HToZA+Prob_DNN_TT)
    - Prob_DNN_HToZA/(Prob_DNN_DY+Prob_DNN_HToZA+Prob_DNN_TT)
    - Prob_DNN_TT/(Prob_DNN_DY+Prob_DNN_HToZA+Prob_DNN_TT)
  labels:
    - P(Drell-Yann)
    - P(Signal $H\rightarrow ZA$)
    - P($t\bar{t}$)
  colors:
    - dodgerblue
    - lawngreen
    - red
  weight : total_weight
  title : DNN
  cut : ''
  selector :
    'TT' : 'TT'
    'DY' : 'DY'
    'HToZA': 'HToZA'
  

