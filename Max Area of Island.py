https://leetcode.com/problems/max-area-of-island/


# DFS 
class Solution:
    def is_valid_island(self, grid, r, c, R, C):
        return 0 <= r < R and 0 <= c < C and grid[r][c] == 1
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        R, C = len(grid), len(grid[0])
        max_area = 0
        visited_islands = set()
        
        for r in range(R):
            for c in range(C):
                
                # We only want to look at the islands that we have not visited.
                if grid[r][c] == 1 and (r, c) not in visited_islands:
                    area = 0
                    
                    stack = []
                    stack.append((r, c))
                    
                    while stack:
                        island_r, island_c = stack.pop()
                        
                        if (island_r, island_c) in visited_islands:
                            continue
                        visited_islands.add((island_r, island_c))
                        
                        # When it gets here it means we are exploring this island.
                        area += 1
                        
                        # Get coordinates for up, down, left and right for this current island
                        potential_neighbours = [(island_r-1, island_c), (island_r+1, island_c), (island_r, island_c-1), (island_r, island_c+1)]
                        for neighbour in potential_neighbours:
                            neighbour_r, neighbour_c = neighbour
                            
                            if self.is_valid_island(grid, neighbour_r, neighbour_c, R, C):
                                stack.append(neighbour)
                    
                    # When the while loop finishes, it means we just finished exploring some islands.
                    max_area = max(max_area, area)
                            
        return max_area
--------------------------------------------------------------------------------------------------------------------------------------------------------------
# BFS
from collections import deque

class Solution:
    def is_valid_island(self, grid, r, c, R, C):
        return 0 <= r < R and 0 <= c < C and grid[r][c] == 1
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        R, C = len(grid), len(grid[0])
        max_area = 0
        visited_islands = set()
        
        for r in range(R):
            for c in range(C):
                
                # We only want to look at the islands that we have not visited.
                if grid[r][c] == 1 and (r, c) not in visited_islands:
                    area = 0
                    
                    queue = deque()
                    queue.append((r, c))
                    
                    while queue:
                        island_r, island_c = queue.popleft()
                        
                        if (island_r, island_c) in visited_islands:
                            continue
                        visited_islands.add((island_r, island_c))
                        
                        # When it gets here it means we are exploring this island.
                        area += 1
                        
                        # Get coordinates for up, down, left and right for this current island
                        potential_neighbours = [(island_r-1, island_c), (island_r+1, island_c), (island_r, island_c-1), (island_r, island_c+1)]
                        for neighbour in potential_neighbours:
                            neighbour_r, neighbour_c = neighbour
                            
                            if self.is_valid_island(grid, neighbour_r, neighbour_c, R, C):
                                queue.append(neighbour)
                    
                    # When the while loop finishes, it means we just finished exploring some islands.
                    max_area = max(max_area, area)
                            
        return max_area
----------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    area = 0
                    
                    stack = [(row, col)]
                    while stack:
                        land_r, land_c = stack.pop()
                        if grid[land_r][land_c] == 0:
                            continue
                        grid[land_r][land_c] = 0
                        area += 1
                        
                        potential_neighbours = [(land_r-1, land_c), (land_r+1, land_c), (land_r, land_c-1), (land_r, land_c+1)]
                        for neighbour in potential_neighbours:
                            neighbour_r, neighbour_c = neighbour
                            
                            if 0 <= neighbour_r < len(grid) and 0 <= neighbour_c < len(grid[row]) and grid[neighbour_r][neighbour_c] == 1:
                                stack.append(neighbour)
                    
                    max_area = max(max_area, area)
                    
        return max_area
