MEM_vs_DNN_weight_DY:
  filename: {file}
  tree: tree
  variablex: -TMath::Log10(weight_DY)
  variabley: -TMath::Log10(output_DY) 
  weight: total_weight
  name: {category}_{name}_sample_MEM_vs_DNN_weight_DY
  cut: {cut}
  binsx: 150
  xmin: 15
  xmax: 45
  binsy: 150
  ymin: 15
  ymax: 45
  title: '{category} {name} sample : MEM vs DNN weight DY'
  xlabel: -log_{{10}}(weight from MEM)
  ylabel: -log_{{10}}(weight from DNN)
  zlabel: Events
  option : colz

MEM_vs_DNN_weight_TT:
  filename: {file}
  tree: tree
  variablex: -TMath::Log10(weight_TT)
  variabley: -TMath::Log10(output_TT)
  weight: total_weight
  name: {category}_{name}_sample_MEM_vs_DNN_weight_TT
  cut: {cut}
  binsx: 150
  xmin: 15
  xmax: 45
  binsy: 150
  ymin: 15
  ymax: 45
  title: '{category} {name} sample : MEM vs DNN weight TT'
  xlabel: -log_{{10}}(weight from MEM)
  ylabel: -log_{{10}}(weight from DNN)
  zlabel: Events
  option : colz
