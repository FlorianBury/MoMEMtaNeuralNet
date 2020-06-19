##################### JEC comparison ####################

Multi_JEC:
  filename: 
  tree: tree
  weight: ''
  name: Multi_JEC
  bins: 50
  xmin: 15
  xmax: 25
  title: ''
  xlabel: -log_{10}(weight)
  ylabel: events
  list_variable:
    - -TMath::Log10(weight_DY)
    - -TMath::Log10(output_DY)
    - -TMath::Log10(weight_DY_JEC)
    - -TMath::Log10(output_DY_JEC)
    - -TMath::Log10(weight_TT)
    - -TMath::Log10(output_TT)
    - -TMath::Log10(weight_TT_JEC)
    - -TMath::Log10(output_TT_JEC)
  list_color:
    - 416
    - 418
    - 600
    - 602
    - 632
    - 634
    - 616
    - 619
  list_legend:
    - MEM Drell-Yan (without JES) 
    - DNN Drell-Yan (without JES) 
    - MEM Drell-Yan (with JES) 
    - DNN Drell-Yan (with JES) 
    - MEM t#bar{t} (without JES) 
    - DNN t#bar{t} (without JES) 
    - MEM t#bar{t} (with JES) 
    - DNN t#bar{t} (with JES) 
  list_cut : 
    - 'weight_DY_err<weight_DY'
    - 'weight_DY_err<weight_DY'
    - 'weight_DY_err<weight_DY'
    - 'weight_DY_err<weight_DY'
    - 'weight_TT_err<weight_TT'
    - 'weight_TT_err<weight_TT'
    - 'weight_TT_err<weight_TT'
    - 'weight_TT_err<weight_TT'
  legend_pos:
    - 0.4
    - 0.65
    - 0.92
    - 0.92

Multi_no_JEC:
  filename: 
  tree: tree
  weight: ''
  name: Multi_no_JEC
  bins: 50
  xmin: 15
  xmax: 25
  title: ''
  xlabel: -log_{10}(weight)
  ylabel: events
  list_variable:
    - -TMath::Log10(weight_DY)
    - -TMath::Log10(output_DY)
    - -TMath::Log10(weight_TT)
    - -TMath::Log10(output_TT)
  list_color:
    - 418
    - 602
    - 634
    - 402
  list_legend:
    - MEM Drell-Yan (without JES) 
    - DNN Drell-Yan (without JES) 
    - MEM t#bar{t} (without JES) 
    - DNN t#bar{t} (without JES) 
  list_cut : 
    - 'weight_DY_err<weight_DY'
    - 'weight_DY_err<weight_DY'
    - 'weight_TT_err<weight_TT'
    - 'weight_TT_err<weight_TT'
  legend_pos:
    - 0.4
    - 0.65
    - 0.92
    - 0.92

Multi_with_JEC:
  filename: 
  tree: tree
  weight: ''
  name: Multi_with_JEC
  bins: 50
  xmin: 15
  xmax: 25
  title: ''
  xlabel: -log_{10}(weight)
  ylabel: events
  list_variable:
    - -TMath::Log10(weight_DY_JEC)
    - -TMath::Log10(output_DY_JEC)
    - -TMath::Log10(weight_TT_JEC)
    - -TMath::Log10(output_TT_JEC)
  list_color:
    - 418
    - 602
    - 634
    - 402
  list_legend:
    - MEM Drell-Yan (with JES) 
    - DNN Drell-Yan (with JES) 
    - MEM t#bar{t} (with JES) 
    - DNN t#bar{t} (with JES) 
  list_cut :
    - 'weight_DY_err<weight_DY'
    - 'weight_DY_err<weight_DY'
    - 'weight_TT_err<weight_TT'
    - 'weight_TT_err<weight_TT'
  legend_pos:
    - 0.4
    - 0.65
    - 0.92
    - 0.92


##################### JEC DeltaW ####################

JEC_DeltaW:
  filename: 
  tree: tree
  weight: ''
  name: JEC_DeltaW
  bins: 60
  xmin: -3
  xmax: 3
  title: ''
  xlabel: '-log_{10}(weight_{JES})+log_{10}(weight_{no JES})'
  ylabel: events
  list_variable:
    - -log10(weight_DY_JEC)+log10(weight_DY)
    - -log10(output_DY_JEC)+log10(output_DY)
    - -log10(weight_TT_JEC)+log10(weight_TT)
    - -log10(output_TT_JEC)+log10(output_TT)
  list_color:
    - 418
    - 602
    - 634
    - 402
  list_legend:
    - "#splitline{Drell-Yan weight}{MoMEMta}"
    - "#splitline{Drell-Yan weight}{DNN}"
    - "#splitline{t#bar{t} weight}{MoMEMta}"
    - "#splitline{t#bar{t} weight}{DNN}"
  list_cut : 
    - 'weight_DY_err<weight_DY'
    - 'weight_DY_err<weight_DY'
    - 'weight_TT_err<weight_TT'
    - 'weight_TT_err<weight_TT'
  legend_pos:
    - 0.60
    - 0.55
    - 0.90
    - 0.92
  logy: True

JEC_RelDeltaW:
  filename: 
  tree: tree
  weight: ''
  name: JEC_DeltaW
  bins: 100
  xmin: -0.15
  xmax: 0.15
  title: ''
  xlabel: '#frac{-log_{10}(W_{JES})+log_{10}(W_{no JES})}{-log_{10}(W_{no JES})}'
  ylabel: events
  list_variable:
    - (-log10(weight_DY_JEC)+log10(weight_DY))/-log10(weight_DY)
    - (-log10(output_DY_JEC)+log10(output_DY))/-log10(output_DY)
    - (-log10(weight_TT_JEC)+log10(weight_TT))/-log10(weight_TT)
    - (-log10(output_TT_JEC)+log10(output_TT))/-log10(output_TT)
  list_color:
    - 418
    - 602
    - 634
    - 402
  list_legend:
    - MEM Drell-Yan weight
    - DNN Drell-Yan weight
    - MEM t#bar{t} weight 
    - DNN t#bar{t} weight
  list_cut : 
    - 'weight_DY_err<weight_DY'
    - 'weight_DY_err<weight_DY'
    - 'weight_TT_err<weight_TT'
    - 'weight_TT_err<weight_TT'
  legend_pos:
    - 0.60
    - 0.72
    - 0.92
    - 0.92
  logy: True

JEC_DeltaW_MEM_DNN:
  filename: 
  tree: tree
  weight: ''
  name: JEC_DeltaW_MEM_DNN 
  bins: 60
  xmin: -3
  xmax: 3
  title: ''
  xlabel: '-log_{10}(weight_{MoMEMta}) + log_{10}(weight_{DNN})'
  ylabel: events
  list_variable:
    - -log10(weight_DY)+log10(output_DY)
    - -log10(weight_DY_JEC)+log10(output_DY_JEC)
    - -log10(weight_TT)+log10(output_TT)
    - -log10(weight_TT_JEC)+log10(output_TT_JEC)
  list_color:
    - 418
    - 602
    - 634
    - 402
  list_legend:
    - "#splitline{Drell-Yan weight}{no JES}"
    - "#splitline{Drell-Yan weight}{with JES}"
    - "#splitline{t#bar{t} weight}{no JES}"
    - "#splitline{t#bar{t} weight}{with JES}"
  list_cut : 
    - 'weight_DY_err<weight_DY'
    - 'weight_DY_err<weight_DY'
    - 'weight_TT_err<weight_TT'
    - 'weight_TT_err<weight_TT'
  legend_pos:
    - 0.62
    - 0.55
    - 0.90
    - 0.93
  logy: True


