'''
Created on October 12, 2016

@author: Kristi Reckart
'''

#LOC = 191 (10/24/16)
#LOC = 292 (12/1/16)
#LOC = 239 (12/4/16)
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
import Navigation.prod.Validate as Validate
import Navigation.prod.Calculate as Calculate


class Fix():
    def __init__(self, logFile=None):
        funcName = "Fix.__init__"
        #initialize logFile if logFile == None
        if (logFile == None) :
            logFile = "log.txt"
        if (isinstance(logFile, str) and len(logFile) > 0):
            #set Fix attribute: logFileName
            self.logFileName = logFile
            #set Fix attribute: ariesFileName, siteFileName, and starFileName
            self. ariesFileName = None
            self.siteFileName = None
            self.starFileName = None
            
            #initialize sightings error found variable
            self.sightingsErrors = 0
            
            #initialize the SightingsList, AriesList, and StarList
            self.sightingsList = SightingsList.SightingsList()
            self.ariesList = AriesList.AriesList()
            self.starsList = StarsList.StarsList()
            
            #initialize assumedLat and assumedLong
            self.assumedLat = None
            self.assumedLong = None
            
            #initialize the Validate class as a variable for this instance of Fix
            #the Validate class has all the functions that check that the data is in correct format;
            # the functions will return True if the entered value is valid, otherwise False
            self.validCheck = Validate.Validate()
            #initialize the Calculate class as a variable for this instance of Fix
            # the Calculate class has all the functions that make calculations for the Fix class
            self.calc = Calculate.Calculate()
            
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
    
    def getAriesFileName(self):
        return self.ariesFileName
    
    def getStarFileName(self):
        return self.starFileName
    
    #note the below 3 function assume that the fileName_IN was checked for .xml and is a string
    def setSiteFileName(self, fileName_IN):
        self.siteFileName = fileName_IN
#LOC above = 50
        pass

    def setAriesFileName(self, fileName_IN):
        self.ariesFileName = fileName_IN
        pass
    
    def setStarFileName(self, fileName_IN):
        self.starFileName = fileName_IN
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
    
    def getSightings(self, assumedLatIN=None, assumedLongIN=None):
        result = ("0d0.0", "0d0.0")
        funcName = "Fix.getSightings"
#LOC above = 100
        
        if assumedLatIN == None:
            assumedLatIN = "0d0.0"
        if assumedLongIN == None:
            assumedLongIN = "0d0.0"
            
        #check if assumedLatIN is valid
        flag1 = self.validCheck.validAssumedLat(assumedLatIN)
        flag2 = self.validCheck.validAssumedLong(assumedLongIN)
        
        if (flag1 == False or flag2 == False):
            raise ValueError(funcName + ":  invalid latitude or longitude input")
        #set Fix's assumedLat and assumedLong
        self.assumedLat = assumedLatIN
        #print "assumedLat: " + str(self.assumedLat)
        self.assumedLong = assumedLongIN
        #print "assumedLong: " + str(self.assumedLong)
        
        #if aries, sighting, and star files have been set -> proceed; else, raise error 
        
        if self.getAriesFileName() <> None and self.getSiteFileName() <> None and self.getStarFileName() <> None:
            #get the data from the sighting file and write each sighting to log file
            flag = self.getData()

        else:
            raise ValueError(funcName + ":  site file is not set or invalid")
        
        
        #write last lines to log file associated with the Fix object
        logFile = open(self.logFileName, "a")
        errorString = "Sighting errors:\t" + str(self.sightingsErrors) + "\n"
        logFile.write(errorString)
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
                #print "body: " + currentSighting.getBody()
                currentSighting.setDate(aSighting.getElementsByTagName('date')[0].firstChild.data)
                currentSighting.setTime(aSighting.getElementsByTagName('time')[0].firstChild.data)
                currentSighting.setObservation(aSighting.getElementsByTagName('observation')[0].firstChild.data)
                #print "nonexist: " + aSighting.getElementsByTagName('nonexist')[0].firstChild.data
            except:
                result = False
            
            #check that the observation has the correct value
            if self.validCheck.validObservation(currentSighting.getObservation()) == False:
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
                #print "height: " + thisHeight
                #below explains why need a thisCanBeAFloat and thisCanBeAnInt
                #https://www.peterbe.com/plog/interesting-casting-in-python
                if self.validCheck.thisCanBeAFloat(thisHeight) == True or self.validCheck.thisCanBeAnInt(thisHeight) == True:
                    #check for int first!!!
                    if self.validCheck.thisCanBeAnInt(thisHeight) == True:
                        currentSighting.setHeight(int(thisHeight))
