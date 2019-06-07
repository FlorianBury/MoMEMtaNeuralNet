##################### MEM ########################

ROC_MEM:
  tree: tree
  variable : Prob_MEM_signal
  weight : total_weight
  title : MEM
  cut : ''
  selector :
    'TT' : 0
    'DY' : 0
    'HToZA' : 0
 
##################### DNN ########################

ROC_DNN:
  tree: tree
  variable : Prob_DNN_signal
  weight : total_weight
  title : DNN
  cut : ''
  selector :
    'TT' : 0
    'DY' : 0
    'HToZA' : 0
 

