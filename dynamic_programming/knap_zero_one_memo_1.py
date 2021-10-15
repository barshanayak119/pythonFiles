def knap_zero_one(wt, val, w, n):
    if n==0 or w==0:
        return 0
    if dp[n][w]!=-1:
        return dp[n][w]
    if wt[n-1]<=w:
        dp[n][w] = max(val[n-1] + knap_zero_one(wt, val, w-wt[n-1], n-1), knap_zero_one(wt, val, w, n-1))
        return dp[n][w]
    else:
        dp[n][w] = knap_zero_one(wt, val, W, n-1)
        return dp[n][w]

val = [60, 100, 120]
wt = [2, 5, 3]
W = 5
n = 3
dp = [[-1]*(W+1) for i in range(n+1)]
# print(knap_zero_one(wt, val, W, n))
# for x in dp:
#     print(*x)
