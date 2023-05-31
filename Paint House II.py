https://leetcode.com/problems/paint-house-ii/
  
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        N, K = len(costs), len(costs[0])
        min_cost, memo = math.inf, {}
        
        def dp(i, color, memo):
            if i == N:
                return 0
            if (i, color) in memo:
                return memo[(i, color)]
            
            memo[(i, color)] = math.inf    
            for c in range(K):
                if c == color:
                    continue    
                memo[(i, color)] = min(memo[(i, color)], costs[i][color] + dp(i + 1, c, memo))
            return memo[(i, color)]
          
        for k in range(K):
            min_cost = min(min_cost, dp(0, k, memo))
        return min_cost
