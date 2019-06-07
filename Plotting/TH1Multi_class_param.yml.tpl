###########################################
######  Parameters mH = 200, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_200_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_200_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 200 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_MEM_TT_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_MEM_HToZA_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
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

DNN_Multi_Prob_mH_200_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_200_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 200 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50)
    - Prob_DNN_TT_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50)
    - Prob_DNN_HToZA_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50)
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

Multi_Prob_mH_200_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_200_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 200 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_DNN_DY_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_MEM_TT_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_DNN_TT_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_MEM_HToZA_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_DNN_HToZA_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)

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

###########################################
######  Parameters mH = 200, mA = 100 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_200_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_200_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 200 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_MEM_TT_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_MEM_HToZA_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
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

DNN_Multi_Prob_mH_200_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_200_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 200 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_200_mA_100/(Prob_DNN_DY_mH_200_mA_100+Prob_DNN_TT_mH_200_mA_100+Prob_DNN_HToZA_mH_200_mA_100)
    - Prob_DNN_TT_mH_200_mA_100/(Prob_DNN_DY_mH_200_mA_100+Prob_DNN_TT_mH_200_mA_100+Prob_DNN_HToZA_mH_200_mA_100)
    - Prob_DNN_HToZA_mH_200_mA_100/(Prob_DNN_DY_mH_200_mA_100+Prob_DNN_TT_mH_200_mA_100+Prob_DNN_HToZA_mH_200_mA_100)
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

Multi_Prob_mH_200_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_200_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 200 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_DNN_DY_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_MEM_TT_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_DNN_TT_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_MEM_HToZA_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_DNN_HToZA_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)

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

###########################################
######  Parameters mH = 250, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_250_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_250_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 250 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_MEM_TT_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_MEM_HToZA_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
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

DNN_Multi_Prob_mH_250_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_250_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 250 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_250_mA_50/(Prob_DNN_DY_mH_250_mA_50+Prob_DNN_TT_mH_250_mA_50+Prob_DNN_HToZA_mH_250_mA_50)
    - Prob_DNN_TT_mH_250_mA_50/(Prob_DNN_DY_mH_250_mA_50+Prob_DNN_TT_mH_250_mA_50+Prob_DNN_HToZA_mH_250_mA_50)
    - Prob_DNN_HToZA_mH_250_mA_50/(Prob_DNN_DY_mH_250_mA_50+Prob_DNN_TT_mH_250_mA_50+Prob_DNN_HToZA_mH_250_mA_50)
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

Multi_Prob_mH_250_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_250_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 250 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_DNN_DY_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_MEM_TT_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_DNN_TT_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_MEM_HToZA_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_DNN_HToZA_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)

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



###########################################
######  Parameters mH = 250, mA = 100 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_250_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_250_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 250 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_MEM_TT_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_MEM_HToZA_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
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

DNN_Multi_Prob_mH_250_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_250_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 250 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_250_mA_100/(Prob_DNN_DY_mH_250_mA_100+Prob_DNN_TT_mH_250_mA_100+Prob_DNN_HToZA_mH_250_mA_100)
    - Prob_DNN_TT_mH_250_mA_100/(Prob_DNN_DY_mH_250_mA_100+Prob_DNN_TT_mH_250_mA_100+Prob_DNN_HToZA_mH_250_mA_100)
    - Prob_DNN_HToZA_mH_250_mA_100/(Prob_DNN_DY_mH_250_mA_100+Prob_DNN_TT_mH_250_mA_100+Prob_DNN_HToZA_mH_250_mA_100)
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

Multi_Prob_mH_250_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_250_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 250 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_DNN_DY_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_MEM_TT_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_DNN_TT_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_MEM_HToZA_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_DNN_HToZA_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)

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



###########################################
######  Parameters mH = 300, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_300_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_300_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 300 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_MEM_TT_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_MEM_HToZA_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
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

DNN_Multi_Prob_mH_300_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_300_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 300 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_300_mA_50/(Prob_DNN_DY_mH_300_mA_50+Prob_DNN_TT_mH_300_mA_50+Prob_DNN_HToZA_mH_300_mA_50)
    - Prob_DNN_TT_mH_300_mA_50/(Prob_DNN_DY_mH_300_mA_50+Prob_DNN_TT_mH_300_mA_50+Prob_DNN_HToZA_mH_300_mA_50)
    - Prob_DNN_HToZA_mH_300_mA_50/(Prob_DNN_DY_mH_300_mA_50+Prob_DNN_TT_mH_300_mA_50+Prob_DNN_HToZA_mH_300_mA_50)
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

