#from workpkg import *
from pyoptics import *
from matplotlib.pyplot import *

def mkfig(fn):
    ynn='g1 g2 g3'.split()
    t=optics.open(fn)
    figure(fn,figsize=(12,8))
    title(fn.split('.')[0])
    clf()
    subplot(221)
    plot(t.betx_mcby_ref,t.bety_mcby_ref,'-o')
    xlabel(r'$\beta_x \rm mcby [m]$')
    ylabel(r'$\beta_y \rm mcby [m]$')
    subplot(222)
    for yy in ynn:
        plot(t.betx_mcby_ref,abs(t[yy]),'-o',label=yy)
    xlabel(r'$\beta_x \rm mcby [m]$')
    ylabel('g [T/m]')
    ylim(128,133)
    legend()
    subplot(223)
    for yy in ynn:
        plot(t.bety_mcby_ref,abs(t[yy]),'-o',label=yy)
    xlabel(r'$\beta_y \rm mcby [m]$')
    ylabel('g [T/m]')
    ylim(128,133)
    legend()
    subplot(224)
    for yy in ynn:
        hist(abs(t[yy]),label=yy,alpha=0.2)
    xlim(128,133)
    xlabel('g [T/m]')
    legend()
    tight_layout()
    figname=fn.replace('tfs','png')
    savefig(figname)
    #os.system('cp %s  ~/dfshome/Desktop/'%figname)

close('all')
mkfig('presqueze_q4_scan100.tfs')
mkfig('presqueze_q4_scan107.tfs')
mkfig('presqueze_q4_scan93.tfs')

draw()
show()



