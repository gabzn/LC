https://leetcode.com/problems/construct-product-matrix/

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        ROWS, COLS = len(grid), len(grid[0])
        TOTAL = ROWS * COLS
        
        flattened_lst = list(chain(*grid))
        pref = [1] * TOTAL
        suff = [1] * TOTAL
        
        for idx in range(1, TOTAL):
            pref[idx] = (pref[idx - 1] * flattened_lst[idx - 1]) % MOD
        
        for idx in reversed(range(TOTAL - 1)):
            suff[idx] = (suff[idx + 1] * flattened_lst[idx + 1]) % MOD
            
        idx = 0
        for r in range(ROWS):
            for c in range(COLS):
                grid[r][c] = (pref[idx] * suff[idx]) % MOD
                idx += 1
                        
        return res
