https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:    
        if grid[0][0] > k:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        pref = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                pref[i][j] = (grid[i - 1][j - 1] + pref[i - 1][j] + pref[i][j - 1]) - pref[i - 1][j - 1]
         
        res = 0
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                if pref[i][j] <= k:
                    res += 1
            
        return res
