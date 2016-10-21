
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
        #note: body, date, time, and observation are mandatory
    
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
    def printSighting(self):
        stringToPrint = (str(self.body) + "\t" + str(self.date) + "\t" + str(self.time) + "\t" + str(self.observation) + "\t"
                         + str(self.height) + "\t" + str(self.temp) + "\t" + str(self.pressure) + "\t" + str(self.horizon))
        print stringToPrint + "\n*****\n"
        pass