https://leetcode.com/problems/maximum-difference-score-in-a-grid/

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[-inf for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        dp[ROWS - 1][COLS - 1] = grid[-1][-1]
        
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                dp[i][j] = max(dp[i+1][j], dp[i][j+1], grid[i][j])
        
        res = -inf
        
        for i in range(ROWS):
            for j in range(COLS):
                if i < ROWS - 1:
                    res = max(res, dp[i+1][j] - grid[i][j])
                if j < COLS - 1:
                    res = max(res, dp[i][j+1] - grid[i][j])

        return res
