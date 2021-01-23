Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].



class Solution 
{
    public int[] sortedSquares(int[] nums) 
    {
        
        // First off, square all of the elements first.
        for(int i=0;i<nums.length;i++)
        {
            nums[i] = nums[i] * nums[i];
        }
        
        // Create a new array with the same size.
        int[] newNums = new int[nums.length];
        
        // 3 pointers. left is for the beginning of the original array, and right is for the end of the original array.
        // p is for the new array starting from the end.
        int left = 0;
        int right = nums.length - 1;
        int p = right;
        
        while(p >= 0)
        {
            if(nums[left] > nums[right])
            {
                newNums[p] = nums[left];
                left++;
            }
            else
            {
                newNums[p] = nums[right];
                right--;
            }
            p--;
        }
        
        return newNums;
    }
}
