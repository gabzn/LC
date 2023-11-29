https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        LEN = len(prices)
        
        @cache
        def dp(idx, next_i_free):
            if idx == LEN:
                return 0
            
            # if can buy for free, use it or buy it to refresh the offer.
            res = math.inf
            if next_i_free:
                res = dp(idx + 1, next_i_free - 1)

            # if not, buy it. 
            res = min(res, prices[idx] + dp(idx + 1, idx + 1))
            return res  
        
        return dp(0, 0)
