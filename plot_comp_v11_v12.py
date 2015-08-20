from pyoptics import *
import matplotlib.pyplot as pl
import numpy as np
from analysispkg import *

pl.close('all')

#**** vdm optics
#v1.1 optics
#plot_opt('vdm30v11/optics/')
#compare v1.1 and v1.2 optics
#comp_optics('vdm30v12/optics/','vdm30v11/optics/')
#comp_aperture('vdm30v12/aperture/','vdm30v11/aperture/',nlim=60)

#**** injection optics
#v1.1 optics
#plot_opt('injv11/optics/')
#compare v1.1 and v1.2 optics
comp_optics('study_presqueze/injv12/optics/','study_presqueze/injv11/optics/')
#comp_aperture('built_optics/injv12/aperture/','built_optics/injv11/aperture/',nlim=9)
#check_aperture('aperture_optics3/ap_ir5b1.tfs','aperture_opticsv11/ap_ir5b1.tfs')
#comp_aperture_v11('temp','aperture_opticsv11')
#check_aperture('temp/ap_ir5b1.tfs','aperture_opticsv11/ap_ir5b1.tfs')
         
#**** presquezed optics
#plot_cross_all('presqueezev12/optics/')

#**** squezed optics
#plot_cross_all('flatv12/optics/')
#plot_cross_all('roundv12/optics/')
pl.draw()
pl.show()
 
