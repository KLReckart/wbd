import Navigation.prod.Sighting as Sighting

class SightingsList():
    
    def __init__(self):
        #initialize list to being empty
        self.thisList = []
        
    def getThisList(self):
        return self.thisList
    
    def addSighting(self, sightingIN=None):
        funcName = "SightingsList.addSighting"
        if sightingIN <> None and isinstance(sightingIN, Sighting):
            self.thisList.append(sightingIN)
        else:
            raise ValueError(funcName + ":  trying to a Null or Non Sighting value to list")
        pass
    
    def sortSightingsList(self):
        
        pass