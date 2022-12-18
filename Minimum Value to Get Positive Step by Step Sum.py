https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
  
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_start_val = nums[0]
        
        for ind in range(1, len(nums)):
            nums[ind] = nums[ind - 1] + nums[ind]
            min_start_val = min(min_start_val, nums[ind])
        
        if min_start_val > 0:
            return 1
        return abs(min_start_val) + 1
