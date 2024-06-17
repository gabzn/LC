https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))
        
        while left <= right:
            x = left * left 
            y = right * right
            
            if x + y == c:
                return True
            
            if x + y < c:
                left += 1
            else:
                right -= 1
        
        return False
