##################### MEM ########################

ROC_MEM_NoJEC:
  tree: tree
  variable : weight_TT/(weight_TT+weight_DY) 
  weight : ''
  title : MoMEMta weight, nominal events
  cut : 'weight_TT_err<weight_TT && weight_DY_err<weight_DY'
  selector :
    'TT' : 1
    'DY' : 0
 
ROC_MEM_JEC:
  tree: tree
  variable : weight_TT_JEC/(weight_TT_JEC+weight_DY_JEC) 
  title : MoMEMta weights, shifted JES
  cut : ''
  cut : 'weight_TT_err<weight_TT && weight_DY_err<weight_DY'
  selector :
    'TT' : 1
    'DY' : 0

##################### DNN ########################

ROC_DNN_NoJEC:
  tree: tree
  variable : output_TT/(output_TT+output_DY) 
  weight : ''
  title : DNN weights, nominal events
  cut : 'weight_TT_err<weight_TT && weight_DY_err<weight_DY'
  selector :
    'TT' : 1
    'DY' : 0
 
ROC_DNN_JEC:
  tree: tree
  variable : output_TT_JEC/(output_TT_JEC+output_DY_JEC) 
  weight : ''
  title : DNN weights, shifted JES
  cut : 'weight_TT_err<weight_TT && weight_DY_err<weight_DY'
  selector :
    'TT' : 1
    'DY' : 0

