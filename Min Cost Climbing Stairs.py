https://leetcode.com/problems/min-cost-climbing-stairs/
  
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        dp = [0] * l
        
        for i in range(2, l):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
            
        return min(cost[l-1] + dp[l-1], cost[l-2] + dp[l-2])
