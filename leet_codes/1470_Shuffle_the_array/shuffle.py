"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
nums = [1,2,3,4,4,3,2,1]

n = int(len(nums)/2)

# Attempt 1
"""
Runtime: 44 ms, faster than 88.71% of Python online submissions for Shuffle the Array.
Memory Usage: 13.8 MB, less than 5.36% of Python online submissions for Shuffle the Array.
"""
shuffled_list =[]
for i  in range(len(nums)):
    if (i < n):
        shuffled_list.append(nums[i])
        shuffled_list.append(nums[n+i])
        i+=1


print('\n\n==printing results==\n\n')
print(nums)
print(shuffled_list)

#  checkou Python oneliner:
#  return[x for y in (zip(nums[:n], nums[n:])) for x in y]

