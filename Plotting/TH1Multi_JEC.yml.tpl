##################### JEC comparison ####################

Multi_JEC:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_JEC
  bins: 50
  xmin: 15
  xmax: 25
  title: '{} sample : Comparison with and without JEC'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_DY)
    - -TMath::Log10(weight_DY_JEC)
    - -TMath::Log10(weight_TT)
    - -TMath::Log10(weight_TT_JEC)
    - -TMath::Log10(output_DY)
    - -TMath::Log10(output_DY_JEC)
    - -TMath::Log10(output_TT)
    - -TMath::Log10(output_TT_JEC)
  list_color:
    - 416
    - 418
    - 600
    - 602
    - 632
    - 634
    - 400
    - 402
  list_legend:
    - MEM Drell-Yann (without JEC) 
    - MEM Drell-Yann (with JEC) 
    - MEM t#bar{t} (without JEC) 
    - MEM t#bar{t} (with JEC) 
    - DNN Drell-Yann (without JEC) 
    - DNN Drell-Yann (with JEC) 
    - DNN t#bar{t} (without JEC) 
    - DNN t#bar{t} (with JEC) 
  list_cut : '1'
  legend_pos:
    - 0.5
    - 0.6
    - 0.9
    - 0.85

##################### JEC DeltaW ####################

JEC_DeltaW:
  filename: 
  tree: tree
  weight: total_weight
  name: JEC_DeltaW
  bins: 50
  xmin: -1
  xmax: 1
  title: '{} sample : Weight difference with JEC'
  xlabel: '-log_{10}(W_{JEC})+log_{10}(W_{no JEC})'
  ylabel: Events
  list_variable:
    - -log10(weight_DY_JEC)+log10(weight_DY)
    - -log10(weight_TT_JEC)+log10(weight_TT)
    - -log10(output_DY_JEC)+log10(output_DY)
    - -log10(output_TT_JEC)+log10(output_TT)
  list_color:
    - 418
    - 600
    - 632
    - 400
  list_legend:
    - MEM Drell-Yann weight
    - MEM t#bar{t} weight 
    - DNN Drell-Yann weight
    - DNN t#bar{t} weight
  list_cut : '1'
  legend_pos:
    - 0.55
    - 0.7
    - 0.9
    - 0.85

JEC_RelDeltaW:
  filename: 
  tree: tree
  weight: total_weight
  name: JEC_DeltaW
  bins: 50
  xmin: -0.05
  xmax: 0.05
  title: '{} sample : Relative weight difference with JEC'
  xlabel: '#frac{-log_{10}(W_{JEC})+log_{10}(W_{no JEC})}{-log_{10}(W_{no JEC})}'
  ylabel: Events
  list_variable:
    - (-log10(weight_DY_JEC)+log10(weight_DY))/-log10(weight_DY)
    - (-log10(weight_TT_JEC)+log10(weight_TT))/-log10(weight_TT)
    - (-log10(output_DY_JEC)+log10(output_DY))/-log10(output_DY)
    - (-log10(output_TT_JEC)+log10(output_TT))/-log10(output_TT)
  list_color:
    - 418
    - 600
    - 632
    - 400
  list_legend:
    - MEM Drell-Yann weight
    - MEM t#bar{t} weight 
    - DNN Drell-Yann weight
    - DNN t#bar{t} weight
  list_cut : '1'
  legend_pos:
    - 0.55
    - 0.7
    - 0.9
    - 0.85

