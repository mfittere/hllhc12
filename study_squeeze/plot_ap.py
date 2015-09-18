from pyoptics import *

for ir in '15':
  for bb in '12':
    optics.open('temp/twiss_ir%sb%s.tfs'%(ir,bb)).plotap(ref=12)
    savefig('ap_ir%sb%s'%(ir,bb))
