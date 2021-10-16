def pattern():
    print("Number of rows : ", end = "")
    r = int(input())
    print("\nNumber of coloumns : ", end = "")
    c = int(input())
    for i in range(r):
        for j in range(c):
            print('*', end = " ")
        print()

if __name__ == '__main__':
    pattern()
