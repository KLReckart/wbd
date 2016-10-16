from datetime import datetime
import os
from __builtin__ import str
import Navigation.prod.Sighting as Sighting
import Navigation.prod.SightingsList as SightingsList

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