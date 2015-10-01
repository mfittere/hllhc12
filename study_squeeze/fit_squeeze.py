from pyoptics import *
from matplotlib.pyplot import *
from numpy import *
from numpy.polynomial.polynomial import polyval
from poly_fit import *
from tfsdata import dump

#plot tables
close('all')
StrTable.open('ir6_log_str.tfs').plot_squeeze_ir6(title='IR6')
StrTable.open('ir6_log_str.tfs').plot_betip()
StrTable.open('squeeze_round/squeeze12/ir6_log_str.tfs').reverse().plot_squeeze_ir6(title='IR6')
StrTable.open('squeeze_round/squeeze12/ir6_log_str.tfs').reverse().plot_betip()

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

#do a fit of manually, second order until point15, linear fit afterwards
ds.poly_fit(var=ds.get_vars('b[xy]dumpb[12]'),order=2,n1=0,n2=81)
ds.poly_fit(var=['kq4.l6b2','kq4.r6b1'],fn='fit_squeeze12_idx_0_14.madx')
ds.poly_fit(var=['kq5.l6b2','kq5.r6b2','kq5.l6b1','kq5.r6b1'],order=2)
ds.poly_fit(var=['kq8.l6b2','kq8.r6b2','kq8.l6b1','kq8.r6b1'],order=2)
ds.poly_fit(var=['kq9.l6b2','kq9.r6b2','kq9.l6b1','kq9.r6b1'],order=2)
ds.poly_fit(var=['kq10.l6b2','kq10.r6b2','kq10.l6b1','kq10.r6b1'],order=2)
ds.poly_fit(var=['kqt12.l6b2','kqt12.r6b2','kqt12.l6b1','kqt12.r6b1'],order=2)
#load polynomial
poly_load('fit.madx')

next: fit the kq4 with idx 14 fixed
#do it manually
var='kq4.l6b2'
var='kq4.r6b1'
var='kq5.r6b1'
var='kq9.l6b2'
var='kq10.l6b1'
var='kqt12.l6b1'
var='bxdumpb1'
close()
var='bydumpb1'
ds=StrTable.open('ir6_log_str.tfs')
plot(ds[var],'r')
#for round squeeze, fixed point is idx=14
ds.poly_fit_var(var,order=2,n1=0,n2=81,x0_idx=[0,20,-1])
p0_14=ds.poly_fit_var(var,order=2,n1=0,n2=15,x0_idx=[0,-1],xp0_idx=[14])
p15_66=ds.poly_fit_var(var,order=2,n1=14,n2=None,x0_idx=[14,-1],xp0_idx=[14])
print p0_14
print p15_66

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
