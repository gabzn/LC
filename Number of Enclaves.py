https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def can_walk_off_grid(x, y):
            for offset_x, offset_y in DIRECTIONS:
                adjacent_x, adjacent_y = x + offset_x, y + offset_y
                
                if adjacent_x == -1 or adjacent_x == ROWS or \
                   adjacent_y == -1 or adjacent_y == COLS:
                    return True
                
            return False    
            
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = deque()
        visited_land_cells = set()
        land_cells = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 1:
                    continue
                
                if can_walk_off_grid(r, c):
                    queue.append((r, c))
                
                land_cells += 1
        
        while queue:
            x, y = queue.popleft()
            if (x, y) in visited_land_cells:
                continue
            visited_land_cells.add((x, y))
            
            land_cells -= 1
            
            for offset_x, offset_y in DIRECTIONS:
                adjacent_x, adjacent_y = x + offset_x, y + offset_y
                
                if is_valid_cell(adjacent_x, adjacent_y) and grid[adjacent_x][adjacent_y] == 1:
                    queue.append((adjacent_x,adjacent_y))
    
        return land_cells
