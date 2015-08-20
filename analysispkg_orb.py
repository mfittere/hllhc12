from pyoptics import *
import glob as glob
import matplotlib.pyplot as pl
import numpy as np
from itertools import chain

def flatten(l):
  return list(chain.from_iterable(l))  
 
def plot_b1_b2(dn,el,bb='b1'):
  for fn in files:
    t=optics.open('%s/twiss_lhc%s.tfs'%(fn,bb))
    pl.plot(t.x[t//el]*1.e3,t.y[t//el]*1.e3,'ko')
    pl.xlabel('x [mm]') 
    pl.ylabel('y [mm]')
  pl.grid(b=True,which='major',axis='both')
  pl.grid(b=True,which='minor',axis='both')
  pl.title(el)
  pl.savefig('%s/%s_xy_lhc%s.png'%(dn,el,bb), bbox_inches='tight')

def plot_b1b2(dn,el,files,lbl):
  for fn in files:
    t1=optics.open('%s/twiss_lhcb1.tfs'%(fn))
    pl.plot(t1.x[t1//el]*1.e3,t1.y[t1//el]*1.e3,'ko')
    t2=optics.open('%s/twiss_lhcb2.tfs'%(fn))
    pl.plot(t2.x[t2//el]*1.e3,t2.y[t2//el]*1.e3,'ko')
    pl.xlabel('x [mm]') 
    pl.ylabel('y [mm]')
  pl.grid(b=True,which='major',axis='both')
  pl.grid(b=True,which='minor',axis='both')
  pl.title(el)
  pl.savefig('%s/%s_xy_lhcb12_%s.png'%(dn,el,lbl), bbox_inches='tight')

def orbmax(dn,opt,elems):
  """return maximum orbit in mm]"""
  out={}
  for fn,kk in zip(['%s_crab_ccp0_ccm0_ccs+1'%opt,'%s_crab_ccp0_ccm+1_ccs0'%opt,'%s_crab_ccp+1_ccm0_ccs0'%opt,'%s_offset_o+1'%opt],['ccs','ccm','ccp','o']):
    t1=optics.open('%s/%s/twiss_lhcb1.tfs'%(dn,fn))
    t2=optics.open('%s/%s/twiss_lhcb2.tfs'%(dn,fn))
    for el in elems:
      if el not in out.keys():
        out[el]={}
      [x1,y1,x2,y2]=[ np.max(np.abs(ii)*1.e3) for ii in [t1.x[t1//el],t1.y[t1//el],t2.x[t2//el],t2.y[t2//el]] ]
      out[el][kk]=[max([x1,y1]),max([x2,y2])]
  return out

def print_orbmax(dn,opt,elems):
  oomax=orbmax(dn,opt,elems)
  print('%-15s '+' %9s '*6) %('elem','ccp [mm]','ccm [mm]','ccs [mm]','o [mm]','cc tot [mm]','tot [mm]')
  print('%-15s '+' %9s '*6) %(('',)+('max(x,y)',)*6)
  for el in elems:
    ccmax_x=sum([ abs(oomax[el][kk][0]) for kk in ['ccp','ccm','ccs'] ])
    ccmax_y=sum([ abs(oomax[el][kk][1]) for kk in ['ccp','ccm','ccs'] ])
    totmax_x=sum([ abs(oomax[el][kk][0]) for kk in ['ccp','ccm','ccs','o'] ])
    totmax_y=sum([ abs(oomax[el][kk][1]) for kk in ['ccp','ccm','ccs','o'] ])
    outaux=(el,)+tuple([ max(abs(oomax[el][kk][0]),abs(oomax[el][kk][0])) for kk in ['ccp','ccm','ccs','o'] ])+tuple([max(ccmax_x,ccmax_y),max(totmax_x,totmax_y)])
    print('%-15s '+(' %4.2f ').center(12)*6) % outaux
  return oomax

def print_orbmax_xy(dn,opt,elems):
  oomax=orbmax(dn,opt,elems)
  print('%-15s '+'  %9s  '*6) %('elem','ccp [mm]','ccm [mm]','ccs [mm]','o [mm]','cc tot [mm]','tot [mm]')
  print('%-15s '+'  %9s  '*6) %(('',)+('x    y',)*6)
  for el in elems:
    ccmax_x=sum([ abs(oomax[el][kk][0]) for kk in ['ccp','ccm','ccs'] ])
    ccmax_y=sum([ abs(oomax[el][kk][1]) for kk in ['ccp','ccm','ccs'] ])
    totmax_x=sum([ abs(oomax[el][kk][0]) for kk in ['ccp','ccm','ccs','o'] ])
    totmax_y=sum([ abs(oomax[el][kk][1]) for kk in ['ccp','ccm','ccs','o'] ])
    outaux=(el,)+tuple(flatten([oomax[el][kk] for kk in 'ccp','ccm','ccs','o']))+tuple([ccmax_x,ccmax_y,totmax_x,totmax_y])
    print('%-15s '+'  %4.2f %4.2f  '*6) % outaux
  return oomax
