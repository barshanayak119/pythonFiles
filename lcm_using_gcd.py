#lcm using gcd

def gcd(x, y):
    if x==0:
        return y
    else:
        return gcd(y%x, x)

def lcm(x, y):
    return (x*y)//gcd(x,y)

#print(lcm(4,6))
