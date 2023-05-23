https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # dp(x, y) returns the number of ways to get to [x, y]
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
-----------------------------------------------------------------------------------
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        
        for x in range(m):
            for y in range(n):
                if x > 0 and y > 0:
                    dp[x][y] = dp[x][y - 1] + dp[x - 1][y]
                if x == 0 and y > 0:
                    dp[x][y] = dp[x][y - 1]
                if y == 0 and x > 0:
                    dp[x][y] = dp[x - 1][y]
                    
        return dp[-1][-1]
