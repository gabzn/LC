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
