#LOC = 24 (12/1/16)
class Aries():
    
    def __init__(self):
        self.date = None
        self.hour = None
        self.geoPosition = None
        
    def getDate(self):
        return self.date
    
    def getHour(self):
        return self.hour
    
    def getGeoPosition(self):
        return self.geoPosition
    
    def setDate(self, dateIN):
        self.date = dateIN
        pass
    
    def setHour(self, hourIN):
        self.hour = hourIN
        pass
    
    def setGeoPosition(self, geoIN):
        self.geoPosition = geoIN
        pass
    
    def printAries(self):
        stringValue = "Date: " + str(self.date) + "\tHour: " + str(self.hour) + "GeoPosition: " + str(self.geoPosition) + "\n"
        print(stringValue)
        pass
    
        