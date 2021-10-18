def heapsort(a):

    def swap(a,i,j):
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp

    def siftdown(a, i, size):
        l = 2*i+1
        r = 2*i+2
        largest = i
        if l <= size-1 and a[l] > a[i]:
            largest = l
        if r <= size-1 and a[r] > a[largest]:
            largest = r
        if largest != i:
            swap(a, i, largest)
            siftdown(a, largest, size)

    def heapify(a, size):
        p = (size//2)-1
        while p>=0:
            siftdown(a, p, size)
            p -= 1

    size = len(a)
    heapify(a, size)
    end = size-1
    while(end > 0):
        swap(a, 0, end)
        siftdown(a, 0, end)
        end -= 1

arr = [1,3,2,4,9,7]
heapsort(arr)
print(arr)

