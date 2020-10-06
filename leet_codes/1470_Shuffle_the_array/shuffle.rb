nums = [1,2,3,4,4,3,2,1]
n = nums.size/2
result = []
nums.each_index do  |i| 
    if i < n 
        result <<  nums[i]
        result << nums[n+i]
    end
end

p nums
p result