Multi_Prob_mH_300_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_300_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 300 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_DNN_DY_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_MEM_TT_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_DNN_TT_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_MEM_HToZA_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_DNN_HToZA_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)

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



###########################################
######  Parameters mH = 300, mA = 100 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_300_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_300_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 300 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_MEM_TT_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_MEM_HToZA_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
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

DNN_Multi_Prob_mH_300_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_300_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 300 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_300_mA_100/(Prob_DNN_DY_mH_300_mA_100+Prob_DNN_TT_mH_300_mA_100+Prob_DNN_HToZA_mH_300_mA_100)
    - Prob_DNN_TT_mH_300_mA_100/(Prob_DNN_DY_mH_300_mA_100+Prob_DNN_TT_mH_300_mA_100+Prob_DNN_HToZA_mH_300_mA_100)
    - Prob_DNN_HToZA_mH_300_mA_100/(Prob_DNN_DY_mH_300_mA_100+Prob_DNN_TT_mH_300_mA_100+Prob_DNN_HToZA_mH_300_mA_100)
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

Multi_Prob_mH_300_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_300_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 300 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_DNN_DY_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_MEM_TT_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_DNN_TT_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_MEM_HToZA_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_DNN_HToZA_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)

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



###########################################
######  Parameters mH = 300, mA = 200 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_300_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_300_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 300 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_MEM_TT_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_MEM_HToZA_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
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

DNN_Multi_Prob_mH_300_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_300_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 300 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_300_mA_200/(Prob_DNN_DY_mH_300_mA_200+Prob_DNN_TT_mH_300_mA_200+Prob_DNN_HToZA_mH_300_mA_200)
    - Prob_DNN_TT_mH_300_mA_200/(Prob_DNN_DY_mH_300_mA_200+Prob_DNN_TT_mH_300_mA_200+Prob_DNN_HToZA_mH_300_mA_200)
    - Prob_DNN_HToZA_mH_300_mA_200/(Prob_DNN_DY_mH_300_mA_200+Prob_DNN_TT_mH_300_mA_200+Prob_DNN_HToZA_mH_300_mA_200)
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

Multi_Prob_mH_300_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_300_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 300 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_DNN_DY_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_MEM_TT_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_DNN_TT_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_MEM_HToZA_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_DNN_HToZA_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)

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



###########################################
######  Parameters mH = 500, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_500_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_500_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 500 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_MEM_TT_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_MEM_HToZA_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
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

DNN_Multi_Prob_mH_500_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_500_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 500 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_500_mA_50/(Prob_DNN_DY_mH_500_mA_50+Prob_DNN_TT_mH_500_mA_50+Prob_DNN_HToZA_mH_500_mA_50)
    - Prob_DNN_TT_mH_500_mA_50/(Prob_DNN_DY_mH_500_mA_50+Prob_DNN_TT_mH_500_mA_50+Prob_DNN_HToZA_mH_500_mA_50)
    - Prob_DNN_HToZA_mH_500_mA_50/(Prob_DNN_DY_mH_500_mA_50+Prob_DNN_TT_mH_500_mA_50+Prob_DNN_HToZA_mH_500_mA_50)
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

Multi_Prob_mH_500_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_500_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 500 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_DNN_DY_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_MEM_TT_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_DNN_TT_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_MEM_HToZA_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_DNN_HToZA_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)

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



###########################################
######  Parameters mH = 500, mA = 100 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_500_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_500_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 500 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_MEM_TT_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_MEM_HToZA_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
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

DNN_Multi_Prob_mH_500_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_500_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 500 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_500_mA_100/(Prob_DNN_DY_mH_500_mA_100+Prob_DNN_TT_mH_500_mA_100+Prob_DNN_HToZA_mH_500_mA_100)
    - Prob_DNN_TT_mH_500_mA_100/(Prob_DNN_DY_mH_500_mA_100+Prob_DNN_TT_mH_500_mA_100+Prob_DNN_HToZA_mH_500_mA_100)
    - Prob_DNN_HToZA_mH_500_mA_100/(Prob_DNN_DY_mH_500_mA_100+Prob_DNN_TT_mH_500_mA_100+Prob_DNN_HToZA_mH_500_mA_100)
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

