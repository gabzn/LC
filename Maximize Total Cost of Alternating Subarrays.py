https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:    
        dp0 = dp1 = nums[0]
        for i in range(1, len(nums)):
            prev0 = dp0
            prev1 = dp1
            dp0 = max(prev0, prev1) + nums[i]
            dp1 = prev0 - nums[i]
        return max(dp0, dp1)
----------------------------------------------------------------------------
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:    
        N = len(nums)
        
        """
        dp[i][0] = the max cost from nums[0] to nums[i] and putting a + sign before nums[i]
        dp[i][1] = the max cost from nums[0] to nums[i] and putting a - sign before nums[i]
        
        When can you pick + and -?
            You can pick + for current when the previous is:
                + -> means the current starts fresh
                - -> means appending the current to previous
            
            You can pick - for current only when the previous is +
        
        dp[0][0] and dp[0][1] is always nums[0]
        """
        dp = [[0, 0] for _ in range(N)]
        dp[0][0] = dp[0][1] = nums[0]
        
        for i in range(1, N):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + nums[i]
            dp[i][1] = dp[i-1][0] - nums[i]
        
        return max(dp[-1])
