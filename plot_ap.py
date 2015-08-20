from pyoptics import *
import matplotlib.pyplot as pl

pl.close('all')
dn='/afs/cern.ch/eng/lhc/optics/HLLHCV1.2/examples/result'
for ip in '1','5':
  for bb in '1','2':
    oo=optics.open('%s/twiss_ir%sb%s.tfs'%(dn,ip,bb))
    print oo.betx[oo//('IP%s'%(ip))]
    print oo.px[oo//('IP%s'%(ip))]
    print oo.py[oo//('IP%s'%(ip))]
    oo.plotap(nlim=30,ref=12)

pl.show()
pl.draw()
