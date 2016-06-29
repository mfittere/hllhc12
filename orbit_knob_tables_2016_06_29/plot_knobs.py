from pyoptics import *
import matplotlib.pyplot as pl

dn='temp/'
dn='opt_round/'
dn='opt_presqueeze/'
dn='opt_flat/'
pl.close('all')
#chromatic functions
o1=optics.open('%stwiss_lhcb1_chrom.tfs'%(dn))
o2=optics.open('%stwiss_lhcb2_chrom.tfs'%(dn))
o1.plotw()
o2.plotw()

#orbit knobs
for cc in 'xing','ccp','ccm','ccs':
  o1=optics.open('%stwiss_lhcb1_%s.tfs'%(dn,cc))
  o2=optics.open('%stwiss_lhcb2_%s.tfs'%(dn,cc))
  if(cc=='xing'):
    o1.plotcross()
    o2.plotcross()
    print o1.betx[o1//'IP5'],o1.bety[o1//'IP5'],o1.x[o1//'IP5']*1.e6,o1.y[o1//'IP5']*1.e6 ,o1.px[o1//'IP5']*1.e6,o1.py[o1//'IP5']*1.e6
    print o1.betx[o1//'IP1'],o1.bety[o1//'IP1'],o1.x[o1//'IP1']*1.e6,o1.y[o1//'IP1']*1.e6 ,o1.px[o1//'IP1']*1.e6,o1.py[o1//'IP1']*1.e6
    o1.select('S.DS.L5.B1','E.DS.R5.B1').plotbeta()
    o2.select('S.DS.L5.B2','E.DS.R5.B2').plotbeta()
    o1.select('S.DS.L1.B1','E.DS.R1.B1').plotbeta()
    o2.select('S.DS.L1.B2','E.DS.R1.B2').plotbeta()
    
  o1.select('S.DS.L5.B1','E.DS.R5.B1').plotcross()
  pl.savefig('%sorb_%s_ir5b1'%(dn,cc))
  o2.select('S.DS.L5.B2','E.DS.R5.B2').plotcross()
  pl.savefig('%sorb_%s_ir5b2'%(dn,cc))
  o1.select('S.DS.L1.B1','E.DS.R1.B1').plotcross()
  pl.savefig('%sorb_%s_ir1b1'%(dn,cc))
  o2.select('S.DS.L1.B2','E.DS.R1.B2').plotcross()
  pl.savefig('%sorb_%s_ir1b2'%(dn,cc))

#--- beam 4
for cc in 'xing','ccp','ccm','ccs':
  start='E.DS.R'
  end  ='S.DS.L'
  o2=optics.open('%stwiss_lhcb2_%s.tfs'%(dn,cc))
  if cc=='xing':
    o2.select(start+'5.B2',end+'5.B2').plotbeta()
    o2.select(start+'1.B2',end+'1.B2').plotbeta()
  o2.select(start+'5.B2',end+'5.B2').plotcross()
  pl.savefig('%sorb_%s_ir5b4'%(dn,cc))
  o2.select(start+'1.B2',end+'1.B2').plotcross()
  pl.savefig('%sorb_%s_ir1b4'%(dn,cc))


# print table with orbit correctors
%run ../toolkit/check_mcb.py 'opt_round/orbit_knobs'
%run ../toolkit/check_mcb.py 'opt_presqueeze/orbit_knobs'
%run ../toolkit/check_mcb.py 'opt_flat/orbit_knobs'
pl.draw()
pl.show()
