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
        
        
        

    
        
        

    
#  helper methods
    def indexInList(self, target, searchList):
        for index in range(len(searchList)):
            if(target in searchList[index]):
                return index
        return -1
    
    def cleanup(self):
        if(os.path.isfile(self.RANDOM_LOG_FILE)):
            os.remove(self.RANDOM_LOG_FILE) 