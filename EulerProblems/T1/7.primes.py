
def getPrimeNumber(toFind): 
    primes = list(getPrimeNumbers(10))
    ii = 2
    while (len(primes) < toFind):
        primes = list(getPrimeNumbers(10 ** ii))
        ii += 1
    primes.sort()
    return primes[toFind-1]

def getPrimeNumbers(end): 

    numbers = set(range(end, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, end+1, p)))
    return primes

print(getPrimeNumber(10001))