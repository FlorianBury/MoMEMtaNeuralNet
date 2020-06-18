###########################################
######  Parameters mH = 200, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_200_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_200_mA_50
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
    - Prob_MEM_DY_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_MEM_TT_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_MEM_HToZA_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_200_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_200_mA_50
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
    - Prob_DNN_DY_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50)
    - Prob_DNN_TT_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50)
    - Prob_DNN_HToZA_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_200_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_200_mA_50
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
    - Prob_MEM_DY_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_DNN_DY_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_MEM_TT_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_DNN_TT_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_MEM_HToZA_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
    - Prob_DNN_HToZA_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True

###########################################
######  Parameters mH = 200, mA = 100 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_200_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_200_mA_100
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
    - Prob_MEM_DY_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_MEM_TT_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_MEM_HToZA_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_200_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_200_mA_100
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
    - Prob_DNN_DY_mH_200_mA_100/(Prob_DNN_DY_mH_200_mA_100+Prob_DNN_TT_mH_200_mA_100+Prob_DNN_HToZA_mH_200_mA_100)
    - Prob_DNN_TT_mH_200_mA_100/(Prob_DNN_DY_mH_200_mA_100+Prob_DNN_TT_mH_200_mA_100+Prob_DNN_HToZA_mH_200_mA_100)
    - Prob_DNN_HToZA_mH_200_mA_100/(Prob_DNN_DY_mH_200_mA_100+Prob_DNN_TT_mH_200_mA_100+Prob_DNN_HToZA_mH_200_mA_100)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_200_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_200_mA_100
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
    - Prob_MEM_DY_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_DNN_DY_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_MEM_TT_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_DNN_TT_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_MEM_HToZA_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
    - Prob_DNN_HToZA_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True

