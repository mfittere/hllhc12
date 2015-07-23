import os, sys

from numpy import *

from pyoptics import *
import matplotlib.pyplot as pl

from aper_utils import *



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

scens=[
'study2/opt_150_150_150_150_295_2000_ms1craboffxing',
'study2/opt_200_200_200_200_255_2000_ms1craboffxing',
'study2/opt_75_300_300_75_245_750_ms1craboffxing',
'study2/opt_100_400_400_100_210_750_ms1craboffxing']


elems=['TAXS','MQXFA.[AB]1','MQXFB.[AB]2','MQXFA.[AB]3',
        'MBXF','TAXN','MBRD','MCBRD',
        'MCBYY','MQYY',
        'TCLMB.5','MCBY[HV].5','MQY.5',
        'TCLMC.6','MCBC[HV].6','MQML.6']


mk_table(scens,elems)
mk_table([s.replace('ms1','ms2') for s in scens],elems)
mk_table([s.replace('ms1','ms3') for s in scens],elems)

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



single=[
  ('TAXS',None,'taxs',12),
  ('MQXFA.[AB]1',0.150,'q1',12),
  ('MQXFB.[AB]2',0.150,'q2',12),
  ('MQXFA.[AB]3',0.150,'q3',12),
  ('MBXF',0.150,'d1',12)]
double=[
  ('TAXN',None,'taxn',12),
  ('MBRD.4L',0.105,'d2cl',12),
  ('MBRD.4R',0.105,'d2cr',12),
  ('MCBRD..4L',0.105,'d2l',12),
  ('MCBRD..4R',0.105,'d2r',12),
  ('MCBYY..4L',0.09,'q4cl',12),
  ('MCBYY..4R',0.09,'q4cr',12),
  ('MQYY.4L',0.09,'q4l',12),
  ('MQYY.4R',0.09,'q4r',12),
  ('MCBY..5L',0.07,'q5cl',12),
  ('MCBY..5R',0.07,'q5cr',12),
  ('MQY.5L',0.07,'q5l',12),
  ('MQY.5R',0.07,'q5r',12),
  ('TCLMB.5L',0.056,'q5ml',18),
  ('TCLMB.5R',0.056,'q5mr',18),
  ('MCBC.6L',0.056,'q6cl',18),
  ('MCBC.6R',0.056,'q6cr',18),
  ('MQML.6L',0.056,'q6l',18),
  ('MQML.6R',0.056,'q6r',18),
  ('TCLMC.6L',0.056,'q6ml',18),
  ('TCLMC.6R',0.056,'q6mr',18)]

scens=[
('study2/opt_150_150_150_150_ms1craboffxing','rnd15'),
('study2/opt_200_200_200_200_ms1craboffxing','rnd20'),
('study2/opt_75_300_300_75_ms1craboffxing','flt7.5'),
('study2/opt_100_400_400_100_ms1craboffxing','flt10')]

for scen,name in scens:
   mk_fig_set(name,scen,single,double)







