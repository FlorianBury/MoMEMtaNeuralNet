###########################################
######  Parameters mH = 200, mA = 50 ######
###########################################
MEM_prob_DY_mH_200_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
  weight: total_weight
  name: Prob_MEM_DY_mH_200_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 200 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_200_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
  weight: total_weight
  name: Prob_MEM_TT_mH_200_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 200 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_200_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_200_mA_50/(Prob_MEM_DY_mH_200_mA_50+Prob_MEM_TT_mH_200_mA_50+Prob_MEM_HToZA_mH_200_mA_50)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_200_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 200 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_200_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50)
  weight: total_weight
  name: Prob_DNN_DY
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 200 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_200_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50)
  weight: total_weight
  name: Prob_DNN_TT
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 200 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_200_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_200_mA_50/(Prob_DNN_DY_mH_200_mA_50+Prob_DNN_TT_mH_200_mA_50+Prob_DNN_HToZA_mH_200_mA_50)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_200_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 200 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events

###########################################
######  Parameters mH = 200, mA = 100 ######
###########################################
MEM_prob_DY_mH_200_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
  weight: total_weight
  name: Prob_MEM_DY_mH_200_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 200 GeV, mA = 100 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_200_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
  weight: total_weight
  name: Prob_MEM_TT_mH_200_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 200 GeV, mA = 100 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_200_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_200_mA_100/(Prob_MEM_DY_mH_200_mA_100+Prob_MEM_TT_mH_200_mA_100+Prob_MEM_HToZA_mH_200_mA_100)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_200_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 200 GeV, mA = 100 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_200_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_200_mA_100/(Prob_DNN_DY_mH_200_mA_100+Prob_DNN_TT_mH_200_mA_100+Prob_DNN_HToZA_mH_200_mA_100)
  weight: total_weight
  name: Prob_DNN_DY_mH_200_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 200 GeV, mA = 100 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_200_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_200_mA_100/(Prob_DNN_DY_mH_200_mA_100+Prob_DNN_TT_mH_200_mA_100+Prob_DNN_HToZA_mH_200_mA_100)
  weight: total_weight
  name: Prob_DNN_TT_mH_200_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 200 GeV, mA = 100 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_200_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_200_mA_100/(Prob_DNN_DY_mH_200_mA_100+Prob_DNN_TT_mH_200_mA_100+Prob_DNN_HToZA_mH_200_mA_100)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_200_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 200 GeV, mA = 100 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


###########################################
######  Parameters mH = 250, mA = 50 ######
###########################################
MEM_prob_DY_mH_250_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
  weight: total_weight
  name: Prob_MEM_DY_mH_250_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 250 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_250_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
  weight: total_weight
  name: Prob_MEM_TT_mH_250_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 250 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_250_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_250_mA_50/(Prob_MEM_DY_mH_250_mA_50+Prob_MEM_TT_mH_250_mA_50+Prob_MEM_HToZA_mH_250_mA_50)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_250_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 250 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_250_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_250_mA_50/(Prob_DNN_DY_mH_250_mA_50+Prob_DNN_TT_mH_250_mA_50+Prob_DNN_HToZA_mH_250_mA_50)
  weight: total_weight
  name: Prob_DNN_DY_mH_250_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 250 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_250_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_250_mA_50/(Prob_DNN_DY_mH_250_mA_50+Prob_DNN_TT_mH_250_mA_50+Prob_DNN_HToZA_mH_250_mA_50)
  weight: total_weight
  name: Prob_DNN_TT_mH_250_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 250 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_250_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_250_mA_50/(Prob_DNN_DY_mH_250_mA_50+Prob_DNN_TT_mH_250_mA_50+Prob_DNN_HToZA_mH_250_mA_50)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_250_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 250 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 250, mA = 100 ######
