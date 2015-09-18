from pyoptics import *
from matplotlib.pyplot import *
from numpy import *
from numpy.polynomial.polynomial import polyval

close('all')
#StrTable.open('squeeze5/ir6_log_str.tfs').plot_squeeze_ir6(title='IR6')
#savefig('ir6_squeeze5.png')
#StrTable.open('squeeze5/ir6_log_str.tfs').plot_betip(title='Twiss IR6')
#savefig('ir6_twiss_squeeze5.png')
ds5=StrTable.open('squeeze5/ir6_log_str.tfs')
#byb1=polyfit([0,66],[ds5.betyip6b1[10],ds5.betyip6b1[66]],1,w=np.append(ones(10)*1.e6,ones(57)))
byb1=ds5.betyip6b1
l=len(byb1)
fbyb1=polyfit(arange(l),byb1,2,w=np.append(np.append(ones(10)*1.e6,ones(56)),[1.e6]))
print fbyb1
plot(byb1,'b')
x=arange(l)
plot(x,[polyval(xx,fbyb1[::-1]) for xx in x],'r')
draw()
show()
