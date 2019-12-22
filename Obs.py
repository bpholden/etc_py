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
        self.filterfn= ''      
        self.filter= None      # Filter
        self.mtype= 0        # Mag flag:  1=AB, 2=Johnson
        self.exptime= 0.0 
        self.redshift= 0.0 
        self.templatefn= ''
        self.template = None
        
        self.vega_templatefn = self.getFilename("alpha_lyr_stis_005.fits","data/templates")
        self.vega_template = self.getFileData(self.vega_templatefn)

    def __repr__(self):
        "<obs %s %.1f %.2f %.2f>" % (self.templatefn, self.seeing, self.airmass, self.mag)


    def genFilename(fn,datapath):
        try:
            inpath = os.path.realpath(__file__)
        else:
            inpath = os.getcwd()
        fullfn = os.path.join(inpath,datapath,fn)
        return = fullfn
        
    def getFileData(fullfn):
        return astropy.io.fits.getdata(fullfn)

    def getTemplate(templatefn):
        self.templatefn = self.getFilename(templatefn,"data/templates")
        self.template = self.getFileData(self.templatefn)

    def getFilter(filterfn):
        self.filterfn = self.getFilename(filterfn,"data/templates")
        self.filter = astropy.io.ascii.read(self.filterfn)
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

        # this is how single_spec2mag wants
        # the flux units, 1e-17 ergs/cm/cm/s/A
        temp['WAVELENGTH'] *= (1+obs.redshift) # note, we are doing NO bounds checking.
        temp_mstar = single_spec2mag(temp,self.filter)

        if self.mtype == 1:
            vega_mstar = single_spec2mag(self.vega_template,self.filter)
            temp_mstar = temp_mstar - vega_mstar
            temp['FLUX'] *= 10^(0.4*temp_mstar)   # force to have 0 mag in filter
            temp['FLUX'] *= temp['WAVELENGTH'] /(6.626d-27 *2.99792e18)    # convert to photons
            n0 = interpol(wave,temp['FLUX'],temp'W[AVELENGTH'])

        
        
