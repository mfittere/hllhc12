import os, sys

from numpy import *

from pyoptics import *
import matplotlib.pyplot as pl

from aper_utils import *

name=r'IR1/5 $\beta^*=15$ cm'
scen='opt_150_150_150_150_ap_ms1'
scen='opt_100_330_330_100_ms1'
pl.figure(figsize=(7.8,7))
plot_case(name,scen,'TAXS',None,'taxs_15round',add_tol=2e-3)
plot_case(name,scen,'MQXFA.[AB]1',0.150,'q1_flat9')
plot_case(name,scen,'MQXFB.[AB]2',0.150,'q2_flat9')
plot_case(name,scen,'MQXFA.[AB]3',0.150,'q3_flat9')
plot_case(name,scen,'MBXF',0.150,'d1_round')
pl.figure(figsize=(15.6,7))
plot_case_2in1(name,scen,'TAXN',None,'taxn_round')
plot_case_2in1(name,scen,'MBRD.4L',0.105,'d2_round')
plot_case_2in1(name,scen,'MBRD.4R',0.105,'d2_round')
plot_case_2in1(name,scen,'MCBRD..4L',0.105,'d2_round')
plot_case_2in1(name,scen,'MCBRD..4R',0.105,'d2_round')
plot_case_2in1(name,scen,'MCBYY..4R',0.09,'mcbyyr_flat9_ms1')
plot_case_2in1(name,scen,'MCBYY..4L',0.09,'mcbyyr_flat9_ms1')
plot_case_2in1(name,scen,'MQYY.4L',0.09,'q4_round')
plot_case_2in1(name,scen,'MQYY.4R',0.09,'q4_round')
plot_case_2in1(name,scen,'MCBY.5L',0.07,'q5l_round')
plot_case_2in1(name,scen,'MCBY.5R',0.07,'q5r_round')
plot_case_2in1(name,scen,'MQY.5L',0.07,'q5l_round')
plot_case_2in1(name,scen,'MQY.5R',0.07,'q5r_round')
plot_case_2in1(name,scen,'MCBC.6L',0.056,'q5l_round')
plot_case_2in1(name,scen,'MCBC.6R',0.056,'q5r_round')
plot_case_2in1(name,scen,'MQML.6L',0.056,'q6l_round',sig=21)
plot_case_2in1(name,scen,'MQML.6R',0.056,'q6r_round',sig=21)
plot_case_2in1(name,scen,'TCLMB.5L',0.056,'mq5l_round_small2')
plot_case_2in1(name,scen,'TCLMB.5R',0.056,'mq5r_round_small2')


elems=['TAXS','MQXFA.[AB]1','MQXFB.[AB]2','MQXFA.[AB]3',
        'MBXF','TAXN','MBRD','MCBRD',
        'MCBYY','MQYY',
        'TCLMB.5L','TCLMB.5R',
        'MCBY[HV].5L','MCBY[HV].5R','MQY.5L','MQY.5R',
        'TCLMC.6L','TCLMC.6R',
        'MCBC[HV].6L','MCBC[HV].6R','MQML.6L','MQML.6R']
scens=[
 'opt_150_150_150_150_ms1',
 'opt_150_150_150_150_ms2',
 'opt_150_150_150_150_ms3',
 'opt_75_300_300_75_ms1',
 'opt_75_300_300_75_ms2',
 'opt_75_300_300_75_ms3',
]

scens=[
 'opt_150_150_150_150_ms1',
 'opt_180_180_180_180_ms1',
 'opt_200_200_200_200_ms1',
 'opt_220_220_220_220_ms1',
 'opt_75_300_300_75_ms1',
 'opt_90_330_330_90_ms1',
 'opt_100_330_330_100_ms1',
 'opt_110_330_330_110_ms1',
 'opt_120_330_330_120_ms1',
]

scens=[
 'opt_150_150_150_150_ms2',
 'opt_180_180_180_180_ms2',
 'opt_200_200_200_200_ms2',
 'opt_220_220_220_220_ms2',
 'opt_75_300_300_75_ms2',
 'opt_90_330_330_90_ms2',
 'opt_100_330_330_100_ms2',
 'opt_110_330_330_110_ms2',
 'opt_120_330_330_120_ms2',
]


