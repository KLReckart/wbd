class Angle():
    def __init__(self):
        #self.angle = ...       set to 0 degrees 0 minutes
        self.angleInDegree = 0
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
            raise ValueError("Angle.checkAngleString:  the angleString has too many 'd's")
        elif countD < 1 :
            result = False
            raise ValueError("Angle.checkAngleString:  the angleString lacks a 'd'")
        else :
        #b/c the next few checks are dependent of the 'd' being in the string, these checks need to be done if countD = 1
            splitStringList = angleString.split("d")
            # does angleString have a digit before 'd'
            if(not(isinstance(self.num(splitStringList[0]), int))):
                result = False
                raise ValueError("Angle.checkAngleString:  the angleString must have an integer value before 'd'")
                pass
            # does angleString have a digit after 'd'
            if(not(isinstance(self.num(splitStringList[1]), int)) and not(isinstance(self.num(splitStringList[1]), float))):
                result = False
                raise ValueError("Angle.checkAngleString:  the angleString must have an integer or float value after 'd'")
            else:
                #check that this int of float is positive, it needs to be
                if self.num(splitStringList[1]) < 0 :
                    result = False
                    raise ValueError("Angle.checkAngleString:  the angleString must have a positive value after 'd'")
                    pass
                
                pass
            pass
        
        return result
    #KLR's made function
    # Purpose: return minutes of an enter degree
    def getMinsOfDegree(self, degreeIN):
        result = (degreeIN - int(degreeIN)) * 60
        #print("mins: " + str(degreeIN) + "->" + str(result))
        return result
    
    def setDegrees(self, degrees=0):
        #default to zero if no numerical value 
        
        #raise an error if the degrees value is neither an int nor float
        if(not(isinstance(degrees, int)) and not(isinstance(degrees, float))):
            raise ValueError("Angle.setDegrees:  the value entered for 'degrees' needs to be an integer or float")
        else:        
            #if degrees is negative, convert to positive
            while degrees < 0 :
                degrees = degrees + 360
                pass
            #if degree is .G.R. 360, subtract until .L.E. 360
            while degrees > 360 :
                degrees = degrees - 360
                pass
            
            #set angleValue
            # calculate the degree value
            self.angleInDegree = degrees
        
            pass
        
        pass
    
    def setDegreesAndMinutes(self, angleString):
        #if the input is valid, set angleValue
        if self.checkAngleString(angleString) == True:
            splitString = angleString.split('d')
            
            #get num1
            num1 = int(splitString[0])
            #print "num1: " + str(num1)
            #get num2
            num2 = float(splitString[1])
            #print "num2: " + str(num2)
            
            #get degrees (num1 modulo 360)
            DM_degree = num1 % 360
            #get mins (num2 modulo 60)
            DM_min = num2 % 60
            
            #convert the degrees and mins to degree decimal
            # divide mins by 60 and then add to degrees
            self.angleInDegree = (DM_min / 60) + DM_degree
            
            pass
            
        
        pass
    
    def add(self, angleIN):
        #raise an error if the angleIN value is not an instance of class Angle
        if(not(isinstance(angleIN, Angle)) and not(isinstance(angleIN, Angle))):
            raise ValueError("Angle.add:  the value entered for 'angleIN' needs to be an instance of Angle")
        else: 
        
            #add the two degrees
            sumVal = self.angleInDegree + angleIN.angleInDegree
            #if the result is Less Than 0, add 360 until .G.E. 0
            while sumVal < 0 :
                sumVal = sumVal + 360
                pass
            #if the result is Greater Than360, subtract until .L.E. 360
            while sumVal > 360 :
                sumVal = sumVal - 360
                pass
            #save the result to self.angleInDegree
            self.angleInDegree = sumVal
            #return the formatted result (format = first digit after decimal)
            pass
        return format(sumVal, '0.1f')
        
    
    def subtract(self, angleIN):
        #raise an error if the angleIN value is not an instance of class Angle
        if(not(isinstance(angleIN, Angle)) and not(isinstance(angleIN, Angle))):
            raise ValueError("Angle.subtract:  the value entered for 'angleIN' needs to be an instance of Angle")
        else: 
        
            #subtract the two degrees
            diffVal = self.angleInDegree - angleIN.angleInDegree
            #if the result is Less Than 0, add 360 until .G.E. 0
            while diffVal < 0 :
                diffVal = diffVal + 360
                pass
            #if the result is Greater Than360, subtract until .L.E. 360
            while diffVal > 360 :
                diffVal = diffVal - 360
                pass
            #save the result to self.angleInDegree
            self.angleInDegree = diffVal
            #return the formatted result (format = first digit after decimal)
            pass
        return format(diffVal, '0.1f')
    
    def compare(self, angleIN):
        #raise an error if the angleIN value is not an instance of class Angle
        if(not(isinstance(angleIN, Angle)) and not(isinstance(angleIN, Angle))):
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
        #make sure the result is formatted correctly 
        result = format(self.angleInDegree, '0.1f')
        #change the  result from string back to a float
        result = float(result)
        
        return result