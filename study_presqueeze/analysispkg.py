from pyoptics import *
from numpy import *
from constants import *

def from_wire_5m(t,ldrift):
  """calculate twiss parameters with ldrift distance
  from 5m wire position"""
  bxlb1=t.betx_wire5mlb1_ref+2*t.alfx_wire5mlb1_ref*ldrift+ldrift**2*(1+t.alfx_wire5mlb1_ref**2)/t.betx_wire5mlb1_ref
  bylb1=t.bety_wire5mlb1_ref+2*t.alfy_wire5mlb1_ref*ldrift+ldrift**2*(1+t.alfy_wire5mlb1_ref**2)/t.bety_wire5mlb1_ref
  bxrb2=t.betx_wire5mrb2_ref-2*t.alfx_wire5mrb2_ref*ldrift+ldrift**2*(1+t.alfx_wire5mrb2_ref**2)/t.betx_wire5mrb2_ref
  byrb2=t.bety_wire5mrb2_ref-2*t.alfy_wire5mrb2_ref*ldrift+ldrift**2*(1+t.alfy_wire5mrb2_ref**2)/t.bety_wire5mrb2_ref
  return bxlb1,bylb1,bxrb2,byrb2

def from_acfa(t,ldrift):
  bxlb1=t.betx_acfalb1_ref+2*t.alfx_acfalb1_ref*ldrift+ldrift**2*(1+t.alfx_acfalb1_ref**2)/t.betx_acfalb1_ref
  bylb1=t.bety_acfalb1_ref+2*t.alfy_acfalb1_ref*ldrift+ldrift**2*(1+t.alfy_acfalb1_ref**2)/t.bety_acfalb1_ref
  bxrb2=t.betx_acfarb2_ref-2*t.alfx_acfarb2_ref*ldrift+ldrift**2*(1+t.alfx_acfarb2_ref**2)/t.betx_acfarb2_ref
  byrb2=t.bety_acfarb2_ref-2*t.alfy_acfarb2_ref*ldrift+ldrift**2*(1+t.alfy_acfarb2_ref**2)/t.bety_acfarb2_ref
  return bxlb1,bylb1,bxrb2,byrb2
def get_cc(t,ll='r',bb='2'):
  """calculate the cc voltage *vcrab* in [MV]:
     vcrab = ncc*Ebeam*tan(xing)*sigma_s/(beta*sin(2*pi*hrf_cc*sigma_s/clight))*1.e-6
  ncc   : number of cc per IP and side (e.g. lb2)
  clight: speed of light [m/s]
  Ebeam : beam energy [V]
  sigma_s: bunch length [m]
  hrf_cc : cc voltage in [V]
  xing   : half crossing angle [rad]
  beta   : is calculated and given by sum(sqrt(beta_star*beta_cc))
           where the sum is taken over all cc per side and beam (e.g. lb2)
  """
  beta_star=0.48 #m
  xing=295.e-6 #rad
  hrf_cc=400.e6 #Hz
  Ebeam=7.0e12 #V
  sigma_s=0.075 #bunch length [m]
  ncc=4#number of crab cavities
  beta  = np.sum(np.array([ sqrt(beta_star*t['betx_acf%s%sb%s_ref'%(aa,ll,bb)]) for aa in 'abcd']),axis=0)
  vcrab = ncc*Ebeam*tan(xing)*sigma_s/(beta*sin(2*pi*hrf_cc*sigma_s/clight))*1.e-6
  return vcrab
def get_cc_max(t):
  """return dictionary *t* and maximum cc voltage *vmax*
  - add t['vcrabh_lb2_ref'] and t['vcrabh_rb2_ref']
  - due to ir1/5 symmetry and b1/b2 symmetries
  it is sufficient to take the max over one beam
  and one ir"""
  if 'v_crabv.r1b1' in t.keys():
    aa=aa='v_crabh.l1b1,v_crabh.r1b1,v_crabh.l5b1,v_crabh.r5b1,v_crabh.l1b2,v_crabh.r1b2,v_crabh.l5b2,v_crabh.r5b2,v_crabv.l1b1,v_crabv.r1b1,v_crabv.l5b1,v_crabv.r5b1,v_crabv.l1b2,v_crabv.r1b2,v_crabv.l5b2,v_crabv.r5b2'.split(',')
    t['vcrabh_lb2_ref'] = t['v_crabh.l5b2']
    t['vcrabh_rb2_ref'] = t['v_crabh.r5b2']
    vmax=np.max([ t[kk] for kk in aa ],axis=0)
  else:
    t['vcrabh_lb2_ref'] = get_cc(t,ll='l',bb='2')
    t['vcrabh_rb2_ref'] = get_cc(t,ll='r',bb='2')
    aa=np.array([ t['vcrabh_lb2_ref'],t['vcrabh_rb2_ref']])
    vmax=aa.max(axis=0)
  return t,vmax

def get_sum_beta(t):
  """get the sum over betas with which the impedance
  scales"""
  beta_crab_l = np.sum(np.array([ t['betx_acf%slb2_ref'%(aa)]+t['bety_acf%slb2_ref'%(aa)] for aa in 'abcd']),axis=0)
  beta_crab_r = np.sum(np.array([ t['betx_acf%srb2_ref'%(aa)]+t['bety_acf%srb2_ref'%(aa)] for aa in 'abcd']),axis=0)
  return beta_crab_l+beta_crab_r
