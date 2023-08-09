https://leetcode.com/problems/find-the-safest-path-in-a-grid/

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def is_valid_cell(x, y):
            return 0 <= x < N and 0 <= y < N
        
        def can_reach_end_with_factor(m):
            if grid[0][0] <= m:
                return False
            
            visited_cells = set((0, 0))
            queue = deque([(0, 0)])
            while queue:
                x, y = queue.popleft()
                if x == N - 1 and y == N - 1:
                    return True
                             
                for offset_x, offset_y in DIRECTIONS:
                    neighbour_x, neighbour_y = offset_x + x, offset_y + y
                    
                    if is_valid_cell(neighbour_x, neighbour_y) and \
                       (neighbour_x, neighbour_y) not in visited_cells and \
                       grid[neighbour_x][neighbour_y] > m:

                        visited_cells.add((neighbour_x, neighbour_y))
                        queue.append((neighbour_x, neighbour_y))
                    
            return False
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
            
        N = len(grid)
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        
        # Find all the thieves
        for row in range(N):
            for col in range(N):
                if grid[row][col] != 1:
                    continue
                
                queue.append((row, col))
        
        # grid[x][y] = the distance from (x, y) to its closest theif + 1
        while queue:
            x, y = queue.popleft()
            
            for offset_x, offset_y in DIRECTIONS:
                neighbour_x, neighbour_y = offset_x + x, offset_y + y
                
                if is_valid_cell(neighbour_x, neighbour_y) and grid[neighbour_x][neighbour_y] == 0:
                    grid[neighbour_x][neighbour_y] = grid[x][y] + 1
                    queue.append((neighbour_x, neighbour_y))
        
        # Use binary search to find the ans
        l, r = -1, 2*N
        while l + 1 != r:
            m = (l + r) // 2
            
            if can_reach_end_with_factor(m):
                l = m
            else:
                r = m
        
        return l
