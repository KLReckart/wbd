#LOC = 27 (12/1/16)
import Navigation.prod.Star as Star
from operator import attrgetter

class StarsList():
    
    def __init__(self):
        self.thisList = []
        
    def addStar(self, starIN=None):
        funcName = "StarsList.addStar"
        if starIN <> None and isinstance(starIN, Star.Star):
            self.thisList.append(starIN)
        else:
            raise ValueError(funcName + ":  trying to a Null or Non Star value to list")
        pass
        
    def printStarsList(self):
        #for each sighting in the list, print it
        indexValue = 1
        for aStar in self.thisList:
            print str(indexValue) + "\n"
            aStar.printStar()
            indexValue = indexValue + 1
        
        pass
    
    def sortStarsList(self):
        
        #https://docs.python.org/2/howto/sorting.html#sortinghowto
        newList = sorted(self.thisList, key=attrgetter('body', 'date', 'longitude', 'latitude'))
        print "OLD LIST:\n"
        self.printSightingsList()
        self.thisList = newList
        print "NEW LIST:\n"
        self.printSightingsList()
        pass