Multi_Prob_mH_500_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_500_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 500 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_DNN_DY_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_MEM_TT_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_DNN_TT_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_MEM_HToZA_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_DNN_HToZA_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)

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



###########################################
######  Parameters mH = 500, mA = 200 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_500_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_500_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 500 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_MEM_TT_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_MEM_HToZA_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
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

DNN_Multi_Prob_mH_500_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_500_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 500 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_500_mA_200/(Prob_DNN_DY_mH_500_mA_200+Prob_DNN_TT_mH_500_mA_200+Prob_DNN_HToZA_mH_500_mA_200)
    - Prob_DNN_TT_mH_500_mA_200/(Prob_DNN_DY_mH_500_mA_200+Prob_DNN_TT_mH_500_mA_200+Prob_DNN_HToZA_mH_500_mA_200)
    - Prob_DNN_HToZA_mH_500_mA_200/(Prob_DNN_DY_mH_500_mA_200+Prob_DNN_TT_mH_500_mA_200+Prob_DNN_HToZA_mH_500_mA_200)
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

Multi_Prob_mH_500_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_500_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 500 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_DNN_DY_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_MEM_TT_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_DNN_TT_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_MEM_HToZA_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_DNN_HToZA_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)

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



###########################################
######  Parameters mH = 500, mA = 300 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_500_mA_300:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_500_mA_300
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 500 GeV, MA = 300 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_MEM_TT_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_MEM_HToZA_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
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

DNN_Multi_Prob_mH_500_mA_300:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_500_mA_300
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 500 GeV, MA = 300 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_500_mA_300/(Prob_DNN_DY_mH_500_mA_300+Prob_DNN_TT_mH_500_mA_300+Prob_DNN_HToZA_mH_500_mA_300)
    - Prob_DNN_TT_mH_500_mA_300/(Prob_DNN_DY_mH_500_mA_300+Prob_DNN_TT_mH_500_mA_300+Prob_DNN_HToZA_mH_500_mA_300)
    - Prob_DNN_HToZA_mH_500_mA_300/(Prob_DNN_DY_mH_500_mA_300+Prob_DNN_TT_mH_500_mA_300+Prob_DNN_HToZA_mH_500_mA_300)
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

Multi_Prob_mH_500_mA_300:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_500_mA_300
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 500 GeV, MA = 300 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_DNN_DY_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_MEM_TT_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_DNN_TT_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_MEM_HToZA_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_DNN_HToZA_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)

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



###########################################
######  Parameters mH = 500, mA = 400 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_500_mA_400:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_500_mA_400
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 500 GeV, MA = 400 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_MEM_TT_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_MEM_HToZA_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
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

DNN_Multi_Prob_mH_500_mA_400:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_500_mA_400
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 500 GeV, MA = 400 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_500_mA_400/(Prob_DNN_DY_mH_500_mA_400+Prob_DNN_TT_mH_500_mA_400+Prob_DNN_HToZA_mH_500_mA_400)
    - Prob_DNN_TT_mH_500_mA_400/(Prob_DNN_DY_mH_500_mA_400+Prob_DNN_TT_mH_500_mA_400+Prob_DNN_HToZA_mH_500_mA_400)
    - Prob_DNN_HToZA_mH_500_mA_400/(Prob_DNN_DY_mH_500_mA_400+Prob_DNN_TT_mH_500_mA_400+Prob_DNN_HToZA_mH_500_mA_400)
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

Multi_Prob_mH_500_mA_400:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_500_mA_400
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 500 GeV, MA = 400 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_DNN_DY_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_MEM_TT_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_DNN_TT_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_MEM_HToZA_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_DNN_HToZA_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)

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



###########################################
######  Parameters mH = 650, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_650_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_650_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 650 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_MEM_TT_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_MEM_HToZA_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
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

