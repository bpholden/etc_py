import scipy
import astropy
import astropy.io
import astropy.io.fits
import numpy
import os
import os.path

class Template():
    def __init__(self,templatename):
        td = os.getenv("TEMPLATE_DIR")
        self.templatename = templatename
        self.templatepath = os.path.join(td,self.templatename)

        try:
            th = astropy.io.fits.open(self.templatepath)
            self.template = th[1].data
        except:
            self.template = None

    def __repr__(self):
        "<template %s %s>" % (self.templatename,self.templatepath)

