#LCM - Prime Factorisation

from collections import Counter

def prime_factors(x):
    factors = []
    if x%2==0:
        while x%2==0 and x:
            factors += [2]
            x//=2
    for i in range(3, x+1):
        if x%i==0:
            while x%i==0 and x:
                factors += [i]
                x//=i
        if x<=0:
            break
    return factors

def LCM(lst):
    n = len(lst)
    if n==0:
        return 0

    all_factors = []
    for x in lst:
        all_factors += [prime_factors(x)]

    common = set(all_factors[0])
    for i in range(1, n):
        common = common.union(set(all_factors[i]))
    ans = 1
    for i,x in enumerate(common):
        mx = 1
        for i in range(n):
            mx = max(mx, all_factors[i].count(x))
        ans *= x**mx
    return ans

#LCM([4, 6, 2])
