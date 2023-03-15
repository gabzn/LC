https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
  
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N, M = len(nums), len(multipliers)
        
        # dp(i, l, r) returns the max score at the i-th operation with l and r
        def dp(i, l, r, memo):
            if i == M:
                return 0
            
            if (i, l, r) not in memo:
                mul = multipliers[i]
                take_left = mul * nums[l] + dp(i + 1, l + 1, r, memo)
                take_right = mul * nums[r] + dp(i + 1, l, r - 1, memo)
                
                memo[(i, l, r)] = max(take_left, take_right)
                
            return memo[(i, l, r)]
        
        return dp(0, 0, N - 1, {})
