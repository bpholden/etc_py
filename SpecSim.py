class SpecSim()
    def __init__(self):
        self.instrument = []
        self.obs = None
        self.transmission = None


        
    def calcS2N(self,instrument=[],obs=None,transmission=None):

        if instrument is not None:
            self.instrument = instrument
        if obs is not None:
            self.obs = obs
        if transmission is not None:
            self.transmission = transmission

        if self.obs is None or self.instrument is None:
            return None


        obs.normalize_template()
        obs.compute_photons()

        # this generates the number of photons per A per cm^2 landing on the telescope
        # now need to take into account 

        if len(self.instrument) > 0:
            obs.phot *= self.instrument[0].telescope.area
