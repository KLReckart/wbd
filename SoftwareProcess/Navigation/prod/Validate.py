'''
Created on December 4, 2016

@author: Kristi Reckart
'''

#going to refactor the valid fucntions from the Fix class to here

from datetime import datetime
import os
import math
from xml.dom import minidom
from __builtin__ import str

import Navigation.prod.Angle as Angle


class Validate():
    
    #takes in a value and tries to cast the value as an int,
    # if this is possible, the function returns True
    # else the function returns False
    #below explains why need a try
    #https://www.peterbe.com/plog/interesting-casting-in-python
    def thisCanBeAnInt(self, valueIN):
        result = True
        try:
            temp = int(valueIN)
        except:
            result = False
                    
        return result
    
    #takes in a value and tries to cast the value as a float,
    # if this is possible, the function returns True
    # else the function returns False
    def thisCanBeAFloat(self, valueIN):
        result = True
        try:
            temp = float(valueIN)
        except:
            result = False
        
        return result
    
    def checkValidTextFileName(self, stringIN=None):
        result = False
        if stringIN <> None and isinstance(stringIN, str):
            if stringIN[-4:] == ".txt" and len(stringIN) > 4:
                result = True
        return result
    
    #returns True if the obersvationIN is a valid observation,
    # else, returns False        
    def validObservation(self, observationIN):
        result = True
        #make the observationIN into an Angle object, this will ensure the correct value
        try:
            tempAngle = Angle.Angle()
            returnedValue = tempAngle.setDegreesAndMinutes(observationIN)
        except:
            result = False
        return result
    
    #returns True if the heightIN is a valid height,
    # else, returns False
    def validHeight(self, heightIN):
        result = False
        #check that the input is a numeric that is greater than or equal to zero
        try:
            if self.thisCanBeAnInt(heightIN) == True or self.thisCanBeAFloat(heightIN) == True:
                # then the value is a numeric
                # let's check >= zero
                if heightIN >= 0:
                    result = True
                else:
                    result = False
            else:
                result = False
        except:
            result = False
        
        return result
    
    #returns True if the tempIN is a valid temperature,
    # else, returns False
    def validTemp(self, tempIN):
        result = False
        #check that the input is an integer with a value of [-20, 120]
        try:
            if isinstance(tempIN, int) == True:
                # then the value is an int -> let's check value is [-20, 120]
                if tempIN >= -20 and tempIN <= 120:
                    result = True
                else:
                    result = False
            else:
                result = False
        except:
            result = False
        return result
    
    #returns True if the pressureIN is a valid pressure
    # else, returns False
    def validPressure(self, pressureIN):
        result = False
        #check that the input is an integer with a value of [100, 1100]
        try:
            if isinstance(pressureIN, int) == True:
                # then the value is an int -> let's check value is [100, 1100]
                if pressureIN >= 100 and pressureIN <= 1100:
                    result = True
                else:
                    result = False
#LOC above = 250
            else:
                result = False
        except:
            result = False
        return result
    
    #returns True if the horizionIN is a valid horizon
    # else, return False
    def validHorizon(self, horizionIN):
        result = False
        #check that the input is a string with one of two values: 'natural' or 'artificial'
        try:

            if horizionIN == "natural" or horizionIN == "artificial":
                result = True
            else:
                result = False

        except:
            result = False
        return result
    
    
    def validAssumedLat(self, assumedLatIN):
        result = False #assume the value in is invalid until proven otherwise
        #if assumedLatIN is <> None, run more checks to see if valid
        if assumedLatIN <> None:
            #check if value is is a string
            if isinstance(assumedLatIN, str) == True:
                #check that value is a non-empty string
                if len(assumedLatIN) > 0:
                    #if first char of string is 'S' or 'N' (EX: S1d1.1), then break up the string into 2 parts, the char and angle
                    inputAsChars = list(assumedLatIN)
                    firstChar = inputAsChars[0]
