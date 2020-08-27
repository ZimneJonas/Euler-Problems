from math import gcd
import time

def smallestMultiple1(until):
    currentItaration=0
    finishBool = True

    #Run until number found
    while(finishBool):
        currentItaration += until #Test all multiplies of highest number
        for test in range(until-1, 1, -1):
            if ((currentItaration % test) != 0):
                break
            elif(test == 2):
                finishBool = False
        ##time.sleep(1)
    
    return currentItaration

def smallestMultiple2(until): #faster (unfinished)
    #Compute prime factorization
    primeFactors = getPrimeFactorziation(until)
    #ToDo

def getPrimeFactorziation(until):
    primeFactors = []
    for ii in range(2, until+1):
        primeFactors.append([])
        dismantling = ii
        jj = 2
        while (dismantling != 1):
            if ((dismantling % jj) == 0):
                primeFactors[ii-2].append(jj)
                dismantling //= jj
            else:
                jj += 1
    return(primeFactors)

print(smallestMultiple1(20))

