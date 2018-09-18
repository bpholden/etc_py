import scipy
import astropy
import astropy.io
import astropy.io.fits
import numpy
import os
import os.path

class Telescope():
    def __init__(self,telescope):
        self.name= '' # KeckI, KeckII, Lick-3m 
        self.area= 0.
        self.plate_scale= 0. 

    def __repr__(self):
        "<telescope %s %f>" % (self.name,self.area)

