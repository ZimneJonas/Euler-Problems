

def SumSquareDifference(until):
    result=0
    for ii in range(1,until+1):
        result += ii**2

    return(((until * (until+1)) // 2 )**2 - result)


print(SumSquareDifference(100))