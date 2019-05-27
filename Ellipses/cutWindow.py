import json
import ROOT
from math import sqrt

class massWindow:
  """A class to construct and apply elliptic mass cuts 
     where the orientation and axes are function of the mass"""
  def __init__(self,filename):
    self.filename = filename
    self.instance = ROOT.gRandom.Rndm()

    # read data
    with open(self.filename) as data_file:    
      self.data = json.load(data_file)

    # store the gauge in four TGraph2D used for interpolation

    # Go from ellipses to circles via the rotation matrix |M11, M12| to favour the couting of the points inside the ellipse
    #                                                     |M21, M22|
    self.M11g = ROOT.TGraph2D(len(self.data))
    #print ("len(self.data): ", len(self.data))
    self.M11g.SetNameTitle("M11g_%d"%self.instance,"M11")
    self.M12g = ROOT.TGraph2D(len(self.data))
    self.M12g.SetNameTitle("M12g_%d"%self.instance,"M12")
    self.M21g = ROOT.TGraph2D(len(self.data))
    self.M21g.SetNameTitle("M21g_%d"%self.instance,"M21")
    self.M22g = ROOT.TGraph2D(len(self.data))
    self.M22g.SetNameTitle("M22g_%d"%self.instance,"M22")
    for i,(mbb, mllbb, a, b, theta, mA, mH) in enumerate(self.data):
       #print "mA=%d, mH=%d, theta=%d, a=%d, b=%d"%(mA,mH,theta,a,b)
       if mA>0 and mH>0 and theta and a>0 and b>0 and mH <= 1000:
        M11 = ROOT.TMath.Cos(theta)/sqrt(a)
        M12 = ROOT.TMath.Sin(theta)/sqrt(a)
        M21 = -ROOT.TMath.Sin(theta)/sqrt(b)
        M22 = ROOT.TMath.Cos(theta)/sqrt(b)
        self.M11g.SetPoint(i, mbb, mllbb, M11)
        self.M12g.SetPoint(i, mbb, mllbb, M12)
        self.M21g.SetPoint(i, mbb, mllbb, M21)
        self.M22g.SetPoint(i, mbb, mllbb, M22)

    self.matrix = [ [self.M11g, self.M12g] , [self.M21g, self.M22g] ] 

  def showBareMaps(self):
    """Show a canvas with the three inputs (theta, sigma_a, sigma_b) 
       of the transformation matrix as a function of mass"""
    # fill bare maps
    instance = ROOT.gRandom.Rndm()
    thetag = ROOT.TGraph2D(len(self.data))
    thetag.SetNameTitle("thetag_%d"%instance,"theta")
    ROOT.SetOwnership( thetag, False )
    ag =     ROOT.TGraph2D(len(self.data))
    ag.SetNameTitle("ag_%d"%instance,"a")
    ROOT.SetOwnership( ag, False )
    bg =     ROOT.TGraph2D(len(self.data))
    bg.SetNameTitle("bg_%d"%instance,"b")
    ROOT.SetOwnership( bg, False )
    for i,(mA, mH, theta, a, b) in enumerate(self.data):
       if mA!=0 and mH!=0 and theta and a!=0 and b!=0:
        thetag.SetPoint(i, mA, mH, theta);
        ag.SetPoint(i, mA, mH, a);
        bg.SetPoint(i, mA, mH, b);

    # create and populate a canvas
    canvas = ROOT.TCanvas("BareMaps","Bare Maps",2)
    canvas.Divide(2,2)
    canvas.cd(1)
    thetag.Draw("contz")
    canvas.cd(2)
    ag.Draw("contz")
    canvas.cd(3)
    bg.Draw("contz")

    # resulting canvas
    return canvas

  def showGaugeMaps(self):
    """Show a canvas with the four components 
       of the transformation matrix as a function of mass"""
    # create and populate a canvas
    canvas = ROOT.TCanvas("GaugeMaps","Gauge Maps",2)
    canvas.Divide(2,2)
    canvas.cd(1)
    self.M11g.Draw("contz")
    canvas.cd(2)
    self.M12g.Draw("contz")
    canvas.cd(3)
    self.M21g.Draw("contz")
    canvas.cd(4)
    self.M22g.Draw("contz")

    # resulting canvas
    return canvas

  def getValue(self,n,m,massPoint):
    """Returns the [n,m] component of the gauge matrix at point (mA,mH)."""
    interpolation = self.matrix[n][m].Interpolate(massPoint[0],massPoint[1])
    if interpolation==0:
       # handle cases that we cannot interpolate (close to the edges)
       # use the value from the closest point
       dist = 1000000
       for (mA, mH, theta, a, b, MA, MH) in self.data:
         if mA>0 and mH>0 and theta and a>0 and b>0:
            distance = sqrt((massPoint[0]-mA)**2+(massPoint[1]-mH)**2)
            if distance < dist:
                if n==0 and m==0:
                    interpolation = ROOT.TMath.Cos(theta)/sqrt(a)
                elif n==0 and m==1:
                    interpolation = ROOT.TMath.Sin(theta)/sqrt(a)
                elif n==1 and m==0:
                    interpolation = -ROOT.TMath.Sin(theta)/sqrt(b)
                elif n==1 and m==1:
                    interpolation = ROOT.TMath.Cos(theta)/sqrt(b)
            else:
                interpolation = 0.
                dist = distance
    return interpolation

  def applyLocalTransformation(self,massPoint):
    """Returns the result of the "gauge" transformation of a (mA,mH) mass point.
       The transformation matrix is evaluated at the mass point itself."""
    return self.applyGlobalTransformation(massPoint,massPoint)

  def applyGlobalTransformation(self,referencePoint,massPoint):
    """Returns the result of the a global transformation applied to a (mA,mH) mass point.
       The transformation matrix is computed at a reference point."""
    m1 = self.getValue(0,0,referencePoint)*massPoint[0] + self.getValue(0,1,referencePoint)*massPoint[1]
    m2 = self.getValue(1,0,referencePoint)*massPoint[0] + self.getValue(1,1,referencePoint)*massPoint[1]
    return (m1,m2)

  def isInWindow(self, center, size, massPoint):
    """Returns a boolean stating if the mass point is contained in the mass ellipse around center.
       Size is the cut value in #sigmas."""
    m1diff = massPoint[0] - center[0]
    m2diff = massPoint[1] - center[1]
    (u,v)  = self.applyGlobalTransformation(center,(m1diff,m2diff))
    return sqrt(u**2+v**2)<size

  def isNoise(self, center, size, massPoint):
    """Test: returns a bool for a ring of noize around signal ellipse"""
    m1diff = massPoint[0] - center[0]
    m2diff = massPoint[1] - center[1]
    (u,v)  = self.applyGlobalTransformation(center,(m1diff,m2diff))
    isN = sqrt(u**2+v**2)>size and sqrt(u**2+v**2)<size*2**0.5
    return isN


