https://leetcode.com/problems/domino-and-tromino-tiling/
  
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = (10 ** 9) + 7

        def dp(n, both_top_bottom, memo):
            if n == 0 or n == 1:
                if both_top_bottom == 'both':
                    return 1
                return 0
            
            if (n, both_top_bottom) in memo:
                return memo[(n, both_top_bottom)]
            
            if both_top_bottom == 'both':
                memo[(n, both_top_bottom)] = dp(n - 2, 'both', memo) + dp(n - 1, 'both', memo) + dp(n - 1, 'top', memo) + dp(n - 1, 'bottom', memo)
            if both_top_bottom == 'top':
                memo[(n, both_top_bottom)] = dp(n - 1, 'bottom', memo) + dp(n - 2, 'both', memo)
            if both_top_bottom == 'bottom':
                memo[(n, both_top_bottom)] = dp(n - 1, 'top', memo) + dp(n - 2, 'both', memo)
            
            return memo[(n, both_top_bottom)]
        
        return dp(n, 'both', {}) % MOD
