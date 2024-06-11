https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def is_in_bound(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
            
        def dfs(r, c):
            stack = [(r, c)]
            visited_cells.add((r, c))
            is_next_to_boundary = False
            
            while stack:
                x, y = stack.pop()
                
                for offset_x, offset_y in DIRECTIONS:
                    next_x = offset_x + x
                    next_y = offset_y + y
                    
                    if not is_in_bound(next_x, next_y):
                        is_next_to_boundary = True
                        continue
                        
                    if ((next_x, next_y) not in visited_cells) and (grid[next_x][next_y] == 0):
                        visited_cells.add((next_x, next_y))
                        stack.append((next_x, next_y))
            
            return is_next_to_boundary
            
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        visited_cells = set()
        res = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 0) and ((r, c) not in visited_cells) and not dfs(r, c):
                    res += 1
        
        return res
