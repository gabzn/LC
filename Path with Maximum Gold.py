https://leetcode.com/problems/path-with-maximum-gold/

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def collect_gold(x, y, total_gold):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 0:
                return total_gold
            
            gold = grid[x][y]
            total_gold += gold            
            grid[x][y] = 0
            
            total_gold = max(collect_gold(x+1, y, total_gold), 
                             collect_gold(x-1, y, total_gold), 
                             collect_gold(x, y+1, total_gold), 
                             collect_gold(x, y-1, total_gold))

            grid[x][y] = gold
            return total_gold
        
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
     
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] != 0:
                    res = max(res, collect_gold(row, col, 0))

        return res
