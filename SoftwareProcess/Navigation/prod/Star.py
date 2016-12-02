#LOC = 31 (12/1/16)
class Star():
    
    def __init__(self):
        self.body = None
        self.date = None
        self.longitude = None
        self.latitude = None
        
    def getBody(self):
        return self.body
    
    def getDate(self):
        return self.date
    
    def getLongitude(self):
        return self.longitude
    
    def getLatitude(self):
        return self.latitude
    
    def setBody(self, bodyIN):
        self.body = bodyIN
        pass
        
    def setDate(self, dateIN):
        self.date = dateIN
        pass
        
    def setLongitude(self, longitudeIN):
        self.longitude = longitudeIN
        pass
        
    def setLatitude(self, latitudeIN):
        self.latitude = latitudeIN
        pass
    
    def printStar(self):
        lineToPrint = ("Body:\t" + str(self.body) + "\tDate:\t" + str(self.date) + "\tLongitude:\t" + str(self.longitude)
                        + "\tLatitude:\t" + str(self.latitude) + "\n" )
        print(lineToPrint)
        pass