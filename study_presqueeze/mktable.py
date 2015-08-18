from pyoptics import *
from matplotlib.pyplot import *
from constants import *
from analysispkg import *
import numpy as np

#--- find optics with minimum voltage
def get_opt_wire(t):
  """return optics with ratio 2 at wire at 5m"""
  b=t['betx_wire5mrb2_ref']/t['bety_wire5mrb2_ref']
  idx=np.argmin(abs(b-2.0))
  return idx
def get_opt_vmax(t):
  """optics with minimum cc voltage"""
  t,vmax=get_cc_max(t)
  idx=np.argmin(vmax)
  return idx
def get_opt_impedance(t):
  """optics with minimum impedance"""
  imp=get_sum_beta(t)
  idx=np.argmin(imp)
  return idx
def get_opt_apq4(t):
  """return optics with minimal betx,bety at Q4"""
  idx=np.argmin(np.max([t['betx_mcby_ref'],t['bety_mcby_ref']],axis=0))
  return idx

def print_opt(t,name,idx,lw5q5):
  # wire
  t['betx_wire7mlb1_ref'],t['bety_wire7mlb1_ref'],t['betx_wire7mrb2_ref'],t['bety_wire7mrb2_ref']=from_wire_5m(t,2)
  bxbywire7=t['betx_wire7mrb2_ref'][idx]/t['bety_wire7mrb2_ref'][idx]
  bxbywire3=t['betx_wire3mrb2_ref'][idx]/t['bety_wire3mrb2_ref'][idx]
  #cc voltage
  t,vmax=get_cc_max(t)
  #impedance
  imp=get_sum_beta(t)
  #Q5
  t['betx_q5lb1_ref'],t['bety_q5lb1_ref'],t['betx_q5rb2_ref'],t['bety_q5rb2_ref']=from_wire_5m(t,lw5q5) 
  #D2
  lacfad2=-18.972000#distance start D2 and ACFA cavity
  t['betx_mbrdlb1_ref'],t['bety_mbrdlb1_ref'],t['betx_mbrdrb2_ref'],t['bety_mbrdrb2_ref']=from_acfa(t,lacfad2)
  fmt='%4u %10s'+(('%5.2f %5.2f'.center(15))*3)+('%5.2f'.center(10))+('%5.4f'.center(16))+('%5.2f %5.2f'.center(15)*3) 
  if 'idx' in t.keys():
    idx0=t.idx[idx]-1
  else:
    idx0=idx
  print fmt%(idx0,name.ljust(10),bxbywire3,bxbywire7,t['betx_wire3mrb2_ref'][idx],t['betx_wire7mrb2_ref'][idx],t['bety_wire3mrb2_ref'][idx],t['bety_wire7mrb2_ref'][idx],vmax[idx],imp[idx]*1.e-3,t['betx_mbrdrb2_ref'][idx],t['bety_mbrdrb2_ref'][idx],t['betx_mcby_ref'][idx],t['bety_mcby_ref'][idx],t['betx_q5rb2_ref'][idx],t['bety_q5rb2_ref'][idx])

def print_con():
  print 'wire: RB2'
  print 'MCBYY: RB2'
  print 'MBRD: RB2'
  print 'MQY: RB2'
  print 'sum_bet_cc: sum_{u=l,r}sum_{s=ABCD}(beta_x(ACFs,u) + beta_y(ACFs,u) ) for B2 = sum over beta left/right of b2 over betx+bety'

def print_header(fn):
  print '\n%s'%fn
  fmt='%4s %10s %15s %15s %15s %10s %16s %15s %15s %15s'
  w37='   3m    7m    '
  print fmt%('idx','optics'.ljust(10),'betx/bety(wire)','betx(wire) [m]'.center(15),'bety(wire) [m]'.center(15),'Vmax [MV]'.center(10),'sum_beta_cc [km]'.center(16),'MBRD [m]'.center(15),'MCBYY [m]'.center(15),'MQY [m]'.center(15))
  print fmt%('','',w37,w37,w37,'','','betx    bety'.center(15),'betx    bety'.center(15),'betx    bety'.center(15))

def mktab(fn):
  print_header(fn)
  t=optics.open(fn)
  lw5q5=21.275
  #origininal presqueeze
  idxps=0
  print_opt(t,'presqueeze',idxps,lw5q5)
  #optimized for wire
  idxw=get_opt_wire(t)
  print_opt(t,'wire',idxw,lw5q5)
  #optimized for cc voltage
  idxv=get_opt_vmax(t)
  print_opt(t,'ccvolt',idxv,lw5q5)
  #optimized for impedance
  idxim=get_opt_impedance(t)
  print_opt(t,'impedance',idxim,lw5q5)
  #optimized for Q4 aperture
  idxap=get_opt_apq4(t)
  print_opt(t,'q4ap',idxap,lw5q5)

def mktab_opt(fn):
  print_header(fn)
  t=optics.open(fn)
  lw5q5=21.275
  for idx,name in zip(range(len(t['idx'])),['presqueeze','wire','ccvolt','impedance','q4ap']):
    print_opt(t,name,idx,lw5q5)

print_con();
#mktab_opt('scan_q4_8m/presqueeze_q4_scan_opt99.3.tfs')
#mktab('scan_q4_8m/presqueze_q4_scan99.3.tfs')
#print '----'
mktab_opt('scan_q4_10m_q5_13m/presqueeze_q4_scan_opt99.3.tfs')
mktab('scan_q4_10m_q5_13m/presqueze_q4_scan99.3.tfs')
#print '----'
#mktab_opt('scan_q4_6m_q5_9m/presqueeze_q4_scan_opt99.3.tfs')
#mktab('scan_q4_6m_q5_9m/presqueze_q4_scan99.3.tfs')

mktab_opt('scan_q4_8m/presqueeze_q4_scan_opt99.3.tfs')
mktab_opt('scan_q4_10m_q5_13m/presqueeze_q4_scan_opt99.3.tfs')
mktab_opt('scan_q4_6m_q5_9m/presqueeze_q4_scan_opt99.3.tfs')
