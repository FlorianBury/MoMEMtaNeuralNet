##################### JEC comparison ####################

Multi_JEC:
  filename: 
  tree: tree
  weight: ''
  name: Multi_JEC
  bins: 40
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
    - MEM Drell-Yan (nominal events) 
    - DNN Drell-Yan (nominal events) 
    - MEM Drell-Yan (shifted JES) 
    - DNN Drell-Yan (shifted JES) 
    - MEM t#bar{t} (nominal events) 
    - DNN t#bar{t} (nominal events) 
    - MEM t#bar{t} (shifted JES) 
    - DNN t#bar{t} (shifted JES) 
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
    - MEM Drell-Yan (nominal events) 
    - DNN Drell-Yan (nominal events) 
    - MEM t#bar{t} (nominal events) 
    - DNN t#bar{t} (nominal events) 
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
    - MEM Drell-Yan (shifted JES) 
    - DNN Drell-Yan (shifted JES) 
    - MEM t#bar{t} (shifted JES) 
    - DNN t#bar{t} (shifted JES) 
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
  xlabel: '-log_{10}(weight_{shifted JES})+log_{10}(weight_{nominal events})'
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
  bins: 30
  xmin: -0.15
  xmax: 0.15
  title: ''
  xlabel: '#frac{-log_{10}(W_{shifted JES})+log_{10}(W_{nominal events})}{-log_{10}(W_{nominal events})}'
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
    - "#splitline{Drell-Yan weight}{nominal events}"
    - "#splitline{Drell-Yan weight}{shifted JES}"
    - "#splitline{t#bar{t} weight}{nominal events}"
    - "#splitline{t#bar{t} weight}{shifted JES}"
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


