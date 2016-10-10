import unittest
import Navigation.prod.Angle as A

#def main():
    
myAngle = A.Angle()
    
print("test get string: " + myAngle.getString() + " -> should be 0d0.0")
print("test get degree: " + str(myAngle.getDegrees()) + " -> should be 0.0")
print("")

# test getMinsOfDegree
print("test getMinsOfDegree: " + str(myAngle.getMinsOfDegree(1.5)) + " -> should be 30")
print("test getMinsOfDegree: " + str(myAngle.getMinsOfDegree(.1)) + " -> should be 6.0")
print("")

# test setDegrees
print("myAngle.setDegrees()")
myAngle.setDegrees()
print("test setDegrees: " + str(myAngle.getDegrees()) + " -> should be zero")
print("test setDegrees: " + str(myAngle.getString()) + " -> should be 0d0.0")
print("myAngle.setDegrees(60)")
myAngle.setDegrees(60)
print("test setDegress: " + str(myAngle.getDegrees()) + " -> should be 60")
print("test setDegrees: " + str(myAngle.getString()) + " -> should be 60d0.0")
print("myAngle.setDegrees(400.5)")
myAngle.setDegrees(400.5)
print("test setDegrees: " + str(myAngle.getDegrees()) + " -> should be 40.5")
print("test setDegrees: " + str(myAngle.getString()) + " -> should be 40d30.0")
print("")

# test setDegreesAndMinutes
print("myAngle.setDegreesAndMinutes('0d0.0')")
myAngle.setDegreesAndMinutes("0d0.0")
print("test setDegreesAndMinutes: " + str(myAngle.getDegrees()) + " -> should be zero")
print("test setDegreesAndMinutes: " + str(myAngle.getString()) + " -> should be 0d0.0")
 
myAngle.setDegreesAndMinutes("60d0.0")
print("test setDegrees: " + str(myAngle.getDegrees()) + " -> should be 60")
print("test setDegrees: " + str(myAngle.getString()) + " -> should be 60d0.0")

myAngle.setDegreesAndMinutes("75d1")
print("test setDegreesAndMinutes: " + str(myAngle.getDegrees()) + " -> should be 75.?")
print("test setDegreesAndMinutes: " + str(myAngle.getString()) + " -> should be 75d1.0")
print(myAngle.angleInDegree)

myAngle.setDegreesAndMinutes("-60d1")
print("test setDegreesAndMinutes: " + str(myAngle.getDegrees()) + " -> should be 300.?")
print("test setDegreesAndMinutes: " + str(myAngle.getString()) + " -> should be 300d1.0")
print(myAngle.angleInDegree)
print("")

# test add()
myAngle2 = A.Angle()
print("myAngle2 initial degrees: " + str(myAngle2.getDegrees()) + " -> should be 0.0")
print("myAngle2 initial string: " + str(myAngle2.getString()) + " -> should be 0d0.0")
print("add myAngle to myAngle2")
print(myAngle2.add(myAngle))
print("myAngle2 final degrees: " + str(myAngle2.getDegrees()) + " -> should be 300.?")
print("myAngle2 final string: " + str(myAngle2.getString()) + " -> should be 300d1.0")
print("")

#test subtract()
myAngle3 = A.Angle()
print("myAngle3 initial degrees: " + str(myAngle3.getDegrees()) + " -> should be 0.0")
print("myAngle3 initial string: " + str(myAngle3.getString()) + " -> should be 0d0.0")
print("subtract myAngle from myAngle3")
print(myAngle3.subtract(myAngle))
print("myAngle2 final degrees: " + str(myAngle3.getDegrees()) + " -> should be 60.?")
print("myAngle2 final string: " + str(myAngle3.getString()) + " -> should be 59d59.0")
print("")

#test compare()
print("compare myAngle2 to myAngle3")
print(str(myAngle2.compare(myAngle3)) + " -> should be +1")
print("compare myAngle3 to myAngle2")
print(str(myAngle3.compare(myAngle2)) + " -> should be -1")
print("compare myAngle and myAngge2")
print(str(myAngle.compare(myAngle2)) + " -> should be 0")
print("")

#create sad path tests

