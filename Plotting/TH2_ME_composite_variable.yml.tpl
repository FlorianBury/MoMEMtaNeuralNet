########## LorentVector variableys ############

#####################
#####  W bosons #####
#####################

ME_Wminus_M_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector2M(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wminus_M_vs_MEPdf
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 20
  ymax: 150
  title: '{} W- Boson : M vs ME x PDF'
  ylabel: M
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

ME_Wminus_E_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector2E(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wminus_E_vs_MEPdf 
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 0
  ymax: 2000
  title: '{} W- Boson : E vs ME x PDF'
  ylabel: E
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

ME_Wminus_Pt_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector2Pt(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wminus_Pt_vs_MEPdf
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 0
  ymax: 2000
  title: '{} W- Boson : Pt vs ME x PDF'
  ylabel: Pt
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

ME_Wplus_M_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector2M(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wplus_M_vs_MEPdf 
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 20
  ymax: 150
  title: '{} W+ Boson : M vs ME x PDF'
  ylabel: M
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

ME_Wplus_E_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector2E(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wplus_E_vs_MEPdf 
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 0
  ymax: 2000
  title: '{} W+ Boson : E vs ME x PDF'
  ylabel: E
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

ME_Wplus_Pt_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector2Pt(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wplus_Pt_vs_MEPdf
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 0
  ymax: 2000
  title: '{} W+ Boson : Pt vs ME x PDF'
  ylabel: Pt
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

#####################
###  top quarks  ####
#####################

ME_antitop_M_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector3M(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E(),antibjet_p4.Px(),antibjet_p4.Py(),antibjet_p4.Pz(),antibjet_p4.E())
  weight: '' 
  name: ME_antitop_M_vs_MEPdf
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 100
  ymax: 280
  title: '{} Antitop quark : M vs ME x PDF'
  ylabel: M
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

ME_antitop_E_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector3E(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E(),antibjet_p4.Px(),antibjet_p4.Py(),antibjet_p4.Pz(),antibjet_p4.E())
  weight: '' 
  name: ME_antitop_E_vs_MEPdf
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 0
  ymax: 2000
  title: '{} Antitop quark : E vs ME x PDF'
  ylabel: E
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

ME_antitop_Pt_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector3Pt(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E(),antibjet_p4.Px(),antibjet_p4.Py(),antibjet_p4.Pz(),antibjet_p4.E())
  weight: '' 
  name: ME_antitop_Pt_vs_MEPdf
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 0
  ymax: 2000
  title: '{} Antitop quark : Pt vs ME x PDF'
  ylabel: Pt
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

ME_top_M_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector3M(positron_p4.Px(),positron_p4.Py(),positron_p4.Pz(),positron_p4.E(),neutrino_p4.Px(),neutrino_p4.Py(),neutrino_p4.Pz(),neutrino_p4.E(),bjet_p4.Px(),bjet_p4.Py(),bjet_p4.Pz(),bjet_p4.E())
  weight: '' 
  name: ME_top_M_vs_MEPdf
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 100
  ymax: 280
  title: '{} Top quark : M vs ME x PDF'
  ylabel: M
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

ME_top_E_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector3E(positron_p4.Px(),positron_p4.Py(),positron_p4.Pz(),positron_p4.E(),neutrino_p4.Px(),neutrino_p4.Py(),neutrino_p4.Pz(),neutrino_p4.E(),bjet_p4.Px(),bjet_p4.Py(),bjet_p4.Pz(),bjet_p4.E())
  weight: '' 
  name: ME_top_E_vs_MEPdf
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 0
  ymax: 2000
  title: '{} Top quark : E vs ME x PDF'
  ylabel: E
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True

ME_top_Pt_vs_MEPdf:
  filename: 
  tree: tree
  variablex: -TMath::Log10(MEPdf)
  variabley: LorentzVector3Pt(positron_p4.Px(),positron_p4.Py(),positron_p4.Pz(),positron_p4.E(),neutrino_p4.Px(),neutrino_p4.Py(),neutrino_p4.Pz(),neutrino_p4.E(),bjet_p4.Px(),bjet_p4.Py(),bjet_p4.Pz(),bjet_p4.E())
  weight: '' 
  name: ME_top_Pt_vs_MEPdf
  cut: '1'
  binsx: 100
  xmin: 0
  xmax: 15
  binsy: 100
  ymin: 0
  ymax: 2000
  title: '{} Top quark : Pt vs ME x PDF'
  ylabel: Pt
  xlabel: -log_{10}(ME x PDF)
  normalizeY: True
