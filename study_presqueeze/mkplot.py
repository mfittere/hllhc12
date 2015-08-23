from pyoptics import *
from matplotlib.pyplot import *
from numpy import *
from constants import *
from analysispkg import *

scl_lim=0.03 #real lower limit

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
    legend(fontsize=12)
    subplot(223)
    for yy in ynn:
        plot(t.bety_mcby_ref,abs(t[yy]),'-o',label=yy)
    xlabel(r'$\beta_y \rm mcby [m]$')
    ylabel('g [T/m]')
    ylim(128,133)
    legend(fontsize=12)
    subplot(224)
    for yy in ynn:
        hist(abs(t[yy]),label=yy,alpha=0.2)
    xlim(128,133)
    xlabel('g [T/m]')
    legend(fontsize=12)
    tight_layout()
    figname=fn.replace('tfs','png')
    savefig(figname)

def plot_range(t,lpar):
  pmax=max([max(t[ll]) for ll in lpar])
  pmin=min([min(t[ll]) for ll in lpar])
  return (pmin-20,pmax+100)
def mkfig_crab_wire(fn,indfig=False):
    """create all plots in one big figure
    indfig = False: one figure
    indfig = True : each subplot in a individual figure"""
    ynn='g1 g2 g3'.split()
    t=optics.open(fn)
    fnbase=fn.split('.tfs')[0]
    case=fnbase.split('/')[0].split('scan')[1]
    if(indfig == True): figname=fnbase+'_cc'+case
    else: figname=(fnbase+'_cc'+case+'.png')
    brho7TeV=23348.89927
    qtlimq5= 200.0#Q5
    qtlim3 = 200.0#Q7
    #calculate cc voltage
    t,vmax=get_cc_max(t)#adds also t['vcrabh_lb2_ref'] and t['vcrabh_rb2_ref'] to t
    #--- IT gradient vs betax mcbyy
    if(indfig == True):
      figure()
    else:
      figure(fn+'_cc',figsize=(20,12))
      title(fnbase+'_cc')
      clf()
      subplot(341)
    for yy in ynn:
        plot(t.betx_acfdrb2_ref,abs(t[yy]),'.',label=yy)
        plot(t.betx_acfdrb2_ref[0],abs(t[yy])[0],'ko')#starting point
    plot([1,3000],[132.6,132.6],'k-')
    xlabel(r'$\beta_x \rm ACFD 5RB2 [m]$')
    ylabel('g [T/m]')
    xlim(1000,1700)
    ylim(128,133)
    legend(fontsize=12)
    grid()
    #--- IT gradient vs betay mcbyy
    if(indfig == True):
      savefig(figname+'_1.png', bbox_inches='tight')
      figure() 
    else: subplot(342)
    for yy in ynn:
        plot(t.bety_acfdrb2_ref,abs(t[yy]),'.',label=yy)
        plot(t.bety_acfdrb2_ref[0],abs(t[yy])[0],'ko')#starting point
    plot([1,3000],[132.6,132.6],'k-')
    xlabel(r'$\beta_y \rm ACFD 5RB2 [m]$')
    ylabel('g [T/m]')
    xlim(700,1000)
    ylim(128,133)
    legend(fontsize=12)
    grid()
    #betx vs betay at crab cavities
    if(indfig == True):
      savefig(figname+'_2.png', bbox_inches='tight')
      figure()
    else: subplot(343)
    for cc in 'abcd':
      for ll in 'lr':
        pp='_acf%s%sb2_ref'%(cc,ll)
        plot(t['betx'+pp],t['bety'+pp],'.',label='ACF%s %s5B2'%(cc.upper(),ll.upper()))
        plot(t['betx'+pp][0],t['bety'+pp][0],'ko')#starting point
    plot([400,2000],[400,2000],'k-')
    xlabel(r'$\beta_x \rm (cc) \  [m]$')
    ylabel(r'$\beta_y \rm (cc) \ [m]$')
    xlim(800,2800)
    ylim(600,2000)
    legend(fontsize=12)
    grid()
    #betx vs bety wire
    if(indfig == True):
      savefig(figname+'_3.png', bbox_inches='tight')
      figure()
    else: subplot(344)
    #calculate beta at wire at 7m
    t['betx_wire7mlb1_ref'],t['bety_wire7mlb1_ref'],t['betx_wire7mrb2_ref'],t['bety_wire7mrb2_ref']=from_wire_5m(t,2)
    for pw in '357':
      plot(t['betx_wire'+pw+'mlb1_ref'],t['bety_wire'+pw+'mlb1_ref'],'.',label='Wire '+pw+'m LB1')
      plot(t['betx_wire'+pw+'mlb1_ref'][0],t['bety_wire'+pw+'mlb1_ref'][0],'ko')#starting point
      plot(t['betx_wire'+pw+'mrb2_ref'],t['bety_wire'+pw+'mrb2_ref'],'.',label='Wire '+pw+'m RB2')
      plot(t['betx_wire'+pw+'mrb2_ref'][0],t['bety_wire'+pw+'mrb2_ref'][0],'ko')#starting point
    plot(arange(100,5000,500),0.5*arange(100,5000,500),'-k')
    xlabel(r'$\beta_x \rm (wire) \ [m]$')
    ylabel(r'$\beta_y \rm (wire) \ [m]$')
    legend(fontsize=12)
    grid()