###########################################
######  Parameters mH = 250, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_250_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_250_mA_50
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
    - Prob_MEM_DY_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_MEM_TT_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_MEM_HToZA_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_250_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_250_mA_50
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
    - Prob_DNN_DY_mH_250_mA_50/(Prob_DNN_DY_mH_250_mA_50+Prob_DNN_TT_mH_250_mA_50+Prob_DNN_HToZA_mH_250_mA_50)
    - Prob_DNN_TT_mH_250_mA_50/(Prob_DNN_DY_mH_250_mA_50+Prob_DNN_TT_mH_250_mA_50+Prob_DNN_HToZA_mH_250_mA_50)
    - Prob_DNN_HToZA_mH_250_mA_50/(Prob_DNN_DY_mH_250_mA_50+Prob_DNN_TT_mH_250_mA_50+Prob_DNN_HToZA_mH_250_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_250_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_250_mA_50
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
    - Prob_MEM_DY_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_DNN_DY_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_MEM_TT_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_DNN_TT_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_MEM_HToZA_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
    - Prob_DNN_HToZA_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 250, mA = 100 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_250_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_250_mA_100
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
    - Prob_MEM_DY_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_MEM_TT_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_MEM_HToZA_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_250_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_250_mA_100
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
    - Prob_DNN_DY_mH_250_mA_100/(Prob_DNN_DY_mH_250_mA_100+Prob_DNN_TT_mH_250_mA_100+Prob_DNN_HToZA_mH_250_mA_100)
    - Prob_DNN_TT_mH_250_mA_100/(Prob_DNN_DY_mH_250_mA_100+Prob_DNN_TT_mH_250_mA_100+Prob_DNN_HToZA_mH_250_mA_100)
    - Prob_DNN_HToZA_mH_250_mA_100/(Prob_DNN_DY_mH_250_mA_100+Prob_DNN_TT_mH_250_mA_100+Prob_DNN_HToZA_mH_250_mA_100)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_250_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_250_mA_100
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
    - Prob_MEM_DY_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_DNN_DY_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_MEM_TT_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_DNN_TT_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_MEM_HToZA_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
    - Prob_DNN_HToZA_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 300, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_300_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_300_mA_50
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
    - Prob_MEM_DY_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_MEM_TT_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_MEM_HToZA_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_300_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_300_mA_50
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
    - Prob_DNN_DY_mH_300_mA_50/(Prob_DNN_DY_mH_300_mA_50+Prob_DNN_TT_mH_300_mA_50+Prob_DNN_HToZA_mH_300_mA_50)
    - Prob_DNN_TT_mH_300_mA_50/(Prob_DNN_DY_mH_300_mA_50+Prob_DNN_TT_mH_300_mA_50+Prob_DNN_HToZA_mH_300_mA_50)
    - Prob_DNN_HToZA_mH_300_mA_50/(Prob_DNN_DY_mH_300_mA_50+Prob_DNN_TT_mH_300_mA_50+Prob_DNN_HToZA_mH_300_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_300_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_300_mA_50
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
    - Prob_MEM_DY_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_DNN_DY_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_MEM_TT_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_DNN_TT_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_MEM_HToZA_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
    - Prob_DNN_HToZA_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 300, mA = 100 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_300_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_300_mA_100
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
    - Prob_MEM_DY_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_MEM_TT_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_MEM_HToZA_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_300_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_300_mA_100
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
    - Prob_DNN_DY_mH_300_mA_100/(Prob_DNN_DY_mH_300_mA_100+Prob_DNN_TT_mH_300_mA_100+Prob_DNN_HToZA_mH_300_mA_100)
    - Prob_DNN_TT_mH_300_mA_100/(Prob_DNN_DY_mH_300_mA_100+Prob_DNN_TT_mH_300_mA_100+Prob_DNN_HToZA_mH_300_mA_100)
    - Prob_DNN_HToZA_mH_300_mA_100/(Prob_DNN_DY_mH_300_mA_100+Prob_DNN_TT_mH_300_mA_100+Prob_DNN_HToZA_mH_300_mA_100)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_300_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_300_mA_100
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
    - Prob_MEM_DY_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_DNN_DY_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_MEM_TT_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_DNN_TT_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_MEM_HToZA_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
    - Prob_DNN_HToZA_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 300, mA = 200 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_300_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_300_mA_200
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
    - Prob_MEM_DY_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_MEM_TT_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_MEM_HToZA_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_300_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_300_mA_200
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
    - Prob_DNN_DY_mH_300_mA_200/(Prob_DNN_DY_mH_300_mA_200+Prob_DNN_TT_mH_300_mA_200+Prob_DNN_HToZA_mH_300_mA_200)
    - Prob_DNN_TT_mH_300_mA_200/(Prob_DNN_DY_mH_300_mA_200+Prob_DNN_TT_mH_300_mA_200+Prob_DNN_HToZA_mH_300_mA_200)
    - Prob_DNN_HToZA_mH_300_mA_200/(Prob_DNN_DY_mH_300_mA_200+Prob_DNN_TT_mH_300_mA_200+Prob_DNN_HToZA_mH_300_mA_200)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_300_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_300_mA_200
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
    - Prob_MEM_DY_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_DNN_DY_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_MEM_TT_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_DNN_TT_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_MEM_HToZA_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
    - Prob_DNN_HToZA_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 500, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_500_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_500_mA_50
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
    - Prob_MEM_DY_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_MEM_TT_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_MEM_HToZA_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_500_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_500_mA_50
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
    - Prob_DNN_DY_mH_500_mA_50/(Prob_DNN_DY_mH_500_mA_50+Prob_DNN_TT_mH_500_mA_50+Prob_DNN_HToZA_mH_500_mA_50)
    - Prob_DNN_TT_mH_500_mA_50/(Prob_DNN_DY_mH_500_mA_50+Prob_DNN_TT_mH_500_mA_50+Prob_DNN_HToZA_mH_500_mA_50)
    - Prob_DNN_HToZA_mH_500_mA_50/(Prob_DNN_DY_mH_500_mA_50+Prob_DNN_TT_mH_500_mA_50+Prob_DNN_HToZA_mH_500_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_500_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_500_mA_50
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
    - Prob_MEM_DY_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_DNN_DY_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_MEM_TT_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_DNN_TT_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_MEM_HToZA_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
    - Prob_DNN_HToZA_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 500, mA = 100 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_500_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_500_mA_100
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
    - Prob_MEM_DY_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_MEM_TT_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_MEM_HToZA_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_500_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_500_mA_100
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
    - Prob_DNN_DY_mH_500_mA_100/(Prob_DNN_DY_mH_500_mA_100+Prob_DNN_TT_mH_500_mA_100+Prob_DNN_HToZA_mH_500_mA_100)
    - Prob_DNN_TT_mH_500_mA_100/(Prob_DNN_DY_mH_500_mA_100+Prob_DNN_TT_mH_500_mA_100+Prob_DNN_HToZA_mH_500_mA_100)
    - Prob_DNN_HToZA_mH_500_mA_100/(Prob_DNN_DY_mH_500_mA_100+Prob_DNN_TT_mH_500_mA_100+Prob_DNN_HToZA_mH_500_mA_100)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_500_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_500_mA_100
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
    - Prob_MEM_DY_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_DNN_DY_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_MEM_TT_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_DNN_TT_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_MEM_HToZA_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
    - Prob_DNN_HToZA_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 500, mA = 200 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_500_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_500_mA_200
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
    - Prob_MEM_DY_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_MEM_TT_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_MEM_HToZA_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_500_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_500_mA_200
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
    - Prob_DNN_DY_mH_500_mA_200/(Prob_DNN_DY_mH_500_mA_200+Prob_DNN_TT_mH_500_mA_200+Prob_DNN_HToZA_mH_500_mA_200)
    - Prob_DNN_TT_mH_500_mA_200/(Prob_DNN_DY_mH_500_mA_200+Prob_DNN_TT_mH_500_mA_200+Prob_DNN_HToZA_mH_500_mA_200)
    - Prob_DNN_HToZA_mH_500_mA_200/(Prob_DNN_DY_mH_500_mA_200+Prob_DNN_TT_mH_500_mA_200+Prob_DNN_HToZA_mH_500_mA_200)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_500_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_500_mA_200
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
    - Prob_MEM_DY_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_DNN_DY_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_MEM_TT_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_DNN_TT_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_MEM_HToZA_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
    - Prob_DNN_HToZA_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 500, mA = 300 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_500_mA_300:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_500_mA_300
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
    - Prob_MEM_DY_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_MEM_TT_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_MEM_HToZA_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_500_mA_300:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_500_mA_300
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
    - Prob_DNN_DY_mH_500_mA_300/(Prob_DNN_DY_mH_500_mA_300+Prob_DNN_TT_mH_500_mA_300+Prob_DNN_HToZA_mH_500_mA_300)
    - Prob_DNN_TT_mH_500_mA_300/(Prob_DNN_DY_mH_500_mA_300+Prob_DNN_TT_mH_500_mA_300+Prob_DNN_HToZA_mH_500_mA_300)
    - Prob_DNN_HToZA_mH_500_mA_300/(Prob_DNN_DY_mH_500_mA_300+Prob_DNN_TT_mH_500_mA_300+Prob_DNN_HToZA_mH_500_mA_300)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_500_mA_300:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_500_mA_300
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
    - Prob_MEM_DY_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_DNN_DY_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_MEM_TT_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_DNN_TT_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_MEM_HToZA_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
    - Prob_DNN_HToZA_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 500, mA = 400 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_500_mA_400:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_500_mA_400
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
    - Prob_MEM_DY_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_MEM_TT_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_MEM_HToZA_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_500_mA_400:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_500_mA_400
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
    - Prob_DNN_DY_mH_500_mA_400/(Prob_DNN_DY_mH_500_mA_400+Prob_DNN_TT_mH_500_mA_400+Prob_DNN_HToZA_mH_500_mA_400)
    - Prob_DNN_TT_mH_500_mA_400/(Prob_DNN_DY_mH_500_mA_400+Prob_DNN_TT_mH_500_mA_400+Prob_DNN_HToZA_mH_500_mA_400)
    - Prob_DNN_HToZA_mH_500_mA_400/(Prob_DNN_DY_mH_500_mA_400+Prob_DNN_TT_mH_500_mA_400+Prob_DNN_HToZA_mH_500_mA_400)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_500_mA_400:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_500_mA_400
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
    - Prob_MEM_DY_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_DNN_DY_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_MEM_TT_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_DNN_TT_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_MEM_HToZA_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
    - Prob_DNN_HToZA_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 650, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_650_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_650_mA_50
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
    - Prob_MEM_DY_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_MEM_TT_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_MEM_HToZA_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_650_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_650_mA_50
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
    - Prob_DNN_DY_mH_650_mA_50/(Prob_DNN_DY_mH_650_mA_50+Prob_DNN_TT_mH_650_mA_50+Prob_DNN_HToZA_mH_650_mA_50)
    - Prob_DNN_TT_mH_650_mA_50/(Prob_DNN_DY_mH_650_mA_50+Prob_DNN_TT_mH_650_mA_50+Prob_DNN_HToZA_mH_650_mA_50)
    - Prob_DNN_HToZA_mH_650_mA_50/(Prob_DNN_DY_mH_650_mA_50+Prob_DNN_TT_mH_650_mA_50+Prob_DNN_HToZA_mH_650_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_650_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_650_mA_50
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
    - Prob_MEM_DY_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_DNN_DY_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_MEM_TT_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_DNN_TT_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_MEM_HToZA_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
    - Prob_DNN_HToZA_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 800, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_800_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_800_mA_50
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
    - Prob_MEM_DY_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_MEM_TT_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_MEM_HToZA_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_800_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_800_mA_50
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
    - Prob_DNN_DY_mH_800_mA_50/(Prob_DNN_DY_mH_800_mA_50+Prob_DNN_TT_mH_800_mA_50+Prob_DNN_HToZA_mH_800_mA_50)
    - Prob_DNN_TT_mH_800_mA_50/(Prob_DNN_DY_mH_800_mA_50+Prob_DNN_TT_mH_800_mA_50+Prob_DNN_HToZA_mH_800_mA_50)
    - Prob_DNN_HToZA_mH_800_mA_50/(Prob_DNN_DY_mH_800_mA_50+Prob_DNN_TT_mH_800_mA_50+Prob_DNN_HToZA_mH_800_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_800_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_800_mA_50
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
    - Prob_MEM_DY_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_DNN_DY_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_MEM_TT_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_DNN_TT_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_MEM_HToZA_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
    - Prob_DNN_HToZA_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 800, mA = 100 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_800_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_800_mA_100
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
    - Prob_MEM_DY_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_MEM_TT_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_MEM_HToZA_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_800_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_800_mA_100
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
    - Prob_DNN_DY_mH_800_mA_100/(Prob_DNN_DY_mH_800_mA_100+Prob_DNN_TT_mH_800_mA_100+Prob_DNN_HToZA_mH_800_mA_100)
    - Prob_DNN_TT_mH_800_mA_100/(Prob_DNN_DY_mH_800_mA_100+Prob_DNN_TT_mH_800_mA_100+Prob_DNN_HToZA_mH_800_mA_100)
    - Prob_DNN_HToZA_mH_800_mA_100/(Prob_DNN_DY_mH_800_mA_100+Prob_DNN_TT_mH_800_mA_100+Prob_DNN_HToZA_mH_800_mA_100)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_800_mA_100:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_800_mA_100
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
    - Prob_MEM_DY_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_DNN_DY_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_MEM_TT_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_DNN_TT_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_MEM_HToZA_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
    - Prob_DNN_HToZA_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 800, mA = 200 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_800_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_800_mA_200
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
    - Prob_MEM_DY_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_MEM_TT_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_MEM_HToZA_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_800_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_800_mA_200
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
    - Prob_DNN_DY_mH_800_mA_200/(Prob_DNN_DY_mH_800_mA_200+Prob_DNN_TT_mH_800_mA_200+Prob_DNN_HToZA_mH_800_mA_200)
    - Prob_DNN_TT_mH_800_mA_200/(Prob_DNN_DY_mH_800_mA_200+Prob_DNN_TT_mH_800_mA_200+Prob_DNN_HToZA_mH_800_mA_200)
    - Prob_DNN_HToZA_mH_800_mA_200/(Prob_DNN_DY_mH_800_mA_200+Prob_DNN_TT_mH_800_mA_200+Prob_DNN_HToZA_mH_800_mA_200)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_800_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_800_mA_200
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
    - Prob_MEM_DY_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_DNN_DY_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_MEM_TT_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_DNN_TT_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_MEM_HToZA_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
    - Prob_DNN_HToZA_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 800, mA = 400 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_800_mA_400:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_800_mA_400
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
    - Prob_MEM_DY_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_MEM_TT_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_MEM_HToZA_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_800_mA_400:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_800_mA_400
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
    - Prob_DNN_DY_mH_800_mA_400/(Prob_DNN_DY_mH_800_mA_400+Prob_DNN_TT_mH_800_mA_400+Prob_DNN_HToZA_mH_800_mA_400)
    - Prob_DNN_TT_mH_800_mA_400/(Prob_DNN_DY_mH_800_mA_400+Prob_DNN_TT_mH_800_mA_400+Prob_DNN_HToZA_mH_800_mA_400)
    - Prob_DNN_HToZA_mH_800_mA_400/(Prob_DNN_DY_mH_800_mA_400+Prob_DNN_TT_mH_800_mA_400+Prob_DNN_HToZA_mH_800_mA_400)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_800_mA_400:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_800_mA_400
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
    - Prob_MEM_DY_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_DNN_DY_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_MEM_TT_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_DNN_TT_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_MEM_HToZA_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
    - Prob_DNN_HToZA_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 800, mA = 700 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_800_mA_700:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_800_mA_700
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
    - Prob_MEM_DY_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_MEM_TT_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_MEM_HToZA_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_800_mA_700:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_800_mA_700
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
    - Prob_DNN_DY_mH_800_mA_700/(Prob_DNN_DY_mH_800_mA_700+Prob_DNN_TT_mH_800_mA_700+Prob_DNN_HToZA_mH_800_mA_700)
    - Prob_DNN_TT_mH_800_mA_700/(Prob_DNN_DY_mH_800_mA_700+Prob_DNN_TT_mH_800_mA_700+Prob_DNN_HToZA_mH_800_mA_700)
    - Prob_DNN_HToZA_mH_800_mA_700/(Prob_DNN_DY_mH_800_mA_700+Prob_DNN_TT_mH_800_mA_700+Prob_DNN_HToZA_mH_800_mA_700)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_800_mA_700:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_800_mA_700
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
    - Prob_MEM_DY_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_DNN_DY_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_MEM_TT_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_DNN_TT_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_MEM_HToZA_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
    - Prob_DNN_HToZA_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 1000, mA = 50 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_1000_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_1000_mA_50
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
    - Prob_MEM_DY_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_MEM_TT_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_MEM_HToZA_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_1000_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_1000_mA_50
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
    - Prob_DNN_DY_mH_1000_mA_50/(Prob_DNN_DY_mH_1000_mA_50+Prob_DNN_TT_mH_1000_mA_50+Prob_DNN_HToZA_mH_1000_mA_50)
    - Prob_DNN_TT_mH_1000_mA_50/(Prob_DNN_DY_mH_1000_mA_50+Prob_DNN_TT_mH_1000_mA_50+Prob_DNN_HToZA_mH_1000_mA_50)
    - Prob_DNN_HToZA_mH_1000_mA_50/(Prob_DNN_DY_mH_1000_mA_50+Prob_DNN_TT_mH_1000_mA_50+Prob_DNN_HToZA_mH_1000_mA_50)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_1000_mA_50:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_1000_mA_50
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
    - Prob_MEM_DY_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_DNN_DY_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_MEM_TT_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_DNN_TT_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_MEM_HToZA_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
    - Prob_DNN_HToZA_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 1000, mA = 200 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_1000_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_1000_mA_200
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
    - Prob_MEM_DY_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_MEM_TT_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_MEM_HToZA_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_1000_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_1000_mA_200
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
    - Prob_DNN_DY_mH_1000_mA_200/(Prob_DNN_DY_mH_1000_mA_200+Prob_DNN_TT_mH_1000_mA_200+Prob_DNN_HToZA_mH_1000_mA_200)
    - Prob_DNN_TT_mH_1000_mA_200/(Prob_DNN_DY_mH_1000_mA_200+Prob_DNN_TT_mH_1000_mA_200+Prob_DNN_HToZA_mH_1000_mA_200)
    - Prob_DNN_HToZA_mH_1000_mA_200/(Prob_DNN_DY_mH_1000_mA_200+Prob_DNN_TT_mH_1000_mA_200+Prob_DNN_HToZA_mH_1000_mA_200)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_1000_mA_200:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_1000_mA_200
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
    - Prob_MEM_DY_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_DNN_DY_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_MEM_TT_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_DNN_TT_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_MEM_HToZA_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
    - Prob_DNN_HToZA_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 1000, mA = 500 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_1000_mA_500:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_1000_mA_500
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
    - Prob_MEM_DY_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_MEM_TT_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_MEM_HToZA_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_1000_mA_500:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_1000_mA_500
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
    - Prob_DNN_DY_mH_1000_mA_500/(Prob_DNN_DY_mH_1000_mA_500+Prob_DNN_TT_mH_1000_mA_500+Prob_DNN_HToZA_mH_1000_mA_500)
    - Prob_DNN_TT_mH_1000_mA_500/(Prob_DNN_DY_mH_1000_mA_500+Prob_DNN_TT_mH_1000_mA_500+Prob_DNN_HToZA_mH_1000_mA_500)
    - Prob_DNN_HToZA_mH_1000_mA_500/(Prob_DNN_DY_mH_1000_mA_500+Prob_DNN_TT_mH_1000_mA_500+Prob_DNN_HToZA_mH_1000_mA_500)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_1000_mA_500:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_1000_mA_500
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
    - Prob_MEM_DY_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_DNN_DY_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_MEM_TT_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_DNN_TT_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_MEM_HToZA_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
    - Prob_DNN_HToZA_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 2000, mA = 1000 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_2000_mA_1000:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_2000_mA_1000
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
    - Prob_MEM_DY_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_MEM_TT_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_MEM_HToZA_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_2000_mA_1000:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_2000_mA_1000
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
    - Prob_DNN_DY_mH_2000_mA_1000/(Prob_DNN_DY_mH_2000_mA_1000+Prob_DNN_TT_mH_2000_mA_1000+Prob_DNN_HToZA_mH_2000_mA_1000)
    - Prob_DNN_TT_mH_2000_mA_1000/(Prob_DNN_DY_mH_2000_mA_1000+Prob_DNN_TT_mH_2000_mA_1000+Prob_DNN_HToZA_mH_2000_mA_1000)
    - Prob_DNN_HToZA_mH_2000_mA_1000/(Prob_DNN_DY_mH_2000_mA_1000+Prob_DNN_TT_mH_2000_mA_1000+Prob_DNN_HToZA_mH_2000_mA_1000)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_2000_mA_1000:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_2000_mA_1000
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
    - Prob_MEM_DY_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_DNN_DY_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_MEM_TT_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_DNN_TT_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_MEM_HToZA_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
    - Prob_DNN_HToZA_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



###########################################
######  Parameters mH = 3000, mA = 2000 ######
###########################################

##################### HToZA MEM weights ########################

MEM_Multi_Prob_mH_3000_mA_2000:
  filename: 
  tree: tree
  weight: ''
  name: MEM_Multi_Prob_mH_3000_mA_2000
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
    - Prob_MEM_DY_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_MEM_TT_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_MEM_HToZA_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True

##################### HToZA DNN weights ########################

DNN_Multi_Prob_mH_3000_mA_2000:
  filename: 
  tree: tree
  weight: ''
  name: DNN_Multi_Prob_mH_3000_mA_2000
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
    - Prob_DNN_DY_mH_3000_mA_2000/(Prob_DNN_DY_mH_3000_mA_2000+Prob_DNN_TT_mH_3000_mA_2000+Prob_DNN_HToZA_mH_3000_mA_2000)
    - Prob_DNN_TT_mH_3000_mA_2000/(Prob_DNN_DY_mH_3000_mA_2000+Prob_DNN_TT_mH_3000_mA_2000+Prob_DNN_HToZA_mH_3000_mA_2000)
    - Prob_DNN_HToZA_mH_3000_mA_2000/(Prob_DNN_DY_mH_3000_mA_2000+Prob_DNN_TT_mH_3000_mA_2000+Prob_DNN_HToZA_mH_3000_mA_2000)
  list_color:
    - 602
    - 633
    - 420
  list_legend:
    - P(Drell-Yan)
    - P(t\bar{t})
    - P(H\rightarrowZA)
  list_cut : '1'
  logy: True


##################### HToZA DNN+MEM weights ########################

Multi_Prob_mH_3000_mA_2000:
  filename: 
  tree: tree
  weight: ''
  name: Multi_Prob_mH_3000_mA_2000
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
    - Prob_MEM_DY_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_DNN_DY_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_MEM_TT_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_DNN_TT_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_MEM_HToZA_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
    - Prob_DNN_HToZA_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)

  list_color:
    - 602
    - 861
    - 636
    - 629
    - 420
    - 413
  list_legend:
    - P(Drell-Yan) from MEM
    - P(Drell-Yan) from DNN
    - P(t\bar{t}) from MEM
    - P(t\bar{t}) from DNN
    - P(H\rightarrowZA) from MEM
    - P(H\rightarrowZA) from DNN
  list_cut : '1'
  logy: True



















