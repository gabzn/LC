https://leetcode.com/problems/coin-change-ii/
# https://www.youtube.com/watch?v=EqBJ7ogzrYI&t=651s

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:    
        # dp[i][j] = the # of combinations to make up i amount using all the coins from [0: j]
        dp = [[0 for _ in range(len(coins))] for _ in range(amount + 1)]
        
        # dp[0][j] = the # of combinations to make up 0 using all the coins from [0: j] is always 1
        for j in range(len(coins)):
            dp[0][j] = 1
        
        for i in range(1, amount + 1):
            for j, val in enumerate(coins):
                skip_current_coin = dp[i][j - 1] if j > 0 else 0
                use_current_coin = dp[i - val][j] if i - val >= 0 else 0
                
                dp[i][j] += (skip_current_coin + use_current_coin)
        
        # dp[amount][-1] = the # of combinations to make up amount using all the coins
        return dp[amount][-1]
---------------------------------------------------------------------
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        LEN = len(coins)
        
        @cache
        def dp(index, amt):
            if amt < 0 or index == LEN:
                return 0            
            if amt == 0:
                return 1
            
            # 2 OPTIONS
            # 1: We take the current coin, and we have the option to take it again
            # 2: We skip the current coin, and we move onto the next coin
            take_current_coin = dp(index, amt - coins[index])
            skip_current_coin = dp(index + 1, amt)
            return take_current_coin + skip_current_coin
            
        return dp(0, amount)
