https://leetcode.com/problems/number-of-islands/
  
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        islands = 0
            
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    stack.append((r, c))
                    
                    self.dfs(grid, len(grid), len(grid[r]), stack)
                    islands += 1
        
        return islands
    
    def dfs(self, grid, max_r, max_c, stack):
        while stack:
            land_r, land_c = stack.pop()
            grid[land_r][land_c] = '0'
                        
            potential_lands = [(land_r-1, land_c), (land_r+1, land_c), (land_r, land_c-1), (land_r, land_c+1)]
            for potential_land in potential_lands:
                potential_land_r, potential_land_c = potential_land
                            
                if self.is_a_valid_land(grid, potential_land_r, potential_land_c, max_r, max_c):
                    stack.append(potential_land)
                    
    def is_a_valid_land(self, grid, r, c, max_r, max_c):
        return 0 <= r < max_r and 0 <= c < max_c and grid[r][c] == '1'
------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:   
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        visited_islands = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited_islands:
                    self.dfs(grid, r, c, visited_islands, rows, cols)
                    count += 1
                
        return count
    
    def dfs(self, grid, r, c, visited_islands, rows, cols):
        stack = []
        stack.append((r, c))
        
        while stack:
            island_r, island_c = stack.pop()
                    
            if (island_r, island_c) in visited_islands:
                continue
            visited_islands.add((island_r, island_c))
                                        
            potential_neighbours = [(island_r-1, island_c), (island_r+1, island_c), (island_r, island_c-1), (island_r, island_c+1)]
            for neighbour in potential_neighbours:
                neighbour_r, neighbour_c = neighbour
                        
                if self.is_an_island(grid, neighbour_r, neighbour_c, rows, cols):
                    stack.append(neighbour)        
    
    def is_an_island(self, grid, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1"
