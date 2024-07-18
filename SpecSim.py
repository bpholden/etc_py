class SpecSim()
    def __init__(self):
        self.instrument = []
        self.obs = None
        self.transmission = None
        self.sky = None

        
    def calc_sn(self, instrument=None, obs=None, transmission=None, sky=None):

        if instrument is not None:
            self.instrument = instrument
        if obs is not None:
            self.obs = obs
        if transmission is not None:
            self.transmission = transmission
        if sky is not None:
            self.sky = sky

        if self.obs is None or self.instrument is None:
            return None
        if self.sky is None:
            self.sky = Sky()


        self.obs.normalize_template()
        self.obs.compute_photons()

        # this generates the number of photons per A per cm^2 landing on the telescope
        # now need to take into account 

        if len(self.instrument) > 0:
            self.obs.phot *= self.instrument[0].telescope.area
