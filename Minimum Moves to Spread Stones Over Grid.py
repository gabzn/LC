https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def dfs(index, moves):
            if index == 9:
                res[0] = min(moves, res[0])
                return
            
            # This will get the x, y coordinates for the current cell on grid
            x, y = divmod(index, 3)
            
            # Skip cells that already have stones in them
            if grid[x][y] != 0:
                dfs(index + 1, moves)
                return
            
            # The current cell has no stones. We find cells that have extra stones and move one to current
            for i in range(3):
                for j in range(3):
                    if grid[i][j] <= 1:
                        continue
                        
                    distance = abs(x - i) + abs(y - j)
                    
                    # Move the extra stone in [i][j] to [x][y]
                    grid[x][y] += 1
                    grid[i][j] -= 1
                    
                    dfs(index + 1, moves + distance)
                    
                    # Reset it                    
                    grid[x][y] -= 1
                    grid[i][j] += 1
            
        res = [100]
        dfs(0, 0)
        return res[0]
