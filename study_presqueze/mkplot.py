from pyoptics import *
from matplotlib.pyplot import *
from numpy import *
from constants import *

def mkfig(fn):
    ynn='g1 g2 g3'.split()
    t=optics.open(fn)
    figure(fn,figsize=(12,8))
    title(fn.split('.')[0])
    clf()
    subplot(221)
    plot(t.betx_mcby_ref,t.bety_mcby_ref,'-o')
    xlabel(r'$\beta_x \rm mcby [m]$')
    ylabel(r'$\beta_y \rm mcby [m]$')
    subplot(222)
    for yy in ynn:
        plot(t.betx_mcby_ref,abs(t[yy]),'-o',label=yy)
    xlabel(r'$\beta_x \rm mcby [m]$')
    ylabel('g [T/m]')
    ylim(128,133)
    legend()
    subplot(223)
    for yy in ynn:
        plot(t.bety_mcby_ref,abs(t[yy]),'-o',label=yy)
    xlabel(r'$\beta_y \rm mcby [m]$')
    ylabel('g [T/m]')
    ylim(128,133)
    legend()
    subplot(224)
    for yy in ynn:
        hist(abs(t[yy]),label=yy,alpha=0.2)
    xlim(128,133)
    xlabel('g [T/m]')
    legend()
    tight_layout()
    figname=fn.replace('tfs','png')
    savefig(figname)

def plot_range(t,lpar):
  pmax=max([max(t[ll]) for ll in lpar])
  pmin=min([min(t[ll]) for ll in lpar])
  return (pmin-20,pmax+100)
def get_wire_7m(t,ldrift):
  """calculate twiss parameters with ldrift distance
  from previous wire position"""
  bxlb1=t.betx_wire5mlb1_ref+2*t.alfx_wire5mlb1_ref*ldrift+ldrift**2*(1+t.alfx_wire5mlb1_ref**2)/t.betx_wire5mlb1_ref
  bylb1=t.bety_wire5mlb1_ref+2*t.alfy_wire5mlb1_ref*ldrift+ldrift**2*(1+t.alfy_wire5mlb1_ref**2)/t.bety_wire5mlb1_ref
  bxrb2=t.betx_wire5mrb2_ref-2*t.alfx_wire5mrb2_ref*ldrift+ldrift**2*(1+t.alfx_wire5mrb2_ref**2)/t.betx_wire5mrb2_ref
  byrb2=t.bety_wire5mrb2_ref-2*t.alfy_wire5mrb2_ref*ldrift+ldrift**2*(1+t.alfy_wire5mrb2_ref**2)/t.bety_wire5mrb2_ref
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
  t['vcrabh_lb2_ref'] = get_cc(t,ll='l',bb='2')
  t['vcrabh_rb2_ref'] = get_cc(t,ll='r',bb='2')
  aa=np.array([ t['vcrabh_lb2_ref'],t['vcrabh_rb2_ref']])
  vmax=aa.max(axis=0)
  return t,vmax
def mkfig_crab_wire(fn):
    ynn='g1 g2 g3'.split()
    t=optics.open(fn)
    fnbase=fn.split('.tfs')[0]
    case=fnbase.split('/')[0].split('scan')[1]
    #--- figure 1
    figure(fn+'_cc',figsize=(16,12))
    title(fnbase+'_cc')
    clf()
    subplot(331)
    for yy in ynn:
        plot(t.betx_acfdrb2_ref,abs(t[yy]),'.',label=yy)
        plot(t.betx_acfdrb2_ref[0],abs(t[yy])[0],'ko')#starting point
    plot([1,3000],[132.6,132.6],'k-')
    xlabel(r'$\beta_x \rm ACFD 5RB2 [m]$')
    ylabel('g [T/m]')
    xlim(1000,1700)
    ylim(128,133)
    legend()
    grid()
    subplot(332)
    for yy in ynn:
        plot(t.bety_acfdrb2_ref,abs(t[yy]),'.',label=yy)
        plot(t.bety_acfdrb2_ref[0],abs(t[yy])[0],'ko')#starting point
    plot([1,3000],[132.6,132.6],'k-')
    xlabel(r'$\beta_y \rm ACFD 5RB2 [m]$')
    ylabel('g [T/m]')
    xlim(700,1000)
    ylim(128,133)
    legend()
    grid()
    subplot(333)
    for cc in 'abcd':
      for ll in 'lr':
        pp='_acf%s%sb2_ref'%(cc,ll)
        plot(t['betx'+pp],t['bety'+pp],'.',label='ACF%s %s5B2'%(cc.upper(),ll.upper()))
        plot(t['betx'+pp][0],t['bety'+pp][0],'ko')#starting point
    plot([400,2000],[400,2000],'k-')
    xlabel(r'$\beta_x \rm (cc) \  [m]$')
    ylabel(r'$\beta_y \rm (cc) \ [m]$')
    xlim(800,2300)
    ylim(600,1800)
    legend()
    grid()
    subplot(334)
    #calculate beta at wire at 7m
    t['betx_wire7mlb1_ref'],t['bety_wire7mlb1_ref'],t['betx_wire7mrb2_ref'],t['bety_wire7mrb2_ref']=get_wire_7m(t,2)
    for pw in '357':
      plot(t['betx_wire'+pw+'mlb1_ref'],t['bety_wire'+pw+'mlb1_ref'],'.',label='Wire '+pw+'m LB1')
      plot(t['betx_wire'+pw+'mlb1_ref'][0],t['bety_wire'+pw+'mlb1_ref'][0],'ko')#starting point
      plot(t['betx_wire'+pw+'mrb2_ref'],t['bety_wire'+pw+'mrb2_ref'],'.',label='Wire '+pw+'m RB2')
      plot(t['betx_wire'+pw+'mrb2_ref'][0],t['bety_wire'+pw+'mrb2_ref'][0],'ko')#starting point
    plot(arange(100,5000,500),0.5*arange(100,5000,500),'-k')
    xlabel(r'$\beta_x \rm (wire) \ [m]$')
    ylabel(r'$\beta_y \rm (wire) \ [m]$')
    legend()
    grid()
