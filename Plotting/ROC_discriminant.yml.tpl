##################### MEM ########################

ROC_MEM:
  tree: tree
  variable : weight_TT/(weight_TT+weight_DY)
  weight : total_weight
  title : MEM
  cut : ''
  selector :
    'TT' : 1
    'DY' : 0
 
##################### DNN ########################

ROC_DNN:
  tree: tree
  variable : output_TT/(output_TT+output_DY)
  weight : total_weight
  title : DNN
  cut : ''
  selector :
    'TT' : 1
    'DY' : 0
  
  

