https://leetcode.com/problems/online-stock-span/
  
class StockSpanner:

    def __init__(self):
        self.stock_prices = []

    def next(self, price: int) -> int:
        days = 1
        
        while self.stock_prices and self.stock_prices[-1][0] <= price:
            days += self.stock_prices[-1][1]
            self.stock_prices.pop()
        
        self.stock_prices.append((price, days))
        return days
