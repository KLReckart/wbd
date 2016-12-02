#LOC = 151 (10/24/16)
#LOC = 153 (12/1/16)
import math

class Angle():
    def __init__(self):
        #self.angle = ...       set to 0 degrees 0 minutes
        self.angleInDegree = 0.0
        #self.mins = 0.0
        pass
    
    #KLR's made function
    # Purpose: return the entered value as an integer or float if possible
    def num(self, valueIN):
        try:
            return int(valueIN)
        except ValueError:
            try:
                return float(valueIN)
            except ValueError:
                return False
            
        return True
    
    #KLR's made function
    # Purpose: return True if the string is a valid value, else returns False
    def checkAngleString(self, angleString):
        result = True
        # does angleString have only 1 'd'
        countD = angleString.count("d")
        if countD > 1 :
            result = False
            #raise ValueError("Angle.checkAngleString:  the angleString has too many 'd's")
        elif countD < 1 :
            result = False
            #raise ValueError("Angle.checkAngleString:  the angleString lacks a 'd'")
        else :
        #b/c the next few checks are dependent of the 'd' being in the string, these checks need to be done if countD = 1
            splitStringList = angleString.split("d")
            
            try:
            
                # does angleString have a digit before 'd'
                if(not(isinstance(self.num(splitStringList[0]), int))):
                    result = False
                    #raise ValueError("Angle.checkAngleString:  the angleString must have an integer value before 'd'")
                    pass
                # does angleString have anything after 'd'
                if(len(splitStringList[1]) == 0):
                    result = False
                    #raise ValueError("Angle.checkAngleString:  the angleString must have an integer or float value after 'd'")
                # does angleString have a digit or float after 'd'; test for float b/c an int can be converted to a float
            
                elif(not(isinstance(self.num(splitStringList[1]), float)) and not(isinstance(self.num(splitStringList[1]), int))):
                    result = False
                    #raise ValueError("Angle.checkAngleString:  the angleString must have an integer or float value after 'd'")
                else:
                    print(float(splitStringList[1]))
                    #check that this int or float is positive, it needs to be
                    if self.num(splitStringList[1]) < 0.0 :
                        result = False
                        #raise ValueError("Angle.checkAngleString:  the angleString must have a positive value after 'd'")
                        pass
                
                    pass
                    #check that if float, there is only one digit after "."
                    if isinstance(self.num(splitStringList[1]), float):
                        temp = str(self.num(splitStringList[1]))
                        splitStringList2 = temp.split(".")
                        if len(splitStringList2[1]) > 1:
                            result = False
                            #raise ValueError("Angle.checkAngleString:  the angleString must have 1 digit value after '.'")
                            pass                    
                pass
            
            except:
                result = False
            
        return result
    #KLR's made function
    # Purpose: return minutes of an enter degree
    def getMinsOfDegree(self, degreeIN):
        result = (degreeIN - int(degreeIN)) * 60.0
        #print("mins: " + str(degreeIN) + "->" + str(result))
        return result
#above = 50 LOC
    
    def setDegrees(self, degrees=0.0):
        #default to zero if no numerical value 
        result = 0.0
        #raise an error if the degrees value is neither an int nor float
        if(not(isinstance(degrees, int)) and not(isinstance(degrees, float))):
            raise ValueError("Angle.setDegrees:  the value entered for 'degrees' needs to be an integer or float")
        else:        
            #if is an int, convert to float
            degrees = float(degrees)
            #if degrees is negative, convert to positive
            while degrees < 0.0 :
                degrees = degrees + 360.0
                pass
            #if degree is .G.R. 360, subtract until .L.E. 360
            while degrees >= 360.0 :
                degrees = degrees - 360.0
                pass
            
            #set angleValue
            # calculate the degree value
            result = degrees
            self.angleInDegree = result
            pass
        
        return result
    
    def setDegreesAndMinutes(self, angleString):
        result = 0.0
        funcName = "Angle.setDegreesAndMinutes"
        #if the input is valid, set angleValue
        if (angleString <> None and self.checkAngleString(angleString) == True):
            splitString = angleString.split('d')
            #print "splitString[0]: " + splitString[0]
            #print "splitString[1]" + splitString[1]
            #get num1
            try:
                num1 = int(splitString[0])
                #print "num1: " + str(num1)
            except:
                raise ValueError(funcName + ":  invalid input")
            
            #get num2
            try:
                num2 = float(splitString[1])
                #print "num2: " + str(num2)
            except:
                raise ValueError(funcName + ":  invalid input")
            
            
            #get degrees (num1 modulo 360)
            DM_degree = abs(num1) % 360.0
            #print "DM_ degree: " + str(DM_degree)
            #get mins (num2 modulo 60)
            DM_min = num2 % 60.0
            #print "DM_min: " + str(DM_min)
            #convert the degrees and mins to degree decimal
            # divide mins by 60 and then add to degrees
            if num1 >= 0:
                result = (DM_min / 60) + DM_degree
            else:
                result = 360 - ((DM_min / 60) + DM_degree)
            
            self.angleInDegree = result
            
            return result
        
        elif self.checkAngleString(angleString) == False:
            raise ValueError("Angle.setDegreesAndMinutes:  the angleString must be a valid input, please look at previous error messages")
            #for more info on specific input error, un-comment raises in the function checkAngleString()
            pass
            
        
        pass
    
    def add(self, angleIN=None):
        if(angleIN == None):
            raise ValueError("Angle.add:  the value entered for 'angleIN' needs to be an non-empty value")
        #raise an error if the angleIN value is not an instance of class Angle
        elif(not(isinstance(angleIN, Angle)) and not(isinstance(angleIN, Angle))):
            raise ValueError("Angle.add:  the value entered for 'angleIN' needs to be an instance of Angle")
        else: 
        
            #add the two degrees
            sumVal = self.angleInDegree + angleIN.angleInDegree
            #if the result is Less Than 0, add 360 until .G.E. 0
            while sumVal < 0.0 :
                sumVal = sumVal + 360.0
