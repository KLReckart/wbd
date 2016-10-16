import unittest
import Navigation.prod.Fix as Fix
import os.path

class FixTest(unittest.TestCase):
    
    def setUp(self):
        self.className = "Fix."
    def tearDown(self):
        pass
    
#    Acceptance Test: 100
#       Analysis: Constructor

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
        expectedEnd = "Start of log\n"
        if (os.path.isfile(file01Name) == True):
            file01 = open(file01Name, "r")
            lineInFile = file01.readline()
            print(lineInFile)
            self.assertEquals(lineInFile[:5], expectedBeg, "file01 missing 'LOG: '")
            self.assertEquals(lineInFile[-13:], expectedEnd, "file01 missing 'Start of log'")
             
    def test100_011CreateWithInput(self):
        fix02 = Fix.Fix("log02.txt")
        #check that the object was created
        self.assertIsInstance(fix02, Fix.Fix, "fix02 was not created")
        #check that the file was created
        file02Name = "log02.txt"
        self.assertTrue(os.path.isfile(file02Name), "file02 does not exist")
        #if file was created, check that the first line is correct
        expectedBeg = "LOG: "
        expectedEnd = "Start of log\n"
        if (os.path.isfile(file02Name) == True):
            file02 = open(file02Name, "r")
            lineInFile = file02.readline()
            print(lineInFile)
            self.assertEquals(lineInFile[:5], expectedBeg, "file02 missing 'LOG: '")
            self.assertEquals(lineInFile[-13:], expectedEnd, "file02 missing 'Start of log'")
             
    def test100_012AppendToEExistingFile(self):
        fix03 = Fix.Fix()
        #get the 2nd line of the file, check that line
        file03Name = fix03.getLogFileName()
        expectedBeg = "LOG: "
        expectedEnd = "Start of log\n"
        file03 = open(file03Name, "r")
        lineInFile = file03.readline()
        lineInFile02 = file03.readline()
        print(lineInFile02)
        self.assertEquals(lineInFile02[:5], expectedBeg, "file02 missing 'LOG: '")
        self.assertEquals(lineInFile02[-13:], expectedEnd, "file02 missing 'Start of log'")
 
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
    
    #FOR BELOW TEST, must change file01 = open(logFile, "a") to file01 = open(logFile, "w")
#     def test100_912FailToCreateFile(self):
#         expectedDia = "Fix.__init__:  failed to create or append file"
#         with self.assertRaises(ValueError) as context:
#             fix06 = Fix.Fix("test")
#         self.assertEquals(expectedDia, context.exception.args[0][0:len(expectedDia)], "error for file creating not raised")
#         
     
     
#    Acceptance Test: 200
#        Analysis: setSightingFile()

#    Happy Path
    def test200_010ReturnString(self):
        fix20 = Fix.Fix()
        siteName_IN = "site01.xml"
        result01 = fix20.setSightingFile(siteName_IN)
        result02 = fix20.getSiteFileName()
        self.assertEquals(result01, siteName_IN, "site01.xml was not returned for fix20.setSightingFile(...)")
        self.assertEquals(result02, siteName_IN, "site01.xml was not returned for fix20.getSiteFileName()")
        
    def test200_011LineInFile(self):
        fix21 = Fix.Fix("log20.txt")
        siteFileName_IN = "site01.xml"
        fix21.setSightingFile(siteFileName_IN)
        #open the log file for reading
        logFile = open("log20.txt", "r")
        #position the read pointer to the last line
        logFile.seek(-41, 2)
        #get the line as a string
        lastLine = logFile.readline()
        print("lastLine: " + lastLine)
        #set expectedString
        expectedStringBeg = "LOG: "
        expectedStringEnd = "Start of sighting file: " + siteFileName_IN + "\n"
        self.assertEquals(lastLine[:5], expectedStringBeg, "log20.txt missing 'LOG: '")
        self.assertEquals(lastLine[-35:], expectedStringEnd, "log20.txt missing 'Start of sighting file: " + siteFileName_IN + "'")
        
#    Sad Path
    def test200_900LacksFileExt(self):
        fix22 = Fix.Fix()
        siteFileName_IN = "site01"
        expectedException = "Fix.setSightingFile:  invalid input"
        with self.assertRaises(ValueError) as context:
            fix22.setSightingFile(siteFileName_IN)
        self.assertEquals(expectedException, context.exception.args[0][0:len(expectedException)], "error for invalid setSightingFile input not raised")
        
    def test200_901NonStringInput(self):
        fix22 = Fix.Fix()
        siteFileName_IN = 55
        expectedException = "Fix.setSightingFile:  invalid input"
        with self.assertRaises(ValueError) as context:
            fix22.setSightingFile(siteFileName_IN)
        self.assertEquals(expectedException, context.exception.args[0][0:len(expectedException)], "error for invalid setSightingFile input not raised")
        
    def test200_902NullInput(self):
        fix22 = Fix.Fix()
        siteFileName_IN = None
        expectedException = "Fix.setSightingFile:  invalid input"
        with self.assertRaises(ValueError) as context:
            fix22.setSightingFile(siteFileName_IN)
        self.assertEquals(expectedException, context.exception.args[0][0:len(expectedException)], "error for invalid setSightingFile input not raised")
        
    def test200_903SightingFileNotInDir(self):
        fix23 = Fix.Fix()
        siteFileName_IN = "site.xml"
        expectedException = "Fix.setSightingFile:  sighting file does not exist in current directory"
        with self.assertRaises(ValueError) as context:
            fix23.setSightingFile(siteFileName_IN)
        self.assertEquals(expectedException, context.exception.args[0][0:len(expectedException)], "error for invalid setSightingFile input not raised")
        
        