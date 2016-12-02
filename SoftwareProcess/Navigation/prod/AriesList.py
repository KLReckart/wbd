#LOC = 29 (12/1/16)
import Navigation.prod.Aries as Aries
from operator import attrgetter

class AriesList():
    
    def __init__(self):
        self.thisList = []
        
    def getThisList(self):
        return self.thisList
    
    def addAries(self, ariesIN=None):
        funcName = "AriesList.addAries"
        if ariesIN <> None and isinstance(ariesIN, Aries.Aries):
            self.thisList.append(ariesIN)
        else:
            raise ValueError(funcName + ":  trying to a Null or Non Aries value to list")
        pass
        
    def printAriesList(self):
        #for each sighting in the list, print it
        indexValue = 1
        for anAries in self.thisList:
            print str(indexValue) + "\n"
            anAries.printAries()
            indexValue = indexValue + 1
        
        pass
    
    def sortAriesList(self):
        
        #https://docs.python.org/2/howto/sorting.html#sortinghowto
        newList = sorted(self.thisList, key=attrgetter('date', 'hour', 'geoPosition'))
        print "OLD LIST:\n"
        self.printSightingsList()
        self.thisList = newList
        print "NEW LIST:\n"
        self.printSightingsList()
        pass