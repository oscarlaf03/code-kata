const p = console.log;
let nums = [1,2,3,4,4,3,2,1];
let n = nums.length/2;
let result = []
for(let i =0; i < n; i++){
    result.push(nums[i]);
    result.push(nums[n+i]);
};
p(nums);
p(result);