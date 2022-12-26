https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
  
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        
        for index, price in enumerate(prices):
            
            while stack and stack[-1][0] >= price:
                prev_price, prev_index = stack.pop()
                prices[prev_index] = prev_price - price
            
            stack.append((price, index))
            
        return prices
        
        
#         for left_index in range(len(prices)):
#             for right_index in range(left_index+1, len(prices)):
#                 if prices[left_index] >= prices[right_index]:
#                     prices[left_index] -= prices[right_index]
#                     break
    
#         return prices
