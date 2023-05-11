https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
  
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        def dp(day, operations, is_holding, memo):
            if day == len(prices) or operations == 0:
                return 0
            if (day, operations, is_holding) in memo:
                return memo[(day, operations, is_holding)]
            
            memo[(day, operations, is_holding)] = 0
            
            if not is_holding:
                buy_now = -prices[day] + dp(day + 1, operations, True, memo)
                buy_later = dp(day + 1, operations, False, memo)
                memo[(day, operations, is_holding)] = max(buy_now, buy_later)
            else:
                sell_now = prices[day] + dp(day + 1, operations - 1, False, memo)
                sell_later = dp(day + 1, operations, True, memo)
                memo[(day, operations, is_holding)] = max(sell_now, sell_later)
            
            return memo[(day, operations, is_holding)]
            
        return dp(0, k, False, {})
