import unittest
import Navigation.prod.Sighting as Sighting
import Navigation.prod.SightingsList as SightingsList
import os.path

class SightingsListTest(unittest.TestCase):
    
    def setUp(self):
        self.className = "SightingsList."
    def tearDown(self):
        pass
    
#   Acceptance Test: 100
#       Analysis: Constructor

# HAPPY PATH
    def test100_010Initialize(self):
        aList = SightingsList.SightingsList()
        result = isinstance(aList, SightingsList.SightingsList)
        expected = True
        self.assertEqual(result, expected, str(result) + " != " + str(expected))
        

#   Acceptance Test: 200
#       Analysis: getThisList

#HAPPY PATH
    def test200_010EmptyList(self):
        aList = SightingsList.SightingsList()
        expectedList = []
        result = len(aList.getThisList())
        expected = len(expectedList)
        self.assertEquals(result, expected, "list sizes for aList and expectedList do not match: " + str(result) + " != " + str(expected))
        

#   Acceptance Test: 300
#       Analysis: addSighting

#HAPPY PATH
    def test300_010AddOne(self):
        aList = SightingsList.SightingsList()
        aSighting = Sighting.Sighting()
        aSighting.setBody("sighting01_Body")
        aList.addSighting(aSighting)
        
        #check that the len = 1
        
        #check that the Body for first and only Sighting in list is "sighting01_Body"
        
        pass 
        


#   Acceptance Test: 400
#       Analysis: printSightingsList

#   Acceptance Test: 500
#       Analysis: sortSightingsList

#DELETE THE sortKey functions if unused like anticipating