https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        def is_valid_cell(x, y):
            return (0 <= x < N) and (0 <= y < N) and (grid[x][y] == 0)
        
        N = len(grid)
        queue = deque([(0, 0, 1)])
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        
        while queue:
            x, y, current_length = queue.popleft()
            if x == y == N - 1:
                return current_length
                        
            for offset_x, offset_y in directions:
                neighbour_x, neighbour_y = x + offset_x, y + offset_y
                if is_valid_cell(neighbour_x, neighbour_y):
                    queue.append((neighbour_x, neighbour_y, current_length + 1))
                    
                    # After we add it to the queue, we mark it as 1 to avoid revisiting
                    grid[neighbour_x][neighbour_y] = 1
                            
        return -1
------------------------------------------------------------------------------------------
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        def is_valid_cell(x, y):
            return (0 <= x < N) and (0 <= y < N) and (grid[x][y] == 0)
        
        N, length = len(grid), math.inf
        visited_cells = set()
        queue = deque()
        queue.append((0, 0, 1))

        while queue:
            x, y, current_length = queue.popleft()
            
            # One of the paths reaches bottom-right, we check the length
            if x == N - 1 and y == N - 1:
                length = min(length, current_length)
                continue
            
            if (x, y) in visited_cells:
                continue
            visited_cells.add((x, y))
            
            neighbour_cells = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
            for neighbour_x, neighbour_y in neighbour_cells:
                if is_valid_cell(neighbour_x, neighbour_y):
                    queue.append((neighbour_x, neighbour_y, current_length + 1))
                            
        return length if length != math.inf else -1
---------------------------------------------------------------------------------------------------------------------
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        def is_valid_cell(x, y):
            return (0 <= x < N) and (0 <= y < N) and (grid[x][y] == 0)
        
        N = len(grid)
        queue = deque([(0, 0, 1)])
        
        while queue:
            x, y, current_length = queue.popleft()
            if x == y == N - 1:
                return current_length
                        
            neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
            for neighbour_x, neighbour_y in neighbours:
                if is_valid_cell(neighbour_x, neighbour_y):
                    queue.append((neighbour_x, neighbour_y, current_length + 1))
                    
                    # After we add it to the queue, we mark it as 1 to avoid revisiting
                    grid[neighbour_x][neighbour_y] = 1
                            
        return -1
