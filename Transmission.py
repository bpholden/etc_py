import os
import os.path

import scipy
import astropy
import astropy.io.ascii
import astropy.io.fits
import numpy

class Transmission():
    def __init__(self,inwave, airmass, site="MH"):
        self.site= site
        self.inwave = inwave
        self.airmass = airmass
        self.inextinc = None
        self.extgrid = None
        self.infile = self.extfilename()
        if self.infile is not '':
            self.readin_ext()

    def extfilename(self):
        if self.site == "MH":
            return "mthamextinct.dat"
        elif self.site == "MK":
            return "mkoextinct.dat"
        else:
            return ""
        

    def __repr__(self):
        "<obs %s>" % (self.site)


    def readin_ext(self):

        try:
            inpath = os.path.realpath(__file__)
        except:
            inpath = os.getcwd()
        infile = os.path.join(inpath,"data",self.infile)
        if os.path.exists(infile):
            ext = astropy.io.ascii.read(inpath)
            self.inwave = ext['col1']
            self.inextinc = ext['col2']
        else:
            return

    def trans(self,wavegrid):
        self.extgrid = numpy.interp(wavegrid,self.inwave,self.inextinc)
        return self.extgrid
    