DNN_Multi_Prob_mH_650_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_650_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 650 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_650_mA_50/(Prob_DNN_DY_mH_650_mA_50+Prob_DNN_TT_mH_650_mA_50+Prob_DNN_HToZA_mH_650_mA_50)
    - Prob_DNN_TT_mH_650_mA_50/(Prob_DNN_DY_mH_650_mA_50+Prob_DNN_TT_mH_650_mA_50+Prob_DNN_HToZA_mH_650_mA_50)
    - Prob_DNN_HToZA_mH_650_mA_50/(Prob_DNN_DY_mH_650_mA_50+Prob_DNN_TT_mH_650_mA_50+Prob_DNN_HToZA_mH_650_mA_50)
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

Multi_Prob_mH_650_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_650_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 650 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_DNN_DY_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_MEM_TT_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_DNN_TT_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_MEM_HToZA_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_DNN_HToZA_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)

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



###########################################
######  Parameters mH = 800, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_800_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_800_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 800 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_MEM_TT_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_MEM_HToZA_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
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

DNN_Multi_Prob_mH_800_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_800_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 800 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_800_mA_50/(Prob_DNN_DY_mH_800_mA_50+Prob_DNN_TT_mH_800_mA_50+Prob_DNN_HToZA_mH_800_mA_50)
    - Prob_DNN_TT_mH_800_mA_50/(Prob_DNN_DY_mH_800_mA_50+Prob_DNN_TT_mH_800_mA_50+Prob_DNN_HToZA_mH_800_mA_50)
    - Prob_DNN_HToZA_mH_800_mA_50/(Prob_DNN_DY_mH_800_mA_50+Prob_DNN_TT_mH_800_mA_50+Prob_DNN_HToZA_mH_800_mA_50)
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

Multi_Prob_mH_800_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_800_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 800 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_DNN_DY_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_MEM_TT_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_DNN_TT_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_MEM_HToZA_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_DNN_HToZA_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)

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



###########################################
######  Parameters mH = 800, mA = 100 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_800_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_800_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 800 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_MEM_TT_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_MEM_HToZA_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
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

DNN_Multi_Prob_mH_800_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_800_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 800 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_800_mA_100/(Prob_DNN_DY_mH_800_mA_100+Prob_DNN_TT_mH_800_mA_100+Prob_DNN_HToZA_mH_800_mA_100)
    - Prob_DNN_TT_mH_800_mA_100/(Prob_DNN_DY_mH_800_mA_100+Prob_DNN_TT_mH_800_mA_100+Prob_DNN_HToZA_mH_800_mA_100)
    - Prob_DNN_HToZA_mH_800_mA_100/(Prob_DNN_DY_mH_800_mA_100+Prob_DNN_TT_mH_800_mA_100+Prob_DNN_HToZA_mH_800_mA_100)
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

Multi_Prob_mH_800_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_800_mA_100
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 800 GeV, MA = 100 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_DNN_DY_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_MEM_TT_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_DNN_TT_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_MEM_HToZA_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_DNN_HToZA_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)

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



###########################################
######  Parameters mH = 800, mA = 200 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_800_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_800_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 800 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_MEM_TT_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_MEM_HToZA_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
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

DNN_Multi_Prob_mH_800_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_800_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 800 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_800_mA_200/(Prob_DNN_DY_mH_800_mA_200+Prob_DNN_TT_mH_800_mA_200+Prob_DNN_HToZA_mH_800_mA_200)
    - Prob_DNN_TT_mH_800_mA_200/(Prob_DNN_DY_mH_800_mA_200+Prob_DNN_TT_mH_800_mA_200+Prob_DNN_HToZA_mH_800_mA_200)
    - Prob_DNN_HToZA_mH_800_mA_200/(Prob_DNN_DY_mH_800_mA_200+Prob_DNN_TT_mH_800_mA_200+Prob_DNN_HToZA_mH_800_mA_200)
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

Multi_Prob_mH_800_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_800_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 800 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_DNN_DY_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_MEM_TT_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_DNN_TT_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_MEM_HToZA_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_DNN_HToZA_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)

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



###########################################
######  Parameters mH = 800, mA = 400 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_800_mA_400:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_800_mA_400
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 800 GeV, MA = 400 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_MEM_TT_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_MEM_HToZA_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
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

