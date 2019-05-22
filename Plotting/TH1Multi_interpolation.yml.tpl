##################### interpolation weights ########################

Multi_interpolation:
  filename: 
  tree: tree
  weight: total_weight
  name: Multi_interpolation
  bins: 60
  xmin: 15
  xmax: 45
  title: '{} sample : signal weights ( M_{{H}} = 600 GeV, M_{{A}} = 250 GeV) '
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_600_mA_250) 
    - -TMath::Log10(inter_HToZA_mH_600_mA_250) 
    - -TMath::Log10(output_HToZA_mH_600_mA_250) 
    - -TMath::Log10(output_HToZA_mH_600_mA_250) 
  list_color:
    - 418
    - 633
    - 601
    - 429
  list_legend:
    - MEM
    - Delaunay
    - DNN
    - DNN (invalids)
  list_cut : 
    - 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err && weight_HToZA_mH_200_mA_50>weight_HToZA_mH_200_mA_50_err'
    - 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err && weight_HToZA_mH_200_mA_50>weight_HToZA_mH_200_mA_50_err'
    - 'weight_HToZA_mH_600_mA_250>weight_HToZA_mH_600_mA_250_err && weight_HToZA_mH_200_mA_50>weight_HToZA_mH_200_mA_50_err'
    - 'weight_HToZA_mH_600_mA_250<=weight_HToZA_mH_600_mA_250_err && weight_HToZA_mH_200_mA_50<=weight_HToZA_mH_200_mA_50_err'

