import os
import os.path

import scipy
import astropy
import astropy.io
import astropy.io.fits
import numpy as np

class Obs():
    def __init__(self):
        self.seeing= 0.
        self.airmass= 0.
        self.mphase= 0
        self.mstar= 0.       # Mag
        self.filterfn= ''      
        self.filter= None      # Filter
        self.mtype= 0        # Mag flag:  1=AB, 2=Johnson
        self.exptime= 0.0 
        self.redshift= 0.0 
        self.templatefn= ''
        self.template = None
        
        self.vega_templatefn = self.getFilename("alpha_lyr_stis_005.fits","data/templates")
        self.vega_template = self.getFileData(self.vega_templatefn)

    def __repr__(self):
        "<obs %s %s>" % (self.,self.)

