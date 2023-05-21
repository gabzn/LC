https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      
        def dp(x, y, memo):
            if x == 0 and y == 0:
                return 1
            if x < 0 or y < 0:
                return 0
            if (x, y) in memo:
                return memo[(x, y)]
            
            memo[(x, y)] = dp(x - 1, y, memo) + dp(x, y - 1, memo)
            return memo[(x, y)]
            
        return dp(m - 1, n - 1, {})  
