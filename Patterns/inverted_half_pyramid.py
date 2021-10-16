def pattern():
    print("Height of the pyramid : ", end = "")
    h = int(input())
    print()
    while(h):
        for i in range(h):
            print('*', end = " ")
        print()
        h -= 1


if __name__ == '__main__':
    pattern()
