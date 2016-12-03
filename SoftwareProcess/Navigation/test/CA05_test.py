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
        
        pass
        
    def test100_02testDefaultLongitudeInput(self):
        
        pass
        
    def test100_03testDefaultLatitudeInput(self):
        
        pass
    
    def test100_04testDefaultInputs(self):
        
        pass
    
    def test100_05testLogData(self):
        
        #check 7th line
        
        #check 8th line
        
        pass
    
# *** SAD PATH TESTS

    def test100_06testInvalidLatInputs(self):
       
        pass
    
    def test100_07testInvalidLongInputs(self):
        
        pass