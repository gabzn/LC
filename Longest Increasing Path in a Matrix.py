https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dp(x, y):
            if memo[x][y] > 1:
                return memo[x][y]
            
            res = 1
            for offset_x, offset_y in DIRECTIONS:
                adjacent_x, adjacent_y = offset_x + x, offset_y + y
                
                if 0 <= adjacent_x < ROWS and 0 <= adjacent_y < COLS and matrix[adjacent_x][adjacent_y] > matrix[x][y]:
                    res = max(res, 1 + dp(adjacent_x, adjacent_y))
            
            memo[x][y] = res
            return res
        
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        memo = [[1 for _ in range(COLS)] for _ in range(ROWS)]
        res = 1
        
        for x in range(ROWS):
            for y in range(COLS):
                res = max(res, dp(x, y))
            
        return res
