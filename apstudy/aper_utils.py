import os, sys

from numpy import *

from pyoptics import *
import matplotlib.pyplot as pl

def plot_circle(diam=0.015,color='b',label=None):
    t=linspace(0,2*pi,120)
    pl.plot(diam/2*cos(t),diam/2*sin(t),label=label,color=color)

def load_study(basedir='ap_round_2'):
    aps=[('%s_aperture'%l) for l in 'q1 q23 d2 q4'.split()]
    apfiles=dict( [(aa.upper(),loadtxt(os.path.join(basedir,aa)).T) for aa in aps])
    out=[]
    for irn in '15':
        for beam in '12':
          ir='ir%sb%s'%(irn,beam)
          ap=optics.open(os.path.join(basedir,'ap_%s.tfs'%ir))
          tw=optics.open(os.path.join(basedir,'twiss_%s.tfs'%ir))
          su=optics.open(os.path.join(basedir,'survey_%s.tfs'%ir))
          out.append(BeamEnvelope(tw,su,ap,apfiles))
    return out

def plot_s(name,scen,figname):
    pl.figure(figsize=(24,12))
    a11,a12,a51,a52=load_study(scen)
    pl.subplot(221)
    pl.title('IR1')
    a11.plot_aper_sx()
    a12.plot_aper_sx()
    a11.plot_beam_sx(nsig=12.0,color='b')
    a12.plot_beam_sx(nsig=12.0,color='r')
    #a11.plot_beam_sx(nsig=20.0,color='b',n1=0,n2=684 )
    #a12.plot_beam_sx(nsig=20.0,color='r',n1=1385,n2=None)
    pl.ylim(-0.08,0.08)
    pl.subplot(222)
    pl.title('IR5')
    a51.plot_aper_sx()
    a52.plot_aper_sx()
    a51.plot_beam_sx(nsig=12.0,color='b')
    a52.plot_beam_sx(nsig=12.0,color='r')
    #a51.plot_beam_sx(nsig=20.0,color='b',n1=0,n2=684 )
    #a52.plot_beam_sx(nsig=20.0,color='r',n1=1385,n2=None)
    pl.ylim(-0.08,0.08)
    pl.subplot(223)
    pl.title('IR1')
    a11.plot_aper_sy()
    a12.plot_aper_sy()
    a11.plot_beam_sy(nsig=12.0,color='b')
    a12.plot_beam_sy(nsig=12.0,color='r')
    #a11.plot_beam_sy(nsig=20.0,color='b',n1=0,n2=684 )
    #a12.plot_beam_sy(nsig=20.0,color='r',n1=1385,n2=None)
    pl.ylim(-0.08,0.08)
    pl.subplot(224)
    pl.title('IR5')
    a51.plot_aper_sy()
    a52.plot_aper_sy()
    a51.plot_beam_sy(nsig=12.0,color='b')
    a52.plot_beam_sy(nsig=12.0,color='r')
    #a51.plot_beam_sy(nsig=20.0,color='b',n1=0,n2=684 )
    #a52.plot_beam_sy(nsig=20.0,color='r',n1=1385,n2=None)
    pl.ylim(-0.08,0.08)
    pl.suptitle(name)
    pl.tight_layout()
    pl.savefig(figname)


def plot_case(name,scen,elem,coil,figname,sig=12,add_tol=0):
    pl.clf()
    if coil is not None:
      plot_circle(coil,'g','coil aperture')
    a11,a12,a51,a52=load_study(scen)
    for aaa in a11,a12,a51,a52:
        aaa.ap.xtol[aaa.ap//elem]+=add_tol
        aaa.ap.ytol[aaa.ap//elem]+=add_tol
    lbl=r'Beam %%d ($%g \sigma$)'%sig
    a11.plot_halo_name(elem,n1=sig,color='b',lbl=None,lblap='aperture')
    a51.plot_halo_name(elem,n1=sig,color='b',lbl=lbl%1)
    a12.plot_halo_name(elem,n1=sig,color='r',lbl=None)
    a52.plot_halo_name(elem,n1=sig,color='r',lbl=lbl%2)
    n1m=min([ s.get_halo_min_name(elem) for s in [a11,a12,a51,a52]])
    pl.title(r'%s: %s, $a_{min}=%2.2f\,\sigma$'%(elem,name,n1m))
    pl.legend()
    pl.savefig(figname)
    return a11,a12,a51,a52


def plot_case_2in1(name,scen,elem,coil,figname,sig=12.0,scalebeta=1.0):
    pl.clf()
    a11,a12,a51,a52=load_study(scen)
    for aa in a11,a12,a51,a52:
      aa.ap.betx[aa.ap//elem]*=scalebeta;
      aa.ap.bety[aa.ap//elem]*=scalebeta;
    pl.subplot(121)
    if coil is not None:
      plot_circle(coil,'g','coil aperture')
    a11.plot_halo_name(elem,n1=sig,color='b',lbl=None,lblap='aperture')
    a51.plot_halo_name(elem,n1=sig,color='b',lbl='Beam 1')
    pl.title('')
    pl.legend()
    if coil<0.12:
        pl.xlim(-0.06,0.06); pl.ylim(-0.06,0.06);
        tv=linspace(-0.06,0.06,7)
        pl.xticks(tv,map(str,tv*1000))
        pl.yticks(tv,map(str,tv*1000))
    ax=pl.subplot(122)
    if coil is not None:
      plot_circle(coil,'g','coil aperture')
    a12.plot_halo_name(elem,n1=sig,color='r',lbl=None,lblap='aperture')
    a52.plot_halo_name(elem,n1=sig,color='r',lbl='Beam 2')
    n1m=min([ s.get_halo_min_name(elem) for s in [a11,a12,a51,a52]])
    if coil<0.12:
        #ax.set_xlim(-0.6,0.6); ax.set_ylim(-0.06,0.06);
        tv=linspace(-0.06,0.06,7);        tvl=map(str,tv*1000)
        ax.set_xticks(tv); ax.set_xticklabels(tvl)
        ax.set_yticks(tv); ax.set_yticklabels(tvl)
    pl.draw()
    pl.title('')
    pl.legend()
    pl.suptitle(r'%s: %s, $a_{min}=%2.2f\,\sigma$'%(name,elem,n1m))
    pl.savefig(figname)
    return a11,a12,a51,a52



def mk_table(scens,elems,var='n1',fmt='%4.1f'):
    tab=[]
    for nn,scen in enumerate(scens):
      a11,a12,a51,a52=load_study(scen)
      out=[]
      print "(%d) %s" % (nn,scen)
      for el in elems:
         res=[aaa.ap[var][aaa.ap//el].min() for aaa in a11,a12,a51,a52]
         out.append(min(res))
      tab.append(out)
    ffmt=fmt[:2]+'s'
    print "%-15s %s"%('',' '.join([ffmt%v for v in range(len(scens))] ))
    for el,row in zip(elems,zip(*tab)):
        print "%-15s %s"%(el,' '.join([fmt%v for v in row] ))


def mk_fig_set(name,scen,label,single,double):
    pl.figure(figsize=(7.8,7))
    for elname,coil,elshort,sig in single:
       figname='%s/%s_%s.png'%(scen,elshort,name)
       plot_case(label,scen,elname,coil,figname,sig=sig)
       print figname
    pl.figure(figsize=(15.6,7))
    for elname,coil,elshort,sig in double:
       figname='%s/%s_%s.png'%(scen,elshort,name)
       plot_case_2in1(label,scen,elname,coil,figname,sig=sig)
       print figname


