from random import randint
MIN = 1
MAX = 10
SIZE = MAX

def positive_int(max = MAX, min = MIN):
    return randint(min,max)

my_target = positive_int()
def sorted_array( size = SIZE , max = MAX):
    arr = []
    for i in range(size):
        arr.append(positive_int(max))
    arr.sort()
    return arr

print(my_target)

my_list = sorted_array()
print(my_list)

print(my_target in my_list)

def bin_search(arr,target):
    low = 0
    high = len(arr) -1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if target > arr[mid]:
            low += 1
        elif target < arr[mid]:
            high -= 1
        else:
            print('found and "bin_search":  ')
            return mid
    print('NOT found on "bin_search":  ')
    return -1

print("\n\nreturning from 'bin_search' \n\n")
print(bin_search(my_list,my_target))