DNN_Multi_Prob_mH_800_mA_400:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_800_mA_400
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 800 GeV, MA = 400 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_800_mA_400/(Prob_DNN_DY_mH_800_mA_400+Prob_DNN_TT_mH_800_mA_400+Prob_DNN_HToZA_mH_800_mA_400)
    - Prob_DNN_TT_mH_800_mA_400/(Prob_DNN_DY_mH_800_mA_400+Prob_DNN_TT_mH_800_mA_400+Prob_DNN_HToZA_mH_800_mA_400)
    - Prob_DNN_HToZA_mH_800_mA_400/(Prob_DNN_DY_mH_800_mA_400+Prob_DNN_TT_mH_800_mA_400+Prob_DNN_HToZA_mH_800_mA_400)
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

Multi_Prob_mH_800_mA_400:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_800_mA_400
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 800 GeV, MA = 400 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_DNN_DY_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_MEM_TT_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_DNN_TT_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_MEM_HToZA_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_DNN_HToZA_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)

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



###########################################
######  Parameters mH = 800, mA = 700 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_800_mA_700:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_800_mA_700
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 800 GeV, MA = 700 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_MEM_TT_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_MEM_HToZA_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
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

DNN_Multi_Prob_mH_800_mA_700:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_800_mA_700
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 800 GeV, MA = 700 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_800_mA_700/(Prob_DNN_DY_mH_800_mA_700+Prob_DNN_TT_mH_800_mA_700+Prob_DNN_HToZA_mH_800_mA_700)
    - Prob_DNN_TT_mH_800_mA_700/(Prob_DNN_DY_mH_800_mA_700+Prob_DNN_TT_mH_800_mA_700+Prob_DNN_HToZA_mH_800_mA_700)
    - Prob_DNN_HToZA_mH_800_mA_700/(Prob_DNN_DY_mH_800_mA_700+Prob_DNN_TT_mH_800_mA_700+Prob_DNN_HToZA_mH_800_mA_700)
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

Multi_Prob_mH_800_mA_700:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_800_mA_700
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 800 GeV, MA = 700 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_DNN_DY_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_MEM_TT_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_DNN_TT_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_MEM_HToZA_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_DNN_HToZA_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)

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



###########################################
######  Parameters mH = 1000, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_1000_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_1000_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 1000 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_MEM_TT_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_MEM_HToZA_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
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

DNN_Multi_Prob_mH_1000_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_1000_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 1000 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_1000_mA_50/(Prob_DNN_DY_mH_1000_mA_50+Prob_DNN_TT_mH_1000_mA_50+Prob_DNN_HToZA_mH_1000_mA_50)
    - Prob_DNN_TT_mH_1000_mA_50/(Prob_DNN_DY_mH_1000_mA_50+Prob_DNN_TT_mH_1000_mA_50+Prob_DNN_HToZA_mH_1000_mA_50)
    - Prob_DNN_HToZA_mH_1000_mA_50/(Prob_DNN_DY_mH_1000_mA_50+Prob_DNN_TT_mH_1000_mA_50+Prob_DNN_HToZA_mH_1000_mA_50)
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

Multi_Prob_mH_1000_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_1000_mA_50
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 1000 GeV, MA = 50 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_DNN_DY_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_MEM_TT_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_DNN_TT_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_MEM_HToZA_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_DNN_HToZA_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)

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



###########################################
######  Parameters mH = 1000, mA = 200 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_1000_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_1000_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 1000 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_MEM_TT_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_MEM_HToZA_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
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

DNN_Multi_Prob_mH_1000_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_1000_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 1000 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_1000_mA_200/(Prob_DNN_DY_mH_1000_mA_200+Prob_DNN_TT_mH_1000_mA_200+Prob_DNN_HToZA_mH_1000_mA_200)
    - Prob_DNN_TT_mH_1000_mA_200/(Prob_DNN_DY_mH_1000_mA_200+Prob_DNN_TT_mH_1000_mA_200+Prob_DNN_HToZA_mH_1000_mA_200)
    - Prob_DNN_HToZA_mH_1000_mA_200/(Prob_DNN_DY_mH_1000_mA_200+Prob_DNN_TT_mH_1000_mA_200+Prob_DNN_HToZA_mH_1000_mA_200)
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

Multi_Prob_mH_1000_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_1000_mA_200
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 1000 GeV, MA = 200 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_DNN_DY_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_MEM_TT_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_DNN_TT_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_MEM_HToZA_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_DNN_HToZA_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)

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