###########################################
MEM_prob_DY_mH_250_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
  weight: total_weight
  name: Prob_MEM_DY_mH_250_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 250 GeV, mA = 100 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_250_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
  weight: total_weight
  name: Prob_MEM_TT_mH_250_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 250 GeV, mA = 100 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_250_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_250_mA_100/(Prob_MEM_DY_mH_250_mA_100+Prob_MEM_TT_mH_250_mA_100+Prob_MEM_HToZA_mH_250_mA_100)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_250_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 250 GeV, mA = 100 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_250_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_250_mA_100/(Prob_DNN_DY_mH_250_mA_100+Prob_DNN_TT_mH_250_mA_100+Prob_DNN_HToZA_mH_250_mA_100)
  weight: total_weight
  name: Prob_DNN_DY_mH_250_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 250 GeV, mA = 100 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_250_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_250_mA_100/(Prob_DNN_DY_mH_250_mA_100+Prob_DNN_TT_mH_250_mA_100+Prob_DNN_HToZA_mH_250_mA_100)
  weight: total_weight
  name: Prob_DNN_TT_mH_250_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 250 GeV, mA = 100 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_250_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_250_mA_100/(Prob_DNN_DY_mH_250_mA_100+Prob_DNN_TT_mH_250_mA_100+Prob_DNN_HToZA_mH_250_mA_100)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_250_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 250 GeV, mA = 100 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 300, mA = 50 ######
###########################################
MEM_prob_DY_mH_300_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
  weight: total_weight
  name: Prob_MEM_DY_mH_300_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 300 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_300_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
  weight: total_weight
  name: Prob_MEM_TT_mH_300_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 300 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_300_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_300_mA_50/(Prob_MEM_DY_mH_300_mA_50+Prob_MEM_TT_mH_300_mA_50+Prob_MEM_HToZA_mH_300_mA_50)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_300_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 300 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_300_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_300_mA_50/(Prob_DNN_DY_mH_300_mA_50+Prob_DNN_TT_mH_300_mA_50+Prob_DNN_HToZA_mH_300_mA_50)
  weight: total_weight
  name: Prob_DNN_DY_mH_300_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 300 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_300_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_300_mA_50/(Prob_DNN_DY_mH_300_mA_50+Prob_DNN_TT_mH_300_mA_50+Prob_DNN_HToZA_mH_300_mA_50)
  weight: total_weight
  name: Prob_DNN_TT_mH_300_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 300 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_300_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_300_mA_50/(Prob_DNN_DY_mH_300_mA_50+Prob_DNN_TT_mH_300_mA_50+Prob_DNN_HToZA_mH_300_mA_50)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_300_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 300 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 300, mA = 100 ######
###########################################
MEM_prob_DY_mH_300_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
  weight: total_weight
  name: Prob_MEM_DY_mH_300_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 300 GeV, mA = 100 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_300_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
  weight: total_weight
  name: Prob_MEM_TT_mH_300_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 300 GeV, mA = 100 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_300_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_300_mA_100/(Prob_MEM_DY_mH_300_mA_100+Prob_MEM_TT_mH_300_mA_100+Prob_MEM_HToZA_mH_300_mA_100)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_300_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 300 GeV, mA = 100 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_300_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_300_mA_100/(Prob_DNN_DY_mH_300_mA_100+Prob_DNN_TT_mH_300_mA_100+Prob_DNN_HToZA_mH_300_mA_100)
  weight: total_weight
  name: Prob_DNN_DY_mH_300_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 300 GeV, mA = 100 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_300_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_300_mA_100/(Prob_DNN_DY_mH_300_mA_100+Prob_DNN_TT_mH_300_mA_100+Prob_DNN_HToZA_mH_300_mA_100)
  weight: total_weight
  name: Prob_DNN_TT_mH_300_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 300 GeV, mA = 100 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_300_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_300_mA_100/(Prob_DNN_DY_mH_300_mA_100+Prob_DNN_TT_mH_300_mA_100+Prob_DNN_HToZA_mH_300_mA_100)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_300_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 300 GeV, mA = 100 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 300, mA = 200 ######
###########################################
MEM_prob_DY_mH_300_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
  weight: total_weight
  name: Prob_MEM_DY_mH_300_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 300 GeV, mA = 200 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_300_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
  weight: total_weight
  name: Prob_MEM_TT_mH_300_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 300 GeV, mA = 200 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_300_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_300_mA_200/(Prob_MEM_DY_mH_300_mA_200+Prob_MEM_TT_mH_300_mA_200+Prob_MEM_HToZA_mH_300_mA_200)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_300_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 300 GeV, mA = 200 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_300_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_300_mA_200/(Prob_DNN_DY_mH_300_mA_200+Prob_DNN_TT_mH_300_mA_200+Prob_DNN_HToZA_mH_300_mA_200)
  weight: total_weight
  name: Prob_DNN_DY_mH_300_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 300 GeV, mA = 200 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_300_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_300_mA_200/(Prob_DNN_DY_mH_300_mA_200+Prob_DNN_TT_mH_300_mA_200+Prob_DNN_HToZA_mH_300_mA_200)
  weight: total_weight
  name: Prob_DNN_TT_mH_300_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 300 GeV, mA = 200 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_300_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_300_mA_200/(Prob_DNN_DY_mH_300_mA_200+Prob_DNN_TT_mH_300_mA_200+Prob_DNN_HToZA_mH_300_mA_200)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_300_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 300 GeV, mA = 200 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 500, mA = 50 ######
