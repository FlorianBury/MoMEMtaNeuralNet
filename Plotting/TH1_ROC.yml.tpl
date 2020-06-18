MEM_ratio_DNN_weight_DY:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_DY)
  variable2: -TMath::Log10(output_DY)
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_DY
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight_DY'
  xlabel: -log_{{10}}(weight)
  ylabel: events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_TT:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_TT)
  variable2: -TMath::Log10(output_TT)
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_TT
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight_TT'
  xlabel: -log_{{10}}(weight)
  ylabel: events
  legend1: 'MEM'
  legend2: 'DNN' 

Discriminant_ratio:
  filename: {file}
  tree: tree
  variable1: weight_TT/(weight_TT+weight_DY)
  variable2: output_TT/(output_TT+output_DY)
  name: {category}_{name}_sample_Discriminant_Ratio
  cut: {cut}
  bins: 50
  xmin: 0
  xmax: 1
  title: '{category} {name} sample : Discriminant Ratio'
  xlabel: Discriminant
  ylabel: events
  legend1: 'MEM'
  legend2: 'DNN' 
