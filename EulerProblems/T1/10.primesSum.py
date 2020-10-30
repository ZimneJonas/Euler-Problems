

def getPrimeNumbers(end): 

    numbers = set(range(end, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, end+1, p)))
    return primes

sum = 0
for prime in getPrimeNumbers(2000000):
    sum += prime

print(sum)