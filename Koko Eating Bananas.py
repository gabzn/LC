https://leetcode.com/problems/koko-eating-bananas/
Very interesting question. Binary Search might not seem obvious.
  
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # If the rate is the maximum in the piles, that guarantees that he can finish all bananas in h hours
        # But we want to minimize the rate, the range of the rates can only be from 1 to whatever the max is.
        # Perform binary search on the rates we can get the optimal solution.
        l, r = 1, max(piles)
        min_rate = r
        
        while l <= r:
            mid = (l + r) // 2
            
            if self.can_finish(piles, mid, h):
                min_rate = min(min_rate, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_rate
    
    def can_finish(self, piles, speed, h):
        total_hours = 0
        
        for pile in piles:
            hours = math.ceil(pile / speed)
            total_hours += hours
        
        return total_hours <= h