###########################################
MEM_prob_DY_mH_500_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
  weight: total_weight
  name: Prob_MEM_DY_mH_500_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 500 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_500_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
  weight: total_weight
  name: Prob_MEM_TT_mH_500_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 500 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_500_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_500_mA_50/(Prob_MEM_DY_mH_500_mA_50+Prob_MEM_TT_mH_500_mA_50+Prob_MEM_HToZA_mH_500_mA_50)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_500_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 500 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_500_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_500_mA_50/(Prob_DNN_DY_mH_500_mA_50+Prob_DNN_TT_mH_500_mA_50+Prob_DNN_HToZA_mH_500_mA_50)
  weight: total_weight
  name: Prob_DNN_DY_mH_500_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 500 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_500_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_500_mA_50/(Prob_DNN_DY_mH_500_mA_50+Prob_DNN_TT_mH_500_mA_50+Prob_DNN_HToZA_mH_500_mA_50)
  weight: total_weight
  name: Prob_DNN_TT_mH_500_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 500 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_500_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_500_mA_50/(Prob_DNN_DY_mH_500_mA_50+Prob_DNN_TT_mH_500_mA_50+Prob_DNN_HToZA_mH_500_mA_50)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_500_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 500 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 500, mA = 100 ######
###########################################
MEM_prob_DY_mH_500_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
  weight: total_weight
  name: Prob_MEM_DY_mH_500_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 500 GeV, mA = 100 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_500_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
  weight: total_weight
  name: Prob_MEM_TT_mH_500_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 500 GeV, mA = 100 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_500_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_500_mA_100/(Prob_MEM_DY_mH_500_mA_100+Prob_MEM_TT_mH_500_mA_100+Prob_MEM_HToZA_mH_500_mA_100)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_500_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 500 GeV, mA = 100 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_500_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_500_mA_100/(Prob_DNN_DY_mH_500_mA_100+Prob_DNN_TT_mH_500_mA_100+Prob_DNN_HToZA_mH_500_mA_100)
  weight: total_weight
  name: Prob_DNN_DY_mH_500_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 500 GeV, mA = 100 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_500_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_500_mA_100/(Prob_DNN_DY_mH_500_mA_100+Prob_DNN_TT_mH_500_mA_100+Prob_DNN_HToZA_mH_500_mA_100)
  weight: total_weight
  name: Prob_DNN_TT_mH_500_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 500 GeV, mA = 100 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_500_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_500_mA_100/(Prob_DNN_DY_mH_500_mA_100+Prob_DNN_TT_mH_500_mA_100+Prob_DNN_HToZA_mH_500_mA_100)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_500_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 500 GeV, mA = 100 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 500, mA = 200 ######
###########################################
MEM_prob_DY_mH_500_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
  weight: total_weight
  name: Prob_MEM_DY_mH_500_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 500 GeV, mA = 200 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_500_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
  weight: total_weight
  name: Prob_MEM_TT_mH_500_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 500 GeV, mA = 200 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_500_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_500_mA_200/(Prob_MEM_DY_mH_500_mA_200+Prob_MEM_TT_mH_500_mA_200+Prob_MEM_HToZA_mH_500_mA_200)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_500_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 500 GeV, mA = 200 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_500_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_500_mA_200/(Prob_DNN_DY_mH_500_mA_200+Prob_DNN_TT_mH_500_mA_200+Prob_DNN_HToZA_mH_500_mA_200)
  weight: total_weight
  name: Prob_DNN_DY_mH_500_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 500 GeV, mA = 200 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_500_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_500_mA_200/(Prob_DNN_DY_mH_500_mA_200+Prob_DNN_TT_mH_500_mA_200+Prob_DNN_HToZA_mH_500_mA_200)
  weight: total_weight
  name: Prob_DNN_TT_mH_500_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 500 GeV, mA = 200 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_500_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_500_mA_200/(Prob_DNN_DY_mH_500_mA_200+Prob_DNN_TT_mH_500_mA_200+Prob_DNN_HToZA_mH_500_mA_200)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_500_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 500 GeV, mA = 200 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 500, mA = 300 ######
