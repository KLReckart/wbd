'''
Created on Octber 24, 2016

@author: Kristi Reckart
'''

#LOC made = 35 (10/24/16)
#LOC total = 153 (12/1/16)
import math
class TCurve(object):

# outward facing methods
    def __init__(self, n=None):
        functionName = "TCurve.__init__: "
        if(n == None):
            raise ValueError(functionName + "invalid n")
        if(not(isinstance(n, int))):
            raise ValueError(functionName + "invalid n")
        if((n < 2) or (n >= 30)):
            raise ValueError(functionName + "invalid n")
        self.n = n

    
    def p(self, t=None, tails=1):
        functionName = "TCurve.p: "
        if(t == None):
            raise ValueError(functionName + "missing t")
        if(not(isinstance(t, float))):
            raise ValueError(functionName + "invalid t")
        if(t < 0.0):
            raise ValueError(functionName + "invalid t")
        
        if(not(isinstance(tails, int))):
            raise ValueError(functionName + "invalid tails")
        if((tails != 1) & (tails != 2)):
            raise ValueError(functionName + "invalid tails")
        
        constant = self. calculateConstant(self.n)
        integration = self.integrate(t, self.n, self.f)
        if(tails == 1):
            result = constant * integration + 0.5
        else:
            result = constant * integration * 2
            
        if(result > 1.0):
            raise ValueError(functionName + "result > 1.0")
        
        return result
        
# internal methods
    def gamma(self, x):
        if(x == 1):
            return 1
        if(x == 0.5):
            return math.sqrt(math.pi)
        return (x - 1) * self.gamma(x - 1)
    
    def calculateConstant(self, n):
        n = float(n)
        numerator = self.gamma((n + 1.0) / 2.0)
        denominator = self.gamma(n / 2.0) * math.sqrt(n * math.pi)
        result = numerator / denominator
        return result
    
    def f(self, u, n):
        n = float(n)
        base = (1 + (u ** 2) / n)
        exponent = -(n + 1.0) / 2
        result = base ** exponent
        return result
#above = 50 LOC
    
    def testingTemp(self, u, n):
        return u
    
    def testingTemp02(self, u, n):
        return u ** 2
    
    def testingTemp03(self, u, n):
        return u ** 6
    
    def integrate(self, t, n_IN, f_IN):
        
        #note: this integrates from 0 to n -> [0, n]; b/c p() takes care of (-infinity, 0]
        
        # f_IN is the inputted function
        # n_IN is the variable n in the given equation
        # t is the upperbound
        # note: 0 is assumed to be the lower bound in this function
        
        result = 0.0
        #beginning and end coefficient
        begendCoef = 1
        #even coefficient
        evenCoef = 4
        #odd coefficient
        oddCoef = 2
        
        epsilon = 0.001
        simpsonOld = 0.000
        simpsonNew = epsilon
        slices = 4.0
        #print("(simpsonNew - simpsonOld)/simpsonNew:" + str((simpsonNew - simpsonOld)/simpsonNew))
        while (abs((simpsonNew - simpsonOld)/simpsonNew) > epsilon):
            simpsonOld = simpsonNew
            w = (t - 0.0) / slices
            #simpsonNew = (w/3) * (f_IN(0) + 4f_IN(0 + w) + 2f_IN(0 + 2w) + ... + f(t))
            
            #calculate the 2nd part of simpsonNew
            
            # currentIteration = 1 -> this value will increase by 1 for each time it iterates in the below while loop
            #  the below loop will loop x times where x = slices
            
            currIteration = 1
            simpsonNewPart2 = 0.0 #initialize simpsonNewPart2
            while(currIteration <= slices) :
                
                #if currentIteration = 1, then treat this as: begendCoef * f_IN(0)
                if (currIteration == 1):
                    simpsonNewPart2 = simpsonNewPart2 + (begendCoef * f_IN(0, self.n))
                
                #else-if the currentIteration != slices, identify if this needs an odd or even coefficient
                #  treat this as: coefficient*f_IN((currentIteration - 1) * w)
                elif (currIteration != slices):
                    #if currIteration is divisible by 2 (meaning: currIteration % 2 = 0), then use the evenCoef
                    if (currIteration % 2 == 0):
                        simpsonNewPart2 = simpsonNewPart2 + (evenCoef * f_IN((currIteration - 1) * w, self.n))
                    
                    #else, currIteration is odd, then use oddCoef
                    else:
                        simpsonNewPart2 = simpsonNewPart2 + (oddCoef * f_IN((currIteration - 1) * w, self.n))
                
                #else (currentIteration = slices, then treat this as: begendCoef * f_IN(t))
                else:
                    simpsonNewPart2 = simpsonNewPart2 + (begendCoef * f_IN(t, self.n))
                
                #increment the current iteration
                currIteration = currIteration + 1
            
            simpsonNew = (w/3.0) * simpsonNewPart2
            
            #multiply slices by 2 for the next while loop's simpsonNew value
            slices = slices * 2
        
        result = simpsonNew
                
        return result
#above = 85 LOC (12/1/16)
