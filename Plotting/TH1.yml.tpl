MEM_weight_DY:
  filename: {file}
  tree: tree
  variable: -TMath::Log10(MEM_weight_DY)
  name: {category}_{name}_sample_MEM_weight_DY
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : MEM weight DY'
  xlabel: -log_{{10}}(weight)
  ylabel: Events

MEM_weight_TT:
  filename: {file}
  tree: tree
  variable: -TMath::Log10(MEM_weight_TT)
  name: {category}_{name}_sample_MEM_weight_TT
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : MEM weight TT'
  xlabel: -log_{{10}}(weight)
  ylabel: Events

DNN_weight_DY:
  filename: {file}
  tree: tree
  variable: -TMath::Log10(output_DY)
  name: {category}_{name}_sample_DNN_weight_DY
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : DNN weight DY'
  xlabel: -log_{{10}}(weight)
  ylabel: Events

DNN_weight_TT:
  filename: {file}
  tree: tree
  variable: -TMath::Log10(output_TT)
  name: {category}_{name}_sample_DNN_weight_TT
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : DNN weight TT'
  xlabel: -log_{{10}}(weight)
  ylabel: Events

Discriminant_MEM:
  filename: {file}
  tree: tree
  variable: MEM_weight_TT/(MEM_weight_TT+MEM_weight_DY)
  name: {category}_{name}_sample_MEM_Discriminant
  cut: {cut}
  bins: 50
  xmin: 0
  xmax: 1
  title: '{category} {name} sample : MEM Discriminant '
  xlabel: Discriminant
  ylabel: Events

Discriminant_DNN:
  filename: {file}
  tree: tree
  variable: output_TT/(output_TT+output_DY)
  name: {category}_{name}_sample_DNN_Discriminant
  cut: {cut}
  bins: 50
  xmin: 0
  xmax: 1
  title: '{category} {name} sample : DNN Discriminant '
  xlabel: Discriminant
  ylabel: Events



