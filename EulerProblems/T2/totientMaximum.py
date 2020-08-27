from math import gcd
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum


##################
#TO SLOW
##################

def totientMaximum(end): # slow
    primeNumbers = list(getPrimeNumbers(end))
    primeNumbers.sort()
    primeSets = [set(range(p,end,p)) for p in primeNumbers]
    result = -1
    maximum = 0

    for n in range(2 , end+1): # go through all numbers
        relativePrimeNumbers = set(range(1,n)) # fill List with all numbers between 0, n-1
        # find last prime < n//2
        neededUntilHere = getAllSmallerAs(n//2 , primeNumbers)

        # Go through all prime Numbers < n//2
        for count in range(0,neededUntilHere):
            # Delete all primes wich are not relative Primes
            # Delete all multiples of the deleted Primes
            if (n % primeNumbers[count] == 0):
                relativePrimeNumbers.difference_update(primeSets[count])
        # get n/φ(n)
        # if it is new max, save it
        if (n/len(relativePrimeNumbers) > maximum):
            maximum = n/len(relativePrimeNumbers)
            result = n
            print(" n:" + str(n) + " max:" + str(maximum))
        
        if((n % 10000) == 0):
            print(str(n//10000) + "'%' finished")
        

    return result

def getAllSmallerAs(n , sortedNumbers):
    previous = len(sortedNumbers)
    current = previous // 2
    while(True):
        if (current == 0 or current == previous):
            break
        if(n > sortedNumbers[current+1]):
            save = previous
            previous = current
            current = (current + save) // 2
            
        elif(n < sortedNumbers[current-1]):
            previous = current
            current //= 2
        else:
            break    
    return current
        
    


def totientMaximum2(end): # slower
    result = -1
    maximum = 0
    
    for n in range(2 , end+1): # go through all numbers
        relativePrimeNumbers = []
        for ii in range(1,n):
            if (gcd(ii,n)==1):
                relativePrimeNumbers.append(ii)

        # get n/φ(n)
        # if it is new max, save it
        
        if (n/len(relativePrimeNumbers) > maximum):
            maximum = n/len(relativePrimeNumbers)
            result = n
            print(" n:" + str(n) + " max:" + str(maximum))

    return result
    

def getPrimeNumbers(end): 

    numbers = set(range(end, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, end+1, p)))
    return primes

print(totientMaximum(1000000))

