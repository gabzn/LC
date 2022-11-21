https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
  
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if not maze:
            return -1
        
        R, C = len(maze), len(maze[0])
        steps = math.inf
        
        visited_cells = set()
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        
        while queue:
            r, c, cur_step = queue.popleft()
            
            if (r, c) in visited_cells:
                continue
            visited_cells.add((r, c))
            
            # If the entrance is at the border, it cannot be counted as an exit.
            if cur_step != 0 and self.is_an_exit(maze, R, C, r, c):
                steps = min(steps, cur_step)
                continue
            
            neighbours = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for neighbour in neighbours:
                neighbour_r, neighbour_c = neighbour
                
                if self.is_a_cell(maze, R, C, neighbour_r, neighbour_c):
                    queue.append((neighbour_r, neighbour_c, cur_step+1))
                
        return steps if steps != math.inf else -1
    
    def is_an_exit(self, maze, R, C, r, c):
        return r == 0 or r == R-1 or c == 0 or c == C-1
    
    def is_a_cell(self, maze, R, C, r, c):
        return 0 <= r < R and 0 <= c < C and maze[r][c] == '.'
