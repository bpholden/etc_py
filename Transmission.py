import os
import os.path

import scipy
import astropy
import astropy.io.ascii
import astropy.io.fits
import numpy

class Transmission():
    def __init__(self,site=""):
        self.site= site
        self.inwave = None
        self.inextinc = None
        self.extgrid = None
        self.infile = self.extfilename()

    def extfilename(self):
        if self.site == "MH":
            return "mthamextinct.dat"
        elif self.site == "MK":
            return "mkoextinct.dat"
        else:
            return ""
        

    def __repr__(self):
        "<obs %s>" % (self.site)


    def readin_ext(self)

        try:
            inpath = os.path.realpath(__file__)
        else:
            inpath = os.getcwd()
        infile = os.path.join(inpath,"data",self.infile)
        mtham_ext = astropy.io.ascii.read(inpath)
        self.inwave = mtham_ext['col1']
        self.inextinc = mtham_ext['col2']

    def trans(self,wavegrid):
        self.extgrid = numpy.interp(wavegrid,self.inwave,self.inextinc)
        return self.extgrid
    
