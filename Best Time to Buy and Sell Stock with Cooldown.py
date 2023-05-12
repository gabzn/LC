https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
  
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dp(day, is_holding, can_buy, memo):
            if day == len(prices):
                return 0
            
            if (day, is_holding, can_buy) in memo:
                return memo[(day, is_holding, can_buy)]
            
            memo[(day, is_holding, can_buy)] = 0
            
            # When we have a stock, we can either sell now or sell later. Pick the most profitable one.
            if is_holding:
                sell_now = prices[day] + dp(day + 1, False, False, memo)
                sell_later = dp(day + 1, True, False, memo)
                memo[(day, is_holding, can_buy)] = max(sell_now, sell_later)
            else:
                # When we don't have a stock and we are not in cooldown. 
                # We can buy now or buy later. Pick the most profitable one.
                if can_buy:
                    buy_now = -prices[day] + dp(day + 1, True, False, memo)
                    buy_later = dp(day + 1, False, True, memo)
                    memo[(day, is_holding, can_buy)] = max(buy_now, buy_later) 
                # When we don't have a stock and we are in cooldown, go to next day.
                else:
                    memo[(day, is_holding, can_buy)] = dp(day + 1, False, True, memo)
                    
            return memo[(day, is_holding, can_buy)]
        
        return dp(0, False, True, {})
