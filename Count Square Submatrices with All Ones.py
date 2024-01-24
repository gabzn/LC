https://leetcode.com/problems/count-square-submatrices-with-all-ones/
https://leetcode.com/problems/maximal-square/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        
        # dp[r][c] tells us the max len ENDING at [r][c]
        dp = [[0 for _ in range(N)] for _ in range(M)]
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 1:
                    dp[r][c] = 1
                    
                    # look at the surrounding 3 squares and pick the min
                    if r > 0 and c > 0:
                        dp[r][c] += min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                    
        return sum(chain(*dp))
