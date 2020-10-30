
"""There exists exactly one Pythagorean triplet 
for which a + b + c = 1000"""

def pythagoreanTriplet(Product):
    for cc in range(Product, 1, -1):
        for bb in range((Product-cc), 1, -1):
            aa = Product - cc - bb
            if (aa**2 + bb**2 == cc**2 and (aa < bb < cc)):
                print("a:" + str(aa) + " b:" + str(bb) + " c:" + str(cc))
                return aa*bb*cc



print(pythagoreanTriplet(1000))