def binary_search(my_list, ele):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if my_list[middle] == ele:
            return middle+1
        elif my_list[middle] < ele:
            low = middle + 1
        else:
            high = middle - 1
    return -1

if __name__ == '__main__':
    print('Enter the elements in increasing order')
    my_list = [int(x) for x in input().split()]
    # my_list = [0, 1, 3, 4, 7, 8, 9]
    print('\nEnter the element to be searched')
    ele = int(input())
    pos = binary_search(my_list, ele)
    if pos > 0:
        print("\nElement found at", pos)
    else:
        print("\nElement not found")
