def spiral_traversal(a, R, C):
    r, c, R, C = 0, 0, R, C
    while r<R and c<C:
        for i in range(c, C):
            print(a[r][i], end = " ")
        r+=1
        for i in range(r, R):
            print(a[i][C-1], end = " ")
        C-=1
        if (r < R) :
            for i in range(C-1, c-1, -1):
                print(a[R-1][i], end = " ")
        R-=1
        for i in range(R-1, r-1, -1):
            print(a[i][c], end = " ")
        c+=1

# a= [[1, 2, 3, 4, 5, 6],
#    [7, 8, 9, 10, 11, 12],
#    [13, 14, 15, 16, 17, 18]]
# r, c = 3, 6
# spiral_traversal(a,r,c)
