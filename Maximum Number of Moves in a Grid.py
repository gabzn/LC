https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        @cache
        def dfs(x, y, moves):    
            max_moves = moves
            
            for offset_x, offset_y in DIRECTIONS:
                next_x = x + offset_x
                next_y = y + offset_y
                if is_valid_cell(next_x, next_y) and \
                   grid[x][y] < grid[next_x][next_y]:
                    max_moves = max(max_moves, dfs(next_x, next_y, moves + 1))
            
            return max_moves
        
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(-1, 1), (0, 1), (1, 1)]
        
        res = 0
        for row in range(ROWS):
            res = max(res, dfs(row, 0, 0))
        return res
-----------------------------------------------------------------------------------------
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        @cache
        def dfs(x, y):    
            max_moves = 0
            
            for offset_x, offset_y in DIRECTIONS:
                next_x = x + offset_x
                next_y = y + offset_y
                if is_valid_cell(next_x, next_y) and \
                   grid[x][y] < grid[next_x][next_y]:
                    max_moves = max(max_moves, 1 + dfs(next_x, next_y))
            
            return max_moves
        
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(-1, 1), (0, 1), (1, 1)]
        
        res = 0
        for row in range(ROWS):
            res = max(res, dfs(row, 0))
        return res
