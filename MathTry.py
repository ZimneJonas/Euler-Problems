
def fun():
    var = 1
    t=0
    end = (3800000//0.95)
    while(True):
        t += 1
        
        var = (4*(1-(var/3800000)))**t
        print(var , t) 
        
        if (var > end):
            return(t)

print(fun())