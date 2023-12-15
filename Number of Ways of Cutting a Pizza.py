https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/
https://www.youtube.com/watch?v=RFyJMlpA-pY

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:        
        @cache
        def dp(r, c, cuts):
            # Return early if the current pizza has no apple left
            if prefix[r][c] == 0:
                return 0
            
            # Base case where we've used all the cuts, return 1 if current pizza has apple else 0
            if cuts == k - 1:
                return 1 if prefix[r][c] else 0
            
            res = 0
            
            # Cut horizontally
            for next_r in range(r + 1, ROWS):
                if prefix[r][c] - prefix[next_r][c] > 0:
                    res += dp(next_r, c, cuts + 1)
            
            # Cut vertically
            for next_c in range(c + 1, COLS):
                if prefix[r][c] - prefix[r][next_c] > 0:
                    res += dp(r, next_c, cuts + 1)
            
            return res % MOD
        
        MOD = 10 ** 9 + 7
        ROWS, COLS = len(pizza), len(pizza[0])
        
        prefix = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                prefix[r][c] = (pizza[r][c] == 'A') + prefix[r + 1][c] + prefix[r][c + 1] - prefix[r + 1][c + 1]
        
        return dp(0, 0, 0)
