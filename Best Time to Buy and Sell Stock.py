https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
  
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        
        for price in prices:
            if price < buy:
                buy = price
            else:
                max_profit = max(max_profit, price - buy)
        
        return max_profit
-----------------------------------------------------------------------------------------------------------------------------------------------------------  
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        # Assume you always buy on day 1. The reason being you need to buy before you sell.
        buy_in = prices[0]
        current_profit, profit = 0, 0
        
        # Go through each day to see if the current price is less than the price we bought in
        # If it's less, we buy on that day instead.
        # If it's more, we check how much we can profit from that day, and compare with the max profit we currently have.
        for price in prices:
            if price < buy_in:
                buy_in = price
            else:
                current_profit = price - buy_in
            
            profit = max(current_profit, profit)
        
        return profit
