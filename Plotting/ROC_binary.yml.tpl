##################### MEM ########################

ROC_MEM:
  tree: tree
  variable : Prob_MEM_signal
  weight : ''
  title : MoMEMta
  cut : ''
  selector :
    'TT' : 0
    'DY' : 0
    'HToZA' : 1
 
##################### DNN ########################

ROC_DNN:
  tree: tree
  variable : Prob_DNN_signal
  weight : ''
  title : DNN
  cut : ''
  selector :
    'TT' : 0
    'DY' : 0
    'HToZA' : 1
 

