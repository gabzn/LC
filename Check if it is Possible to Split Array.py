https://leetcode.com/problems/check-if-it-is-possible-to-split-array/
https://leetcode.com/problems/check-if-it-is-possible-to-split-array/discuss/3870201/Python-oror-Beats-100-oror-Easy-oror-Understandable

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) <= 2:
            return True
          
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] >= m:
                return True
              
        return False   
