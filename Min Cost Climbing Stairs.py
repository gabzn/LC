https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.climb(cost, len(cost), {})
    
    # climb(i) tells us the min cost to be on i-th step
    # whereas memo[i] tells us the min cost to reach the i-th step
    # the difference is to be on the i-th step, you need to pay the i-1 or i-2 cost
    def climb(self, cost, i, memo):
        if i <= 1:
            return 0
        
        if i not in memo:
            memo[i] = min(cost[i - 1] + self.climb(cost, i - 1, memo), cost[i - 2] + self.climb(cost, i - 2, memo))
        
        return memo[i]
-----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        LEN = len(cost)
        dp = [0] * (LEN + 1)
        
        for i in range(2, LEN + 1):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        
        return dp[-1]
