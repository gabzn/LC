https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def findPaths(self, m: int, n: int, max_move: int, start_row: int, start_col: int) -> int:
        def is_in_bound(x, y):
            return 0 <= x < m and 0 <= y < n
            
        @cache
        def dp(x, y, moves):
            if not is_in_bound(x, y):
                return 1
            
            if moves == max_move:
                return 0
                        
            res = 0
            
            for offset_x, offset_y in DIRECTIONS:
                next_x, next_y = x + offset_x, y + offset_y                
                res += (dp(next_x, next_y, moves + 1))
            
            return res % MOD
        
        MOD = 10 ** 9 + 7
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        return dp(start_row, start_col, 0)
