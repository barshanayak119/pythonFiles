@functools.lru_cache()
def fib(n):
    if n==0:
        return 0
    elif 0>n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        
#print(fib(1000))
