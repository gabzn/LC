https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        LEN = len(prices)    
        
        def dp(i, holding, memo):
            if i == LEN:
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            """
            There are only two things we can do on a given day, 
            depending on whether we are holding a stock or not.
            
            If we are holding a stock, we can either sell it on day i or sell it later.
            If we are not holding a stock, we can either buy it on day i or buy a stock later.
            """
            if holding:
                sell_now = (prices[i] - fee) + dp(i + 1, False, memo)
                sell_later = dp(i + 1, True, memo)
                memo[(i, holding)] = max(sell_now, sell_later)
            else:
                buy_now = -prices[i] + dp(i + 1, True, memo)
                buy_later = dp(i + 1, False, memo)
                memo[(i, holding)] = max(buy_now, buy_later)
            
            return memo[(i, holding)]
        return dp(0, False, {})
--------------------------------------------------------------------------------------------------------------
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        LEN = len(prices)
        dp = [[0, 0] for _ in range(LEN)]
        dp[0][1] = -prices[0]
             
        """
        dp[i][0] means not holding the stock on day i
            do nothing but still want no stock -> dp[i - 1][0]
            not holding -> max profit of holding on previous day + selling on day i - the fee
        
        dp[i][1] means holding the stock on day i
            do nothing but still want a stock -> dp[i - 1][1]
            holding -> max profit of not holding on previous day - buying on day i
        """
        for i in range(1, LEN):
            dp[i][0] = max(dp[i - 1][1] + prices[i] - fee, dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])        
        
        return max(dp[-1][0], dp[-1][1])
