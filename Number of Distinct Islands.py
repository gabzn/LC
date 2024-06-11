https://leetcode.com/problems/number-of-distinct-islands/

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def is_land_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 1
        
        def dfs(r, c):
            island = []            
            visited_cells.add((r, c))
            stack.append((r, c))
            
            while stack:
                x, y = stack.pop()
                island.append((x - r, y - c))
                
                for offset_x, offset_y in DIRECTIONS:
                    next_x = offset_x + x
                    next_y = offset_y + y
                    
                    if is_land_cell(next_x, next_y) and (next_x, next_y) not in visited_cells:
                        stack.append((next_x, next_y))
                        visited_cells.add((next_x, next_y))
            
            unique_islands.add(tuple(island))
        
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        unique_islands = set()
        visited_cells = set()
        stack = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited_cells:
                    dfs(r, c)
        
        return len(unique_islands)
