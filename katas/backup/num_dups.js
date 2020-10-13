const nums  = [1,1,2,4,5,6,7,7,7,7,7,8,9,9,9,9,99,9]

function removeDups(nums){
    let bag = {};
    nums.forEach(element => {
        bag[element] ? bag[element] += 1 : bag[element] = 1;
    });
    return Object.keys(bag).map(i => parseInt(i));
}

// console.log(removeDups(nums));

function removeInPlace(nums){
   nums.forEach( (element,i) => {
        console.log('here i:',i)
        if (nums[i] === nums[i-1] && i > 0){
            console.log('in here true');
            nums.splice(i-1,1);
        }
    });
    return nums;
}

console.log(removeInPlace(nums));
