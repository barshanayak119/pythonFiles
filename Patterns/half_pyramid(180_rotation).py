def pattern():
    print("Height of the pyramid : ", end = "")
    h = int(input())
    print()
    for i in range(h):
        for j in range(h):
            if j < h-i-1:
                print(" ", end = " ")
            else:
                print('*', end = " ")
        print()


if __name__ == '__main__':
    pattern()
