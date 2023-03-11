https://leetcode.com/problems/climbing-stairs/

 class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb(n, dict())
        
    def climb(self, n, memo):
        if n <= 2:
            return n
        
        if n not in memo:
            memo[n] = self.climb(n - 1, memo) + self.climb(n - 2, memo) 
            
        return memo[n] 
---------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
