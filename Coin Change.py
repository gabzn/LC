https://leetcode.com/problems/coin-change/

  
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp(cur_amount) returns the min number of coins to make up cur_amount
        def dp(cur_amount, memo):
            if cur_amount == 0:
                return 0
            
            if cur_amount not in memo:
                res = math.inf
                
                for coin in coins:
                    if cur_amount == coin:
                        res = 1
                    elif cur_amount > coin:
                        res = min(res, 1 + dp(cur_amount - coin, memo))
                    
                memo[cur_amount] = res
                
            return memo[cur_amount]
        
        res = dp(amount, {})
        return res if res != math.inf else -1  
-------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                elif i > coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[-1] if dp[-1] != math.inf else -1
