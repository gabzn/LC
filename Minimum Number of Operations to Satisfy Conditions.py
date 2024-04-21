https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        @cache
        def dp(i, prev):
            if i == COLS:
                return 0
            
            res = inf
            for x in range(10):
                if x != prev:
                    res = min(res, (ROWS - freq[i][x]) + dp(i + 1, x))
            return res        
        
        ROWS, COLS = len(grid), len(grid[0])
        
        freq = []
        for col in range(COLS):
            counter = Counter()
            for row in range(ROWS):
                counter[grid[row][col]] += 1
            freq.append(counter)
                
        return dp(0, -1)
