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
        return "<inst %s %s>" % (self.name ,self.grating)

    def __str__(self):
        return "<inst %s %s>" % (self.name ,self.grating)


    def scale(self, mag):
        return self.telescope.plate_scale * mag * self.pixel_size/1000.

        
    def kastRed(self,grating):

        self.name = 'Kast Red'
        self.mag_perp = 20.9
        self.mag_para = 20.9
        self.pixel_size = 15.0
        self.telescope = Telescope.Telescope(name='Shane')

        self.scale_perp = self.scale(self.mag_perp)
        self.scale_para = self.scale(self.mag_para)
        self.grating = grating
        if grating == '600/7500':
            self.R = 3164
        self.readno = 4.3
        self.dark = 0.001
        self.wvmnx = [5000., 10000.]
        self.bind = 1
        self.bins = 1
        self.swidth = 1.0
        self.sheight = 120.0

        
        return
    
    def kastBlue(self,grism):

        self.name = 'Kast Blue'
        self.mag_perp = 20.9
        self.mag_para = 20.9
        self.pixel_size = 15.0
        self.telescope = Telescope.Telescope(name='Shane')

        self.scale_perp = self.scale(self.mag_perp)
        self.scale_para = self.scale(self.mag_para)
        self.grating = grism
        if grism == 'G1':
            self.R = 2344
        elif grism == 'G2':
            self.R = 4254
        elif grism == 'G3':
            self.R = 5492
        else:
            self.R = 4254
            self.grating = 'G2'

        self.readno = 3.7
        self.dark = 0.001
        self.wvmnx = [3500., 6000.]
        self.bind = 1
        self.bins = 1
        self.swidth = 1.0
        self.sheight = 120.0
            
        
        
        return

    def levy_decker(self,decker):
        if decker[0:1] == 'N':
            self.swidth = 0.5
            self.sheight = 8.0
        elif decker[0:1] == 'S':
            self.swidth = 0.75
            self.sheight = 8.0
        elif decker[0:1] == 'M':
            self.swidth = 1.0
            self.sheight = 8.0
        elif decker[0:1] == 'W':
            self.swidth = 1.0
            self.sheight = 3.0
        elif decker[0:1] == 'T':
            self.swidth = 2.0
            self.sheight = 3.0
        elif decker[0:1] == 'B':
            self.swidth = 2.0
            self.sheight = 8.0
        else:
            self.swidth = 1.0
            self.sheight = 3.0
    
    def levy(self,decker='W'):
        self.name = 'Levy'
        self.mag_perp = 5.5136 # Magnification perpendicular to dispesion
        self.mag_para = 4.9913 # Magnification parallel to dispesion
        self.pixel_size = 13.5 # in microns
        self.telescope = Telescope.Telescope(name='APF')

        self.scale_perp = self.scale(self.mag_perp)
        self.scale_para = self.scale(self.mag_para)
        self.R     = 282160.8
        self.mlambda = 465980.24
        self.readno = 3.75
        self.dark = 0.001
        self.bind = 1
        self.bins = 1
        self.wvmnx = [3742., 7700.]
        self.levy_decker(decker)
        
        return

    def DARTSBlue(self):
        self.name = 'DARTS Blue'
        self.pixel_size = 13.5 # in microns
        self.telescope = Telescope.Telescope(name='APF')

        self.scale_perp = self.scale(self.mag_perp)
        self.scale_para = self.scale(self.mag_para)
        self.R = 750
        self.readno = 5
        self.dark = 0.001
        self.bind = 1
        self.bins = 1
        self.wvmnx = [3500, 6000.]
        self.swidth = 1.0
        self.sheight = 30.0
        
        return

    def DARTSRed(self):
        self.name = 'DARTS Red'        
        self.pixel_size = 13.5 # in microns
        self.telescope = Telescope.Telescope(name='APF')

        self.scale_perp = self.scale(self.mag_perp)
        self.scale_para = self.scale(self.mag_para)
        self.R = 750
        self.readno = 5
        self.dark = 0.001
        self.bind = 1
        self.bins = 1
        self.wvmnx = [6000, 9000.]
        self.swidth = 1.0
        self.sheight = 30.0

        return

