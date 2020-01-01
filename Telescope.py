import os
import os.path

import scipy
import astropy
import astropy.io
import astropy.io.fits
import numpy

class Telescope():
    def __init__(self,name=''):
        self.name= name # Keck, Shane, APF
        self.area= 0.
        self.plate_scale= 0.
        if name is 'APF':
            self.APF()
        elif name is 'Shane':
            self.Shane()
        elif name is 'Keck':
            self.Keck()

    def __repr__(self):
        return "<telescope %s %.1f %.1f>" % (self.name,self.area,self.plate_scale)


    def Keck(self):
        self.name = 'Keck'
        self.area = 723674.
        self.plate_scale = 1.379

    def Shane(self):
        self.name = 'Shane'
        self.area = 63617.
        self.plate_scale = 1.379

    def APF(self):
        self.name = 'APF'
        self.area = 42053.
        self.plate_scale = 5.8241

