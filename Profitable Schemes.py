https://leetcode.com/problems/profitable-schemes/

class Solution:
    def profitableSchemes(self, n: int, min_profit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        LEN = len(profit)
        
        @cache
        def dp(i, members, cur_profit):
            if i == LEN:
                return 1 if cur_profit >= min_profit else 0
            
            # Skip the current crime
            res = dp(i + 1, members, cur_profit)
            
            # Pick the current crime only when we have enough members
            m = group[i]
            p = profit[i]            
            if members >= m:
                # If picking the current crime will yield at least min_profit, 
                # we keep cur_profit as min_profit.
                # We don't care when the cur_profit > min_profit. We only care whether it's AT LEAST min_profit 
                res += dp(i + 1, members - m, min(p + cur_profit, min_profit))
                
            return res % MOD
        
        return dp(0, n, 0)
