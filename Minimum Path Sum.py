https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        dp = [[0 for _ in range(N)] for _ in range(M)]
        dp[0][0] = grid[0][0]
        
        for x in range(M):
            for y in range(N):
                if x > 0 and y > 0:
                    dp[x][y] = grid[x][y] + min(dp[x - 1][y], dp[x][y - 1])
                if x == 0 and y > 0:
                    dp[x][y] = grid[x][y] + dp[x][y - 1]
                if y == 0 and x > 0:
                    dp[x][y] = grid[x][y] + dp[x - 1][y]
                    
        return dp[-1][-1]
--------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0 for n in range(N)] for m in range(M)]
        dp[0][0] = grid[0][0]
        
        for r in range(M):
            for c in range(N):
                if r == 0 and c == 0:
                    continue
                    
                grid_val = grid[r][c]
                if 0 <= r-1 < M and 0 <= c-1 < N:
                    dp[r][c] = grid_val + min(dp[r-1][c], dp[r][c-1])
                elif 0 <= r-1 < M:
                    dp[r][c] = grid_val + dp[r-1][c]
                else:
                    dp[r][c] = grid_val + dp[r][c-1]        
        
        return dp[-1][-1]
--------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        # dp(x, y) returns the min sum to get to grid[x][y]
        def dp(x, y, memo):
            if x == 0 and y == 0:
                return grid[x][y]
            if x < 0 or y < 0:
                return math.inf
            if (x, y) in memo:
                return memo[(x, y)]
            
            memo[(x, y)] = grid[x][y] + min(dp(x - 1, y, memo), dp(x, y - 1, memo))
            return memo[(x, y)]
            
        return dp(M - 1, N - 1, {})
