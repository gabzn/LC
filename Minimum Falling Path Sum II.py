https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if i == N:
                return 0
            
            res = inf
            for c in range(N):
                if c != j:
                    res = min(res, dp(i + 1, c))
            
            if res == inf:
                return grid[i][j]
            return res + grid[i][j]
        
        N = len(grid)
        res = inf
        for c in range(N):
            res = min(res, dp(0, c))
        return res
