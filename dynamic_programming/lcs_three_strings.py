def lc_sequence(T, a, b):
    st = []
    n = len(T) 
    m = len(T[0])
    for j in range(m-1, 0, -1):
        for i in range(n-1, 0, -1):
            if T[i][j]>T[ i-1 ][ j ]  and T[i][j]>T[ i ][ j-1 ] and T[i][j]>T[i-1][j-1]:
                if (j-1)-a.index(b[j-1])>=0:
                    st += [b[j-1]]
                    i-=1
                    continue
    return st[::-1]

def lcs2 ( a , b ) :
    T = [ [ float ( " inf " ) ] * ( len ( b ) + 1) for _ in range ( len ( a ) + 1 ) ]
    for i in range ( len ( a ) + 1 ) :
        T[ i ] [ 0 ] = 0
    for j in range ( len ( b ) + 1 ) :
        T[ 0 ] [ j ] = 0
    for i in range ( 1 , len ( a ) + 1 ) :
        for j in range ( 1 , len ( b ) + 1 ) :
            diff = 1 if a [i-1] == b [ j-1 ] else 0
            T[ i ] [ j ] = max(T[ i-1 ][ j ] , T[ i ][ j-1 ] , T[ i-1 ][ j-1 ] + diff )
    st = lc_sequence(T, a, b)
    return T[len(a)][len(b)], st

def lcs3 (a, b, c):
    _, inter = lcs2(a, b)
    return lcs2(inter, c)[0]

# print(lcs3([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]))
# print(lcs3("edit", "distance", "editing"))
