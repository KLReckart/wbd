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
            #print(lineInFile)
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
            #print(lineInFile)
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
        #print(lineInFile02)
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
        #get the 2nd to last line as a string
        secondTolastLine = ""
        numOfLines = 0
        for line in logFile:
            numOfLines = numOfLines + 1
        position = logFile.seek(0, 0)
        currentLine = 0
        for line2 in logFile:
            if (currentLine == numOfLines - 1):
                secondTolastLine = line2
            #print "line#: " + str(currentLine)
            #print "line2: " + line2
            currentLine = currentLine + 1
        #print("secondTolastLine: " + secondTolastLine)
        #set expectedString
        expectedStringBeg = "LOG: "
        expectedStringEnd = "Start of sighting file: " + siteFileName_IN + "\n"
        self.assertEquals(secondTolastLine[:5], expectedStringBeg, (secondTolastLine[:5] + " ! =" + expectedStringBeg))
        self.assertEquals(secondTolastLine[-35:], expectedStringEnd, "log20.txt missing 'Start of sighting file: " + siteFileName_IN + "'")
        
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
        
#    Acceptance Test: 300
#        Analysis: calcAdjustedAlt(...)

#    Happy path
    def test300_010CalculatesCorrectly(self):
        
        #needs: height, pressure, temp, observation (AKS: observed altitude)
        height = 6.0
        pressure = 1010
        temp = 72
        observation = "015d04.9"
        horizon = "artificial"
        #observation = Angle.Angle()
        #observation.setDegreesAndMinutes("015d04.9")
        expectedResult = "15d01.5"
        fix30 = Fix.Fix()
        result = fix30.calcAdjustedAlt(height, pressure, temp, observation, horizon)
        self.assertEquals(result, expectedResult, (str(result) + " != " + str(expectedResult)))
        
#    Acceptance Test: 400
#        Analysis: getSightings(...)

#    Happy path
    def test400_010ReturnssTuple(self):
        fix40 = Fix.Fix()
        logFileName = fix40.setSightingFile("site01.xml")
        result = fix40.getSightings()
        self.assertEquals(result, (0, 0), str(result) + " != (0, 0)")
        
    def test400_011CheckLastLineInLog(self):
        expectBeg = "LOG: "
        expectEnd = "End of sighting file: site01.xml\n"
        logFileNameIN = "log40.txt"
        fix41 = Fix.Fix(logFileNameIN)
        logFileName = fix41.setSightingFile("site01.xml")
        getResult = fix41.getSightings()
        logFile = open(logFileNameIN, "r")
        #get the 2nd to last line as a string, last line = "" b/c of "\n"
        secondTolastLine = ""
        numOfLines = 0
        for line in logFile:
            numOfLines = numOfLines + 1
        position = logFile.seek(0, 0)
        currentLine = 0
        for line2 in logFile:
            if (currentLine == numOfLines - 1):
                secondTolastLine = line2
            #print "line#: " + str(currentLine)
            #print "line2: " + line2
            currentLine = currentLine + 1
        self.assertEquals(secondTolastLine[:5], expectBeg, (secondTolastLine[:5] + " ! =" + expectBeg))
        self.assertEquals(secondTolastLine[-33:], expectEnd, (secondTolastLine[-33:] + " != " + expectEnd))
        
    def test400_011wroteCorrectValuesToLog(self):
        expected = "LOG: 2016-10-01 10:01:10-06:00 Aldebaran\t2016-03-01\t23:40:01\t15d01.5"
        expectedEnd = "Aldebaran\t2016-03-01\t23:40:01\t15d01.5"
        logFileNameIN = "log42.txt"
        fix41 = Fix.Fix(logFileNameIN)
        logFileName = fix41.setSightingFile("site01.xml")
        getResult = fix41.getSightings()
        logFile = open(logFileNameIN, "r")
        #get 3rd to last line for testing
        result = ""
        numOfLines = 0
        for line in logFile:
            numOfLines = numOfLines + 1
        position = logFile.seek(0, 0)
        currentLine = 0
        for line2 in logFile:
            if (currentLine == numOfLines - 2):
                result = line2
            #print "line#: " + str(currentLine)
            #print "line2: " + line2
            currentLine = currentLine + 1
        #42, 39
        self.assertEquals(result[-38:], expectedEnd, (result[-38:] + " != " + expectedEnd))
        
#   Sad path
    def test400_910DidNotSetXML(self):
        expected = "Fix.getSightings:  site file is not set or invalid"
        fix49 = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            result = fix49.getSightings()
        self.assertEquals(expected, context.exception.args[0][0:len(expected)], expected + " != " + context.exception.args[0][0:len(expected)])
    
    def test400_911LacksMandatoryData(self):
        expected = "Fix.getSightings:  invalid xml data"
        fix49 = Fix.Fix("log49.txt")
        here = fix49.setSightingFile("site02.xml")
        with self.assertRaises(ValueError) as context:
            result = fix49.getSightings()
        self.assertEquals(expected, context.exception.args[0][0:len(expected)], expected + " != " + context.exception.args[0][0:len(expected)])
    
        
#    Acceptance Test: 500
#        Analysis: getData(...)

    def test500_010viewResults(self):
        siteFileName = "site01.xml"
        logFileName = "log50.txt"
        fix50 = Fix.Fix(logFileName)
        val01 = fix50.setSightingFile(siteFileName)
        #test the printing of data
        fix50.getData()
        
        