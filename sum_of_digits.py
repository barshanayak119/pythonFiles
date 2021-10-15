def sumOfDigits(n):
    if len(str(n))==1:
        return n
    else:
        s = sum(str(map(int, n)))
        sumOfDigits(n)

#print(sumOfDigits(123456789))
