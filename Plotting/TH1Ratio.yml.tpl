MEM_ratio_DNN_weight_DY:
  filename: {file}
  tree: tree
  variable1: MEM_weight_DY
  variable2: output_DY 
  name: {name}_sample_MEM_ratio_DNN_weight_DY
  cut: ''
  bins: 150
  xmin: 0
  xmax: 30
  title: '{name} sample : Ratio MEM/DNN weight_DY'
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_TT:
  filename: {file}
  tree: tree
  variable1: MEM_weight_TT
  variable2: output_TT 
  name: {name}_sample_MEM_ratio_DNN_weight_TT
  cut: ''
  bins: 150
  xmin: 0
  xmax: 30
  title: '{name} sample : Ratio MEM/DNN weight_TT'
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 
