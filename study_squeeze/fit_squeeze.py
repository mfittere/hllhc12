import matplotlib as mpl
from matplotlib.pyplot import *
from numpy import *
from pyoptics import *
from poly_fit import *
from tfsdata import dump

#compare squeeze
ds=StrTable.open('ir6_log_str.tfs')
ds.plot_squeeze()
ds.plot_squeeze_diff(fn='squeeze_round/squeeze17/ir6_log_str.tfs')

#fitting round optics, index runs from 0 to 66
var='betytcdqb1'
p=ds.poly_fit(ds.get_vars('tcdq'),order=r,x0_idx=[0,66])
p=ds.poly_fit(ds.get_vars('tcdq'),order=r,x0_idx=[0,20,66],y0_idx=[ds[var][0],ds[var][20],ds[var][66]])
#fitting flat optics: round optics starts at index 80, change in squeeze are 5 and 20
p=ds.poly_fit(ds.get_vars('tcdq'),order=r,x0_idx=[0,5])
p=ds.poly_fit(ds.get_vars('tcdq'),order=r,x0_idx=[5,20])
p=ds.poly_fit(ds.get_vars('tcdq'),order=r,x0_idx=[20,80])

close('all')
ds=StrTable.open('ir6_log_str.tfs')
#always use poly_fit_betip with different orders, then edit the
#final fit.out file manually by combining the fits for the 
#different order
#fit full range
ds.poly_fit_betip(order=2,force=True,fn='fit.madx')
#fit values form n1 to n2
ds.poly_fit_betip(order=2,n1=0,n2=15,force=True,fn='fit.madx')
#plot beta functions at dump
ds.plot_dump(fn='fit_squeeze7_idx_15_66.madx')

#plot all tables
def pl_sq_all():
  close('all')
  for i in '24':
#  for i in '248':
#  i='4'
    ds=StrTable.open('squeeze_flathv/squeeze24a/ir%s_log_str.tfs'%i)
    ds.plot_squeeze_diff(fn='ir%s_log_str.tfs'%i,title='squeeze IR%s'%i)
#    ds.plot_squeeze(title='squeeze IR%s'%i)
    dsnew=StrTable.open('ir%s_log_str.tfs'%i)
    for k in dsnew.get_vars('tarir'): 
        print i,argmax(dsnew[k]) ,max(dsnew[k])
        print dsnew[k]
#remove trims from table
ds=StrTable.open('squeeze_round/squeeze11/ir6_log_str.tfs')
ds['col_names']=ds.get_vars('k(?!qt)')#all variables except for the kqts
fn='squeeze_round/squeeze11/ir6_log_str_nokqt.tfs'
fh=open(fn,'w')
dump(ds,fh)
fh.close()
dsnew=StrTable.open(fn)
draw()
show()
