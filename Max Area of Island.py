https://leetcode.com/problems/max-area-of-island/
  
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
