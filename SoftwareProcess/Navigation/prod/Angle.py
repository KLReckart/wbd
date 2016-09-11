class Angle():
    def __init__(self):
        #self.angle = ...       set to 0 degrees 0 minutes
        self.degree = 0
        self.mins = 0.0
        pass
    
    
    #KLR's made function
    # Purpose: return True if the string is a valid value, else returns False
    def checkAngleString(self, angleString):
        result = True
        # does angleString have only 1 'd'
        
        # does angleString have a digit before 'd'
        
        # does angleString have a digit after 'd'
        
        
        return result
    
    def setDegrees(self, degrees):
        #default to zero if no numerical value 
        
        #if degrees is negative, convert to positive
        
        #set angleValue
        
        pass
    
    def setDegreesAndMinutes(self, angleString):
        #if the input is valid, set angleValue
        if self.checkAngleString(angleString) == True:
            
            
            pass
            
            
        
        
        
        pass
    
    def add(self, angle):
        pass
    
    def subtract(self, angle):
        pass
    
    def compare(self, angle):
        pass
    
    def getString(self):
        #get the self.mins (up to the first decimal point)
        formatMins = "{0:.1f}".format(self.mins)
        result = "" + str(self.degree) + "d" + formatMins
        
        return result
    
    def getDegrees(self):
        #divide the minutes (up to the first digit behind decimal) by 60 to convert to degrees
        minsToDegree = self.mins / 60.0
        #add the minsToDegree to the degree value
        result = self.degree + minsToDegree
        #make sure the result is formatted correctly 
        result = format(result, '0.1f')
        #change the  result from string back to a float
        result = float(result)
        return result