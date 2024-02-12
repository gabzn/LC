https://leetcode.com/problems/cherry-pickup-ii/

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        @cache
        def dp(row, col_1, col_2):        
            res = 0
            if col_1 == col_2:
                res = grid[row][col_1]
            else:
                res = grid[row][col_1] + grid[row][col_2]
                
            best = 0
            for i in DIRECTIONS:
                for j in DIRECTIONS:
                    if is_valid_cell(row + 1, col_1 + i) and is_valid_cell(row + 1, col_2 + j):
                        best = max(best, dp(row + 1, col_1 + i, col_2 + j))
            
            return res + best
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [-1, 0, 1]
        return dp(0, 0, COLS - 1)
