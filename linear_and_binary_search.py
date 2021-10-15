def binary_search(item_list, item):
    first = 0
    last = len(item_list)-1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        if item_list[mid] == item :
            found = True
            return mid
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1    
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1
