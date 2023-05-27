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
