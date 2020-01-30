MEM_vs_DNN_MEPdf:
  filename: 
  tree: tree
  variablex: -log10(MEPdf)
  variabley: -log10(output_ME)
  weight: ''
  name: MEM_vs_DNN_MEPdf 
  cut: ''
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 0
  ymax: 15
  title: '{} sample : ME x PDF (MoMEMta vs DNN)'
  xlabel: -log_{10}(ME x PDF) from MoMEMta
  ylabel: -log_{10}(ME x PDF) from DNN
  zlabel: Events
  option : 'colz'
  logz : True

MEM_vs_DNN_MEPdf_prof:
  filename: 
  tree: tree
  variablex: -log10(MEPdf)
  variabley: -log10(output_ME)
  weight: ''
  name: MEM_vs_DNN_MEPdf_prof
  cut: ''
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 0
  ymax: 15
  title: '{} sample : ME x PDF (MoMEMta vs DNN)'
  xlabel: -log_{10}(ME x PDF) from MoMEMta
  ylabel: -log_{10}(ME x PDF) from DNN
  zlabel: Events
  option : 'prof'

