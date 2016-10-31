'''
Created on 10/10/16
@author: Kristi Reckart

Purpose: tests the new changes to the Fix class from CA02 to CA03 AND tests the new additions to the Fix class from CA02 to CA03

'''

import unittest
import uuid
import os
import Navigation.prod.Fix as Fix



class Fix_CA03_Test(unittest.TestCase):
    
    def setUp(self):
        self.className = "Fix."
        self.logStartString = "Log file:\t"
        self.logSightingString = "Sighting file:\t"
        self.logAriesString = "Aries file:\t"
        
        # set default log file name
        self.DEFAULT_LOG_FILE = "log.txt"
        
        # generate random log file name
        self.RANDOM_LOG_FILE = "log" + str(uuid.uuid4())[-12:] + ".txt"


# 100 Constructor
#    Analysis:
#        a line should be written to the log text file with the following format:
#             "Log file:\t" + the absolute filepath of the log file
    
#   Happy path
    def test100_010CreateWithNoneInput(self):
        fix01 = Fix.Fix()
        #check that the object was created
        self.assertIsInstance(fix01, Fix.Fix, "fix01 was not created")
        #check that the file was created
        file01Name = "log.txt"
        self.assertTrue(os.path.isfile(file01Name), "file01 does not exist")
        #if file was created, check that the first line is correct
        expectedBeg = "LOG: "
        expectedEnd = "Log file:\t" + "C:\College\GitRepository\SoftwareProcess\SoftwareProcess\Navigation\\" + "test\log.txt\n"
        if (os.path.isfile(file01Name) == True):
            file01 = open(file01Name, "r")
            lineInFile = file01.readline()
            #print(lineInFile)
            file01.close()
            self.assertEquals(lineInFile[:5], expectedBeg, "file01 missing 'LOG: '")
            self.assertEquals(lineInFile[-91:], expectedEnd, lineInFile[-91:] + " != " + expectedEnd)
            
             
    def test100_011CreateWithInput(self):
        fix02 = Fix.Fix("log02.txt")
        #check that the object was created
        self.assertIsInstance(fix02, Fix.Fix, "fix02 was not created")
        #check that the file was created
        file02Name = "log02.txt"
        self.assertTrue(os.path.isfile(file02Name), "file02 does not exist")
        #if file was created, check that the first line is correct
        expectedBeg = "LOG: "
        expectedEnd = "Log file:\t" + "C:\College\GitRepository\SoftwareProcess\SoftwareProcess\Navigation\\test\log02.txt\n"
        if (os.path.isfile(file02Name) == True):
            file02 = open(file02Name, "r")
            lineInFile = file02.readline()
            file02.close()
            #print(lineInFile)
            self.assertEquals(lineInFile[:5], expectedBeg, "file02 missing 'LOG: '")
            self.assertEquals(lineInFile[-93:], expectedEnd, lineInFile[-93:] + " != " + expectedEnd)
            
             
    def test100_012AppendToEExistingFile(self):
        fix03 = Fix.Fix()
        #get the 2nd line of the file, check that line
        file03Name = fix03.getLogFileName()
        expectedBeg = "LOG: "
        expectedEnd = "Log file:\t" + "C:\College\GitRepository\SoftwareProcess\SoftwareProcess\Navigation\\test\log.txt\n"
        file03 = open(file03Name, "r")
        lineInFile = file03.readline()
        lineInFile02 = file03.readline()
        #print(lineInFile02)
        self.assertEquals(lineInFile02[:5], expectedBeg, "file03 missing 'LOG: '")
        self.assertEquals(lineInFile[-91:], expectedEnd, lineInFile[-91:] + " != " + expectedEnd)
        file03.close()
 
    def test100_040_ShouldConstructFixWithExistingFile(self):
        theFix = Fix.Fix(self.RANDOM_LOG_FILE)
        theFix = Fix.Fix(self.RANDOM_LOG_FILE)
        pathHere = os.path.abspath(self.RANDOM_LOG_FILE)
        #print "random file: " + self.RANDOM_LOG_FILE
        try:
            theLogFile = open(self.RANDOM_LOG_FILE, 'r')
            numberOfExpectedEntries = 2
            for _ in range(numberOfExpectedEntries):
                entry = theLogFile.readline()
                #print "entry: " + entry
                self.assertNotEquals(-1, entry.find(self.logStartString + pathHere + "\n"), 
                                     "Minor:  first line of log is incorrect")
            theLogFile.close()
        except IOError:
            self.fail()
        self.assertIsInstance(theFix, Fix.Fix, 
                              "Major:  log file failed to create")
        self.cleanup()  
 
#   Sad path
    def test100_110FailInitialEmptyString(self):
        expectedDia = "Fix.__init__:  invalid input"
        with self.assertRaises(ValueError) as context:
            fix04 = Fix.Fix("")
        self.assertEquals(expectedDia, context.exception.args[0][0:len(expectedDia)], "error for empty string input not raised")
    def test100_111FailInitialNumberInput(self):
        expectedDia = "Fix.__init__:  invalid input"
        with self.assertRaises(ValueError) as context:
            fix05 = Fix.Fix(55)
        self.assertEquals(expectedDia, context.exception.args[0][0:len(expectedDia)], "error for number input not raised")
        
        
        
