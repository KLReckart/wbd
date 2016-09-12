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

#create sad path tests


    #pass

#def testAngleInstance():
    
    #pass

#def testgetString(self, angleIN):
    
    #pass

#def testgetDegree():
    
    #pass