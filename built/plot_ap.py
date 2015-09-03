from pyoptics import *

close('all')
o1=optics.open('temp/twiss_ir6b1.tfs').plotbeta()
a1=optics.open('temp/twiss_ir6b1.tfs').plotap(ref=9.6)
o2=optics.open('temp/twiss_ir6b2.tfs').plotbeta()
a2=optics.open('temp/twiss_ir6b2.tfs').plotap(ref=9.6)

optics.open('ap_opt9/twiss_ir6b1.tfs').plotap(ref=9.6)
a7b1=optics.open('ap_opt7/ap_ir6b1.tfs')
plot(a7b1.s,a7b1.n1,'r')
optics.open('ap_opt9/twiss_ir6b2.tfs').plotap(ref=9.6)
a7b2=optics.open('ap_opt7/ap_ir6b2.tfs')
plot(a7b2.s,a7b2.n1,'r')
