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
        self.mtype= 0        # Mag flag:  AB, Vega, AB default
        self.exptime= 0.0 
        self.redshift= 0.0
        
        self.filterfn= None
        self.filterfulln = None
        self.filter= None      # Filter
        
        self.templatefn= None
        self.templatefullfn= None        
        self.template = None

        self.transmission = None
        
        self.vega_templatefn = self.getFilename("alpha_lyr_stis_005.fits","data/templates")
        self.vega_template = self.getFileData(self.vega_templatefn)

    def __repr__(self):
        "<obs %s %.1f %.2f %.2f>" % (self.templatefn, self.seeing, self.airmass, self.mag)


    def genFilename(self,datapath):
        try:
            inpath = os.path.realpath(__file__)
        else:
            inpath = os.getcwd()
        self.filterfullfn = os.path.join(inpath,datapath,self.filterfn)
        return
        
    def getFileData(self):
        return astropy.io.fits.getdata(self.filterfullfn)

    def getTemplate(self):
        self.templatefullfn = self.getFilename(templatefn,"data/templates")
        self.template = self.getFileData(self.templatefullfn)

    def getFilter(self):
        self.filterfn = self.getFilename(self.filterfullfn,"data/templates")
        self.filter = astropy.io.ascii.read(self.filterfullfn)
        self.filter['wavelength'] = self.filter['col1']
        self.filter['thru'] = self.filter['col2']        


    def spec2Mag(spec,filter_thru):
        C= 2.9979000e+10 # the speed of light
        careful = 1.0
        wave = spec['WAVELENGTH']
        flux = spec['FLUX']

        frac_filt = 0.0
        fwave=filter_thru['wavelength']
        fthru=filt_thru['thru']

        fthru /= np.trapz(fthru)

        wh=(fwave > min(wave)) & (fwave <= max(wave))
        

        if len(fwave[wh]) > 0 :
            frac_filt=np.trapz(fthru[wh], x=fwave[wh])/np.trapz(fthru, x=fwave)
            
            if frac_filt >= careful:
                
                llambda=np.trapz(fthru*fwave,x=fwave)/np.trapz(fthru,x=fwave)
                filt_interp = np.interp(wave,fwave, fthru)
                totfilt=np.trapz(interpfilt,x=wave)
                totflux=1d-17*llambda^2*1d-8*np.ttrapz(flux*interpfilt,x=wave)/totfilt/c
                                # flux convolved with filter/ integral over filter
                                # times lambda^2/c
                                # factor of 1d-17 for the initial units
                                # factor of 1d-8 to convert from angstroms

                mag=-2.5*np.log10(totflux)-48.6
            else:
                mag = -99
            
        else:
            mag = -99
        return mag



    def normalizeTemplate(self):

        mag = self.specFilterMag()
        dmag = self.mstar - mag
        self.template['FLUX'] *= 10**(-0.4*dmag)

        
        
