def edit_distance ( a , b ):
    T = [[float(" inf ")] * (len(b)+1) for _ in range (len(a)+1)]
    for i in range (len(a)+1):
        T[i][0] = i
    for j in range (len(b)+1):
        T[0][j] = j
    for i in range (1 ,len(a)+1):
        for j in range (1 ,len(b)+1):
            diff = 0 if a [i-1] == b [ j-1 ] else 1
            T[i][j] = min(T[i-1][j] + 1 , T[i][j-1] + 1 , T[i-1][j-1] + diff )
    return T[len(a)][len(b)]
    
# print ( edit_distance ( a="distance" , b="editing" ) )
