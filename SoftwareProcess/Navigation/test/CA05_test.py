'''
Created on Dec 2, 2016

@author: Kristi
'''

import unittest
import uuid
import os
import Navigation.prod.Fix as F

class FixTest_CA05(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.className = "Fix."
        cls.logStartString = "Log file:"
        cls.starSightingString = "Sighting file:"
        cls.starSightingErrorString = "Sighting errors:"
        cls.ariesFileString = "Aries file:"
        cls.starFileString = "Star file:"
        cls.DEFAULT_LOG_FILE = "log.txt"
        cls.ariesFileName = "CA03_Valid_Aries.txt"
        cls.starFileName = "CA03_Valid_Stars.txt"
        cls.sightFileName = "sightFile.xml"
        
#----------          
    def setUp(self):
        if(os.path.isfile(self.DEFAULT_LOG_FILE)):
            os.remove(self.DEFAULT_LOG_FILE) 
        # generate random log file name
        self.RANDOM_LOG_FILE = "log" + str(uuid.uuid4())[-12:] + ".txt"
        self.deleteNamedLogFlag = False
    
    def tearDown(self):
        if(self.deleteNamedLogFlag):
            try:
                if(os.path.isfile(self.RANDOM_LOG_FILE)):
                    os.remove(self.RANDOM_LOG_FILE)  
            except:
                pass
    
    def cleanup(self):
        if(os.path.isfile("log.txt")):
            os.remove("log.txt") 
#---------- 

# Fix.getSightings
# 100 getSightings
#
# *** HAPPY PATH TESTS

    def test100_01testNormalOutput(self):
        #create Fix object
        thisFix = F.Fix()
        
        #set aries, sighting, and star files
        ariesFile = self.ariesFileName
        sightFile = self.sightFileName
        starFile = self.starFileName
        
        file01 = thisFix.setSightingFile(sightFile)
        file02 = thisFix.setAriesFile(ariesFile)
        file03 = thisFix.setStarFile(starFile)
        
        #test return
        result = thisFix.getSightings("N27d59.5", "85d33.4")
        expected = ("N29d6.8", "82d52.9")
        self.assertEquals(result, expected, str(result) + " != " + str(expected))
        
        # I have decide to come back to this test last, after performing TDD on all other tests since the other tests are
        #  less complex
        self.cleanup()
        pass
        
    def test100_02testDefaultLongitudeInput(self):
        #create Fix object
        thisFix02 = F.Fix()
        
        #set aries, sighting, and star files
        ariesFile = self.ariesFileName
        sightFile = self.sightFileName
        starFile = self.starFileName
        
        file01 = thisFix02.setSightingFile(sightFile)
        file02 = thisFix02.setAriesFile(ariesFile)
        file03 = thisFix02.setStarFile(starFile)
        
        #test return
        getResult = thisFix02.getSightings("N27d59.5")
        result = thisFix02.assumedLong
        expected = ("0d0.0")
        self.assertEquals(result, expected, str(result) + " != " + str(expected))
        
        self.cleanup()
        pass
        
    def test100_03testDefaultLatitudeInput(self):
        #create Fix object
        thisFix = F.Fix()
        
        #set aries, sighting, and star files
        
        ariesFile = self.ariesFileName
        sightFile = self.sightFileName
        starFile = self.starFileName
        
        file01 = thisFix.setSightingFile(sightFile)
        file02 = thisFix.setAriesFile(ariesFile)
        file03 = thisFix.setStarFile(starFile)
        
        #test return
        getResult = thisFix.getSightings(assumedLongIN="85d33.4")
        result = thisFix.assumedLat
        expected = ("0d0.0")
        self.assertEquals(result, expected, str(result) + " != " + str(expected))
        
        #self.cleanup()
        pass
    
    def test100_04testDefaultInputs(self):
        #create Fix object
        thisFix = F.Fix()
        
        #set aries, sighting, and star files
        
        ariesFile = self.ariesFileName
        sightFile = self.sightFileName
        starFile = self.starFileName
        
        file01 = thisFix.setSightingFile(sightFile)
        file02 = thisFix.setAriesFile(ariesFile)
        file03 = thisFix.setStarFile(starFile)
        
        #test return
        getResult = thisFix.getSightings()
        result01 = thisFix.assumedLat
        result02 = thisFix.assumedLong
        expected = ("0d0.0")
        self.assertEquals(result01, expected, str(result01) + " != " + str(expected))
        self.assertEquals(result02, expected, str(result01) + " != " + str(expected))
        
        pass
    
    def test100_05testLogData(self):
        #create Fix object
        thisFix = F.Fix()
        
        #set aries, sighting, and star files
        ariesFile = self.ariesFileName
        sightFile = self.sightFileName
        starFile = self.starFileName
        file01 = thisFix.setSightingFile(sightFile)
        file02 = thisFix.setAriesFile(ariesFile)
        file03 = thisFix.setStarFile(starFile)
        
        #call getSighitngs
        assumedLat = "N27d59.5"
        assumedLong = "85d33.4"
        getResult = thisFix.getSightings(assumedLat, assumedLong)
        
        #check that the file was created
        file01Name = "log.txt"
        self.assertTrue(os.path.isfile(file01Name), "file01 does not exist")
        #if file was created, check that the first line is correct
        
        
        #open the log file for reading
        logFile = open("log.txt", "r")
        #get the 5th and 7th lines as a string
        line5 = ""
        line7 = ""
        
        position = logFile.seek(0, 0)
        currentLine = 1
        for aLine in logFile:
            print (aLine + "\n")
            if (currentLine == 5):
                line5 = aLine
            #print "line#: " + str(currentLine)
            #print "line2: " + line2
            if (currentLine == 7):
                line7 = aLine
            currentLine = currentLine + 1
        
        #close file
        logFile.close()
        #print("secondTolastLine: " + secondTolastLine)
        #set expectedString
        expectedString5 = ("LOG: 2016-10-01 10:01:10-06:00\t" + "Pollux\t" + "2017-04-14\t"+ "23:50:14\t" + "15d01.5\t" 
                             + "27d59.1\t" + "84d33.4\t" + "N27d59.5\t" + "85d33.4\t" + "292d44.6\t" + "174\n")
        expectedString7 = ("LOG: 2016-10-01 10:01:11-06:00\t" + "Approximate latitude:\t" + "N29d6.8\t" 
                           + "Approximate longitude:\t" + "82d52.9\n")
        #check 5th line
        self.assertEquals(line5, expectedString5, (line5 + " ! =" + expectedString5))
        #check 7th line
        self.assertEquals(line7, expectedString7, (line7 + " != " + expectedString7))
        
        pass
    
# *** SAD PATH TESTS

    def test100_06testInvalidLatInputs(self):
        #create Fix object
        thisFix = F.Fix()
        
        #set aries, sighting, and star files
        ariesFile = self.ariesFileName
        sightFile = self.sightFileName
        starFile = self.starFileName
        file01 = thisFix.setSightingFile(sightFile)
        file02 = thisFix.setAriesFile(ariesFile)
        file03 = thisFix.setStarFile(starFile)
        
        expectedError = "Fix.getSightings:  invalid latitude or longitude input"
        
        #test getSightings("", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result01 = thisFix.getSightings("", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings(5, "85d33.4")
        with self.assertRaises(ValueError) as context:
            result02 = thisFix.getSightings(5, "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("S00.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result03 = thisFix.getSightings("S00.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("S1.1d0.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result04 = thisFix.getSightings("S1.1d0.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("S-1d0.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result05 = thisFix.getSightings("S-1d0.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError)
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("S90d0.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result06 = thisFix.getSightings("S90d0.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("S0d0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result07 = thisFix.getSightings("S0d0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("S0d-1.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result08 = thisFix.getSightings("S0d-1.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("S0d60.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result09 = thisFix.getSightings("S0d60.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("S0d-1.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result10 = thisFix.getSightings("S0d-1.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("S0d60.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result11 = thisFix.getSightings("S0d60.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("0d1.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result12 = thisFix.getSightings("0d1.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("E0d1.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result13 = thisFix.getSightings("E0d1.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("S0d0.0", "85d33.4")
        with self.assertRaises(ValueError) as context:
            result14 = thisFix.getSightings("S0d0.0", "85d33.4")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        
        pass
    
    def test100_07testInvalidLongInputs(self):
        #create Fix object
        thisFix = F.Fix()
        
        #set aries, sighting, and star files
        ariesFile = self.ariesFileName
        sightFile = self.sightFileName
        starFile = self.starFileName
        file01 = thisFix.setSightingFile(sightFile)
        file02 = thisFix.setAriesFile(ariesFile)
        file03 = thisFix.setStarFile(starFile)
        
        expectedError = "Fix.getSightings:  invalid latitude or longitude input"
        
        #test getSightings("N27d59.5", "")
        with self.assertRaises(ValueError) as context:
            result01 = thisFix.getSightings("N27d59.5", "")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("N27d59.5", 5)
        with self.assertRaises(ValueError) as context:
            result02 = thisFix.getSightings("N27d59.5", 5)
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("N27d59.5", "00.0")
        with self.assertRaises(ValueError) as context:
            result03 = thisFix.getSightings("N27d59.5", "00.0")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("N27d59.5", "1.1d0.0")
        with self.assertRaises(ValueError) as context:
            result04 = thisFix.getSightings("N27d59.5", "1.1d0.0")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("N27d59.5", "-1d0.0")
        with self.assertRaises(ValueError) as context:
            result05 = thisFix.getSightings("N27d59.5", "-1d0.0")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("N27d59.5", "3600d0.0")
        with self.assertRaises(ValueError) as context:
            result06 = thisFix.getSightings("N27d59.5", "3600d0.0")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("N27d59.5", "S0d0")
        with self.assertRaises(ValueError) as context:
            result07 = thisFix.getSightings("N27d59.5", "S0d0")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("N27d59.5", "S0d-1.0")
        with self.assertRaises(ValueError) as context:
            result08 = thisFix.getSightings("N27d59.5", "S0d-1.0")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        #test getSightings("N27d59.5", "S0d60.0")
        with self.assertRaises(ValueError) as context:
            result09 = thisFix.getSightings("N27d59.5", "S0d60.0")
        self.assertEquals(expectedError, context.exception.args[0][0:len(expectedError)], str(expectedError) 
                          + " != " + str(context.exception.args[0][0:len(expectedError)]))
        
        
        pass