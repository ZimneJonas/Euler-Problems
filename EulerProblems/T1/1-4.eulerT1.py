
# Euler Difficulty 5%

def multOfAandB(a, b, unt):
    Numbers = []
    aS=a
    bS=b
    for ii in range(1,((unt-1)//a)+1):
        aS = a * ii
        Numbers.append(aS)     
    for ii in range(1,((unt-1)//b)+1):
        if bS in Numbers:
            bS = b * ii
        Numbers.append(bS)
    result = 0
    for ii in Numbers:
        result += ii
  
    return result

def testPali(n):
    diggits = []
    till = 1
    while (n//(till) != 0):
        till = till * 10
    
    while (till != 1):
        till = till//10
        diggits.append(n//till)
        n = n%till

    for i in range(0,(len(diggits)//2)):
        if (diggits[i] != diggits[len(diggits)-1-i]):
            return False
    return True

        
def palindromeProd():
    result = -1
    for ii in range(999,100,-1):
        for jj in range(999,100,-1):
            if testPali(ii*jj):
                print(ii*jj)
                if (ii*jj>result):
                    result = ii*jj
                    print("result is now: ", result)
    return result        

def same(n2,n3,n4,n5,n6):
    nStrings = [str(n2),str(n3),str(n4),str(n5),str(n6)]
    print(nStrings)
    for i in nStrings:
        for j in i:
            for t in nStrings:
                if j not in t:
                    return False
    return True
    
def perMult():
    t = 1
    while (True):
        if (same(t*2,t*3,t*4,t*5,t*6)):
            return t
        t += 1