#test add on sad path
print("test add on sad path")
try:
    print(str(myAngle3.add(100)))
except ValueError as e:
    print(e)

#test subtract on sad path
print("test subtract on sad path")
try:
    print(str(myAngle3.subtract(100)))
except ValueError as e:
    print(e)

#test subtract on sad path
print("test compare on sad path")
try:
    print(str(myAngle3.compare(100)))
except ValueError as e:
    print(e)
    
#test num
try:
    print("test num")
    print(myAngle3.num("5"))
    print(myAngle3.num("5.5"))
    print(myAngle3.num("abc"))
except:
    print("exception raised")
    pass

print("")

#test checkAngleString
try:
    print(str(myAngle.checkAngleString("1d0")) + " -> should be True")
    print(str(myAngle.checkAngleString("1d0.4")) + " -> should be True")
    print(str(myAngle.checkAngleString("ad0")) + " -> should be False")

except ValueError as e:
    print(e)

try:
    print(str(myAngle.checkAngleString("1d-2")) + " -> should be False")
except ValueError as e:
    print(e)
    
try:
    print(str(myAngle.checkAngleString("10")) + " -> should be False")
except ValueError as e:
    print(e)
    
try:
    print(str(myAngle.checkAngleString("1dd0")) + " -> should be False")
except ValueError as e:
    print(e)


try:
    print("setDegreesAndMinutes('80')")
    print(myAngle.setDegreesAndMinutes("80"))
except ValueError as e:
    print(e)
    #pass
    
#def testAngleInstance():
    
    #pass

#def testgetString(self, angleIN):
    
    #pass

#def testgetDegree():
    
    #pass
    
class AngleTest(unittest.TestCase):    
    #test return type is float for: add and subtract
    def test_090_AddShouldReturnFloat(self):
        #create angle1
        angle1 = A.Angle(); 
        #create angle2
        angle2 = A.Angle();
        #check that the return for add() is a float
        result = angle1.add(angle2);
        self.assertIsInstance(result, float);
    def test_091_SubShouldReturnFloat(self):
        #create angle1
        angle1 = A.Angle(); 
        #create angle2
        angle2 = A.Angle();
        #check that the return for aubtract() is a float
        result = angle1.subtract(angle2);
        self.assertIsInstance(result, float);
    
    #test error raised for null inputs for: add, subtract, and compare
    def test_092_AddNullInputError(self):
        expectedString = "Angle.add:  the value entered for 'angleIN' needs to be an non-empty value";
        angle1 = A.Angle();
        with self.assertRaises(ValueError) as context:
            angle1.add();
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    def test_093_SubNullInputError(self):
        expectedString = "Angle.subtract:  the value entered for 'angleIN' needs to be an non-empty value";
        angle1 = A.Angle();
        with self.assertRaises(ValueError) as context:
            angle1.subtract();
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    def test_094_CompNullInputError(self):
        expectedString = "Angle.compare:  the value entered for 'angleIN' needs to be an non-empty value";
        angle1 = A.Angle();
        with self.assertRaises(ValueError) as context:
            angle1.compare();
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
    #test setDegreesAndMinutes() returns correct values
    def test_095_setDegreesAndMinutesReturn01(self):
        #create angle1
        angle1 = A.Angle()
        result = angle1.setDegreesAndMinutes("45d0.0")
        self.assertEquals(45.0, result)
    def test_096_setDegreesAndMinutesReturnFloat(self):
        angle1 = A.Angle()
        result = angle1.setDegreesAndMinutes("45d0.0")
        self.assertIsInstance(result, float, "float?")
    def test_097_setDegreesAndMinutesReturn02(self):
        #create angle1
        angle1 = A.Angle()
        result = angle1.setDegreesAndMinutes("0d30.0")
        self.assertEquals(0.5, result)
    def test_098_setDegreesAndMinutesReturn02(self):
        expectedString = "Angle.setDegreesAndMinutes:  the angleString must be a valid input, please look at previous error messages"
        #create angle1
        angle1 = A.Angle()
        with self.assertRaises(ValueError) as context:
            result = angle1.setDegreesAndMinutes("030.0")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
