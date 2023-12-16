https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:                
        def dp(x, y):
            if memo[x][y] != -1:
                return memo[x][y]
            
            res = 1
            
            for offset_x, offset_y in DIRECTIONS:
                adjacent_x, adjacent_y = offset_x + x, offset_y + y
    
                if 0 <= adjacent_x < ROWS and 0 <= adjacent_y < COLS and grid[adjacent_x][adjacent_y] > grid[x][y]:
                    res += dp(adjacent_x, adjacent_y) % MOD
            
            memo[x][y] = res
            return res

        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7        
        
        memo = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        res = 0
    
        for x in range(ROWS):
            for y in range(COLS):
                res += dp(x, y) % MOD
        
        return res % MOD
