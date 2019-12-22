import os
import os.path

import scipy
import astropy
import astropy.io
import astropy.io.fits
import numpy

import Telescope

class Instrument():
    def __init__(self):
        self.name = ""
        self.mag_perp = 0
        self.mag_para = 0
        self.pixel_scale = 0.
        self.scale_perp= 0.
        self.scale_para= 0.0
        self.R= 0.
        self.mlambda= 0.0
        self.dark= 0.0
        self.readno= 0.0
        self.dichroic= ''
        self.grating= ''

        self.swidth= 0.    # Slit width
        self.sheight= 0.   # Slit height
        self.wvmnx= []   # wavelength min/max
        self.bins= 0       # Spatial binning
        self.bind= 0       # Dispersion binning
        self.dely= 0.0 
        self.telescope = None
        
    def __repr__(self):
        "<inst %s %s>" % (self.name ,self.grating)

    def __str__(self):
        "<inst %s %s>" % (self.name ,self.grating)


    def 
