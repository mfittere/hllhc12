from pyoptics import *

close('all')
o1=optics.open('temp/twiss_ir6b1.tfs').plotbeta()
a1=optics.open('temp/twiss_ir6b1.tfs').plotap(ref=9.6)
o2=optics.open('temp/twiss_ir6b2.tfs').plotbeta()
a2=optics.open('temp/twiss_ir6b2.tfs').plotap(ref=9.6)

#optics.open('temp/twiss_ir6b1.tfs').plotap(ref=9.6)
#optics.open('inj/ap_opt10/twiss_ir6b1.tfs').plotap(ref=9.6)
optics.open('inj/ap_opt19/twiss_ir6b1.tfs').plotap(ref=9.5)
a7b1=optics.open('inj/ap_opt7/ap_ir6b1.tfs')
plot(a7b1.s,a7b1.n1,'r')
#optics.open('temp/twiss_ir6b2.tfs').plotap(ref=9.6)
#optics.open('inj/ap_opt10/twiss_ir6b2.tfs').plotap(ref=9.6)
optics.open('inj/ap_opt19/twiss_ir6b2.tfs').plotap(ref=9.5)
a7b2=optics.open('inj/ap_opt7/ap_ir6b2.tfs')
plot(a7b2.s,a7b2.n1,'r')

o2=optics.open('inj/ap_opt18/ap_ir6b2.tfs')

o2.s[o2//'TCDQA.A4L6.B2']
 o2.s[o2//'MQY.5L6.B2']

#check beta at the TCDQ
optdir='/afs/cern.ch/work/l/lhcopt/public/lhc_optics_web/www/'
for layout in ['opt2015','hllhc10','hllhc11']:
  tb1=optics.open(optdir+layout+'/inj/twiss_ir6b1.tfs')
  tb1.show('TCDQA','betx bety')

for layout in ['opt2015','hllhc10','hllhc11']:
  tb2=optics.open(optdir+layout+'/inj/twiss_ir6b2.tfs')
  tb2.show('TCDQA','betx bety')
