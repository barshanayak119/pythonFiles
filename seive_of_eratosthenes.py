def find_primes_in_range(n):
    if n<=1: return []
    lst = [1]*(n+1)
    lst[0]=0
    lst[1]=0
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i*j>n:
                break
            if lst[i]:
                lst[i*j]=0
            else:
                break
    primes = [i for i in range(n) if lst[i]]
    return primes

#print(find_primes_in_range(10**5)
