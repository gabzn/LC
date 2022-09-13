You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
  
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
