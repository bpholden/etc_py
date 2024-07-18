import os
import os.path

import scipy
import scipy.constants
import astropy
import astropy.io
import astropy.io.fits
import numpy as np

class Obs():
    def __init__(self):
        self.seeing= 1.
        self.airmass= 1.
        self.exptime= 1.0 
        self.redshift= 0.0

        self.mstar= 0.       # Mag
        self.mtype= 0        # Mag flag:  AB, Vega, AB default

        self.filterfn= None
        self.filterfulln = None
        self.filter= None      # Filter
        
        self.templatefn= None
        self.templatefullfn= None        
        self.template = None
        self.phot = None
        
        self.transmission = None
        
        self.vega_templatefn = self.gen_filename("alpha_lyr_stis_005.fits","data/templates")
        self.vega_template = self.get_file_data(self.vega_templatefn)

    def __repr__(self):
        "<obs %s %.1f\" %.1f s %.2f %.2f mag %s %s>" % (self.templatefn, self.seeing, self.exptime, self.airmass, self.mag, self.mtype, self.filterfn)


    def gen_filename(self,datapath):
        try:
            inpath = os.path.realpath(__file__)
        except:
            inpath = os.getcwd()
        self.filterfullfn = os.path.join(inpath,datapath,self.filterfn)
        return
        
    def get_file_data(self):
        return astropy.io.fits.getdata(self.filterfullfn)

    def get_template(self):
        self.templatefullfn = self.gen_filename(self.templatefn,"data/templates")
        self.template = self.get_file_data(self.templatefullfn)
        self.template['WAVELENGTH'] *= 1+self.redshift

    def get_filter(self):
        self.filterfn = self.gen_filename(self.filterfullfn,"data/templates")
        self.filter = astropy.io.ascii.read(self.filterfullfn)
        self.filter['wavelength'] = self.filter['col1']
        self.filter['thru'] = self.filter['col2']        


    def spec_filter_flux(self,template):

        c = scipy.constants.c*1e10 # Ang

        wave = template['WAVELENGTH']
        flux = template['FLUX']
        if self.transmission is not None:
            t_ext=self.transmission.trans(wave)
            flux *= 10**(-0.4*t_ext*self.airmass)
        filtwave=self.filter['wavelength']
        filtthru=self.filter['thru']

        good = (filtwave > wave.min()) & (filtwave < wave.max())

        interpfilt = np.interp(wave, filtwave[good], filtthru[good])
    
        # Normalize filter, this is a filter specific property
        # so we do not use the interpolated filter throughput
        # nor trimmed wavelength range
        wave_p_sq = np.trapz(filtthru*filtwave,x=filtwave)
        wave_p_sq /= np.trapz(filtthru/filtwave,x=filtwave)

        totfilt = np.trapz(interpfilt,x=wave)
        totflux = np.trapz(flux*interpfilt,x=wave)
        totflux /= totfilt
    
        totflux *= wave_p_sq/c

        return totflux, np.sqrt(wave_p_sq)
        


    def spec_filter_mag(self):

        tot_flux, _ = self.spec_filter_flux(self.template)

        if self.mtype is 'Vega':
            vega_flux, _ = self.spec_filter_flux(self.vegatemplate)
            mag = -2.5*np.log10(tot_flux) + 2.5*np.log10(vega_flux)
        elif self.mtype is 'AB':
            mag=-2.5*np.log10(tot_flux)-48.6
        else:
            mag=-2.5*np.log10(tot_flux)-48.6

        return mag


    def normalize_template(self):

        self.getFilter()
        self.getTemplate()
        
        mag = self.specFilterMag()
        dmag = self.mstar - mag
        self.template['FLUX'] *= 10**(-0.4*dmag)

        
    def compute_photons(self):
    
        self.phot = self.template['FLUX']  * self.template['WAVELENGTH'] / (scipy.constants.c*1e10)
        # fnu = flambda * lambda *lambda / c , c in Angstroms per second!
        self.phot /= scipy.constants.h * 1e7 # ergs - s
        if self.transmission is not None:
            self.phot *= 10**(-0.4*self.transmission.trans(self.template['WAVELENGTH'])*self.airmass)
        self.phot *= self.exptime
        
