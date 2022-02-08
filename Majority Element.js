Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

var majorityElement = function(nums) {
    if(nums.length === 1) return nums[0];
    
    let count_map = {}
    
    for(let num of nums) {
        if(count_map[num]) {
            if(++count_map[num] > (nums.length / 2))
                return num;
        } else count_map[num] = 1;
    }
};
