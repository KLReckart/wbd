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
        
        
        