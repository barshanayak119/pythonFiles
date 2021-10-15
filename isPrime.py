def isPrime(n):
    if n==2:
        return 1
    if n%2==0:
        return 0
    else:
        for i in range(3, n//2+1):
            if n%i==0:
                return 0
        return 1

#print(isPrime(29))
