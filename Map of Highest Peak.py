https://leetcode.com/problems/map-of-highest-peak/

class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        def is_valid_land_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 0
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        res = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        queue = deque()
        
        # Find all the water cells
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r, c, 0))
        
        # Perform a multi-source BFS
        while queue:
            n = len(queue)
            
            for _ in range(n):
                x, y, height = queue.popleft()
                
                for offset_x, offset_y in DIRECTIONS:
                    adjacent_x, adjacent_y = x + offset_x, y + offset_y
                    
                    if is_valid_land_cell(adjacent_x, adjacent_y):
                        new_height = height + 1
                        
                        res[adjacent_x][adjacent_y] = new_height
                        queue.append((adjacent_x, adjacent_y, new_height))
                        
                        grid[adjacent_x][adjacent_y] = 1
        
        return res