###########################################
MEM_prob_DY_mH_500_mA_300:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
  weight: total_weight
  name: Prob_MEM_DY_mH_500_mA_300
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 500 GeV, mA = 300 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_500_mA_300:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
  weight: total_weight
  name: Prob_MEM_TT_mH_500_mA_300
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 500 GeV, mA = 300 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_500_mA_300:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_500_mA_300/(Prob_MEM_DY_mH_500_mA_300+Prob_MEM_TT_mH_500_mA_300+Prob_MEM_HToZA_mH_500_mA_300)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_500_mA_300
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 500 GeV, mA = 300 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_500_mA_300:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_500_mA_300/(Prob_DNN_DY_mH_500_mA_300+Prob_DNN_TT_mH_500_mA_300+Prob_DNN_HToZA_mH_500_mA_300)
  weight: total_weight
  name: Prob_DNN_DY_mH_500_mA_300
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 500 GeV, mA = 300 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_500_mA_300:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_500_mA_300/(Prob_DNN_DY_mH_500_mA_300+Prob_DNN_TT_mH_500_mA_300+Prob_DNN_HToZA_mH_500_mA_300)
  weight: total_weight
  name: Prob_DNN_TT_mH_500_mA_300
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 500 GeV, mA = 300 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_500_mA_300:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_500_mA_300/(Prob_DNN_DY_mH_500_mA_300+Prob_DNN_TT_mH_500_mA_300+Prob_DNN_HToZA_mH_500_mA_300)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_500_mA_300
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 500 GeV, mA = 300 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 500, mA = 400 ######
###########################################
MEM_prob_DY_mH_500_mA_400:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
  weight: total_weight
  name: Prob_MEM_DY_mH_500_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 500 GeV, mA = 400 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_500_mA_400:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
  weight: total_weight
  name: Prob_MEM_TT_mH_500_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 500 GeV, mA = 400 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_500_mA_400:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_500_mA_400/(Prob_MEM_DY_mH_500_mA_400+Prob_MEM_TT_mH_500_mA_400+Prob_MEM_HToZA_mH_500_mA_400)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_500_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 500 GeV, mA = 400 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_500_mA_400:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_500_mA_400/(Prob_DNN_DY_mH_500_mA_400+Prob_DNN_TT_mH_500_mA_400+Prob_DNN_HToZA_mH_500_mA_400)
  weight: total_weight
  name: Prob_DNN_DY_mH_500_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 500 GeV, mA = 400 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_500_mA_400:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_500_mA_400/(Prob_DNN_DY_mH_500_mA_400+Prob_DNN_TT_mH_500_mA_400+Prob_DNN_HToZA_mH_500_mA_400)
  weight: total_weight
  name: Prob_DNN_TT_mH_500_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 500 GeV, mA = 400 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_500_mA_400:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_500_mA_400/(Prob_DNN_DY_mH_500_mA_400+Prob_DNN_TT_mH_500_mA_400+Prob_DNN_HToZA_mH_500_mA_400)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_500_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 500 GeV, mA = 400 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 650, mA = 50 ######
###########################################
MEM_prob_DY_mH_650_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
  weight: total_weight
  name: Prob_MEM_DY_mH_650_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 650 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_650_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
  weight: total_weight
  name: Prob_MEM_TT_mH_650_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 650 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_650_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_650_mA_50/(Prob_MEM_DY_mH_650_mA_50+Prob_MEM_TT_mH_650_mA_50+Prob_MEM_HToZA_mH_650_mA_50)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_650_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 650 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_650_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_650_mA_50/(Prob_DNN_DY_mH_650_mA_50+Prob_DNN_TT_mH_650_mA_50+Prob_DNN_HToZA_mH_650_mA_50)
  weight: total_weight
  name: Prob_DNN_DY_mH_650_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 650 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_650_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_650_mA_50/(Prob_DNN_DY_mH_650_mA_50+Prob_DNN_TT_mH_650_mA_50+Prob_DNN_HToZA_mH_650_mA_50)
  weight: total_weight
  name: Prob_DNN_TT_mH_650_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 650 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_650_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_650_mA_50/(Prob_DNN_DY_mH_650_mA_50+Prob_DNN_TT_mH_650_mA_50+Prob_DNN_HToZA_mH_650_mA_50)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_650_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 650 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 800, mA = 50 ######
