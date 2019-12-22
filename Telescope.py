import os
import os.path

import scipy
import astropy
import astropy.io
import astropy.io.fits
import numpy

class Telescope():
    def __init__(self,name):
        self.name= name # Keck, Shane, APF
        self.area= 0.
        self.plate_scale= 0. 

    def __repr__(self):
        "<telescope %s %f>" % (self.name,self.area)

