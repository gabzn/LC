https://leetcode.com/problems/n-th-tribonacci-number/
  
class Solution:
    def tribonacci(self, n: int) -> int:
        return self.dp(n, {})
    
    def dp(self, n, memo):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        if n not in memo:
            memo[n] = self.dp(n - 1, memo) + self.dp(n - 2, memo) + self.dp(n - 3, memo)
        
        return memo[n]
---------------------------------------------------------------------------------------------------
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
            
        return dp[-1]
