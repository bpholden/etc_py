class SpecSim()
    def __init__(self):
        self.instrument = None
        self.obs = None
        self.transmission = None


        
    def calcS2N(self,instrument,obs,transmission):
        
        self.instrument = instrument
        self.obs = obs
        self.transmission = transmission

        
