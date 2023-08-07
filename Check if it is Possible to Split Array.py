https://leetcode.com/problems/check-if-it-is-possible-to-split-array/
https://leetcode.com/problems/check-if-it-is-possible-to-split-array/discuss/3870201/Python-oror-Beats-100-oror-Easy-oror-Understandable

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) <= 2:
            return True

        N = len(nums)
        
        @cache
        def dp(start, end):
            # If there's only 1 digit, True
            if end - start == 1:
                return True
            # If there are 2 digits and the sum is greater than m, True
            if end - start == 2:
                return sum(nums[start: end]) >= m

            for i in range(start + 1, end):
                if dp(start, i) and dp(i, end):
                    return True
            return False
               
        for i in range(1, N):
            if dp(0, i) and dp(i, N):
                return True
            
        return False
---------------------------------------------------------------------
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) <= 2:
            return True
          
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] >= m:
                return True
              
        return False   
