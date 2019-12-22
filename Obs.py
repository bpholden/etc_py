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
        "<obs %s %.1f\" %.1f s %.2f %.2f mag %s %s>" % (self.templatefn, self.seeing, self.exptime, self.airmass, self.mag, self.mtype, self.filterfn)


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


    def specFilterFlux(self,template):

        c = scipy.constants.c*1e10 # Ang

        wave = template['WAVELENGTH']
        flux = template['FLUX']
        if self.transmission is not None:
            t_ext=self.transmission.trans(wave)
            flux *= t_ext
        fwave=self.filter['wavelength']
        fthru=self.filt['thru']

        interpfilt = np.interp(, filtwave, filtthru)
    
        good = (filtwave > wave.min()) & (filtwave < wave.max())


        wave_p_sq = np.trapz(filtthru*filtwave,x=filtwave)
        wave_p_sq /= np.trapz(filtthru/filtwave,x=filtwave)

        totfilt = np.trapz(interpfilt,x=wave)
        totflux = np.trapz(flux*interpfilt,x=wave)
        totflux /= totfilt
    
        totflux *= wave_p_sq/c

        return totflux, np.sqrt(wave_p_sq)
        


    def specFilterMag(self):

        tot_flux, wave_p = self.specFilterFlux(self.template)

        if self.mtype is 'Vega':
            vega_flux, wave_p = self.specFilterFlux(self.vegatemplate)
            mag = -2.5*np.log10(tot_flux) + 2.5*np.log10(vega_flux)
        elif self.mtype is 'AB':
            mag=-2.5*np.log10(tot_flux)-48.6
        else:
            mag=-2.5*np.log10(tot_flux)-48.6

        return mag


    def normalizeTemplate(self):

        self.getFilter()
        self.getTemplate()
        
        mag = self.specFilterMag()
        dmag = self.mstar - mag
        self.template['FLUX'] *= 10**(-0.4*dmag)

        
    def computePhotons(self):
    
        phot = self.template['FLUX']  * self.template['WAVELENGTH'] / (2.99792e18)
        # fnu = flambda * lambda *lambda / c , c in Angstroms per second!
        phot /= 6.626e-27 # ergs - s
        return phot
        
