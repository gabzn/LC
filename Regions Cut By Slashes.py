https://leetcode.com/problems/regions-cut-by-slashes/

"""
   --------- 
   |   0   |      0   
   | 3   1 |    3   1
   |   2   |      2
   ---------
   
    N
 W     E
    S
"""
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def is_in_bound(r, c):
            return 0 <= r < N and 0 <= c < N
        
        def get_directions(row, col, side):
            directions = []
            
            if side == 0:
                directions.append((row - 1, col, 2))
                if grid[row][col] != '/':
                    directions.append((row, col, 1))
                if grid[row][col] != '\\':
                    directions.append((row, col, 3))
                    
            if side == 1:
                directions.append((row, col + 1, 3))
                if grid[row][col] != '/':
                    directions.append((row, col, 0))
                if grid[row][col] != '\\':
                    directions.append((row, col, 2))
                    
            if side == 2:    
                directions.append((row + 1, col, 0))
                if grid[row][col] != '/':
                    directions.append((row, col, 3))
                if grid[row][col] != '\\':
                    directions.append((row, col, 1))
                    
            if side == 3:
                directions.append((row, col - 1, 1))
                if grid[row][col] != '/':
                    directions.append((row, col, 2))
                if grid[row][col] != '\\':
                    directions.append((row, col, 0))
                    
            return directions
        
        def dfs(row, col, side):
            visited.add((row, col, side))
            stack = [(row, col, side)]
            
            while stack:
                r, c, s = stack.pop()
                
                for next_r, next_c, next_side in get_directions(r, c, s):
                    if is_in_bound(next_r, next_c) and (next_r, next_c, next_side) not in visited:
                        visited.add((next_r, next_c, next_side))
                        stack.append((next_r, next_c, next_side))
                       
        N = len(grid)        
        visited = set()
        res = 0
        
        for r in range(N):
            for c in range(N):
                for side in range(4):
                    if (r, c, side) not in visited:
                        dfs(r, c, side)
                        res += 1
        return res
