##################### MEM ########################

ROC_MEM_NoJEC:
  tree: tree
  variable : weight_TT/(weight_TT+weight_DY) 
  weight : total_weight
  title : MEM without JEC
  cut : ''
  selector :
    'TT' : 1
    'DY' : 0
 
ROC_MEM_JEC:
  tree: tree
  variable : weight_TT_JEC/(weight_TT_JEC+weight_DY_JEC) 
  weight : total_weight
  title : MEM with JEC
  cut : ''
  selector :
    'TT' : 1
    'DY' : 0

##################### DNN ########################

ROC_DNN_NoJEC:
  tree: tree
  variable : output_TT/(output_TT+output_DY) 
  weight : total_weight
  title : DNN without JEC
  cut : ''
  selector :
    'TT' : 1
    'DY' : 0
 
ROC_DNN_JEC:
  tree: tree
  variable : output_TT_JEC/(output_TT_JEC+output_DY_JEC) 
  weight : total_weight
  title : DNN with JEC
  cut : ''
  selector :
    'TT' : 1
    'DY' : 0

