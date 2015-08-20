from pyoptics import *
import matplotlib.pyplot as pl

def plot_ap():
  pl.close('all')
  o1=optics.open('twiss_ir5b1.tfs').plotbeta()
#  pl.savefig('/Users/mfittere/Desktop/ir5b1.png')
  o2=optics.open('twiss_ir5b2.tfs').plotbeta()
#  pl.savefig('/Users/mfittere/Desktop/ir5b2.png')
  return o1,o2

plot_ap()
pl.draw()
pl.show()
