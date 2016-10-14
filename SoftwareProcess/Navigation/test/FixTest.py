import unittest
import Navigation.prod.Fix as Fix

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
        file01 = open("log.txt", "r")
        self.assertIsNotNone(file01, "file01 does not exist")
        #check that the first line is correct
        expectedBeg = "LOG: "
        expectedEnd = "Start of log"
        lineInFile = file01.readline()
        self.assertEquals(lineInFile[:5], expectedBeg, "file01 missing 'LOG: '")
        self.assertEquals(lineInFile[-12:], expectedEnd, "file01 missing 'Start of log'")

#   Sad path