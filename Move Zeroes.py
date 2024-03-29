https://leetcode.com/problems/move-zeroes/
  
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
  
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
