import os, sys

from numpy import *

from pyoptics import *
import matplotlib.pyplot as pl

from aper_utils import *


single=[
  ('TAXS'       ,None ,'taxs',12) ,
  ('MQXFA.[AB]1',0.150,'q1'  ,12) ,
  ('MQXFB.[AB]2',0.150,'q2'  ,12) ,
  ('MQXFA.[AB]3',0.150,'q3'  ,12) ,
  ('MBXF'       ,0.150,'d1'  ,12)]

double=[
  ('TAXN.4L',None ,'taxnl',12) ,
  ('TAXN.4R',None ,'taxnr',12) ,
  ('MBRD.4L'  ,0.105,'d2cl',12) ,
  ('MBRD.4R'  ,0.105,'d2cr',12) ,
  ('MCBRD..4L',0.105,'d2l' ,12) ,
  ('MCBRD..4R',0.105,'d2r' ,12) ,
  ('MCBYY..4L',0.09 ,'q4cl',12) ,
  ('MCBYY..4R',0.09 ,'q4cr',12) ,
  ('MQYY.4L'  ,0.09 ,'q4l' ,12) ,
  ('MQYY.4R'  ,0.09 ,'q4r' ,12) ,
  ('MCBY...5L' ,0.07 ,'q5cl',12) ,
  ('MCBY...5R' ,0.07 ,'q5cr',12) ,
  ('MQY.5L'   ,0.07 ,'q5l' ,12) ,
  ('MQY.5R'   ,0.07 ,'q5r' ,12) ,
  ('TCLMB.5L' ,0.07,'q5ml',18) ,
  ('TCLMB.5R' ,0.07,'q5mr',18) ,
  ('MCBC..6L'  ,0.056,'q6cl',18) ,
  ('MCBC..6R'  ,0.056,'q6cr',18) ,
  ('MQML.6L'  ,0.056,'q6l' ,18) ,
  ('MQML.6R'  ,0.056,'q6r' ,18) ,
  ('TCLMC.6L' ,0.056,'q6ml',18) ,
  ('TCLMC.6R' ,0.056,'q6mr',18)]

scens=[
('study2/opt_150_150_150_150_295_2000_ms1craboffxing','rnd15') ,
('study2/opt_200_200_200_200_255_2000_ms1craboffxing','rnd20') ,
('study2/opt_75_300_300_75_245_750_ms1craboffxing'   ,'flt7.5'),
('study2/opt_100_400_400_100_210_750_ms1craboffxing' ,'flt10')]



leg={'rnd15':r'IR1/5 $\beta^*=15$ cm, $\pm 295\,\mu$rad',
     'rnd20':r'IR1/5 $\beta^*=20$ cm, $\pm 255\,\mu$rad',
     'flt7.5':r'IR1/5 $\beta^*=30,7.5$ cm, $\pm 245\,\mu$rad',
     'flt10':r'IR1/5 $\beta^*=40,10$ cm, $\pm 210\,\mu$rad' }

double=[
  ('MBRD.4L'  ,0.105,'d2cl',12) ,
  ('MBRD.4R'  ,0.105,'d2cr',12) ,
  ('MCBRD..4L',0.105,'d2l' ,12) ,
  ('MCBRD..4R',0.105,'d2r' ,12) ]

for scen,name in scens:
   mk_fig_set(name,scen,leg[name],[],double)

leg={'rnd15':r'IR1/5 $\beta^*=15$ cm, $\pm 295\,\mu$rad',
     'rnd20':r'IR1/5 $\beta^*=20$ cm, $\pm 255\,\mu$rad',
     'flt7.5':r'IR1/5 $\beta^*=30,7.5$ cm, $\pm 245\,\mu$rad',
     'flt10':r'IR1/5 $\beta^*=40,10$ cm, $\pm 210\,\mu$rad' ,
     'rnd15ms2':r'IR1/5 $\beta^*=15$ cm, $\pm 295\,\mu$rad',
     'rnd20ms2':r'IR1/5 $\beta^*=20$ cm, $\pm 255\,\mu$rad',
     'flt7.5ms2':r'IR1/5 $\beta^*=30,7.5$ cm, $\pm 245\,\mu$rad',
     'flt10ms2':r'IR1/5 $\beta^*=40,10$ cm, $\pm 210\,\mu$rad' ,
     'rnd15ms3':r'IR1/5 $\beta^*=15$ cm, $\pm 295\,\mu$rad',
     'rnd20ms3':r'IR1/5 $\beta^*=20$ cm, $\pm 255\,\mu$rad',
     'flt7.5ms3':r'IR1/5 $\beta^*=30,7.5$ cm, $\pm 245\,\mu$rad',
     'flt10ms3':r'IR1/5 $\beta^*=40,10$ cm, $\pm 210\,\mu$rad' }


double=[
  ('MCBYY..4L',0.08 ,'q4cl',12) ,
  ('MCBYY..4R',0.08 ,'q4cr',12) ,
  ('MQYY.4L'  ,0.08 ,'q4l' ,12) ,
  ('MQYY.4R'  ,0.08 ,'q4r' ,12) ,
  ('MCBY...5L' ,0.056 ,'q5cl',12) ,
  ('MCBY...5R' ,0.056 ,'q5cr',12) ,
  ('MQY.5L'   ,0.056 ,'q5l' ,12) ,
  ('MQY.5R'   ,0.056 ,'q5r' ,12) ,
  ('TCLMB.5L' ,0.056,'q5ml',18) ,
  ('TCLMB.5R' ,0.056,'q5mr',18) ]

scens=[
('study2/opt_200_200_200_200_255_2000_ms2craboffxing','rnd20ms2') ,
('study2/opt_100_400_400_100_210_750_ms2craboffxing' ,'flt10ms2')]

for scen,name in scens:
   mk_fig_set(name,scen,leg[name],[],double)

double=[
  ('MCBYY..4L',0.07 ,'q4cl',12) ,
  ('MCBYY..4R',0.07 ,'q4cr',12) ,
  ('MQYY.4L'  ,0.07 ,'q4l' ,12) ,
  ('MQYY.4R'  ,0.07 ,'q4r' ,12) ,
  ('MCBY...5L' ,0.056 ,'q5cl',12) ,
  ('MCBY...5R' ,0.056 ,'q5cr',12) ,
  ('MQY.5L'   ,0.056 ,'q5l' ,12) ,
  ('MQY.5R'   ,0.056 ,'q5r' ,12) ,
  ('TCLMB.5L' ,0.056,'q5ml',18) ,
  ('TCLMB.5R' ,0.056,'q5mr',18) ]

scens=[
('study2/opt_200_200_200_200_255_2000_ms3craboffxing','rnd20ms3'),
('study2/opt_100_400_400_100_210_750_ms3craboffxing' ,'flt10ms3')]

for scen,name in scens:
   mk_fig_set(name,scen,leg[name],[],double)


