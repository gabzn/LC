https://leetcode.com/problems/minimum-falling-path-sum/
  
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:        
        def dp(r, c, memo):
            if c == N or c == -1:
                return math.inf
            if r == N - 1:
                return matrix[r][c]
            if (r, c) in memo:
                return memo[(r, c)]
                                                # diagonally left       # directly below     # diagonally right
            memo[(r, c)] = matrix[r][c] + min(dp(r + 1, c - 1, memo), dp(r + 1, c, memo), dp(r + 1, c + 1, memo))
            return memo[(r, c)]
        
        N, res, memo = len(matrix), math.inf, {}
        
        for c in range(N):
            res = min(res, dp(0, c, memo))
            
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
