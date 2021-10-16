def pattern():
    print("Height of the pyramid : ", end = "")
    h = int(input())
    print()
    for i in range(h):
        for j in range(i+1):
            print('*', end = " ")
        print()


if __name__ == '__main__':
    pattern()
