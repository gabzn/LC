https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        minutes, fresh_oranges = 0, 0
        queue = deque()
        
        # Find the number of fresh oranges and the coordinates of all rotten oranges
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 2:
                    queue.append((x, y, 0))
                if grid[x][y] == 1:
                    fresh_oranges += 1
        
        while queue:
            x, y, minutes = queue.popleft()
            
            for offset_x, offset_y in directions:
                new_x, new_y = x + offset_x, y + offset_y
                
                # If the neighbour is a fresh orange, 
                # mark it rotten and decrement the number of fresh oranges by 1.
                if self.is_fresh_orange(grid, M, N, new_x, new_y):
                    grid[new_x][new_y] = 2
                    fresh_oranges -= 1
                    queue.append((new_x, new_y, minutes + 1))
                    
        return minutes if fresh_oranges == 0 else -1
    
    def is_fresh_orange(self, grid, M, N, x, y):
        return 0 <= x < M and 0 <= y < N and grid[x][y] == 1
