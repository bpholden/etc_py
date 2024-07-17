import os
import numpy as np
import astropy.io.fits

class Sky:

    def __init__(self, site='MK'):

        self.sky_dir = 'data/sky'
        self.site = site

        if site == 'MK':
            self.MK()

        elif site == 'MH':
            self.MH()

        
    def MK(self):

        self.bfn = os.path.join(self.sky_dir,'bsky.eps_pang_parcsec.fits')
        self.rfn = os.path.join(self.sky_dir,'rsky.eps_pang_parcsec_onemicron.fits')

        self.bpix, self.bwave, self.bspec = self.read_spec(self.bfn)
        self.rpix, self.rwave, self.rspec = self.read_spec(self.rfn)

    def MH(self):

        self.bfn = os.path.join(self.sky_dir,'lick_sky_d55_2011aug29.fits.gz')
        self.rfn = os.path.join(self.sky_dir,'lick_sky_d55_2011aug29.fits.gz')

        self.bpix, self.bwave, self.bspec = self.read_spec(self.bfn)
        self.rpix, self.rwave, self.rspec = self.read_spec(self.rfn)

    def read_spec(self, fn):

        spec_hdu = astropy.io.fits.open(fn)
        hdr = spec_hdu[0].header
        spec = spec_hdu[0].data
        pix = np.arange(0,len(spec))
        wave =  hdr['CRVAL1'] + pix*hdr['CDELT1']

        return pix, wave, spec

    def rescale(instrument, wave, spec):

        #instrument.Ang_per_pix *= instrument.pixel_size # dwave is for a 1" slit
        sq_arcsec = instrument.swidth * instrument.sheight
        spec *= sq_arcsec * instrument.Ang_per_pix
        # this should be e-/pix/s

        return wave, spec
