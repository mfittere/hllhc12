from pyoptics import *
import matplotlib.pyplot as pl

def plot_opt_ir15():
  pl.close('all')
  o1=optics.open('twiss_ir5b1.tfs').plotbeta()
#  pl.savefig('/Users/mfittere/Desktop/ir5b1.png')
  o2=optics.open('twiss_ir5b2.tfs').plotbeta()
#  pl.savefig('/Users/mfittere/Desktop/ir5b2.png')
  return o1,o2

def plot_opt():
  o1=optics.open('twiss_lhcb1.tfs')
  o2=optics.open('twiss_lhcb2.tfs')
  o1.select('S.DS.L5.B1','E.DS.R5.B1').plotbeta()
  pl.title('IR5B1')
  ax = pl.gca()
  ax.legend().remove()
  pl.legend()
  pl.savefig('/Users/mfittere/Desktop/ir5b1.png')
  o2.select('S.DS.L5.B2','E.DS.R5.B2').plotbeta()
  pl.title('IR5B2')
  pl.savefig('/Users/mfittere/Desktop/ir5b2.png')

#plot_opt_ir15()
plot_opt()
pl.draw()
pl.show()
