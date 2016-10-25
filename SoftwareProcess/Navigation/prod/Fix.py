#LOC = 191 (10/24/16)
from datetime import datetime
import os
import math
from xml.dom import minidom
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

            #print(str(os.getcwd()))
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
                stringToAdd = "LOG: "+ str(datetime.today()) +" Start of sighting file: " + sightingFile + "\n"
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
        #else:
            #raise ValueError(funcName + ":  has an invalid or Null input")
        return result
    
    def getSightings(self):
        result = (0, 0)
        funcName = "Fix.getSightings"
        
        #if getData() = False, raise Value Error (invalid data from sighting file)
        if self.siteFileName <> None and os.path.isfile(self.siteFileName):
            flag = self.getData()
            if flag == False:
                raise ValueError(funcName + ":  invalid xml data")
        else:
            raise ValueError(funcName + ":  site file is not set or invalid")
        
        
        #write last line to log file associated with the Fix object
        logFile = open(self.logFileName, "a")
        endString = "LOG: " + str(datetime.today()) + " End of sighting file: " + str(self.siteFileName) + "\n"
        logFile.write(endString)
        logFile.close()
        
        return result
    
    def getData(self):
        
        #returns True if all data was correct and has mandatory data
        result = True
        logFile = open(self.logFileName, "a")
        #parse the xml file
        xmlDocument = minidom.parse(self.siteFileName)
        #get the sightings
        thisFix = xmlDocument.documentElement
        sightings = thisFix.getElementsByTagName("sighting")
        #get data for each sighting
        for aSighting in sightings:
            currentSighting = Sighting.Sighting()
            
            # body, date, time, and observation are mandatory
            # if one of these does not exist, raise an exception
            
            #get mandatory data
            try:
                currentSighting.setBody(aSighting.getElementsByTagName('body')[0].firstChild.data) 
                print "body: " + currentSighting.getBody()
                currentSighting.setDate(aSighting.getElementsByTagName('date')[0].firstChild.data)
                currentSighting.setTime(aSighting.getElementsByTagName('time')[0].firstChild.data)
                currentSighting.setObservation(aSighting.getElementsByTagName('observation')[0].firstChild.data)
                #print "nonexist: " + aSighting.getElementsByTagName('nonexist')[0].firstChild.data
            except:
                result = False
            
            #get possible data
            if len(aSighting.getElementsByTagName('height')) > 0:
                currentSighting.setHeight(float(aSighting.getElementsByTagName('height')[0].firstChild.data))
                #print "height: " + currentSighting.getHeight()
            #else:
                #print "no height"
            if len(aSighting.getElementsByTagName('horizon')) > 0:
                currentSighting.setHorizon(aSighting.getElementsByTagName('horizon')[0].firstChild.data)
            if len(aSighting.getElementsByTagName('pressure')) > 0:
                currentSighting.setPressure(float(aSighting.getElementsByTagName('pressure')[0].firstChild.data))
            if len(aSighting.getElementsByTagName('temperature')) > 0:
                currentSighting.setTemp(float(aSighting.getElementsByTagName('temperature')[0].firstChild.data))
            
            #if have time go back and check for correct values of data
            #if have time go back and trim off extra white spaces
            
            
            #add currentSighting to the SightingsList object
            
            #if have time come back and do the above and sort the list by date, body, etc
            # for now, just write sighting to log file
            stringToWrite = ("LOG: " + str(datetime.today()) + " " + str(currentSighting.getBody()) + "\t" + str(currentSighting.getDate()) + "\t"
                + str(currentSighting.getTime()) + "\t" 
                + str(self.calcAdjustedAlt(currentSighting.getHeight(), currentSighting.getPressure(), currentSighting.getTemp(),
                                            currentSighting.getObservation(), currentSighting.getHorizon())))
            print "stringToWrite: " + stringToWrite
            logFile.write(stringToWrite + "\n")
            
        #done looping through site file
        logFile.close()
        return result
        
        