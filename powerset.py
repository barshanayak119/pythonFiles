def powerset(l):
    result = [[]]
    for x in l:
        result.extend([subset+[x] for subset in result])
    return result

#arr = [1, 2, 3]
#print(powerset(arr))