# 200 setSightingFile

    def test200_010_ShouldConstructWithKeywordParm(self):
        'Minor:  '
        theFix = Fix.Fix(logFile=self.RANDOM_LOG_FILE)
        try:
            result = theFix.setSightingFile("CA02_200_ValidStarSightingFile.xml")
            self.assertEquals(result, str(os.path.abspath("CA02_200_ValidStarSightingFile.xml")))
        except:
            self.fail("Minor: incorrect keyword specified in setSighting parm")
        self.cleanup()   

    def test200_020_ShouldSetValidSightingFileAndReturnsPath(self):
        theFix = Fix.Fix()
        result = theFix.setSightingFile("CA02_200_ValidStarSightingFile.xml")

        theLogFile = open(self.DEFAULT_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        self.assertNotEquals(-1, logFileContents[-1].find(self.logSightingString + os.path.abspath("CA02_200_ValidStarSightingFile.xml") + "\n"), 
                             "Minor:  first setSighting logged entry is incorrect")
        expected = str(os.path.abspath("CA02_200_ValidStarSightingFile.xml"))
        self.assertEquals(result, expected, result + " != " + expected)
        theLogFile.close()
        
    def test200_910_ShouldRaiseExceptionOnNonStringFileName(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile(55)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for non-string sighting file name")  
        
    def test200_920_ShouldRaiseExceptionOnFileLengthError(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile(".xml")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for .GE. 1 sighting file name") 
        
    def test200_930_ShouldRaiseExceptionOnNonXmlFile1(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("sighting.")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for non.xml sighting file extension")
        
    def test200_940_ShouldRaiseExceptionOnNonXmlFile2(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("xml")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to delineate between sighting file name and extension") 
        
    def test200_950_SholdRaiseExceptionOnMissingFileName(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for missing sighting file")       
        
           
    def test200_960_SholdRaiseExceptionOnMissingFile(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile(self.RANDOM_LOG_FILE+".xml")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for missing sighting file") 
    
        
        
# 300 setAriesFile

    def test300_010_ShouldConstructParam(self):
        thisFix = Fix.Fix()
        result = thisFix.setAriesFile("aries.txt")
        expected = str(os.path.abspath("aries.txt"))
        self.assertEquals(result, expected, result + " != " + expected)
        
    def test300_020_LineWrittenToLog(self):
        logFile = self.RANDOM_LOG_FILE
        thisFix = Fix.Fix(logFile)
        temp = thisFix.setAriesFile("aries.txt")
        expectedLine = os.path.abspath("aries.txt") + "\n"

        print "random file: " + logFile
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        sightingCount = 0
        for logEntryNumber in range(0, len(logFileContents)):
            if(logFileContents[logEntryNumber].find(expectedLine) > -1):
                sightingCount += 1
                #for target in targetStringList:
                self.assertNotEquals(-1, logFileContents[logEntryNumber].find(expectedLine), 
                                         "Major:  Log entry is not correct for getSightings")
        self.assertEquals(1, sightingCount)
        self.cleanup()  
        
        self.assertIsInstance(thisFix, Fix.Fix, 
                              "Major:  log file failed to create")
        self.cleanup()  
        
    def test300_910_FailWithNoExt(self):
        logFile = self.RANDOM_LOG_FILE
        thisFix = Fix.Fix(logFile)
        ariesFile = "aries"
        expectedDiag = "Fix.setAriesFile:  invalid input"
        with self.assertRaises(ValueError) as context:
            temp = thisFix.setAriesFile(ariesFile)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)], 
                          expectedDiag + " != " + context.exception.args[0][0:len(expectedDiag)])  
        
    def test300_920_FailWithNoFileName(self):
        logFile = self.RANDOM_LOG_FILE
        thisFix = Fix.Fix(logFile)
        ariesFile = ".txt"
        expectedDiag = "Fix.setAriesFile:  invalid input"
        with self.assertRaises(ValueError) as context:
            temp = thisFix.setAriesFile(ariesFile)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)], 
                          expectedDiag + " != " + context.exception.args[0][0:len(expectedDiag)])  
        
    def test300_920_FailWithNonStringInput(self):
        logFile = self.RANDOM_LOG_FILE
        thisFix = Fix.Fix(logFile)
        ariesFile = 55
        expectedDiag = "Fix.setAriesFile:  invalid input"
        with self.assertRaises(ValueError) as context:
            temp = thisFix.setAriesFile(ariesFile)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)], 
                          expectedDiag + " != " + context.exception.args[0][0:len(expectedDiag)]) 
        
            
        
    
#  helper methods
    def indexInList(self, target, searchList):
        for index in range(len(searchList)):
            if(target in searchList[index]):
                return index
        return -1
    
    def cleanup(self):
        if(os.path.isfile(self.RANDOM_LOG_FILE)):
            os.remove(self.RANDOM_LOG_FILE) 