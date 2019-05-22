####################### list_cut ###########################
###################### list_legend #########################

###################### list_color ##########################
##################### HToZA MEM weights ########################

Stack_MEM_weight_HToZA_mH_200_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_200_mA_50
  bins: 100
  xmin: 12
  xmax: 45
  title: '{} sample : MEM weight M_{{H}} = 200 GeV, M_{{A}} = 50 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_200_mA_50)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922

Stack_MEM_weight_HToZA_mH_200_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_200_mA_100
  bins: 100
  xmin: 12
  xmax: 45
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 200 GeV, M_{{A}} = 100 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_200_mA_100)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_250_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_250_mA_50
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 250 GeV, M_{{A}} = 50 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_250_mA_50)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_250_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_250_mA_100
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 250 GeV, M_{{A}} = 100 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_250_mA_100)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_300_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_300_mA_50
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 300 GeV, M_{{A}} = 50 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_300_mA_50)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_300_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_300_mA_100
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 300 GeV, M_{{A}} = 100 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_300_mA_100)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_300_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_300_mA_200
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 300 GeV, M_{{A}} = 200 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_300_mA_200)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_500_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_500_mA_50
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 500 GeV, M_{{A}} = 50 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_500_mA_50)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_500_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_500_mA_100
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 500 GeV, M_{{A}} = 100 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_500_mA_100)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_500_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_500_mA_200
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 500 GeV, M_{{A}} = 200 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_500_mA_200)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_500_mA_300:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_500_mA_300
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 500 GeV, M_{{A}} = 300 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_500_mA_300)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_500_mA_400:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_500_mA_400
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 500 GeV, M_{{A}} = 400 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_500_mA_400)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922


Stack_MEM_weight_HToZA_mH_650_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_650_mA_50
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 650 GeV, M_{{A}} = 50 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_650_mA_50)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922


Stack_MEM_weight_HToZA_mH_800_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_800_mA_50
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 800 GeV, M_{{A}} = 50 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_800_mA_50)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_800_mA_100:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_800_mA_100
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 800 GeV, M_{{A}} = 100 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_800_mA_100)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_800_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_800_mA_200
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 800 GeV, M_{{A}} = 200 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_800_mA_200)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_800_mA_400:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_800_mA_400
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 800 GeV, M_{{A}} = 400 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_800_mA_400)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_800_mA_700:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_800_mA_700
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 800 GeV, M_{{A}} = 700 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_800_mA_700)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_1000_mA_50:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_1000_mA_50
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 1000 GeV, M_{{A}} = 50 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_1000_mA_50)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_1000_mA_200:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_1000_mA_200
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 1000 GeV, M_{{A}} = 200 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_1000_mA_200)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_1000_mA_500:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_1000_mA_500
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 1000 GeV, M_{{A}} = 500 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_1000_mA_500)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_2000_mA_1000:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_2000_mA_1000
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 2000 GeV, M_{{A}} = 1000 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_2000_mA_1000)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922



Stack_MEM_weight_HToZA_mH_3000_mA_2000:
  filename: 
  tree: tree
  weight: total_weight
  name: Stack_MEM_weight_HToZA_mH_3000_mA_2000
  bins: 100
  xmin: 12
  xmax: 45 
  legend_pos:
    - 0.55
    - 0.3
    - 0.9
    - 0.85
  title: '{} sample : MEM weight M_{{H}} = 3000 GeV, M_{{A}} = 2000 GeV'
  xlabel: -log_{10}(weight)
  ylabel: Events
  list_variable:
    - -TMath::Log10(weight_HToZA_mH_3000_mA_2000)
  list_cut:
    - "mH_gen == 200 && mA_gen == 50"
    - "mH_gen == 200 && mA_gen == 100"
    - "mH_gen == 250 && mA_gen == 50"
    - "mH_gen == 250 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 50"
    - "mH_gen == 300 && mA_gen == 100"
    - "mH_gen == 300 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 50"
    - "mH_gen == 500 && mA_gen == 100"
    - "mH_gen == 500 && mA_gen == 200"
    - "mH_gen == 500 && mA_gen == 300"
    - "mH_gen == 500 && mA_gen == 400"
    - "mH_gen == 650 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 50"
    - "mH_gen == 800 && mA_gen == 100"
    - "mH_gen == 800 && mA_gen == 200"
    - "mH_gen == 800 && mA_gen == 400"
    - "mH_gen == 800 && mA_gen == 700"
    - "mH_gen == 1000 && mA_gen == 50"
    - "mH_gen == 1000 && mA_gen == 200"
    - "mH_gen == 1000 && mA_gen == 500"
    - "mH_gen == 2000 && mA_gen == 1000"
    - "mH_gen == 3000 && mA_gen == 2000"
  list_legend:
    - "M_{H} = 200 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 200 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 250 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 300 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 300 GeV"
    - "M_{H} = 500 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 650 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 50 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 100 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 200 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 400 GeV"
    - "M_{H} = 800 GeV,  M_{A} = 700 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 50 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 200 GeV"
    - "M_{H} = 1000 GeV, M_{A} = 500 GeV"
    - "M_{H} = 2000 GeV, M_{A} = 1000 GeV"
    - "M_{H} = 3000 GeV, M_{A} = 2000 GeV"
  list_color:
    - 407
    - 416
    - 417
    - 420
    - 423
    - 426
    - 432
    - 591
    - 601
    - 603
    - 604
    - 619
    - 623
    - 626
    - 627
    - 633
    - 797
    - 800
    - 802
    - 899
    - 904
    - 920
    - 922

