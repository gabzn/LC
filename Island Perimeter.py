https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def is_water(x, y):
            if x == -1 or x == ROWS or y == -1 or y == COLS:
                return True
            return grid[x][y] == 0
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        res = 0
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    for offset_x, offset_y in DIRECTIONS:
                        res += is_water(offset_x + x, offset_y + y)
    
        return res
