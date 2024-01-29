https://leetcode.com/problems/paint-house/

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        LEN = len(costs)
        
        dp = [[0, 0, 0] for _ in range(LEN)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        
        for i in range(1, LEN):
            # paint the current house 0, depending on the previous 1 and 2
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            
            # paint the current house 1, depending on the previous 0 and 2
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            
            # paint the current house 2, depending on the previous 0 and 1            
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
        return min(dp[-1])
-----------------------------------------------------------------------------------------------
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        memo = {}
        
        # dp(i, color_index) returns the min cost to start painting house i with color_index
        def dp(i, color_index, memo):
            if i == N:
                return 0
            if (i, color_index) in memo:
                return memo[(i, color_index)]
            
            if color_index == 0:
                memo[(i, color_index)] = costs[i][color_index] + min(dp(i + 1, 1, memo), dp(i + 1, 2, memo))
            if color_index == 1:
                memo[(i, color_index)] = costs[i][color_index] + min(dp(i + 1, 0, memo), dp(i + 1, 2, memo))
            if color_index == 2:
                memo[(i, color_index)] = costs[i][color_index] + min(dp(i + 1, 0, memo), dp(i + 1, 1, memo))
            
            return memo[(i, color_index)]
        return min(dp(0, 0, memo), dp(0, 1, memo), dp(0, 2, memo))  
