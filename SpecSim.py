class SpecSim()
    def __init__(self):
        self.instrument = None
        self.obs = None
        self.transmission = None


        
    def calcS2N(self,instrument=None,obs=None,transmission=None):

        if instrument is not None:
            self.instrument = instrument
        if obs is not None:
            self.obs = obs
        if transmission is not None:
            self.transmission = transmission

        

        
