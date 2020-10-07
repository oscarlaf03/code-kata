groupSizes = [2,1,3,3,3,2,3,3]

def group(groupSizes):
    res =[]
    tracker = {}
    for i in range(len(groupSizes)):
        if groupSizes[i] not in tracker:
          tracker[groupSizes[i]] = [i]
        else:
          tracker[groupSizes[i]].append(i)

    for (size,elements) in tracker.items():
        if len(elements) <= size:
            res.append(elements)
        else:
            i = 0
            while i < len(elements):
                res.append(elements[i:min(i + size, len(elements))])
                i += size
    return res

final_answer = group(groupSizes)

print(final_answer)