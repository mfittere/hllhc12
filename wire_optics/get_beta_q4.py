from pyoptics import *
from matplotlib.pyplot import *

#fn = 'opt_round'
fn = 'opt_round_wire'
o1=optics.open(fn+'/twiss_lhcb1.tfs')
o2=optics.open(fn+'/twiss_lhcb2.tfs')

o1.select('S.DS.L5.B1','E.DS.R5.B1').plotbeta()
savefig(fn+'/twiss_ir5b1.png')
o2.select('S.DS.L5.B2','E.DS.R5.B2').plotbeta()
savefig(fn+'/twiss_ir5b2.png')
o1.select('MBXF.4R5','MQY.5R5.B1').plotbeta()
savefig(fn+'/twiss_ir5b1_D1_Q5.png')
o2.select('MBXF.4R5','MQY.5R5.B2').plotbeta()
savefig(fn+'/twiss_ir5b2_D1_Q5.png')

idxq4rb1 = int(np.where(o1.name == 'MQYY.4R5.B1')[0])
idxq4lb1 = int(np.where(o1.name == 'MQYY.4L5.B1')[0])
idxq4rb2 = int(np.where(o2.name == 'MQYY.4R5.B2')[0])
idxq4lb2 = int(np.where(o2.name == 'MQYY.4L5.B2')[0])

print 'name      side  betax alfax betay alfay' 
#right side
print '%s IP  %4.2f %2.2f %4.2f %2.2f'%(o1.name[idxq4rb1],o1.betx[idxq4rb1-1],o1.alfx[idxq4rb1-1],o1.bety[idxq4rb1-1],o1.alfy[idxq4rb1-1])
print '%s arc %4.2f %2.2f %4.2f %2.2f'%(o1.name[idxq4rb1],o1.betx[idxq4rb1],o1.alfx[idxq4rb1],o1.bety[idxq4rb1],o1.alfy[idxq4rb1])
print '%s IP  %4.2f %2.2f %4.2f %2.2f'%(o1.name[idxq4rb2],o1.betx[idxq4rb2-1],o1.alfx[idxq4rb2-1],o1.bety[idxq4rb2-1],o1.alfy[idxq4rb2-1])
print '%s arc %4.2f %2.2f %4.2f %2.2f'%(o1.name[idxq4rb2],o1.betx[idxq4rb2],o1.alfx[idxq4rb2],o1.bety[idxq4rb2],o1.alfy[idxq4rb2])
#left side
print '%s IP  %4.2f %2.2f %4.2f %2.2f'%(o1.name[idxq4lb1],o1.betx[idxq4lb1],o1.alfx[idxq4lb1],o1.bety[idxq4lb1],o1.alfy[idxq4lb1])
print '%s arc %4.2f %2.2f %4.2f %2.2f'%(o1.name[idxq4lb1],o1.betx[idxq4lb1-1],o1.alfx[idxq4lb1-1],o1.bety[idxq4lb1-1],o1.alfy[idxq4lb1-1])
print '%s IP  %4.2f %2.2f %4.2f %2.2f'%(o1.name[idxq4lb2],o1.betx[idxq4lb2],o1.alfx[idxq4lb2],o1.bety[idxq4lb2],o1.alfy[idxq4lb2])
print '%s arc %4.2f %2.2f %4.2f %2.2f'%(o1.name[idxq4lb2],o1.betx[idxq4lb2-1],o1.alfx[idxq4lb2-1],o1.bety[idxq4lb2-1],o1.alfy[idxq4lb2-1])
