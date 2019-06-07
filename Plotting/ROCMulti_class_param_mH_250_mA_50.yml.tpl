##################### MEM ########################

ROC_MEM_mH_200_mA_50:
  tree: tree
  classes:
    - DY
    - HToZA
    - TT
  prob_branches:
    - Prob_MEM_DY_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50)
    - Prob_MEM_HToZA_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50)
    - Prob_MEM_TT_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50)

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

ROC_DNN_mH_200_mA_50:
  tree: tree
  classes:
    - DY
    - HToZA
    - TT
  prob_branches:
    - Prob_DNN_DY_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50)
    - Prob_DNN_HToZA_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50)
    - Prob_DNN_TT_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50)

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

