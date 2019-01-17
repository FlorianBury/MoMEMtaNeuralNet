MEM_vs_DNN_weight_DY:
  filename: {file}
  tree: tree
  variablex: MEM_weight_DY
  variabley: output_DY 
  name: {name}_sample_MEM_vs_DNN_weight_DY
  cut: ''
  binsx: 150
  xmin: 0
  xmax: 30
  binsy: 150
  ymin: 0
  ymax: 30
  title: '{name} sample : MEM vs DNN weight DY'
  xlabel: -log_{{10}}(weight from MEM)
  ylabel: -log_{{10}}(weight from DNN)
  zlabel: Events

MEM_vs_DNN_weight_TT:
  filename: {file}
  tree: tree
  variablex: MEM_weight_TT
  variabley: output_TT 
  name: {name}_sample_MEM_vs_DNN_weight_TT
  cut: ''
  binsx: 150
  xmin: 0
  xmax: 30
  binsy: 150
  ymin: 0
  ymax: 30
  title: '{name} sample : MEM vs DNN weight TT'
  xlabel: -log_{{10}}(weight from MEM)
  ylabel: -log_{{10}}(weight from DNN)
  zlabel: Events
