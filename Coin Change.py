https://leetcode.com/problems/coin-change/
  
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        
        """
        the size of dp has to be (amount + 1) is because we want to know the number of coins to change from 0 up to amount.
        dp[x] = # of coins it needs to change the amount of x.
        if x - coin is equal to 0, that means x can be changed exactly using 1 of this coin.
        if x - coin is greater than 0, that means after we use coin to change x there's still some something we can change.
        """
        
        for x in range(1, amount + 1):
            for coin in coins:
                if x - coin == 0:
                    dp[x] = 1
                if x - coin > 0:
                    dp[x] = min(dp[x], 1 + dp[x-coin])
        
        return dp[amount] if dp[amount] != math.inf else -1