#LOC above = 150

                    elif self.validCheck.thisCanBeAFloat(thisHeight) == True:
                        currentSighting.setHeight(float(thisHeight))

                else:
                    #do not set the height
                    result = False
                    errorString = "could not set Height\n"

            else:
                #no height, so set default
                currentSighting.setHeight(0.0)
                #print "no height found"
            if len(aSighting.getElementsByTagName('pressure')) > 0:
                thisPressure = aSighting.getElementsByTagName('pressure')[0].firstChild.data
                if self.validCheck.thisCanBeAnInt(thisPressure) == True:
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
                if self.validCheck.thisCanBeAnInt(thisTemp) == True:                
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
                if self.validCheck.validHeight(currentSighting.getHeight()) == False:
                    result = False
                    errorString = errorString + "invalid Height\n"
            if currentSighting.getTemp() <> None:
                if self.validCheck.validTemp(currentSighting.getTemp()) == False:
                    result = False
                    errorString = errorString + "invalid Temp\n"
            if currentSighting.getPressure() <> None:
                if self.validCheck.validPressure(currentSighting.getPressure()) == False:
                    result = False
                    errorString = errorString + "invalid Pressure\n"
            if currentSighting.getHorizon() <> None:
                if self.validCheck.validHorizon(currentSighting.getHorizon()) == False:
                    result = False
                    errorString = errorString + "invalid Horizon\n"
            
            #if have time go back and trim off extra white spaces
            
            #add currentSighting to the SightingsList object
            
            #if result = False, there was a sighting error; increment sightingsErrors by 1
            if (result == False):
                self.sightingsErrors = self.sightingsErrors + 1 #increment the sightingsErrors by 1
            
            #else there was no sighting error, so write valid log entry
            else:
                #if have time come back and do the above and sort the list by date, body, etc
                # for now, just write sighting to log file
                stringToWrite = ("LOG: " + str(datetime.today()) + " " + str(currentSighting.getBody()) + "\t" + str(currentSighting.getDate()) + "\t"
                    + str(currentSighting.getTime()) + "\t" 
                    + str(self.calcAdjustedAlt(currentSighting.getHeight(), currentSighting.getPressure(), currentSighting.getTemp(),
                                            currentSighting.getObservation(), currentSighting.getHorizon())))
                #print "stringToWrite: " + stringToWrite
                logFile.write(stringToWrite + "\n")
            
        #done looping through site file
        logFile.close()
#LOC above = 200
        #print "error string: " + errorString + "\n"
        return result
    
    def setAriesFile(self, ariesFile=None):
        funcName = "Fix.setAriesFile"
        result = None
        if self.validCheck.checkValidTextFileName(ariesFile) == True:
            
            #check that the file exists, if not, raise error; else, set result
            if os.path.isfile(ariesFile) == False:
                raise ValueError(funcName + ":  aries file does not exist")
            else:
                result = str(os.path.abspath(ariesFile))

            #if get to here, the file exists, so set the ariesFileName value
            self.setAriesFileName(ariesFile)
            #create string to write to log
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
    
    def setStarFile(self, starFile=None):
        funcName = "Fix.setStarFile"
        result = None
        if self.validCheck.checkValidTextFileName(starFile) == True:
            
            #check that the file exists, if not, raise error; else, set result
            if os.path.isfile(starFile) == False:
                raise ValueError(funcName + ":  star file does not exist")
            else:
                result = str(os.path.abspath(starFile))
                
            #if get to here, the file exists, so set the ariesFileName value
            self.setStarFileName(starFile)
            #create string to write to log
            lineToWrite = "LOG: " + str(datetime.today()) + " Star file:\t" + result + "\n"
            try:
                logFile = open(self.logFileName, "a")
                logFile.write(lineToWrite)
                logFile.close()
            except:
                raise ValueError(funcName + ":  cannot open and write to the log file for some reason")
        else:
            raise ValueError(funcName + ":  invalid input")
        
        return result
        
#LOC above = 239 (12/4/16)