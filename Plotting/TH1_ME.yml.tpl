MEPdf:
  filename: 
  tree: tree
  variable: -log10(MEPdf)
  name: MEPdf
  weight: ''
  cut: '1'
  bins: 150
  xmin: 0
  xmax: 15
  title: '{} sample : ME x PDF (MoMEMta)'
  xlabel: -log_{10}(ME x PDF)
  ylabel: events

output_ME:
  filename: 
  tree: tree
  variable: -log10(output_ME)
  name: output_ME
  weight: ''
  cut: '1'
  bins: 150
  xmin: 0
  xmax: 15
  title: '{} sample : ME x PDF (DNN)'
  xlabel: -log_{10}(ME x PDF)
  ylabel: events

MEM_DNN_comp:
  filename: 
  tree: tree
  variable: abs(MEPdf-output_ME)
  name: MEM_DNN_comp
  weight: ''
  cut: '1'
  bins: 100
  xmin: 0
  xmax: 0.1
  title: '{} sample : comparison'
  xlabel: '|(ME x PDF)_{MoMEMta} - (ME x PDF)_{DNN}|'
  ylabel: events

MEM_DNN_comp_rel:
  filename: 
  tree: tree
  variable: abs(MEPdf-output_ME)
  name: MEM_DNN_comp_rel
  weight: ''
  cut: '1'
  bins: 100
  xmin: 0
  xmax: 1
  title: '{} sample : comparison'
  xlabel: '|(ME x PDF)_{MoMEMta} - (ME x PDF)_{DNN}|/(ME x PDF)_{MoMEMta}'
  ylabel: events


