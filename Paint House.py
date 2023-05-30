https://leetcode.com/problems/paint-house/
  
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
