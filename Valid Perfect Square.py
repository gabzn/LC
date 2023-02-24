https://leetcode.com/problems/valid-perfect-square/
  
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        
        while l <= r:
            m = (l + r) // 2
            square_of_m = m * m
            
            if square_of_m == num:
                return True
            
            if square_of_m < num:
                l = m + 1
            else:
                r = m - 1
                
        return False