#fixed range
    xlim(600,1600)
    ylim(300,800)
#flexibel range
#    xlim(plot_range(t,['betx_wire3mlb1_ref','betx_wire5mlb1_ref','betx_wire7mlb1_ref','betx_wire3mrb2_ref','betx_wire5mrb2_ref','betx_wire7mrb2_ref']))
#    ylim(plot_range(t,['bety_wire3mlb1_ref','bety_wire5mlb1_ref','bety_wire7mlb1_ref','bety_wire3mrb2_ref','bety_wire5mrb2_ref','bety_wire7mrb2_ref']))
    #---- Vmax vs betx/bety wire
    if(indfig == True):
      savefig(figname+'_4.png', bbox_inches='tight')
      figure()
    else: subplot(345)
    #calculate beta at wire at 7m
    t['betx_wire7mlb1_ref'],t['bety_wire7mlb1_ref'],t['betx_wire7mrb2_ref'],t['bety_wire7mrb2_ref']=from_wire_5m(t,2)
    for pw in '357':
      plot(vmax,t['betx_wire'+pw+'mrb2_ref']/t['bety_wire'+pw+'mrb2_ref'],'.',label='Wire '+pw+'m RB2')
      plot(vmax[0],t['betx_wire'+pw+'mrb2_ref'][0]/t['bety_wire'+pw+'mrb2_ref'][0],'ko')#starting point
    plot([0,20],[2.0,2.0],'k-')
    xlabel(r'$V_{\rm crab, max} \ [MV]$')
    ylabel(r'$\beta_x/\beta_y(\rm wire)$')
    legend(fontsize=12,loc='upper left')
    grid()
    xlim(11.3,13.2)
    ylim(1.4,4.0)
    #---- Vmax vs beta_min(MCBYY), beta_max(MCBYY)
    if(indfig == True):
      savefig(figname+'_5.png', bbox_inches='tight')
      figure()
    else: subplot(346)
    bmin_mcbyy=np.min([t.betx_mcby_ref,t.bety_mcby_ref], axis=0)
    bmax_mcbyy=np.max([t.betx_mcby_ref,t.bety_mcby_ref], axis=0)
    plot(vmax,bmin_mcbyy,'.',label='min(beta(MCBYY))')
    plot(vmax[0],bmin_mcbyy[0],'ko')#starting point
    plot(vmax,bmax_mcbyy,'.',label='max(beta(MCBYY))')
    plot(vmax[0],bmax_mcbyy[0],'ko')#starting point
    xlabel(r'$V_{\rm crab,max} \ [MV]$')
    ylabel(r'$\beta_{x/y}(\rm MCBYY) \ [m]$')
    legend(fontsize=12,loc='upper right')
    xlim(11.3,13.2)
    ylim(300,1600)
    grid()
    #---- Vmax vs impedance
    if(indfig == True):
      savefig(figname+'_6.png', bbox_inches='tight')
      figure()
    else: subplot(347)
    beta_crab_sum = get_sum_beta(t)
    plot(vmax,beta_crab_sum*1.e-3,'.',label='LB2+RB2')
    plot(vmax[0],beta_crab_sum[0]*1.e-3,'ko')#starting point
    xlabel(r'$V_{\rm crab, max} \ [MV]$')
    ylabel(r'$\sum_{s=ABCD}(\beta_x(\rm ACFs) + \beta_y(\rm ACFs) ) \ [km]$')
    legend(fontsize=12,loc='lower right')
    xlim(11.3,13.2)
    ylim(17,22)
    grid()
    #---- Vmax vs kq5
    if(indfig == True):
      savefig(figname+'_7.png', bbox_inches='tight')
      figure()
    else: subplot(348)
    for ss in 'lr':
      for bb in '12':
        plot(vmax,abs(t['kq5.%s5b%s'%(ss,bb)])*brho7TeV,'.',label='kq5.%s5b%s'%(ss,bb)) 
        plot(vmax[0],abs(t['kq5.%s5b%s'%(ss,bb)][0])*brho7TeV,'ko')
    plot([10,13],[scl_lim*qtlimq5,scl_lim*qtlimq5],'k-')#lower limit Q5 strength 
