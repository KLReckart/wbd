from datetime import datetime
import os
import math
from xml.dom import minidom
from __builtin__ import str

import Navigation.prod.Sighting as Sighting
import Navigation.prod.SightingsList as SightingsList
import Navigation.prod.AriesList as AriesList
import Navigation.prod.StarsList as StarsList
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
            
            #initialize the SightingsList, AriesList, and StarList
            
            
            
            #create or append the file with the desired name
            try:
                file01 = open(logFile, "a")
            except:
                #if file was not created, raise exception
                raise ValueError(funcName + ":  failed to create or append file")
            #append the desired line to the beginning of the file
            string01 = "LOG: " + str(datetime.today()) + " Log file:\t" + os.path.abspath(logFile) + "\n"
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
    
    def setSightingFile(self, sightingFile=None):
        funcName = "Fix.setSightingFile"
        if sightingFile == None:
            raise ValueError(funcName + ":  missing sightingFile")
        
        if isinstance(sightingFile, str) and sightingFile[-4:] == ".xml":
            #check that the sightingFile exists
            if (os.path.isfile(sightingFile) == True):
                self.setSiteFileName(sightingFile)
                #add line to log file associated with the Fix instance
                stringToAdd = "LOG: "+ str(datetime.today()) +" Sighting file:\t" + os.path.abspath(sightingFile) + "\n"
                logFile = open(self.getLogFileName(), "a")
                logFile.write(stringToAdd)
                #close the log file
                logFile.close()
            else:
                raise ValueError(funcName + ":  sighting file does not exist in current directory")
        else:
            raise ValueError(funcName + ":  invalid input")
        result = str(os.path.abspath(sightingFile))
        return result
    
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
        result = ("0d0.0", "0d0.0")
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
        errorString = "Sight File: " + self.siteFileName + "\n"
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
            
            #check that the observation has the correct value
            if self.validObservation(currentSighting.getObservation()) == False:
                result = False
                errorString = errorString + "invalidObservation\n"
            
            #get possible data,
            # if data does not exist, set default values
            if len(aSighting.getElementsByTagName('horizon')) > 0:
                thisHorizon = aSighting.getElementsByTagName('horizon')[0].firstChild.data
                #set the horizon to all lower case letters
                currentSighting.setHorizon(thisHorizon.lower())
            else:
                currentSighting.setHorizon("natural")
            # b/c the next few values need to be converted to int or floats, there is more code to ensure this before setting Sighting object values
            if len(aSighting.getElementsByTagName('height')) > 0:
                thisHeight = aSighting.getElementsByTagName('height')[0].firstChild.data
                #below explains why need a thisCanBeAFloat and thisCanBeAnInt
                #https://www.peterbe.com/plog/interesting-casting-in-python
                if self.thisCanBeAFloat(thisHeight) == True or self.thisCanBeAnInt(thisHeight) == True:
                    #check for int first!!!
                    if self.thisCanBeAnInt(thisHeight) == True:
                        currentSighting.setHeight(int(thisHeight))
                    elif self.thisCanBeAFloat(thisHeight) == True:
                        currentSighting.setHeight(float(thisHeight))
                    else:
                        #do not set the height
                        result = False
                        errorString = "could not set Height\n"
            else:
                #no height, so set default
                currentSighting.setHeight(0.0)
            if len(aSighting.getElementsByTagName('pressure')) > 0:
                thisPressure = aSighting.getElementsByTagName('pressure')[0].firstChild.data
                if self.thisCanBeAnInt(thisPressure) == True:
                    currentSighting.setPressure(int(thisPressure))
                else:
                    #do not set pressure
                    result = False
                    errorString = "could not set Pressure\n"
            else:
                #no pressure, so set default
                currentSighting.setPressure(1010)
            if len(aSighting.getElementsByTagName('temperature')) > 0:
                thisTemp = aSighting.getElementsByTagName('temperature')[0].firstChild.data
                if self.thisCanBeAnInt(thisTemp) == True:                
                    currentSighting.setTemp(int(thisTemp))
                else:
                    result = False
                    errorString = "could not set Temp\n"
            else:
                #no temp, so set default
                currentSighting.setTemp(72)
                
            #check that the possible values that have been set (AKA: not None)
            # check that these values are correct have the correct values
            if currentSighting.getHeight() <> None:
                if self.validHeight(currentSighting.getHeight()) == False:
                    result = False
                    errorString = errorString + "invalid Height\n"
            if currentSighting.getTemp() <> None:
                if self.validTemp(currentSighting.getTemp()) == False:
                    result = False
                    errorString = errorString + "invalid Temp\n"
            if currentSighting.getPressure() <> None:
                if self.validPressure(currentSighting.getPressure()) == False:
                    result = False
                    errorString = errorString + "invalid Pressure\n"
            if currentSighting.getHorizon() <> None:
                if self.validHorizon(currentSighting.getHorizon()) == False:
                    result = False
                    errorString = errorString + "invalid Horizon\n"
            
            
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
        print "getData errorString:\n" + errorString
        return result
    
    #returns True if the obersvationIN is a valid observation,
    # else, returns False        
    def validObservation(self, observationIN):
        result = True
        #make the observationIN into an Angle object, this will ensure the correct value
        try:
            tempAngle = Angle.Angle()
            returnedValue = tempAngle.setDegreesAndMinutes(observationIN)
        except:
            result = False
        return result
    
    #returns True if the heightIN is a valid height,
    # else, returns False
    def validHeight(self, heightIN):
        result = False
        #check that the input is a numeric that is greater than or equal to zero
        try:
            if isinstance(heightIN, int) == True or isinstance(heightIN, float) == True:
                # then the value is a numeric
                # let's check >= zero
                if heightIN >= 0:
                    result = True
                else:
                    result = False
            else:
                result = False
        except:
            result = False
        
        return result
    
    #returns True if the tempIN is a valid temperature,
    # else, returns False
    def validTemp(self, tempIN):
        result = False
        #check that the input is an integer with a value of [-20, 120]
        try:
            if isinstance(tempIN, int) == True:
                # then the value is an int -> let's check value is [-20, 120]
                if tempIN >= -20 and tempIN <= 120:
                    result = True
                else:
                    result = False
            else:
                result = False
        except:
            result = False
        return result
    
    #returns True if the pressureIN is a valid pressure
    # else, returns False
    def validPressure(self, pressureIN):
        result = False
        #check that the input is an integer with a value of [100, 1100]
        try:
            if isinstance(pressureIN, int) == True:
                # then the value is an int -> let's check value is [100, 1100]
                if pressureIN >= 100 and pressureIN <= 1100:
                    result = True
                else:
                    result = False
            else:
                result = False
        except:
            result = False
        return result
    
    #returns True if the horizionIN is a valid horizon
    # else, return False
    def validHorizon(self, horizionIN):
        result = False
        #check that the input is a string with one of two values: 'natural' or 'artificial'
        try:

            if horizionIN == "natural" or horizionIN == "artificial":
                result = True
            else:
                result = False

        except:
            result = False
        return result
        
    #takes in a value and tries to cast the value as an int,
    # if this is possible, the function returns True
    # else the function returns False
    #below explains why need a try
    #https://www.peterbe.com/plog/interesting-casting-in-python
    def thisCanBeAnInt(self, valueIN):
        result = True
        try:
            temp = int(valueIN)
        except:
            result = False
                    
        return result
    
    #takes in a value and tries to cast the value as a float,
    # if this is possible, the function returns True
    # else the function returns False
    def thisCanBeAFloat(self, valueIN):
        result = True
        try:
            temp = float(valueIN)
        except:
            result = False
        
        return result
    
    def checkValidTextFileName(self, stringIN=None):
        result = False
        if stringIN <> None and isinstance(stringIN, str):
            if stringIN[-4:] == ".txt" and len(stringIN) > 4:
                result = True
        return result
    
    def setAriesFile(self, ariesFile=None):
        funcName = "Fix.setAriesFile"
        if self.checkValidTextFileName(ariesFile) == True:
            try:
                result = str(os.path.abspath(ariesFile))
            except:
                raise ValueError(funcName + ":  aries file does not exist")
            lineToWrite = "LOG: " + str(datetime.today()) + " Aries file:\t" + result + "\n"
            try:
                logFile = open(self.logFileName, "a")
                logFile.write(lineToWrite)
                logFile.close()
            except:
                raise ValueError(funcName + ":  cannot open and write to the log file for some reason")
        else:
            raise ValueError(funcName + ":  invalid input")
        
        return result
    
    