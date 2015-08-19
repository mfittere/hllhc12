from pyoptics import *
import glob as glob
import matplotlib.pyplot as pl
import numpy as np
from itertools import chain
from analysispkg_orb import *

pl.ioff()
elems=['TAXS','MQXFA.[AB]1','MQXFB.[AB]2','MQXFA.[AB]3',
        'MBXF','TAXN','MBRD','MCBRD',
        'MCBYY','MQYY',
        'TCLMB.5L','TCLMB.5R',
        'MCBY[HV].5L','MCBY[HV].5R','MQY.5L','MQY.5R',
        'MCBC[HV].6L','MCBC[HV].6R','MQML.6L','MQML.6R',
        'TCLMC.6L','TCLMC.6R']
#elems=['MCBRD','MQYY']
scens=[
 'opt_150_150_150_150_ap_ms1',
 'opt_150_150_150_150_ap_ms2',
 'opt_150_150_150_150_ap_ms3']

#dn='orbitknobstudy/Q4_4m/orbit_crab_offset/'
#opt='opt_presqueeze_Q4_4m'
#dn='orbitknobstudy/Q4_8m/orbit_crab_offset/'
#opt='opt_150_150_150_150'
dn='orbitknobstudy/Q4_8m/orbit_crab_offset_presqueeze_1_8m_mcbrd_mcbyy/'
opt='opt_presqueeze_1_8m_mcbrd_mcbyy'
#pl.close('all')
##plot orbit of permutation of cc knobs in different elements
##plot orbit of in differnet elements for offset knob
#for files,lbl in zip([glob.glob('%s/%s_crab_ccp*'%(dn,opt)),glob.glob('%s/%s_offset_*'%(dn,opt))],['crab','offset']):
##  print '%s/%s_crab_ccp*'%(dn,opt)
##  print files
#  for el in elems:
#    print el
#    pl.close('all')
#    pl.figure()
#    plot_b1b2(dn,el,files,lbl)

#calculate maximum orbit from different contributions
#print_orbmax_xy(dn,opt,elems)
print_orbmax(dn,opt,elems)

#pl.show()
#pl.draw()
