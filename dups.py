nums = [1,1,2,4,5,6,7,7,7,7,7,8,9,9,9,9,99,9]

def remove_dups(array):
    array.sort()
    to_remove = []
    for index,element in enumerate(array):
        if index > 0 and array[index] == array[index-1]:
            to_remove.append(index) 
    # print(to_remove)
    to_remove.reverse()
    for i in to_remove:
        del array[i]
    return array

print(remove_dups(nums))

