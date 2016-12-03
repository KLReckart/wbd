#LOC = 42 (10/24/16)
#LOC = 47 (12/1/16)
class Sighting():
    
    def __init__(self):
        #initialize all attributes as None
        self.body = None
        self.date = None
        self.time = None
        self.observation = None
        self.height = None
        self.temp = None
        self.pressure = None
        self.horizon = None
        self.geoLatitude = None  #geographical latitude
        self.geoLongitude = None #geographical longitude
        self.azimuthAdjument = None
        self.distanceAdjustment = None
        #note: body, date, time, and observation are mandatory
#   GET FUNCTIONS
    def getBody(self):
        return self.body
    
    def getDate(self):
        return self.date
    
    def getTime(self):
        return self.time
    
    def getObservation(self):
        return self.observation
    
    def getHeight(self):
        return self.height
    
    def getTemp(self):
        return self.temp
    
    def getPressure(self):
        return self.pressure
    
    def getHorizon(self):
        return self.horizon
    
    def getGeoLatitude(self):
        return self.geoLatitude
    
    def getGeoLongitude(self):
        return self.geoLongitude
    
    def getAzimuthAdjustment(self):
        return self.azimuthAdjument
    
    def getDistanceAdjustment(self):
        return self.distanceAdjustment
    
#   SET FUNCTIONS
    def setBody(self, bodyIN):
        self.body = bodyIN
        
    def setDate(self, dateIN):
        self.date = dateIN
        
    def setTime(self, timeIN):
        self.time = timeIN
        
    def setObservation(self, observationIN):
        self.observation = observationIN
        
    def setHeight(self, heightIN):
        self.height = heightIN
        
    def setTemp(self, tempIN):
        self.temp = tempIN
        
    def setPressure(self, pressureIN):
        self.pressure = pressureIN
        
    def setHorizon(self, horizonIN):
        self.horizon = horizonIN
    
    def setGeoLatitude(self, latitudeIN):
        self.geoLatitude = latitudeIN
        
    def setGeoLongitude(self, longitudeIN):
        self.geoLongitude = longitudeIN
        
    def setAzimuthAdjustment(self, adjustIN):
        self.azimuthAdjument = adjustIN
        
    def setDistanceAdjustment(self, adjustIN):
        self.distanceAdjustment = adjustIN
    
#   PRINT FUNCTION
    def printSighting(self):
        stringToPrint = (str(self.body) + "\t" + str(self.date) + "\t" + str(self.time) + "\t" + str(self.observation) + "\t"
                         + str(self.height) + "\t" + str(self.temp) + "\t" + str(self.pressure) + "\t" + str(self.horizon))
        print stringToPrint + "\n*****\n"
        pass