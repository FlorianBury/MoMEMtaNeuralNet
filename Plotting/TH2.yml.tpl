MEM_vs_DNN_prob_HToZA:
  filename: {file}
  tree: tree
  variablex: prob_MEM_HToZA
  variabley: prob_DNN_HToZA
  weight: total_weight
  name: {category}_{name}_MEM_vs_DNN_prob_HToZA
  cut: {cut}
  binsx: 100
  xmin: 0
  xmax: 1
  binsy: 100
  ymin: 15
  ymax: 45
  title: '{category} {name} sample : MEM vs DNN P(HToZA)'
  xlabel: Probability from MEM
  ylabel: Probability from DNN
  zlabel: Events
  option: 'prof'

MEM_vs_DNN_prob_DY:
  filename: {file}
  tree: tree
  variablex: prob_MEM_DY
  variabley: prob_DNN_DY
  weight: total_weight
  name: {category}_{name}_MEM_vs_DNN_prob_DY
  cut: {cut}
  binsx: 100
  xmin: 0
  xmax: 1
  binsy: 100
  ymin: 15
  ymax: 45
  title: '{category} {name} sample : MEM vs DNN P(DY)'
  xlabel: Probability from MEM
  ylabel: Probability from DNN
  zlabel: Events
  option: 'prof'

MEM_vs_DNN_prob_TT:
  filename: {file}
  tree: tree
  variablex: prob_MEM_TT
  variabley: prob_DNN_TT
  weight: total_weight
  name: {category}_{name}_MEM_vs_DNN_prob_TT
  cut: {cut}
  binsx: 100
  xmin: 0
  xmax: 1
  binsy: 100
  ymin: 15
  ymax: 45
  title: '{category} {name} sample : MEM vs DNN P(TT)'
  xlabel: Probability from MEM
  ylabel: Probability from DNN
  zlabel: Events
  option: 'prof'
