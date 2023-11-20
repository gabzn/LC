https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
  
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pref = [nums[0]]
        for i in range(1, len(nums)):
            pref.append(pref[-1] + nums[i])
        
        min_val = min(pref)
        return 1 if min_val > 0 else abs(min_val) + 1
----------------------------------------------------------------------------
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        def no_negative(m):
            for num in nums:
                m += num
                if m <= 0:
                    return False
            
            return True
        
        l, r = 0, 1000000
        
        while l + 1 != r:
            m = (l + r) // 2
            
            if no_negative(m):
                r = m
            else:
                l = m
        
        return r
