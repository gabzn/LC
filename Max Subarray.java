class Solution 
{
    public int maxSubArray(int[] nums) 
    {
        if(nums.length == 1) return nums[0];
        
        // Assume the first element is the max.
        int maxSum = nums[0];
        int currentSum = nums[0];
        
        // Loop starts at the second element.
        for(int i=1;i<nums.length;i++)
        {
            // If nums[i] itself is greater than the sum of all previous numbers,
            // that means we'll be better off dropping all previous numbers, and use nums[i] as our new starting point.
            if(nums[i] > (currentSum + nums[i])) currentSum = nums[i];
            else currentSum = currentSum + nums[i];
            
            if(maxSum < currentSum) maxSum = currentSum;
        }
        return maxSum;
    }
}
