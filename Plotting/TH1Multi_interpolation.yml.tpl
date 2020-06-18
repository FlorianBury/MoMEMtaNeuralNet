##################### interpolation weights ########################

Multi_interpolation:
  filename: 
  tree: tree
  weight: ''
  name: Multi_interpolation
  bins: 25
  xmin: 15
  xmax: 40
  title: ''
  xlabel: -log_{10}(H#rightarrowZA weight | M_{A} = 250 GeV , M_{H} = 600 GeV)
  ylabel: events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_600_mA_250) 
    - -TMath::Log10(inter_HToZA_mH_600_mA_250) 
    - -TMath::Log10(output_HToZA_mH_600_mA_250) 
  list_color:
    - 418
    - 633
    - 601
  list_legend:
    - MEM
    - Delaunay
    - DNN
  list_cut : 
    - 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err && weight_HToZA_mH_200_mA_50>weight_HToZA_mH_200_mA_50_err'
    - 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err && weight_HToZA_mH_200_mA_50>weight_HToZA_mH_200_mA_50_err'
    - 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err && weight_HToZA_mH_200_mA_50>weight_HToZA_mH_200_mA_50_err'
  legend_pos:
    - 0.60
    - 0.6
    - 0.922
    - 0.922