#above = 100 LOC
                pass
            #if the result is Greater Than360, subtract until .L.E. 360
            while sumVal >= 360.0 :
                sumVal = sumVal - 360.0
                pass
            #save the result to self.angleInDegree
            self.angleInDegree = sumVal
            #return the result
            pass
        return sumVal
        
    
    def subtract(self, angleIN=None):
        if(angleIN == None):
            raise ValueError("Angle.subtract:  the value entered for 'angleIN' needs to be an non-empty value")
        #raise an error if the angleIN value is not an instance of class Angle
        elif(not(isinstance(angleIN, Angle)) and not(isinstance(angleIN, Angle))):
            raise ValueError("Angle.subtract:  the value entered for 'angleIN' needs to be an instance of Angle")
        else: 
        
            #subtract the two degrees
            diffVal = self.angleInDegree - angleIN.angleInDegree
            #if the result is Less Than 0, add 360 until .G.E. 0
            while diffVal < 0.0 :
                diffVal = diffVal + 360.0
                pass
            #if the result is Greater Than360, subtract until .L.E. 360
            while diffVal >= 360.0 :
                diffVal = diffVal - 360.0
                pass
            #save the result to self.angleInDegree
            self.angleInDegree = diffVal
            #return the result
            pass
        return diffVal
    
    def compare(self, angleIN=None):
        if(angleIN == None):
            raise ValueError("Angle.compare:  the value entered for 'angleIN' needs to be an non-empty value")
        #raise an error if the angleIN value is not an instance of class Angle
        elif(not(isinstance(angleIN, Angle)) and not(isinstance(angleIN, Angle))):
            raise ValueError("Angle.compare:  the value entered for 'angleIN' needs to be an instance of Angle")
        else:
        
            #return -1 if self.angleInDegree < angleIN.angleInDegree, +1 if self.angleInDegree > angleIN.angleInDegree,
            # 0 if self.angleInDegree = angleIN..angleInDegree
        
            #since the function that sets the degree angle ensure a value that is greater than 0 and less than 360,
            # there is no need to ensure this range here
        
            if self.angleInDegree < angleIN.angleInDegree:
                result = -1
            elif self.angleInDegree > angleIN.angleInDegree:
                result = +1
            else:
                result = 0
                pass
            pass
        return result
    
    def getString(self):
        #get the mins (up to the first decimal point)
        mins = self.getMinsOfDegree(self.angleInDegree)

        mins = format(mins, '0.1f')
        result = str(int(self.angleInDegree)) + "d" + str(mins)
        
        return result
    
    def getDegrees(self):
        #note: the result needs to be rounded to the nearest 1/10 minute
        # to do this: get the minute portion of self.angleInDegree
        # round this piece, and then reunite this part with the degree portion of self.angleInDegree to get result
        
        minutePortion = (self.angleInDegree - int(self.angleInDegree)) * 60
        roundedValue = round(minutePortion, 1)
        result = int(self.angleInDegree) + (roundedValue / 60)
        return result
    
    #added 10/16/16
    def tangent(self):
        #get the angle in degrees with self.getDegrees()
        angleInDegrees = self.getDegrees()
#above = 150 LOC
        #convert the degrees to radians with math.radians(degreesIN)
        angleInRadians = math.radians(angleInDegrees)
        #math.tan(angle) where angle is in radians
        result = math.tan(angleInRadians)
        #convert radians to degrees with degrees(radiansIN)
        #result = math.degrees(result)
        return result
#above = 153 LOC (12/1/16)