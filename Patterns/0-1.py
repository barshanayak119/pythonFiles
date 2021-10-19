def pattern():
    n = int(input("Enter the height of the pattern : "))
    for i in range(1, n+1):
        for j in range(1, i+1):
            if (i+j)%2 == 0:
                print(1, end = " ")
            else:
                print(0, end = " ")
        print()

if __name__ == '__main__':
    pattern()
