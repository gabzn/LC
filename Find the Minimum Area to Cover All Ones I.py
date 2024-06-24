https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        min_x = 1001
        max_x = 0
        
        min_y = 1001
        max_y = 0
        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)
        
        x = max_x - min_x + 1
        y = max_y - min_y + 1
        return x * y
