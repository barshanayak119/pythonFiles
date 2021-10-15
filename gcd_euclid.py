#GCD - Euclidean Algo(Recursion)

def gcd(x, y):
    if x==0:
        return y
    else:
        return gcd(y%x, x)

#print(gcd(4,6))
