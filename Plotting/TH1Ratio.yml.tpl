############################################################
####################### DY weights #########################
############################################################

MEM_ratio_DNN_weight_DY:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_DY)
  variable2: -TMath::Log10(output_DY)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_DY
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight DY'
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

############################################################
####################### TT weights #########################
############################################################

MEM_ratio_DNN_weight_TT:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_TT)
  variable2: -TMath::Log10(output_TT)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_TT
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight TT'
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

############################################################
##################### Dicriminant  #########################
############################################################

Discriminant_ratio:
  filename: {file}
  tree: tree
  variable1: weight_TT/(weight_TT+weight_DY)
  variable2: output_TT/(output_TT+output_DY)
  weight: total_weight
  name: {category}_{name}_sample_Discriminant_Ratio
  cut: {cut}
  bins: 50
  xmin: 0
  xmax: 1
  title: '{category} {name} sample : Discriminant Ratio'
  xlabel: Discriminant
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

############################################################
##################### HToZA weights ########################
############################################################

MEM_ratio_DNN_weight_HToZA_mH_200_mA_50:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_200_mA_50)
  variable2: -TMath::Log10(output_HToZA_mH_200_mA_50)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_200_mA_50
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 200 GeV, MA = 50 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_200_mA_100:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_200_mA_100)
  variable2: -TMath::Log10(output_HToZA_mH_200_mA_100)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_200_mA_100
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 200 GeV, MA = 100 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_250_mA_50:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_250_mA_50)
  variable2: -TMath::Log10(output_HToZA_mH_250_mA_50)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_250_mA_50
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 250 GeV, MA = 50 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_250_mA_100:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_250_mA_100)
  variable2: -TMath::Log10(output_HToZA_mH_250_mA_100)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_250_mA_100
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 250 GeV, MA = 100 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_300_mA_50:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_300_mA_50)
  variable2: -TMath::Log10(output_HToZA_mH_300_mA_50)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_300_mA_50
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 300 GeV, MA = 50 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_300_mA_100:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_300_mA_100)
  variable2: -TMath::Log10(output_HToZA_mH_300_mA_100)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_300_mA_100
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 300 GeV, MA = 100 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_300_mA_200:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_300_mA_200)
  variable2: -TMath::Log10(output_HToZA_mH_300_mA_200)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_300_mA_200
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 300 GeV, MA = 200 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_500_mA_50:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_500_mA_50)
  variable2: -TMath::Log10(output_HToZA_mH_500_mA_50)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_500_mA_50
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 500 GeV, MA = 50 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_500_mA_100:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_500_mA_100)
  variable2: -TMath::Log10(output_HToZA_mH_500_mA_100)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_500_mA_100
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 500 GeV, MA = 50 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_500_mA_200:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_500_mA_200)
  variable2: -TMath::Log10(output_HToZA_mH_500_mA_200)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_500_mA_200
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 500 GeV, MA = 200 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_500_mA_300:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_500_mA_300)
  variable2: -TMath::Log10(output_HToZA_mH_500_mA_300)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_500_mA_300
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 500 GeV, MA = 300 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_500_mA_400:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_500_mA_400)
  variable2: -TMath::Log10(output_HToZA_mH_500_mA_400)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_500_mA_400
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 500 GeV, MA = 400 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_650_mA_50:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_650_mA_50)
  variable2: -TMath::Log10(output_HToZA_mH_650_mA_50)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_650_mA_50
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 650 GeV, MA = 50 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_800_mA_50:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_800_mA_50)
  variable2: -TMath::Log10(output_HToZA_mH_800_mA_50)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_800_mA_50
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 800 GeV, MA = 50 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_800_mA_100:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_800_mA_100)
  variable2: -TMath::Log10(output_HToZA_mH_800_mA_100)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_800_mA_100
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 800 GeV, MA = 100 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_800_mA_200:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_800_mA_200)
  variable2: -TMath::Log10(output_HToZA_mH_800_mA_200)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_800_mA_200
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 800 GeV, MA = 200 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_800_mA_400:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_800_mA_400)
  variable2: -TMath::Log10(output_HToZA_mH_800_mA_400)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_800_mA_400
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 800 GeV, MA = 400 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_800_mA_700:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_800_mA_700)
  variable2: -TMath::Log10(output_HToZA_mH_800_mA_700)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_800_mA_700
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 800 GeV, MA = 700 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_1000_mA_50:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_1000_mA_50)
  variable2: -TMath::Log10(output_HToZA_mH_1000_mA_50)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_1000_mA_50
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 1000 GeV, MA = 50 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_1000_mA_200:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_1000_mA_200)
  variable2: -TMath::Log10(output_HToZA_mH_1000_mA_200)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_1000_mA_200
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 1000 GeV, MA = 200 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_1000_mA_500:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_1000_mA_500)
  variable2: -TMath::Log10(output_HToZA_mH_1000_mA_500)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_1000_mA_500
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 1000 GeV, MA = 500 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_2000_mA_1000:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_2000_mA_1000)
  variable2: -TMath::Log10(output_HToZA_mH_2000_mA_1000)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_2000_mA_1000
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 2000 GeV, MA = 1000 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 

MEM_ratio_DNN_weight_HToZA_mH_3000_mA_2000:
  filename: {file}
  tree: tree
  variable1: -TMath::Log10(weight_HToZA_mH_3000_mA_2000)
  variable2: -TMath::Log10(output_HToZA_mH_3000_mA_2000)
  weight: total_weight
  name: {category}_{name}_sample_MEM_ratio_DNN_weight_HToZA_mH_3000_mA_2000
  cut: {cut}
  bins: 150
  xmin: 15
  xmax: 45
  title: '{category} {name} sample : Ratio MEM/DNN weight HToZA (MH = 3000 GeV, MA = 2000 GeV) '
  xlabel: -log_{{10}}(weight)
  ylabel: Events
  legend1: 'MEM'
  legend2: 'DNN' 




