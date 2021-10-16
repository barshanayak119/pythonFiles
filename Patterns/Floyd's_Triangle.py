def pattern():
    print('Number of rows : ', end = "")
    r = int(input())
    print()
    n = 1
    for i in range(r):
        for j in range(i+1):
            print(n, end = " ")
            n += 1
        print()


if __name__ == '__main__':
    pattern()
