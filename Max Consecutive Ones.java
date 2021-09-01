Given a binary array, find the maximum number of consecutive 1s in this array.

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
             The maximum number of consecutive 1s is 3.
  

class Solution 
{
    public int findMaxConsecutiveOnes(int[] nums) 
    {
        if(nums.length == 0) return 0;
    
        // Classical sliding-windom problem.
        // Two pointers, right to find how many ones are there now.
        // Left to hold the max number of consecutive 1s.
        int left = 0;
        int right = 0;
        
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i] == 1) 
            {
                right++;
                left = Math.max(left,right);
            }
            else right = 0;
        }
        return left;
    }
}
