https://leetcode.com/problems/shortest-bridge/


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def is_valid_cell(x, y):
            return 0 <= x < N and 0 <= y < N
         
        # Find all cells comprising island 1 and put all cells into visited_cells
        def find_island_one(r, c):
            queue = deque([(r, c)])
            
            while queue:
                x, y = queue.popleft()
                if (x, y) in visited_cells:
                    continue
                visited_cells.add((x, y))
                
                for offset_x, offset_y in DIRECTIONS:
                    adjacent_x, adjacent_y = offset_x + x, offset_y + y
                    
                    if is_valid_cell(adjacent_x, adjacent_y) and grid[adjacent_x][adjacent_y] == 1:
                        queue.append((adjacent_x, adjacent_y))
                        
                        
        # Starting from all cells of island 1, perform BFS to find the min distance to island 2
        def find_distance_to_island_two():
            queue = deque([(x, y, 0) for x, y in visited_cells])            
            while queue:
                x, y, distance = queue.popleft()
                
                for offset_x, offset_y in DIRECTIONS:
                    adjacent_x, adjacent_y = offset_x + x, offset_y + y
                    
                    if is_valid_cell(adjacent_x, adjacent_y) and (adjacent_x, adjacent_y) not in visited_cells:
                        if grid[adjacent_x][adjacent_y] == 1:
                            return distance
                        
                        if grid[adjacent_x][adjacent_y] == 0:
                            visited_cells.add((adjacent_x, adjacent_y))
                            queue.append((adjacent_x, adjacent_y, distance + 1))

        N = len(grid)
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited_cells = set()
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    find_island_one(r, c)
                    return find_distance_to_island_two()
------------------------------------------------------------------------------------------------------
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def is_valid_cell(x, y):
            return 0 <= x < N and 0 <= y < N
         
        # Find all cells comprising island 1 and put all cells into visited_cells
        def find_island_one(r, c):
            queue = deque([(r, c)])
            
            while queue:
                x, y = queue.popleft()
                if (x, y) in visited_cells:
                    continue
                visited_cells.add((x, y))
                
                for offset_x, offset_y in DIRECTIONS:
                    adjacent_x, adjacent_y = offset_x + x, offset_y + y
                    
                    if is_valid_cell(adjacent_x, adjacent_y) and grid[adjacent_x][adjacent_y] == 1:
                        queue.append((adjacent_x, adjacent_y))
                        
                        
        # Starting from all cells of island 1, perform BFS to find the min distance to island 2
        def find_distance_to_island_two():
            queue = deque(visited_cells)
            res = 0
            
            while queue:
                n = len(queue)
                
                for _ in range(n):
                    x, y = queue.popleft()
                    
                    for offset_x, offset_y in DIRECTIONS:
                        adjacent_x, adjacent_y = offset_x + x, offset_y + y
                    
                        if is_valid_cell(adjacent_x, adjacent_y) and (adjacent_x, adjacent_y) not in visited_cells:
                            if grid[adjacent_x][adjacent_y] == 1:
                                return res
                
                            if grid[adjacent_x][adjacent_y] == 0:
                                visited_cells.add((adjacent_x, adjacent_y))
                                queue.append((adjacent_x, adjacent_y))
                                
                res += 1
                
            return res
            
        N = len(grid)
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited_cells = set()
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    find_island_one(r, c)
                    return find_distance_to_island_two()
