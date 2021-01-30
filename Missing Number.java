class Solution 
{
    public int missingNumber(int[] nums) 
    {
        int total = 0;
        
        // Add up all the numbers from 1 to n.
        // Minus all the numbers in the array will result in the missing number.
        for(int i=0;i<nums.length;i++)
        {
            total += (i+1);
            total -= nums[i];
        }
        
        return total;
    }
}


Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
