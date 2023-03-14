https://leetcode.com/problems/minimum-path-sum/
  
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
