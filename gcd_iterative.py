#Gcd iterative

def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x
    
#x, y = list(map(int, input().split()))
#print(gcd(x, y))
