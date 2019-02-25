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

MEM_TT_vs_DY:
  filename: {file}
  tree: tree
  variablex: -TMath::Log10(weight_TT)
  variabley: -TMath::Log10(weight_DY)
  weight: total_weight
  name: {category}_{name}_sample_MEM_TT_vs_DY
  cut: {cut}
  binsx: 150
  xmin: 15
  xmax: 45
  binsy: 150
  ymin: 15
  ymax: 45
  title: '{category} {name} sample : MEM weight TT vs weight DY'
  xlabel: -log_{{10}}(TT weight)
  ylabel: -log_{{10}}(DY weights)
  zlabel: Events
  option : colz

DNN_TT_vs_DY:
  filename: {file}
  tree: tree
  variablex: -TMath::Log10(output_TT)
  variabley: -TMath::Log10(output_DY)
  weight: total_weight
  name: {category}_{name}_sample_DNN_TT_vs_DY
  cut: {cut}
  binsx: 150
  xmin: 15
  xmax: 45
  binsy: 150
  ymin: 15
  ymax: 45
  title: '{category} {name} sample : DNN weight TT vs weight DY'
  xlabel: -log_{{10}}(TT weight)
  ylabel: -log_{{10}}(DY weights)
  zlabel: Events
  option : colz

MEM_TT_vs_DY_working_point:
  filename: {file}
  tree: tree
  variablex: -TMath::Log10(weight_TT)
  variabley: -TMath::Log10(weight_DY)
  weight: total_weight
  name: {category}_{name}_sample_MEM_TT_vs_DY_working_point
  cut: {cut} #'&''&' weight_TT/(weight_TT+200*weight_DY)'>'0.61231
  binsx: 150
  xmin: 15
  xmax: 45
  binsy: 150
  ymin: 15
  ymax: 45
  title: '{category} {name} sample : MEM weight TT vs weight DY at working point 80% TPR'
  xlabel: -log_{{10}}(TT weight)
  ylabel: -log_{{10}}(DY weights)
  zlabel: Events
  option : colz

DNN_TT_vs_DY_working_point:
  filename: {file}
  tree: tree
  variablex: -TMath::Log10(output_TT)
  variabley: -TMath::Log10(output_DY)
  weight: total_weight
  name: {category}_{name}_sample_DNN_TT_vs_DY_working_point
  cut: {cut} #'&''&' 'output_TT/(output_TT+200*output_DY)'>'0.52079
  binsx: 150
  xmin: 15
  xmax: 45
  binsy: 150
  ymin: 15
  ymax: 45
  title: '{category} {name} sample : DNN weight TT vs weight DY at working point 80% TPR'
  xlabel: -log_{{10}}(TT weight)
  ylabel: -log_{{10}}(DY weights)
  zlabel: Events
  option : colz
