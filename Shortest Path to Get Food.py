https://leetcode.com/problems/shortest-path-to-get-food/

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        def bfs():
            while queue:
                x, y, steps = queue.popleft()
                if (x, y) in visited_cells:
                    continue
                visited_cells.add((x, y))

                for offset_x, offset_y in DIRECTIONS:
                    adjacent_x, adjacent_y = offset_x + x, offset_y + y
                
                    if is_valid_cell(adjacent_x, adjacent_y) and grid[adjacent_x][adjacent_y] != 'X':
                        if grid[adjacent_x][adjacent_y] == '#':
                            return steps + 1
                        queue.append((adjacent_x, adjacent_y, steps + 1))
                
            return -1
                 
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        visited_cells = set()
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != '*':
                    continue
                    
                queue.append((r, c, 0))
                return bfs()
