https://leetcode.com/problems/arranging-coins/
  
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        
        # Bisect_right problem
        l, r = 0, n
        while l < r:
            m = (l + r) // 2
            total_needed = (m * (m + 1)) // 2               # [k * (k + 1)] // 2
            
            if total_needed <= n:
                l = m + 1
            else:
                r = m
            
        return l - 1
