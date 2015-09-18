from pyoptics import *
from matplotlib.pyplot import *
from numpy import *

def plot_ir(irn):
  o1=optics.open('twiss_lhcb1.tfs')
  o2=optics.open('twiss_lhcb2.tfs')
  o1.select('S.DS.L'+irn+'.B1','E.DS.R'+irn+'.B1').plotbeta()
  title('IR%s Beam 1'%irn)
  gcf().axes[1].plot(o1.s[o1//'TCDQA.A4R6.B1'],o1.betx[o1//'TCDQA.A4R6.B1'],'ko')
  gcf().axes[1].plot(o1.s[o1//'TCDQA.A4R6.B1'],o1.bety[o1//'TCDQA.A4R6.B1'],'ro')
  gcf().axes[1].plot(o1.s[o1//'MKD.H5L6.B1'],o1.bety[o1//'MKD.H5L6.B1'],'bo')
  o2.select('S.DS.L'+irn+'.B2','E.DS.R'+irn+'.B2').plotbeta()
  gcf().axes[1].plot(o2.s[o2//'TCDQA.A4L6.B2'],o2.betx[o2//'TCDQA.A4L6.B2'],'ko')
  gcf().axes[1].plot(o2.s[o2//'TCDQA.A4L6.B2'],o2.bety[o2//'TCDQA.A4L6.B2'],'ro')
  gcf().axes[1].plot(o2.s[o2//'MKD.H5R6.B2'],o2.bety[o2//'MKD.H5R6.B2'],'bo')
  title('IR%s Beam 2'%irn)

def plot_arc():
  o1=optics.open('twiss_lhcb1.tfs')
  o2=optics.open('twiss_lhcb2.tfs')
#  o1.select('S.CELL.56.B1','E.CELL.56.B1').plotbeta()
#  o2.select('S.CELL.56.B2','E.CELL.56.B2').plotbeta()
  o1.select('E.DS.R5.B1','E.DS.R6.B1').plotbeta()
  o2.select('E.DS.R5.B2','E.DS.R6.B2').plotbeta()

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

def print_ir6(oo,elem,lbl):
  elem=oo.name[oo//elem][0]
  idx=int(where(oo.name==elem)[0])
  fmt='%s'+'%4.2f  '*4
  print fmt%((lbl.ljust(15),)+tuple([ oo[tt][idx] for tt in 'betx','bety','alfx','alfy' ]))
def print_comp_layout_mkd_tcdq():
  for bb in '12':
    print '---- Beam '+bb
    optwww='/afs/cern.ch/work/l/lhcopt/public/lhc_optics_web/www/'
    oorunI=optics.open(optwww+'pprun1/coll_4tev/twiss_ir6b'+bb+'.tfs')
    oorunII=optics.open(optwww+'opt2015/coll400/twiss_ir6b'+bb+'.tfs')
    oov10=optics.open(optwww+'hllhc10/round/twiss_lhcb'+bb+'.tfs')
    oov11=optics.open(optwww+'hllhc11/round/twiss_lhcb'+bb+'.tfs')
    #oov12=optics.open(optwww+'hllhc12/twiss_lhcb1.tfs')
    for elem in 'MKD.H5[LR]6.B[12]','TCDQA.A4[LR]6.B[12]':#,'IP6':
      print elem
      print 'layout'.ljust(15)+'betx bety alfx alfy' 
      for lbl,oo in zip(['runI4TeV60cm','runII80cm','hllhc10','hllhc11'],[oorunI,oorunII,oov10,oov11]):
        print_ir6(oo,elem,lbl)

#----- print twiss at TCDQ, MKD and IR6 for LHC optics and HLLHC optics
#print_comp_layout_mkd_tcdq()
##----- aperture for HLLHCV11 flat optics
#optarc45='/afs/cern.ch/work/l/lhcopt/public/lhc_optics_web/www/hllhc11/flat/'
#optarc45='flat/'
#optics.open(optarc45+'/twiss_arc45b1.tfs').plotbeta()
#savefig('flat/twiss_arc45_flat.png')
#ap=optics.open(optarc45+'/twiss_arc45b1.tfs').plotap(ref=17)
#print min(ap.n1)
#savefig('flat/ap_arc45_flat.png')

close('all')
#for ir in '2468':
#  plot_ir(ir)
#plot_arc()
#for ir in '2468':
#  StrTable.open('../slhcv10/squeeze/ir%s_sround.tfs'%ir).plot_squeeze(title='IR%s v10'%ir)
#  savefig('ir%s_squeeze_round_v10.png'%ir)
#for ir in '248':
#  StrTable.open('squeeze5/ir%s_log_str.tfs'%ir).plot_squeeze(title='IR%s'%ir)
#  savefig('ir%s_squeeze5.png'%ir)
#StrTable.open('squeeze5/ir6_log_str.tfs').plot_squeeze_ir6(title='IR6')
#savefig('ir6_squeeze5.png')
#StrTable.open('squeeze5/ir6_log_str.tfs').plot_betip(title='Twiss IR6')
#savefig('ir6_twiss_squeeze5.png')
draw()
show()
