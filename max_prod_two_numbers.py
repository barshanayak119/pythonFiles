#max product of two numbers of a list

from itertools import combinations
import numpy as np

def aliter_1(n, l):
    maxval = 0
    for i, j in combinations(np.arange(n), 2):
        if l[i]*l[j]>maxval:
            maxval = l[i]*l[j]
    return maxval
    # O(n^2)




#max product of two numbers of a list :: aliter

def aliter_2(n, l):
    l = list(sorted(l))
    return l[-1]*l[-2]
    # O(nlog(n))

#n = int(input())
#l = list(map(int, input().split()))
#print(aliter_1(n, l))
#print(aliter_2(n, l))
