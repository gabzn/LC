https://leetcode.com/problems/coin-change-ii/

# https://www.youtube.com/watch?v=DJ4a7cmjZY0
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        LEN = len(coins)
        
        # Each row represents each coin in coins
        # Each col represents the amount from 0 up to amount
        # dp[1][3] means the number of ways to use coins[1 - 1] to make up $3
        # dp[2][9] means the number of ways to use coins[2 - 1] to make up $9
        dp = [[0 for _ in range(amount + 1)] for _ in range(LEN + 1)]
        for row in range(LEN + 1):
            dp[row][0] = 1
        
        # dp[row][amt] = dp[row - 1][amt] + dp[row][amt - coin]
        # coin = coins[row - 1]
        for row in range(1, LEN + 1):            
            for amt in range(1, amount + 1):
                # Not using the current coin
                dp[row][amt] = dp[row - 1][amt]
                
                # Use the current coin only if there's more amt left after using the coin
                coin = coins[row - 1]
                if amt - coin >= 0:
                    dp[row][amt] += dp[row][amt - coin]
      
        return dp[-1][-1]  