#fixed range
    xlim(600,1400)
    ylim(300,700)
#flexibel range
#    xlim(plot_range(t,['betx_wire3mlb1_ref','betx_wire5mlb1_ref','betx_wire7mlb1_ref','betx_wire3mrb2_ref','betx_wire5mrb2_ref','betx_wire7mrb2_ref']))
#    ylim(plot_range(t,['bety_wire3mlb1_ref','bety_wire5mlb1_ref','bety_wire7mlb1_ref','bety_wire3mrb2_ref','bety_wire5mrb2_ref','bety_wire7mrb2_ref']))
    #---- Vmax vs betx/bety wire
    subplot(335)
    #calculate beta at wire at 7m
    t['betx_wire7mlb1_ref'],t['bety_wire7mlb1_ref'],t['betx_wire7mrb2_ref'],t['bety_wire7mrb2_ref']=get_wire_7m(t,2)
    #calculate cc voltage
    t,vmax=get_cc_max(t)
    for pw in '357':
      plot(vmax,t['betx_wire'+pw+'mrb2_ref']/t['bety_wire'+pw+'mrb2_ref'],'.',label='Wire '+pw+'m RB2')
      plot(vmax[0],t['betx_wire'+pw+'mrb2_ref'][0]/t['bety_wire'+pw+'mrb2_ref'][0],'ko')#starting point
    xlabel(r'$V_{\rm crab, max} \ [MV]$')
    ylabel(r'$\beta_x/\beta_y(\rm wire)$')
    legend(loc='upper left')
    grid()
    xlim(11,12.5)
    ylim(1.4,4.0)
    #---- Vmax vs beta_min(MCBYY), beta_max(MCBYY)
    subplot(336)
    #calculate cc voltage
    t,vmax=get_cc_max(t)#adds also t['vcrabh_lb2_ref'] and t['vcrabh_rb2_ref'] to t
    bmin_mcbyy=np.min([t.betx_mcby_ref,t.bety_mcby_ref], axis=0)
    bmax_mcbyy=np.max([t.betx_mcby_ref,t.bety_mcby_ref], axis=0)
    plot(vmax,bmin_mcbyy,'.',label='min(beta(MCBYY))')
    plot(vmax[0],bmin_mcbyy[0],'ko')#starting point
    plot(vmax,bmax_mcbyy,'.',label='max(beta(MCBYY))')
    plot(vmax[0],bmax_mcbyy[0],'ko')#starting point
    xlabel(r'$V_{\rm crab,max} \ [MV]$')
    ylabel(r'$\beta_{x/y}(\rm MCBYY) \ [m]$')
    legend(loc='center right')
    xlim(11,12.5)
    ylim(300,1600)
    grid()
    #---- Vmax vs betx/bety wire
    subplot(337)
    #calculate cc voltage
    t,vmax=get_cc_max(t)#adds also t['vcrabh_lb2_ref'] and t['vcrabh_rb2_ref'] to t
    beta_crab_l = np.sum(np.array([ t['betx_acf%slb2_ref'%(aa)]+t['bety_acf%slb2_ref'%(aa)] for aa in 'abcd']),axis=0)    
    beta_crab_r = np.sum(np.array([ t['betx_acf%srb2_ref'%(aa)]+t['bety_acf%srb2_ref'%(aa)] for aa in 'abcd']),axis=0)    
    beta_crab_sum = beta_crab_l+beta_crab_r
    plot(vmax,beta_crab_sum*1.e-3,'.',label='LB2+RB2')
    plot(vmax[0],beta_crab_sum[0]*1.e-3,'ko')#starting point
    xlabel(r'$V_{\rm crab, max} \ [MV]$')
    ylabel(r'$\sum_{s=ABCD}(\beta_x(\rm ACFs) + \beta_y(\rm ACFs) ) \ [km]$')
    legend(loc='lower right')
    xlim(11,12.5)
    ylim(17,22)
    grid()
    
    tight_layout()
    figname=(fnbase+'_cc'+case+'.png')
    savefig(figname)
close('all')
#mkfig('results_riccardo/presqueze_q4_scan99.3.tfs')
#mkfig('results_riccardo/presqueze_q4_scan100.tfs')
#mkfig('results_riccardo/presqueze_q4_scan107.tfs')
#mkfig('scan_q4_8m/presqueze_q4_scan99.3.tfs')
#mkfig('scan_q4_8m/presqueze_q4_scan100.tfs')
#mkfig('scan_q4_8m/presqueze_q4_scan107.tfs')
mkfig_crab_wire('scan_q4_8m/presqueze_q4_scan100.tfs')
mkfig_crab_wire('scan_q4_8m/presqueze_q4_scan107.tfs')
mkfig_crab_wire('scan_q4_8m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q4_10m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q4_6m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q5_9m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q5_13m/presqueze_q4_scan99.3.tfs')

draw()
show()



