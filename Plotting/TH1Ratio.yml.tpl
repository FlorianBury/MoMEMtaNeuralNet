MEM_ratio_DNN_prob_HToZA:
  filename: {file}
  tree: tree
  variable1: prob_MEM_HToZA
  variable2: prob_DNN_HToZA
  weight: total_weight
  name: {category}_{name}_MEM_ratio_DNN_prob_HToZA
  cut: {cut}
  bins: 100
  xmin: 0
  xmax: 1
  title: '{category} {name} sample : Ratio MEM/DNN P(HToZA)'
  xlabel: Probability of HToZA
  ylabel: Events
  legend1: 'Weights from MEM'
  legend2: 'Weights from DNN' 

MEM_ratio_DNN_prob_DY:
  filename: {file}
  tree: tree
  variable1: prob_MEM_DY
  variable2: prob_DNN_DY
  weight: total_weight
  name: {category}_{name}_MEM_ratio_DNN_prob_DY
  cut: {cut}
  bins: 100
  xmin: 0
  xmax: 1
  title: '{category} {name} sample : Ratio MEM/DNN P(DY)'
  xlabel: Probability of DY
  ylabel: Events
  legend1: 'Weights from MEM'
  legend2: 'Weights from DNN' 

MEM_ratio_DNN_prob_TT:
  filename: {file}
  tree: tree
  variable1: prob_MEM_TT
  variable2: prob_DNN_TT
  weight: total_weight
  name: {category}_{name}_MEM_ratio_DNN_prob_TT
  cut: {cut}
  bins: 100
  xmin: 0
  xmax: 1
  title: '{category} {name} sample : Ratio MEM/DNN P(TT)'
  xlabel: Probability of TT
  ylabel: Events
  legend1: 'Weights from MEM'
  legend2: 'Weights from DNN' 

