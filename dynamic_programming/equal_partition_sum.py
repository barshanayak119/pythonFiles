#equal_partition_sum

def subset_sum(arr, k, n):
    t = [ 0 for i in range(k+1)]
    t[0] = 1
    for i in range(n):
        for j in range(k-arr[i],-1,-1):
            if t[j]:
                t[j+arr[i]] = 1
    return t[k]

def equal_partition_sum(wt, n):
    s = sum(wt)
    if s%2==0:
        w = s//2
        return subset_sum(wt, w, n)
    else:
        return False
        
# wt = [5, 5, 1, 12] 
# n = 4
# print("Possible" if equal_partition_sum(wt, n) else "Not Possible") 