scens=[
 'res/opt_150_150_150_150_ms1craboff',
 'res/opt_180_180_180_180_ms1craboff',
 'res/opt_200_200_200_200_ms1craboff',
 'res/opt_220_220_220_220_ms1craboff',
 'res/opt_75_300_300_75_ms1craboff',
 'res/opt_90_330_330_90_ms1craboff',
 'res/opt_100_330_330_100_ms1craboff',
 'res/opt_110_330_330_110_ms1craboff',
 'res/opt_120_330_330_120_ms1craboff',
]

scens=[
 'res/opt_150_150_150_150_ms2craboffxing',
 'res/opt_180_180_180_180_ms2craboffxing',
 'res/opt_200_200_200_200_ms2craboffxing',
 'res/opt_220_220_220_220_ms2craboffxing',
 'res/opt_75_300_300_75_ms2craboffxing',
 'res/opt_90_330_330_90_ms2craboffxing',
 'res/opt_100_330_330_100_ms2craboffxing',
 'res/opt_110_330_330_110_ms2craboffxing',
 'res/opt_120_330_330_120_ms2craboffxing',
]

scens=[
 'res/opt_150_150_150_150_ms3craboffxing',
 'res/opt_180_180_180_180_ms3craboffxing',
 'res/opt_200_200_200_200_ms3craboffxing',
 'res/opt_220_220_220_220_ms3craboffxing',
 'res/opt_75_300_300_75_ms3craboffxing',
 'res/opt_90_330_330_90_ms3craboffxing',
 'res/opt_100_330_330_100_ms3craboffxing',
 'res/opt_110_330_330_110_ms3craboffxing',
 'res/opt_120_330_330_120_ms3craboffxing',
]

scens=[
 'res/opt_150_150_150_150_ms3crabxing',
 'res/opt_180_180_180_180_ms3crabxing',
 'res/opt_200_200_200_200_ms3crabxing',
 'res/opt_220_220_220_220_ms3crabxing',
 'res/opt_75_300_300_75_ms3crabxing',
 'res/opt_90_330_330_90_ms3crabxing',
 'res/opt_100_330_330_100_ms3crabxing',
 'res/opt_110_330_330_110_ms3crabxing',
 'res/opt_120_330_330_120_ms3crabxing',
]


mk_table(scens,elems)

mk_table(scens,elems,var='x','%5.5f')


for scen in scens:
  a11,a12,a51,a52=load_study(scen)
  print scen


for aaa in a11,a12,a51,a52:
  aaa.twiss.show('IP[15]','x px y py')
  nn=aaa.get_n_name(el)


elems=['TAXS','MQXFA.[AB]1','MQXFB.[AB]2','MQXFA.[AB]3',
        'MBXF','TAXN','MBRD','MCBRD',
        'MCBYY','MQYY',
        'TCLMB.5','MCBY[HV].5','MQY.5',
        'TCLMC.6','MCBC[HV].6','MQML.6']

for el in elems:
    for nn in a11.get_n_name(el)[:1]:
       x,y=a11.get_aperture(nn)
       print "%-31s$%4g,%4g"%(el,x.max()*2000,y.max()*2000)

for el in elems:
    idx=a11.twiss//el
    x=abs(a11.twiss.x[idx]).max()
    y=abs(a11.twiss.y[idx]).max()
    print  "%-31s %4.3f %4.3f"%(el,x*1000,y*1000)


tab=[]
for knob in ((-1,0,0),(0,-1,0),(0,0,-1)):
   scen='opt_150_150_150_150_crab_ccp%d_ccm%d_ccs%d'%knob
   t1=optics.open('miriam/orbit_crab/%s/twiss_lhcb1.tfs'%scen)
   t2=optics.open('miriam/orbit_crab/%s/twiss_lhcb1.tfs'%scen)
   out=[]
   for el in elems:
      idx=t1//el
      x=abs(t1.x[idx]).max(); y=abs(t1.y[idx]).max()
      out.append([x*1000,y*1000])
   tab.extend(zip(*out))
scen='opt_150_150_150_150_offset_o+1'
t1=optics.open('miriam/%s/twiss_lhcb1.tfs'%scen)
t2=optics.open('miriam/%s/twiss_lhcb1.tfs'%scen)
out=[]
for el in elems:
  idx=t1//el
  x=abs(t1.x[idx]).max(); y=abs(t1.y[idx]).max()
  out.append([x*1000,y*1000])
tab.extend(zip(*out))

for el,row in zip(elems,zip(*tab)):
   nrow=row+(sum(row[::2]),sum(row[1::2]))
   print "%-15s %s"%(el,' '.join(['%4.1f'%v for v in nrow] ))










