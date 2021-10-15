#sum of 3 or 5 multiples

def fac3or5_method_1(n):
    s = 0
    for i in range(1, n):
        if i%3==0 or i%5==0:
            s += i
    return s




#sum of 3 or 5 multiples :: aliter

from functools import reduce
def fac3or5_method_2(n):
    return reduce(lambda x,y: x+y, filter(lambda n: n%3==0 or n%5==0, range(n)))




#sum of 3 or 5 multiples :: aliter-2

def fac3or5_method_3(n):
    n3 = n//3
    n5 = n//5
    n15 = n//15
    sum3 = 3*(n3*(n3+1)//2)
    sum5 = 5*(n5*(n5+1)//2)
    sum15 = 15*(n15*(n15+1)//2)
    return sum3+sum5-sum15

#print(fac3or5_method_1(30))
#print(fac3or5_method_2(30))
#print(fac3or5_method_3(30))
