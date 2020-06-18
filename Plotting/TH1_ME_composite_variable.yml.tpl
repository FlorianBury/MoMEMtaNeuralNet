########## LorentVector variables ############

#####################
#####  W bosons #####
#####################

ME_Wminus_M:
  filename: 
  tree: tree
  variable: LorentzVector2M(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wminus_M 
  cut: '1'
  bins: 200
  xmin: 60
  xmax: 100
  title: '{} W- Boson : M'
  xlabel: M
  ylabel: events

ME_Wminus_E:
  filename: 
  tree: tree
  variable: LorentzVector2E(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wminus_E 
  cut: '1'
  bins: 200
  xmin: 0
  xmax: 2000
  title: '{} W- Boson : E'
  xlabel: E
  ylabel: events

ME_Wminus_Pt:
  filename: 
  tree: tree
  variable: LorentzVector2Pt(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wminus_Pt
  cut: '1'
  bins: 200
  xmin: 0
  xmax: 2000
  title: '{} W- Boson : Pt'
  xlabel: Pt
  ylabel: events

ME_Wplus_M:
  filename: 
  tree: tree
  variable: LorentzVector2M(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wplus_M 
  cut: '1'
  bins: 200
  xmin: 60
  xmax: 100
  title: '{} W+ Boson : M'
  xlabel: M
  ylabel: events

ME_Wplus_E:
  filename: 
  tree: tree
  variable: LorentzVector2E(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wplus_E 
  cut: '1'
  bins: 200
  xmin: 0
  xmax: 2000
  title: '{} W+ Boson : E'
  xlabel: E
  ylabel: events

ME_Wplus_Pt:
  filename: 
  tree: tree
  variable: LorentzVector2Pt(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E())
  weight: '' 
  name: ME_Wplus_Pt
  cut: '1'
  bins: 200
  xmin: 0
  xmax: 2000
  title: '{} W+ Boson : Pt'
  xlabel: Pt
  ylabel: events

#####################
###  top quarks  ####
#####################

ME_antitop_M:
  filename: 
  tree: tree
  variable: LorentzVector3M(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E(),antibjet_p4.Px(),antibjet_p4.Py(),antibjet_p4.Pz(),antibjet_p4.E())
  weight: '' 
  name: ME_antitop_M
  cut: '1'
  bins: 200
  xmin: 140
  xmax: 200
  title: '{} Antitop quark : M'
  xlabel: M
  ylabel: events

ME_antitop_E:
  filename: 
  tree: tree
  variable: LorentzVector3E(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E(),antibjet_p4.Px(),antibjet_p4.Py(),antibjet_p4.Pz(),antibjet_p4.E())
  weight: '' 
  name: ME_antitop_E
  cut: '1'
  bins: 200
  xmin: 0
  xmax: 2000
  title: '{} Antitop quark : E'
  xlabel: E
  ylabel: events

ME_antitop_Pt:
  filename: 
  tree: tree
  variable: LorentzVector3Pt(electron_p4.Px(),electron_p4.Py(),electron_p4.Pz(),electron_p4.E(),antineutrino_p4.Px(),antineutrino_p4.Py(),antineutrino_p4.Pz(),antineutrino_p4.E(),antibjet_p4.Px(),antibjet_p4.Py(),antibjet_p4.Pz(),antibjet_p4.E())
  weight: '' 
  name: ME_antitop_Pt
  cut: '1'
  bins: 200
  xmin: 0
  xmax: 2000
  title: '{} Antitop quark : Pt'
  xlabel: Pt
  ylabel: events

ME_top_M:
  filename: 
  tree: tree
  variable: LorentzVector3M(positron_p4.Px(),positron_p4.Py(),positron_p4.Pz(),positron_p4.E(),neutrino_p4.Px(),neutrino_p4.Py(),neutrino_p4.Pz(),neutrino_p4.E(),bjet_p4.Px(),bjet_p4.Py(),bjet_p4.Pz(),bjet_p4.E())
  weight: '' 
  name: ME_top_M
  cut: '1'
  bins: 200
  xmin: 140
  xmax: 200
  title: '{} Top quark : M'
  xlabel: M
  ylabel: events

ME_top_E:
  filename: 
  tree: tree
  variable: LorentzVector3E(positron_p4.Px(),positron_p4.Py(),positron_p4.Pz(),positron_p4.E(),neutrino_p4.Px(),neutrino_p4.Py(),neutrino_p4.Pz(),neutrino_p4.E(),bjet_p4.Px(),bjet_p4.Py(),bjet_p4.Pz(),bjet_p4.E())
  weight: '' 
  name: ME_top_E
  cut: '1'
  bins: 200
  xmin: 0
  xmax: 2000
  title: '{} Top quark : E'
  xlabel: E
  ylabel: events

ME_top_Pt:
  filename: 
  tree: tree
  variable: LorentzVector3Pt(positron_p4.Px(),positron_p4.Py(),positron_p4.Pz(),positron_p4.E(),neutrino_p4.Px(),neutrino_p4.Py(),neutrino_p4.Pz(),neutrino_p4.E(),bjet_p4.Px(),bjet_p4.Py(),bjet_p4.Pz(),bjet_p4.E())
  weight: '' 
  name: ME_top_Pt
  cut: '1'
  bins: 200
  xmin: 0
  xmax: 2000
  title: '{} Top quark : Pt'
  xlabel: Pt
  ylabel: events
