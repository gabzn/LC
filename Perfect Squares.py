https://leetcode.com/problems/perfect-squares/
  
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

class Solution:
    def numSquares(self, n: int) -> int:
        """
        sqrt(12) gives us 3.46.
        Flooring it gives us 3.
        
        Any number greater than 3 and square it will always greater than n.
        So we can only find the solution by using the perfect squares from 1 to math.floor(math.sqrt(n))
        """
        bound = math.floor(math.sqrt(n))
        dp = [n] * (n+1)    
    
        for i in range(1, len(dp)):
            for j in range(1, bound+1):
                square = j**2
                
                if i - square == 0:
                    dp[i] = 1
                
                if i - square > 0 and dp[i] > 1 + dp[i-square]:
                    dp[i] = 1 + dp[i-square]
                
                if i - square < 0:
                    break
          
        return dp[n]
