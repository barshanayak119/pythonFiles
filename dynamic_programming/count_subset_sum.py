#count_subset_sum

def count_subset_sum(wt, w, n):
    t = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1
            elif wt[i-1]<=j:
                t[i][j] = t[i-1][j-wt[i-1]] + t[i-1][j]
            elif wt[i-1]>j:
                t[i][j] = t[i-1][j]
    return t[n][w]
    
#wt = [2, 5, 3, 1, 10, 7] 
#w = 10
#n = len(wt)
#t = [[0 for i in range(w+1)] for j in range(n+1)]
#print(count_subset_sum(wt, w, n)) 
