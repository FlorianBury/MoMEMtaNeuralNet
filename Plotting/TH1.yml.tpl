MEM_weight_DY:
  filename: {file}
  tree: tree
  variable: MEM_weight_DY
  name: {name}_sample_MEM_weight_DY
  cut: ''
  bins: 150
  xmin: 0
  xmax: 30
  title: '{name} sample : MEM weight_DY'
  xlabel: -log_{{10}}(weight)
  ylabel: Events

MEM_weight_TT:
  filename: {file}
  tree: tree
  variable: MEM_weight_TT
  name: {name}_sample_MEM_weight_TT
  cut: ''
  bins: 150
  xmin: 0
  xmax: 30
  title: '{name} sample : MEM weight_TT'
  xlabel: -log_{{10}}(weight)
  ylabel: Events

DNN_weight_DY:
  filename: {file}
  tree: tree
  variable: output_DY
  name: {name}_sample_DNN_weight_DY
  cut: ''
  bins: 150
  xmin: 0
  xmax: 30
  title: '{name} sample : DNN weight_DY'
  xlabel: -log_{{10}}(weight)
  ylabel: Events

DNN_weight_TT:
  filename: {file}
  tree: tree
  variable: output_TT
  name: {name}_sample_DNN_weight_TT
  cut: ''
  bins: 150
  xmin: 0
  xmax: 30
  title: '{name} sample : DNN weight_TT'
  xlabel: -log_{{10}}(weight)
  ylabel: Events
