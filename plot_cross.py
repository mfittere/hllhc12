from pyoptics import *
import matplotlib.pyplot as pl

pl.close('all')
#optics.open('twiss_ir1b1.tfs').plotcross()
#optics.open('twiss_ir1b2.tfs').plotcross()
#optics.open('twiss_ir5b1.tfs').plotcross()
#optics.open('twiss_ir5b2.tfs').plotcross()

#dn='Q4_4m/offset/opt_presqueeze_Q4_4m_offset_o+1'
#dn='temp/'
dn='built_optics/temp/'
#plot full optics in case disp correction is used
o1=optics.open('%s/twiss_lhcb1.tfs'%dn)
o2=optics.open('%s/twiss_lhcb2.tfs'%dn)
#o1=optics.open('opt_150_150_150_150_crab_ccp1_ccm0_ccs0/twiss_lhcb1.tfs')
#o2=optics.open('opt_150_150_150_150_crab_ccp1_ccm0_ccs0/twiss_lhcb2.tfs')
o1.select('S.DS.L5.B1','E.DS.R5.B1').plotcross()
pl.savefig('%s/orb_ir5b1.png'%dn)
o2.select('S.DS.L5.B2','E.DS.R5.B2').plotcross()
pl.savefig('%s/orb_ir5b2.png'%dn)
o1.select('S.DS.L1.B1','E.DS.R1.B1').plotcross()
pl.savefig('%s/orb_ir1b1.png'%dn)
o2.select('S.DS.L1.B2','E.DS.R1.B2').plotcross()
pl.savefig('%s/orb_ir1b2.png'%dn)
pl.draw()
pl.show()
