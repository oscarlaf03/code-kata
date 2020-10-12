def jewels(J,S):
    j = set(J)
    stones = list(S)
    count = 0
    for s in stones:
        if s in j:
            count+=1
    return count
