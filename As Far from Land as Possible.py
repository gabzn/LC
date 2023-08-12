https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def is_valid_cell(x, y):
            return 0 <= x < N and 0 <= y < N
        
        N = len(grid)
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        res = 1
        queue = deque()
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    queue.append((r, c, 0))
        
        if len(queue) == 0 or len(queue) == N * N:
            return -1
        
        while queue:
            n = len(queue)
            
            for _ in range(n):
                x, y, distance = queue.popleft()
                if grid[x][y] == -1:
                    res = max(res, distance)
                
                for offset_x, offset_y in DIRECTIONS:
                    adjacent_x, adjacent_y = offset_x + x, offset_y + y
                    
                    if is_valid_cell(adjacent_x, adjacent_y) and \
                       grid[adjacent_x][adjacent_y] == 0:
                        grid[adjacent_x][adjacent_y] = -1
                        queue.append((adjacent_x, adjacent_y, distance + 1))
                    
        return res
