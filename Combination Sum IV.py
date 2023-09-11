https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0

            res = 0
            for num in nums:
                res += dp(remaining - num)
            
            return res
        
        return dp(target)
