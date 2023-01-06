https://leetcode.com/problems/maximum-ice-cream-bars/
  
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        bars = 0
        for cost in costs:
            if coins - cost >= 0:
                coins -= cost
                bars += 1
            else:
                break
        
        return bars
