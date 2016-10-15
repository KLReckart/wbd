from datetime import datetime
import os
from __builtin__ import str

class Fix():
    def __init__(self, logFile=None):
        funcName = "Fix.__init__"
        #initialize logFile if logFile == None
        if (logFile == None) :
            logFile = "log.txt"
        if (isinstance(logFile, str) and len(logFile) > 0):
            #set Fix attribute: logFileName
            self.logFileName = logFile
            #create or append the file with the desired name
            file01 = open(logFile, "a")
            #append the desired line to the beginning of the file
            string01 = "LOG: " + str(datetime.today()) + " Start of log\n"
            file01.write(string01)
            #close file
            file01.close()
            print(str(os.getcwd()))
        else:
            raise ValueError(funcName + ":  invalid input")
        pass
    
    def getLogFileName(self):
        return self.logFileName