#    plot([10,13],[t.sch*qtlimq5,t.sch*qtlimq5],'k-')#upper limit Q5 strength 
    xlabel(r'$V_{\rm crab, max} \ [MV]$')
    ylabel(r'B [T/m]')
    xlim(11.3,13.2)
    ylim(0.0,120)
    grid()
    legend(fontsize=12,loc='upper left') 
    #---- Vmax vs kq7 strength
    if(indfig == True):
      savefig(figname+'_8.png', bbox_inches='tight')
      figure()
    else: subplot(349)
    for ss in 'lr':
      for bb in '12':
        plot(vmax,abs(t['kq7.%s5b%s'%(ss,bb)])*brho7TeV,'.',label='kq7.%s5b%s'%(ss,bb)) 
        plot(vmax[0],abs(t['kq7.%s5b%s'%(ss,bb)][0])*brho7TeV,'ko') 
#    plot([10,13],[t.scl*qtlim3,t.scl*qtlim3],'k-')#lower limit Q7 strength 
    plot([10,13],[t.sc79*qtlim3,t.sc79*qtlim3],'k-')#upper limit Q7 strength 
    xlabel(r'$V_{\rm crab, max} \ [MV]$')
    ylabel(r'B [T/m]')
    xlim(11.3,13.2)
    ylim(140,200)
    grid()
    legend(fontsize=12,loc='center right')
    #---- imq5l vs kq7 strength
    if(indfig == True):
      savefig(figname+'_9.png', bbox_inches='tight')
      figure()
    else: subplot(3,4,10)
    imq5l=t['kq5.l5b2']/t['kq5.l5b1']
    for ss in 'lr':
      for bb in '12':
        plot(abs(imq5l),abs(t['kq7.%s5b%s'%(ss,bb)])*brho7TeV,'.',label='kq7.%s5b%s'%(ss,bb)) 
        plot(abs(imq5l[0]),abs(t['kq7.%s5b%s'%(ss,bb)][0])*brho7TeV,'ko') 
    plot([0,2],[t.sc79*qtlim3,t.sc79*qtlim3],'k-')#upper limit Q7 strength 
    plot([1/t.imb,1/t.imb],[100,300],'k-')
    plot([t.imb,t.imb],[100,300],'k-')
    xlim(0.7,1.4)
    ylim(140,200)
    xlabel(r'kq5.l5b1/kq5.l5b1')
    ylabel(r'B [T/m]')
    grid()
    legend(fontsize=12,loc='center right')
    #---- imq5r vs kq7 strength
    if(indfig == True):
      savefig(figname+'_10.png', bbox_inches='tight')
      figure()
    else: subplot(3,4,11)
    imq5r=t['kq5.r5b2']/t['kq5.r5b1']
    for ss in 'lr':
      for bb in '12':
        plot(abs(imq5r),abs(t['kq7.%s5b%s'%(ss,bb)])*brho7TeV,'.',label='kq7.%s5b%s'%(ss,bb)) 
        plot(abs(imq5r[0]),abs(t['kq7.%s5b%s'%(ss,bb)][0])*brho7TeV,'ko') 
    plot([0,2],[t.sc79*qtlim3,t.sc79*qtlim3],'k-')#upper limit Q7 strength 
    plot([1/t.imb,1/t.imb],[100,300],'k-')
    plot([t.imb,t.imb],[100,300],'k-')
    xlim(0.7,1.4)
    ylim(140,200)
    xlabel(r'kq5.r5b1/kq5.r5b1')
    ylabel(r'B [T/m]')
    grid()
    legend(fontsize=12,loc='center left')
    if(indfig == True):
      savefig(figname+'_11.png', bbox_inches='tight')
    else:
      tight_layout()
      savefig(figname, bbox_inches='tight')
close('all')
#mkfig('results_riccardo/presqueze_q4_scan99.3.tfs')
#mkfig('results_riccardo/presqueze_q4_scan100.tfs')
#mkfig('results_riccardo/presqueze_q4_scan107.tfs')
#mkfig('scan_q4_8m/presqueze_q4_scan99.3.tfs')
#mkfig('scan_q4_8m/presqueze_q4_scan100.tfs')
#mkfig('scan_q4_8m/presqueze_q4_scan107.tfs')
indfig=False
#indfig=True
#mkfig_crab_wire('scan_q4_8m/presqueze_q4_scan100.tfs')
#mkfig_crab_wire('scan_q4_8m/presqueze_q4_scan107.tfs')
mkfig_crab_wire('scan_q4_8m/presqueze_q4_scan99.3.tfs',indfig)
mkfig_crab_wire('scan_q4_10m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q4_6m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q5_9m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q5_13m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q4_6m_q5_9m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q4_6m_q5_13m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q4_10m_q5_9m/presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('scan_q4_10m_q5_13m/presqueze_q4_scan99.3.tfs')

draw()
show()



