https://leetcode.com/problems/the-maze/

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:     
        def is_empty_space(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and maze[x][y] == 0
        
        ROWS, COLS = len(maze), len(maze[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        visited_cells = set()
        visited_cells.add(tuple(start))
        
        queue = deque([start])
        while queue:
            x, y = queue.popleft()
            
            if x == destination[0] and y == destination[1]:
                return True
            
            for offset_x, offset_y in DIRECTIONS:
                adjacent_x, adjacent_y = offset_x + x, offset_y + y
                
                # The ball keeps rolling in the same direction until it is out of bound or hits a wall
                while is_empty_space(adjacent_x, adjacent_y):
                    adjacent_x += offset_x
                    adjacent_y += offset_y
                
                # After the while loop, the ball is either out of bound or hits a wall
                # Backtrack one step and mark the cell next to the bound or wall as visited
                adjacent_x -= offset_x
                adjacent_y -= offset_y
                
                if (adjacent_x, adjacent_y) in visited_cells:
                    continue
                visited_cells.add((adjacent_x, adjacent_y))
                queue.append((adjacent_x, adjacent_y))
        
        return False