#LOC above = 350
                    angleChars = inputAsChars[1:len(inputAsChars)]
                    #convert angleChars to a single string
                    angleString = "".join(angleChars)
                    if (firstChar == "S" or firstChar == "N"):
                        #check that the angle part has a 'd'
                        #print "assumedLatIN has S or N: " + str(assumedLatIN) + "\n"
                        # does angleString have only 1 'd'
                        countD = assumedLatIN.count("d")
                        #if yes, continue to check if valid
                        if (countD == 1):
                            #check that angle part does not equal '0d0.0'
                            #if yes, continue to check if valid
                            if (angleString <> "0d0.0"):
                                #print ("good, angle is not 0d0.0")
                                #split angle into part before and after 'd'
                                splitStringList = angleString.split("d")
                                
                                try:
                                    #check if part before 'd' is an integer that is greater than or equal to 0 and 
                                    # less than 90
                                    #if yes, continue to check if valid
                                    #print ("before 'd' value: " + splitStringList[0])
                                    if (isinstance(int(splitStringList[0]), int) and int(splitStringList[0]) >= 0 
                                        and int(splitStringList[0]) < 90):
                                        
                                        #print ("first part of assumed lat is an int that is >= 0 and < 90\n")
                                    
                                        #check if part after d is a float that is greater than or equal to 0 and 
                                        # less than 60
                    
                                        #if yes, then result = True
                                        #print("after 'd' value: " + splitStringList[1])
                                        hasDecimal = splitStringList[1].count(".")
                                        #print("hasDecimal: " + str(hasDecimal))
                                        if (hasDecimal == 1 and 
                                            isinstance(float(splitStringList[1]), float) and 
                                            float(splitStringList[1]) >= 0.0 
                                            and float(splitStringList[1]) < 60.0):
                                            
                                            #print("second part of assumed lat is a float >= 0 and < 60")
                                            result = True
                                except:
                                    result = False
                    #if first char is not 'S' or 'N', check if equal to '0d0.0'
                    #if yes, then result = True
                    elif (assumedLatIN == "0d0.0"):
                            result = True
            
        
        #else, keep result = invalid (AKA False)
        
        return result
    
    def validAssumedLong(self, assumedLongIN):
        result = False #assume the value in is invalid until proven otherwise
        #if assumedLatIN is <> None, run more checks to see if valid
        if assumedLongIN <> None:
            #check if value is is a string
            if isinstance(assumedLongIN, str) == True:
                #check that value is a non-empty string
                if len(assumedLongIN) > 0:
                    # does assumedLongIN have only 1 'd'
                    countD = assumedLongIN.count("d")
                    #if yes, continue to check if valid
                    if (countD == 1):
                        #split angle into part before and after 'd'
                        splitStringList = assumedLongIN.split("d")
                        try:
                            #check if part before 'd' is an integer that is greater than or equal to 0 and 
                            # less than 360
                            #if yes, continue to check if valid
                            #print ("before 'd' value: " + splitStringList[0])
                            if (isinstance(int(splitStringList[0]), int) and int(splitStringList[0]) >= 0 
                                and int(splitStringList[0]) < 360):
                                        
                                #print ("first part of assumed lat is an int that is >= 0 and < 360\n")
                                    
                                #check if part after d is a float that is greater than or equal to 0 and 
                                # less than 60
                    
                                #if yes, then result = True
                                #print("after 'd' value: " + splitStringList[1])
                                hasDecimal = splitStringList[1].count(".")
                                #print("hasDecimal: " + str(hasDecimal))
                                if (hasDecimal == 1 and 
                                    isinstance(float(splitStringList[1]), float) and 
                                    float(splitStringList[1]) >= 0.0 
                                    and float(splitStringList[1]) < 60.0):
                                            
                                    #print("second part of assumed lat is a float >= 0 and < 60")
                                    result = True
                        except:
                            result = False
            
        #else, keep result = invalid (AKA False)
        return result