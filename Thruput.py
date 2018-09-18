import scipy
import astropy
import astropy.io
import astropy.io.fits
import numpy
import os
import os.path

class Thruput():
    def __init__(self,comboname):
        td = os.getenv("THRUPUT_DIR")
        self.comboname = comboname
        self.combopath = os.path.join(td,self.comboname)

        try:
            th = astropy.io.fits.open(self.combopath)
            self.thruput = th[1].data
        except:
            self.thruput = None

    def __repr__(self):
        "<thruput %s %s>" % (self.comboname,self.combopath)

