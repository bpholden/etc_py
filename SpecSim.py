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

        

        