###########################################
MEM_prob_DY_mH_800_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
  weight: total_weight
  name: Prob_MEM_DY_mH_800_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 800 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_800_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
  weight: total_weight
  name: Prob_MEM_TT_mH_800_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 800 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_800_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_800_mA_50/(Prob_MEM_DY_mH_800_mA_50+Prob_MEM_TT_mH_800_mA_50+Prob_MEM_HToZA_mH_800_mA_50)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_800_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 800 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_800_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_800_mA_50/(Prob_DNN_DY_mH_800_mA_50+Prob_DNN_TT_mH_800_mA_50+Prob_DNN_HToZA_mH_800_mA_50)
  weight: total_weight
  name: Prob_DNN_DY_mH_800_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 800 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_800_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_800_mA_50/(Prob_DNN_DY_mH_800_mA_50+Prob_DNN_TT_mH_800_mA_50+Prob_DNN_HToZA_mH_800_mA_50)
  weight: total_weight
  name: Prob_DNN_TT_mH_800_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 800 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_800_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_800_mA_50/(Prob_DNN_DY_mH_800_mA_50+Prob_DNN_TT_mH_800_mA_50+Prob_DNN_HToZA_mH_800_mA_50)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_800_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 800 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 800, mA = 100 ######
###########################################
MEM_prob_DY_mH_800_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
  weight: total_weight
  name: Prob_MEM_DY_mH_800_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 800 GeV, mA = 100 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_800_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
  weight: total_weight
  name: Prob_MEM_TT_mH_800_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 800 GeV, mA = 100 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_800_mA_100:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_800_mA_100/(Prob_MEM_DY_mH_800_mA_100+Prob_MEM_TT_mH_800_mA_100+Prob_MEM_HToZA_mH_800_mA_100)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_800_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 800 GeV, mA = 100 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_800_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_800_mA_100/(Prob_DNN_DY_mH_800_mA_100+Prob_DNN_TT_mH_800_mA_100+Prob_DNN_HToZA_mH_800_mA_100)
  weight: total_weight
  name: Prob_DNN_DY_mH_800_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 800 GeV, mA = 100 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_800_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_800_mA_100/(Prob_DNN_DY_mH_800_mA_100+Prob_DNN_TT_mH_800_mA_100+Prob_DNN_HToZA_mH_800_mA_100)
  weight: total_weight
  name: Prob_DNN_TT_mH_800_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 800 GeV, mA = 100 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_800_mA_100:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_800_mA_100/(Prob_DNN_DY_mH_800_mA_100+Prob_DNN_TT_mH_800_mA_100+Prob_DNN_HToZA_mH_800_mA_100)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_800_mA_100
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 800 GeV, mA = 100 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 800, mA = 200 ######
###########################################
MEM_prob_DY_mH_800_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
  weight: total_weight
  name: Prob_MEM_DY_mH_800_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 800 GeV, mA = 200 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_800_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
  weight: total_weight
  name: Prob_MEM_TT_mH_800_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 800 GeV, mA = 200 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_800_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_800_mA_200/(Prob_MEM_DY_mH_800_mA_200+Prob_MEM_TT_mH_800_mA_200+Prob_MEM_HToZA_mH_800_mA_200)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_800_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 800 GeV, mA = 200 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_800_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_800_mA_200/(Prob_DNN_DY_mH_800_mA_200+Prob_DNN_TT_mH_800_mA_200+Prob_DNN_HToZA_mH_800_mA_200)
  weight: total_weight
  name: Prob_DNN_DY_mH_800_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 800 GeV, mA = 200 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_800_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_800_mA_200/(Prob_DNN_DY_mH_800_mA_200+Prob_DNN_TT_mH_800_mA_200+Prob_DNN_HToZA_mH_800_mA_200)
  weight: total_weight
  name: Prob_DNN_TT_mH_800_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 800 GeV, mA = 200 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_800_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_800_mA_200/(Prob_DNN_DY_mH_800_mA_200+Prob_DNN_TT_mH_800_mA_200+Prob_DNN_HToZA_mH_800_mA_200)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_800_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 800 GeV, mA = 200 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 800, mA = 400 ######
