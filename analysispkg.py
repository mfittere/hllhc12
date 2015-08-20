from pyoptics import *
import matplotlib.pyplot as pl
import numpy as np

def comp_aperture(dir12,dir11,nlim=20):
  for ir in '1','5':
    for bb in '1','2':
      #plot aperture
      oov12=optics.open(dir12+'/twiss_ir%sb%s.tfs'%(ir,bb)) 
      oov11=optics.open(dir11+'/ap_ir%sb%s.tfs'%(ir,bb)) 
      oov12.plotap(ref=10,nlim=20)
      pl.plot(oov11.s,oov11.n1,color='orange',label=r'$n1$ V1.1')
      pl.title('ir'+ir+'b'+bb)
      pl.legend()
      pl.savefig(dir12+'/ap_ir%sb%s.png'%(ir,bb))
def comp_optics(dir12,dir11):
  for ir in '1','5':
    for bb in '1','2':
      #plot aperture
      oov12=optics.open(dir12+'/twiss_ir%sb%s.tfs'%(ir,bb)) 
      oov11=optics.open(dir11+'/twiss_ir%sb%s.tfs'%(ir,bb))
      pl.figure() 
#      oov12.plotbeta()
      pl.plot(oov12.s,oov12['bety'],label='V1.2 bety',color='k')
      pl.plot(oov11.s,oov11['bety'],label='V1.1 bety',color='b')
      pl.plot(oov12.s,oov12['betx'],label='V1.2 betx',color='r')
      pl.plot(oov11.s,oov11['betx'],label='V1.1 betx',color='orange')
      pl.legend()
      pl.title('ir'+ir+'b'+bb)
      pl.savefig(dir12+'/dbet_ir%sb%s.png'%(ir,bb))

def check_aperture(fn12,fn11,n1ref='hllhc_inj',eps=0):
  print "Checking %s" % fn12
  print "... comparing with %s" % fn11
  print "aperture margin %s"%n1ref
  ap12=optics.open(fn12)
  ap11=optics.open(fn11)

  out=[]
  limn1={'nominal':{'MSD':7.5,'MQW':5.5,'MQF':7,'MQD':6.7,'TCT':6.5},'hllhc_col':{'MSD':12.0,'MQW':12.0,'MQF':12.0,'MQD':12.0,'TCT':12.0},'hllhc_inj':{'MSD':10.0,'MQW':10.0,'MQF':10.0,'MQD':10.0,'TCT':10.0}}
  print ('  %-15s'+'  %-5s'*3) % tuple(['name','n1 V1.2','n1 V1.1','n1 V1.2 - n1 v1.1'])
  for nn in ap12.name:
    if nn not in [ out[ii][1] for ii in range(len(out)) ]:
      if nn.startswith('M') or nn.startswith('TCT'):
        betxv12=np.mean(ap12.betx[ap12//nn])
        betyv12=np.mean(ap12.bety[ap12//nn])
        n1v12=np.min(ap12.n1[ap12//nn])
        n1v11=np.min(ap11.n1[ap11//nn])
        dn1  =np.min(ap12.n1[ap12//nn]-ap11.n1[ap11//nn])
        if nn.startswith('M'):
          if  nn.startswith('MSD') and n1v12<limn1[n1ref]['MSD']-eps:
            out.append([2,nn,n1v12,n1v11,n1v12-n1v11])
          elif 'MQW' in nn or 'MQTLH' in nn or '6R3' in nn or '6L3' in nn:
            if n1v12<limn1[n1ref]['MQW']-eps:
              out.append([4,nn,n1v12,n1v11,n1v12-n1v11])
          elif betxv12>betyv12 and n1v12<limn1[n1ref]['MQF']-eps:
            out.append([0,nn,n1v12,n1v11,n1v12-n1v11])
          elif betxv12<betyv12 and n1v12<limn1[n1ref]['MQD']-eps:
            out.append([1,nn,n1v12,n1v11,n1v12-n1v11])
        elif  nn.startswith('TCT') and  n1v12<limn1[n1ref]['TCT']-eps:
            out.append([3,nn,n1v12,n1v11,n1v12-n1v11])
  prefix='H V S C 3'.split()
  print np.shape(np.array(out))
  out.sort()
  for t,name,n1v12,n1v11,dn1 in out:
    print ('%s %-15s'+'%7.2f'*3) % (prefix[t],name,n1v12,n1v11,dn1)
  return out

def plot_opt(optdir):
  for ir in '1','5':
    for bb in '1','2':
      oo=optics.open(optdir+'/twiss_ir%sb%s.tfs'%(ir,bb)) 
      oo.plotbeta()
      pl.savefig(optdir+'/opt_ir%sb%s.png'%(ir,bb))

def plot_cross_all(optdir):
  """plot crossing scheme using twiss_lhcb[12].tfs"""
  o1=optics.open(optdir+'/twiss_lhcb1.tfs')
  o2=optics.open(optdir+'/twiss_lhcb2.tfs')
  o1.select('S.DS.L5.B1','E.DS.R5.B1').plotcross()
  o2.select('S.DS.L5.B2','E.DS.R5.B2').plotcross()
  o1.select('S.DS.L1.B1','E.DS.R1.B1').plotcross()
  o2.select('S.DS.L1.B2','E.DS.R1.B2').plotcross()

