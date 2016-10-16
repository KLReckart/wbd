from datetime import datetime
import os
import math
from __builtin__ import str
import Navigation.prod.Sighting as Sighting
import Navigation.prod.SightingsList as SightingsList
import Navigation.prod.Angle as Angle


class Fix():
    def __init__(self, logFile=None):
        funcName = "Fix.__init__"
        #initialize logFile if logFile == None
        if (logFile == None) :
            logFile = "log.txt"
        if (isinstance(logFile, str) and len(logFile) > 0):
            #set Fix attribute: logFileName
            self.logFileName = logFile
            #set Fix attribute: siteFileName
            self.siteFileName = None
            #create or append the file with the desired name
            try:
                file01 = open(logFile, "a")
            except:
                #if file was not created, raise exception
                raise ValueError(funcName + ":  failed to create or append file")
            #append the desired line to the beginning of the file
            string01 = "LOG: " + str(datetime.today()) + " Start of log\n"
            try:
                file01.write(string01)
            except:
                raise ValueError(funcName + ":  failed to create or append file")
            #close file
            file01.close()

            print(str(os.getcwd()))
        else:
            raise ValueError(funcName + ":  invalid input")
        pass
    
    def getLogFileName(self):
        return self.logFileName
    
    def getSiteFileName(self):
        return self.siteFileName
    
    #note the below assumes that the fileName_IN was checked for .xml and is a string
    def setSiteFileName(self, fileName_IN):
        self.siteFileName = fileName_IN
        pass
    
    def setSightingFile(self, sightingFile):
        funcName = "Fix.setSightingFile"

        if isinstance(sightingFile, str) and sightingFile[-4:] == ".xml":
            #check that the sightingFile exists
            if (os.path.isfile(sightingFile) == True):
                self.setSiteFileName(sightingFile)
                #add line to log file associated with the Fix instance
                stringToAdd = "LOG: Start of sighting file: " + sightingFile + "\n"
                logFile = open(self.getLogFileName(), "a")
                logFile.write(stringToAdd)
                #close the log file
                logFile.close()
            else:
                raise ValueError(funcName + ":  sighting file does not exist in current directory")
        else:
            raise ValueError(funcName + ":  invalid input")
        return sightingFile
    
    def celsius(self, farIN):
        #(Fahrenheit - 32) * 5.0/9.0
        result = (float(farIN) - 32.0) * 5.0 / 9.0
        return result
        
    
    def calcAdjustedAlt(self, heightIN=None, pressureIN=None, tempIN=None, altitudeIN=None, horizonIN= None):
        funcName = "Fix.calcAdjustedAlt"
        result = ""
        #proceed only if all of the input is not null
        if (heightIN <> None and pressureIN <> None and tempIN <> None and altitudeIN <> None and horizonIN <> None):
            dip = 0.0
            observedAltAngle = Angle.Angle()
            observedAltDegree = observedAltAngle.setDegreesAndMinutes(altitudeIN)
            # if horizon is natural: dip = ( -0.97 * sqrt( height ) ) / 60
            # else: dip = 0
            if horizonIN == "natural":
                dip = (-0.97 * math.sqrt(heightIN)) / 60
            else:
                dip = 0.0
            
            
            # refraction = ( -0.00452 * pressure ) / ( 273 + celsius( temperature ) ) / tangent( observedAltitude )
            refraction = (-0.00452 * pressureIN) / (273 + self.celsius(tempIN)) / observedAltAngle.tangent()
            
            
            # note: observedAltitude is an Angle, so make found dip and refraction Angle objects
            
            # add all the Angle objects to get adjustedAltitude
            # adjustedAltitude = observedAltitude + dip + refraction
            dipAngle = Angle.Angle()
            dipDegree = dipAngle.setDegrees(dip)
            refractionAngle = Angle.Angle()
            refractionDegree = refractionAngle.setDegrees(refraction)
            
            part01 = observedAltAngle.add(dipAngle)
            #observedAltAngle now has a new value (old value + dip value)
            part02 = observedAltAngle.add(refractionAngle)
            #observedAltAngle now has a new value (old value + refraction value)
            result = observedAltAngle.getString()
            
        #else, raise value error
        else:
            raise ValueError(funcName + ":  has an invalid Null input")
        return result
    
    def getSightings(self):
        
        
        
        pass
    
    