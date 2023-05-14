https://leetcode.com/problems/paint-fence/
  
class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        # dp(posts) returns the number of ways to paint posts
        def dp(posts, memo):
            if posts == 1:
                return k    
            if posts == 2:
                return k * k
            
            if posts in memo:
                return memo[posts]
            
            memo[posts] = (k - 1) * (dp(posts - 1, memo) + dp(posts - 2, memo)) 
            
            return memo[posts]
            
        return dp(n, {})
-------------------------------------------------------------------------------------------------
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k * k
        
        for post in range(3, n + 1):
            dp[post] = (k - 1) * dp[post - 1] + (k - 1) * dp[post - 2]
        
        return dp[n]
