from pyoptics import *
from matplotlib.pyplot import *
from numpy import *

t2=optics.open('ir2_log_str.tfs')
t4=optics.open('ir4_log_str.tfs')
t6=optics.open('ir6_log_str.tfs')
t8=optics.open('ir8_log_str.tfs')

def plot_ir(irn):
  o1=optics.open('twiss_lhcb1.tfs')
  o2=optics.open('twiss_lhcb2.tfs')
  o1.select('S.DS.L'+irn+'.B1','E.DS.R'+irn+'.B1').plotbeta()
  title('IR%s Beam 1'%ir)
  o2.select('S.DS.L'+irn+'.B2','E.DS.R'+irn+'.B2').plotbeta()
  title('IR%s Beam 2'%ir)

def plot_arc():
  o1=optics.open('twiss_lhcb1.tfs')
  o2=optics.open('twiss_lhcb2.tfs')
  o1.select('S.CELL.56.B1','E.CELL.56.B1').plotbeta()
  o2.select('S.CELL.56.B2','E.CELL.56.B2').plotbeta()

def bdump(oo):
  idx=int(where(oo.name=='IP6')[0])
  betx,bety,alfx,alfy=[ oo[tt][idx] for tt in 'betx','bety','alfx','alfy' ]
  if oo.param['sequence']=='LHCB1':
    al_dump=761
    bxdump=betx-2*al_dump*alfx+al_dump**2*(1+alfx**2)/betx
    bydump=bety-2*al_dump*alfy+al_dump**2*(1+alfy**2)/bety
  if oo.param['sequence']=='LHCB2':
    al_dump=761
    bxdump=betx+2*al_dump*alfx+al_dump**2*(1+alfx**2)/betx
    bydump=bety+2*al_dump*alfy+al_dump**2*(1+alfy**2)/bety
  return bxdump,bydump

def print_ir6(oo):
  idx=int(where(oo.name=='IP6')[0])
  print [ oo[tt][idx] for tt in 'betx','bety','alfx','alfy' ]

o1nom=optics.open('runI/twiss_ir6b1_runI.tfs')
o1v10=optics.open('hllhcv10/twiss_lhcb1.tfs')
o1v11=optics.open('hllhcv11/twiss_lhcb1.tfs')
o1v12=optics.open('hllhcv12/twiss_lhcb1.tfs')
print_ir6(o1nom)
print_ir6(o1v10)
print_ir6(o1v11)
print_ir6(o1v12)
#close('all')
#for ir in '2468':
#  plot_ir(ir)
#plot_arc()
#
#draw()
#show()
