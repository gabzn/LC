https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        LEN = len(prices)    
        
        def dp(i, holding, memo):
            if i == LEN:
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            
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