###########################################
MEM_prob_DY_mH_800_mA_400:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
  weight: total_weight
  name: Prob_MEM_DY_mH_800_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 800 GeV, mA = 400 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_800_mA_400:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
  weight: total_weight
  name: Prob_MEM_TT_mH_800_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 800 GeV, mA = 400 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_800_mA_400:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_800_mA_400/(Prob_MEM_DY_mH_800_mA_400+Prob_MEM_TT_mH_800_mA_400+Prob_MEM_HToZA_mH_800_mA_400)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_800_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 800 GeV, mA = 400 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_800_mA_400:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_800_mA_400/(Prob_DNN_DY_mH_800_mA_400+Prob_DNN_TT_mH_800_mA_400+Prob_DNN_HToZA_mH_800_mA_400)
  weight: total_weight
  name: Prob_DNN_DY_mH_800_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 800 GeV, mA = 400 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_800_mA_400:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_800_mA_400/(Prob_DNN_DY_mH_800_mA_400+Prob_DNN_TT_mH_800_mA_400+Prob_DNN_HToZA_mH_800_mA_400)
  weight: total_weight
  name: Prob_DNN_TT_mH_800_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 800 GeV, mA = 400 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_800_mA_400:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_800_mA_400/(Prob_DNN_DY_mH_800_mA_400+Prob_DNN_TT_mH_800_mA_400+Prob_DNN_HToZA_mH_800_mA_400)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_800_mA_400
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 800 GeV, mA = 400 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 800, mA = 700 ######
###########################################
MEM_prob_DY_mH_800_mA_700:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
  weight: total_weight
  name: Prob_MEM_DY_mH_800_mA_700
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 800 GeV, mA = 700 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_800_mA_700:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
  weight: total_weight
  name: Prob_MEM_TT_mH_800_mA_700
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 800 GeV, mA = 700 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_800_mA_700:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_800_mA_700/(Prob_MEM_DY_mH_800_mA_700+Prob_MEM_TT_mH_800_mA_700+Prob_MEM_HToZA_mH_800_mA_700)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_800_mA_700
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 800 GeV, mA = 700 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_800_mA_700:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_800_mA_700/(Prob_DNN_DY_mH_800_mA_700+Prob_DNN_TT_mH_800_mA_700+Prob_DNN_HToZA_mH_800_mA_700)
  weight: total_weight
  name: Prob_DNN_DY_mH_800_mA_700
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 800 GeV, mA = 700 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_800_mA_700:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_800_mA_700/(Prob_DNN_DY_mH_800_mA_700+Prob_DNN_TT_mH_800_mA_700+Prob_DNN_HToZA_mH_800_mA_700)
  weight: total_weight
  name: Prob_DNN_TT_mH_800_mA_700
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 800 GeV, mA = 700 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_800_mA_700:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_800_mA_700/(Prob_DNN_DY_mH_800_mA_700+Prob_DNN_TT_mH_800_mA_700+Prob_DNN_HToZA_mH_800_mA_700)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_800_mA_700
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 800 GeV, mA = 700 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 1000, mA = 50 ######
###########################################
MEM_prob_DY_mH_1000_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
  weight: total_weight
  name: Prob_MEM_DY_mH_1000_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 1000 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_1000_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
  weight: total_weight
  name: Prob_MEM_TT_mH_1000_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 1000 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_1000_mA_50:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_1000_mA_50/(Prob_MEM_DY_mH_1000_mA_50+Prob_MEM_TT_mH_1000_mA_50+Prob_MEM_HToZA_mH_1000_mA_50)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_1000_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 1000 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_1000_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_1000_mA_50/(Prob_DNN_DY_mH_1000_mA_50+Prob_DNN_TT_mH_1000_mA_50+Prob_DNN_HToZA_mH_1000_mA_50)
  weight: total_weight
  name: Prob_DNN_DY_mH_1000_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 1000 GeV, mA = 50 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_1000_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_1000_mA_50/(Prob_DNN_DY_mH_1000_mA_50+Prob_DNN_TT_mH_1000_mA_50+Prob_DNN_HToZA_mH_1000_mA_50)
  weight: total_weight
  name: Prob_DNN_TT_mH_1000_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 1000 GeV, mA = 50 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_1000_mA_50:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_1000_mA_50/(Prob_DNN_DY_mH_1000_mA_50+Prob_DNN_TT_mH_1000_mA_50+Prob_DNN_HToZA_mH_1000_mA_50)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_1000_mA_50
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 1000 GeV, mA = 50 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 1000, mA = 200 ######
###########################################
MEM_prob_DY_mH_1000_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
  weight: total_weight
  name: Prob_MEM_DY_mH_1000_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 1000 GeV, mA = 200 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_1000_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
  weight: total_weight
  name: Prob_MEM_TT_mH_1000_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 1000 GeV, mA = 200 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_1000_mA_200:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_1000_mA_200/(Prob_MEM_DY_mH_1000_mA_200+Prob_MEM_TT_mH_1000_mA_200+Prob_MEM_HToZA_mH_1000_mA_200)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_1000_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 1000 GeV, mA = 200 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_1000_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_1000_mA_200/(Prob_DNN_DY_mH_1000_mA_200+Prob_DNN_TT_mH_1000_mA_200+Prob_DNN_HToZA_mH_1000_mA_200)
  weight: total_weight
  name: Prob_DNN_DY_mH_1000_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 1000 GeV, mA = 200 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_1000_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_1000_mA_200/(Prob_DNN_DY_mH_1000_mA_200+Prob_DNN_TT_mH_1000_mA_200+Prob_DNN_HToZA_mH_1000_mA_200)
  weight: total_weight
  name: Prob_DNN_TT_mH_1000_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 1000 GeV, mA = 200 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_1000_mA_200:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_1000_mA_200/(Prob_DNN_DY_mH_1000_mA_200+Prob_DNN_TT_mH_1000_mA_200+Prob_DNN_HToZA_mH_1000_mA_200)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_1000_mA_200
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 1000 GeV, mA = 200 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 1000, mA = 500 ######
###########################################
MEM_prob_DY_mH_1000_mA_500:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
  weight: total_weight
  name: Prob_MEM_DY_mH_1000_mA_500
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 1000 GeV, mA = 500 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_1000_mA_500:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
  weight: total_weight
  name: Prob_MEM_TT_mH_1000_mA_500
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 1000 GeV, mA = 500 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_1000_mA_500:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_1000_mA_500/(Prob_MEM_DY_mH_1000_mA_500+Prob_MEM_TT_mH_1000_mA_500+Prob_MEM_HToZA_mH_1000_mA_500)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_1000_mA_500
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 1000 GeV, mA = 500 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_1000_mA_500:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_1000_mA_500/(Prob_DNN_DY_mH_1000_mA_500+Prob_DNN_TT_mH_1000_mA_500+Prob_DNN_HToZA_mH_1000_mA_500)
  weight: total_weight
  name: Prob_DNN_DY_mH_1000_mA_500
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 1000 GeV, mA = 500 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_1000_mA_500:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_1000_mA_500/(Prob_DNN_DY_mH_1000_mA_500+Prob_DNN_TT_mH_1000_mA_500+Prob_DNN_HToZA_mH_1000_mA_500)
  weight: total_weight
  name: Prob_DNN_TT_mH_1000_mA_500
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 1000 GeV, mA = 500 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_1000_mA_500:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_1000_mA_500/(Prob_DNN_DY_mH_1000_mA_500+Prob_DNN_TT_mH_1000_mA_500+Prob_DNN_HToZA_mH_1000_mA_500)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_1000_mA_500
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 1000 GeV, mA = 500 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 2000, mA = 1000 ######
###########################################
MEM_prob_DY_mH_2000_mA_1000:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
  weight: total_weight
  name: Prob_MEM_DY_mH_2000_mA_1000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 2000 GeV, mA = 1000 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_2000_mA_1000:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
  weight: total_weight
  name: Prob_MEM_TT_mH_2000_mA_1000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 2000 GeV, mA = 1000 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_2000_mA_1000:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_2000_mA_1000/(Prob_MEM_DY_mH_2000_mA_1000+Prob_MEM_TT_mH_2000_mA_1000+Prob_MEM_HToZA_mH_2000_mA_1000)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_2000_mA_1000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 2000 GeV, mA = 1000 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_2000_mA_1000:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_2000_mA_1000/(Prob_DNN_DY_mH_2000_mA_1000+Prob_DNN_TT_mH_2000_mA_1000+Prob_DNN_HToZA_mH_2000_mA_1000)
  weight: total_weight
  name: Prob_DNN_DY_mH_2000_mA_1000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 2000 GeV, mA = 1000 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_2000_mA_1000:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_2000_mA_1000/(Prob_DNN_DY_mH_2000_mA_1000+Prob_DNN_TT_mH_2000_mA_1000+Prob_DNN_HToZA_mH_2000_mA_1000)
  weight: total_weight
  name: Prob_DNN_TT_mH_2000_mA_1000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 2000 GeV, mA = 1000 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_2000_mA_1000:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_2000_mA_1000/(Prob_DNN_DY_mH_2000_mA_1000+Prob_DNN_TT_mH_2000_mA_1000+Prob_DNN_HToZA_mH_2000_mA_1000)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_2000_mA_1000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 2000 GeV, mA = 1000 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



