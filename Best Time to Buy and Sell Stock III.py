https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LEN = len(prices)
        
        def dp(i, transactions, is_holding, memo):
            if i == LEN:
                return 0
            if (i, transactions, is_holding) in memo:
                return memo[(i, transactions, is_holding)]
            
            res = 0
            if is_holding:                
                sell_now = prices[i] + dp(i + 1, transactions, False, memo)
                sell_later = dp(i + 1, transactions, True, memo)
                
                res = max(sell_now, sell_later)
            else:
                if transactions < 2:
                    buy_now = -prices[i] + dp(i + 1, transactions + 1, True, memo)
                    buy_later = dp(i + 1, transactions, False, memo)
            
                    res = max(buy_now, buy_later)
            
            memo[(i, transactions, is_holding)] = res
            return res
            
        return dp(0, 0, False, {})
------------------------------------------------------------------------------------
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LEN = len(prices)
        
        @cache
        def dp(i, transactions, is_holding):
            if i == LEN:
                return 0

            res = 0
            
            if is_holding:                
                sell_now = prices[i] + dp(i + 1, transactions, False)
                sell_later = dp(i + 1, transactions, True)
                
                res = max(sell_now, sell_later)
            else:
                if transactions < 2:
                    buy_now = -prices[i] + dp(i + 1, transactions + 1, True)
                    buy_later = dp(i + 1, transactions, False)
                    
                    res = max(buy_now, buy_later)
            
            return res
        return dp(0, 0, False)
