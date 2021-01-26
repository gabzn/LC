class Solution 
{
    public void moveZeroes(int[] nums) 
    {
        int pointer = 0;
        
        // Two-pointer approach
        for(int i=0;i<nums.length;i++)
        {
            // Find the non-zero element, and swap it with the value that pointer is currently pointing to.
            
            // If the current value is 0, go to next iteration until the current value is NOT 0.
            // Now the current value is NOT 0, swap the current value with nums[pointer]. Move pointer 1 unit to its right.
            if(nums[i] == 0) continue;
            else
            {
                int temp = nums[pointer];
                nums[pointer] = nums[i];
                nums[i] = temp;
                
                pointer++;
            }
        }
        
    }
}


Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