###########################################
######  Parameters mH = 3000, mA = 2000 ######
###########################################
MEM_prob_DY_mH_3000_mA_2000:
  filename: 
  tree: tree
  variable: Prob_MEM_DY_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
  weight: total_weight
  name: Prob_MEM_DY_mH_3000_mA_2000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from MEM weights (MH = 3000 GeV, mA = 2000 GeV)'
  xlabel: P(DY)
  ylabel: Events

MEM_prob_TT_mH_3000_mA_2000:
  filename: 
  tree: tree
  variable: Prob_MEM_TT_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
  weight: total_weight
  name: Prob_MEM_TT_mH_3000_mA_2000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from MEM weights (MH = 3000 GeV, mA = 2000 GeV)'
  xlabel: P(TT)
  ylabel: Events

MEM_prob_HToZA_mH_3000_mA_2000:
  filename: 
  tree: tree
  variable: Prob_MEM_HToZA_mH_3000_mA_2000/(Prob_MEM_DY_mH_3000_mA_2000+Prob_MEM_TT_mH_3000_mA_2000+Prob_MEM_HToZA_mH_3000_mA_2000)
  weight: total_weight
  name: Prob_MEM_HToZA_mH_3000_mA_2000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from MEM weights (MH = 3000 GeV, mA = 2000 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events


DNN_prob_DY_mH_3000_mA_2000:
  filename: 
  tree: tree
  variable: Prob_DNN_DY_mH_3000_mA_2000/(Prob_DNN_DY_mH_3000_mA_2000+Prob_DNN_TT_mH_3000_mA_2000+Prob_DNN_HToZA_mH_3000_mA_2000)
  weight: total_weight
  name: Prob_DNN_DY_mH_3000_mA_2000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : DY probability from DNN weights (MH = 3000 GeV, mA = 2000 GeV)'
  xlabel: P(DY)
  ylabel: Events

DNN_prob_TT_mH_3000_mA_2000:
  filename: 
  tree: tree
  variable: Prob_DNN_TT_mH_3000_mA_2000/(Prob_DNN_DY_mH_3000_mA_2000+Prob_DNN_TT_mH_3000_mA_2000+Prob_DNN_HToZA_mH_3000_mA_2000)
  weight: total_weight
  name: Prob_DNN_TT_mH_3000_mA_2000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : TT probability from DNN weights (MH = 3000 GeV, mA = 2000 GeV)'
  xlabel: P(TT)
  ylabel: Events

DNN_prob_HToZA_mH_3000_mA_2000:
  filename: 
  tree: tree
  variable: Prob_DNN_HToZA_mH_3000_mA_2000/(Prob_DNN_DY_mH_3000_mA_2000+Prob_DNN_TT_mH_3000_mA_2000+Prob_DNN_HToZA_mH_3000_mA_2000)
  weight: total_weight
  name: Prob_DNN_HToZA_mH_3000_mA_2000
  cut: ''
  bins: 50
  xmin: 0
  xmax: 1
  title: '{} sample : Signal probability from DNN weights (MH = 3000 GeV, mA = 2000 GeV)'
  xlabel: P(H \rightarrow ZA)
  ylabel: Events



