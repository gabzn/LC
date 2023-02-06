https://leetcode.com/problems/monotonic-array/
  
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        is_increasing = nums[0] <= nums[1]
        is_decreasing = nums[0] >= nums[1]
        
        for idx in range(2, len(nums)):
            if not nums[idx] >= nums[idx - 1]:
                is_increasing = False
            
            if not nums[idx] <= nums[idx - 1]:
                is_decreasing = False
                
        return is_increasing or is_decreasing
