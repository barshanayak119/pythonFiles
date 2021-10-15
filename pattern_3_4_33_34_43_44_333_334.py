def print_pattern(n):
    a = [3, 4]
    for i in range(n):
        a += [a[i]*10+3]
        a += [a[i]*10+4]
    return a[:n]

#print(*print_pattern(5)) <!-- 3 4 33 34 43 -->
#print(*print_pattern(20)) <!-- 3 4 33 34 43 44 333 334 343 344 433 434 443 444 3333 3334 3343 3344 3433 3434 -->
