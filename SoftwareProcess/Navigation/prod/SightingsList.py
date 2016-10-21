import Navigation.prod.Sighting as Sighting
from operator import attrgetter

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
        
        #https://docs.python.org/2/howto/sorting.html#sortinghowto
        newList = sorted(self.thisList, key=attrgetter('date', 'time', 'body'))
        print "OLD LIST:\n"
        self.printSightingsList()
        self.thisList = newList
        print "NEW LIST:\n"
        self.printSightingsList()
        pass
    
    def sortKeyByDate(self, sightingIN):
        if isinstance(sightingIN, Sighting)  == True:
            result = sightingIN.getDate()
        return result
    
    def sortKeyByTime(self, sightingIN):
        if isinstance(sightingIN, Sighting) == True:
            result = sightingIN.getTime()
        return result
    
    def sortKeyByBody(self, sightingIN):
        if isinstance(sightingIN, Sighting) == True:
            result = sightingIN.getBody()
        return result
    
    def printSightingsList(self):
        #for each sighting in the list, print it
        indexValue = 1
        for aSighting in self.thisList:
            print str(indexValue) + "\n"
            aSighting.printSighting()
            indexValue = indexValue + 1
        
        pass