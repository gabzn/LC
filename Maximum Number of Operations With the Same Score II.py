https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache
        def dp(left, right, score):
            if right - left < 1:
                return 0
            
            res = 0
            
            if nums[left] + nums[left + 1] == score:
                res = max(res, 1 + dp(left + 2, right, score))
            
            if nums[left] + nums[right] == score:
                res = max(res, 1 + dp(left + 1, right - 1, score))
            
            if nums[right] + nums[right - 1] == score:
                res = max(res, 1 + dp(left, right - 2, score))
            
            return res
        
        LEN = len(nums)
        return 1 + max(dp(2, LEN - 1, nums[0] + nums[1]), 
                       dp(0, LEN - 3, nums[-1] + nums[-2]),
                       dp(1, LEN - 2, nums[0] + nums[-1]))
