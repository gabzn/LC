https://leetcode.com/problems/minimum-falling-path-sum/
  
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS

        @cache
        def dp(x, y):
            if x == ROWS - 1:
                return matrix[x][y]
            
            best = inf
            for offset_x, offset_y in DIRECTIONS:
                next_x, next_y = offset_x + x, offset_y + y
                if is_valid(next_x, next_y):
                    best = min(best, dp(next_x, next_y))
            
            return matrix[x][y] + best        
        
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRECTIONS = [(1, -1), (1, 0), (1, 1)]
        
        res = inf
        
        for c in range(COLS):
            res = min(res, dp(0, c))
        
        return res
--------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        dp = [[matrix[r][c] for c in range(N)] for r in range(N)]
        
        for r in range(1, N):
            for c in range(N):
                if 0 < c < N - 1:
                    dp[r][c] = matrix[r][c] + min(dp[r - 1][c], dp[r - 1][c + 1], dp[r - 1][c - 1])
                if c == 0:
                    dp[r][c] = matrix[r][c] + min(dp[r - 1][c], dp[r - 1][c + 1])
                if c == N - 1:
                    dp[r][c] = matrix[r][c] + min(dp[r - 1][c], dp[r - 1][c - 1])
         
        return min(dp[-1])
--------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        
        for r in range(1, N):
            for c in range(N):
                if 0 < c < N - 1:
                    matrix[r][c] = matrix[r][c] + min(matrix[r - 1][c], matrix[r - 1][c + 1], matrix[r - 1][c - 1])
                if c == 0:
                    matrix[r][c] = matrix[r][c] + min(matrix[r - 1][c], matrix[r - 1][c + 1])
                if c == N - 1:
                    matrix[r][c] = matrix[r][c] + min(matrix[r - 1][c], matrix[r - 1][c - 1])
                               
        return min(matrix[-1])