###########################################
######  Parameters mH = 1000, mA = 500 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_1000_mA_500:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_1000_mA_500
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 1000 GeV, MA = 500 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_MEM_TT_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_MEM_HToZA_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
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

DNN_Multi_Prob_mH_1000_mA_500:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_1000_mA_500
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 1000 GeV, MA = 500 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_1000_mA_500/(Prob_DNN_DY_mH_1000_mA_500+Prob_DNN_TT_mH_1000_mA_500+Prob_DNN_HToZA_mH_1000_mA_500)
    - Prob_DNN_TT_mH_1000_mA_500/(Prob_DNN_DY_mH_1000_mA_500+Prob_DNN_TT_mH_1000_mA_500+Prob_DNN_HToZA_mH_1000_mA_500)
    - Prob_DNN_HToZA_mH_1000_mA_500/(Prob_DNN_DY_mH_1000_mA_500+Prob_DNN_TT_mH_1000_mA_500+Prob_DNN_HToZA_mH_1000_mA_500)
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

Multi_Prob_mH_1000_mA_500:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_1000_mA_500
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 1000 GeV, MA = 500 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_DNN_DY_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_MEM_TT_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_DNN_TT_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_MEM_HToZA_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_DNN_HToZA_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)

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



###########################################
######  Parameters mH = 2000, mA = 1000 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_2000_mA_1000:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_2000_mA_1000
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 2000 GeV, MA = 1000 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_MEM_TT_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_MEM_HToZA_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
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

DNN_Multi_Prob_mH_2000_mA_1000:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_2000_mA_1000
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 2000 GeV, MA = 1000 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_2000_mA_1000/(Prob_DNN_DY_mH_2000_mA_1000+Prob_DNN_TT_mH_2000_mA_1000+Prob_DNN_HToZA_mH_2000_mA_1000)
    - Prob_DNN_TT_mH_2000_mA_1000/(Prob_DNN_DY_mH_2000_mA_1000+Prob_DNN_TT_mH_2000_mA_1000+Prob_DNN_HToZA_mH_2000_mA_1000)
    - Prob_DNN_HToZA_mH_2000_mA_1000/(Prob_DNN_DY_mH_2000_mA_1000+Prob_DNN_TT_mH_2000_mA_1000+Prob_DNN_HToZA_mH_2000_mA_1000)
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

Multi_Prob_mH_2000_mA_1000:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_2000_mA_1000
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 2000 GeV, MA = 1000 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_DNN_DY_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_MEM_TT_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_DNN_TT_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_MEM_HToZA_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_DNN_HToZA_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)

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



###########################################
######  Parameters mH = 3000, mA = 2000 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_3000_mA_2000:
  filename: 
  tree: tree
  weight: total_weight
  name: MEM_Multi_Prob_mH_3000_mA_2000
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from MEM weights (MH = 3000 GeV, MA = 2000 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_MEM_TT_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_MEM_HToZA_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
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

DNN_Multi_Prob_mH_3000_mA_2000:
  filename: 
  tree: tree
  weight: total_weight
  name: DNN_Multi_Prob_mH_3000_mA_2000
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities from DNN weights (MH = 3000 GeV, MA = 2000 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_DNN_DY_mH_3000_mA_2000/(Prob_DNN_DY_mH_3000_mA_2000+Prob_DNN_TT_mH_3000_mA_2000+Prob_DNN_HToZA_mH_3000_mA_2000)
    - Prob_DNN_TT_mH_3000_mA_2000/(Prob_DNN_DY_mH_3000_mA_2000+Prob_DNN_TT_mH_3000_mA_2000+Prob_DNN_HToZA_mH_3000_mA_2000)
    - Prob_DNN_HToZA_mH_3000_mA_2000/(Prob_DNN_DY_mH_3000_mA_2000+Prob_DNN_TT_mH_3000_mA_2000+Prob_DNN_HToZA_mH_3000_mA_2000)
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

Multi_Prob_mH_3000_mA_2000:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_Prob_mH_3000_mA_2000
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Classification probabilities (MH = 3000 GeV, MA = 2000 GeV)'
  xlabel: Probability
  ylabel: Events
  list_variable:
    - Prob_MEM_DY_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_DNN_DY_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_MEM_TT_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_DNN_TT_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_MEM_HToZA_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_DNN_HToZA_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)

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



















