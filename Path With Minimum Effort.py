https://leetcode.com/problems/path-with-minimum-effort/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        l, r = -1, 1000002
        
        while l + 1 != r:
            m = (l + r) // 2
            
            if self.dfs(heights, m, directions):
                r = m
            else:
                l = m
        
        return r
    
    def dfs(self, grid, max_effort, directions):
        ROW, COL = len(grid), len(grid[0])
        visited_cells = set()
        stack = [(0, 0, grid[0][0])]
        
        while stack:
            x, y, current_height = stack.pop()
            if x == (ROW - 1) and y == (COL - 1):
                return True
            
            if (x, y) in visited_cells:
                continue
            visited_cells.add((x, y))
            
            for offset_x, offset_y in directions:
                neighbour_x, neighbour_y = offset_x + x, offset_y + y
                
                if 0 <= neighbour_x < ROW and 0 <= neighbour_y < COL and \
                    abs(grid[neighbour_x][neighbour_y] - current_height) <= max_effort:
                    stack.append((neighbour_x, neighbour_y, grid[neighbour_x][neighbour_y]))
                        
        return False
