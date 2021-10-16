def binaryS(arr, l, r, x):
     if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binaryS(arr, l, mid-1, x)
        else:
            return binaryS(arr, mid + 1, r, x)
     else:
        return -1

arr = [ 100, 234, 453, 143, 537]
x = 537
result = binaryS(arr, 0, len(arr)-1, x)
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")
