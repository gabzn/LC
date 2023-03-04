https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
  
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights) - 1, sum(weights) + 1
        
        while l + 1 != r:
            m = (l + r) // 2

            if self.can_ship_within_days(weights, days, m):
                r = m
            else:
                l = m
        
        return r
    
    def can_ship_within_days(self, weights, days, m):
        current_w, days_needed = 0, 1
        
        for w in weights:
            current_w += w
            if current_w > m:
                days_needed += 1
                current_w = w
        
        return days_needed <= days        
