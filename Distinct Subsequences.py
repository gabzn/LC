https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """    
        dp[i-1][j-1] = The number of distinct subsequences of s[i-1] = t[j-1]
        
        dp[i-1][j]
                i
        x x x a a
              j
        y y y a
        
        dp[i][j-1] ??? 
              i
        x x x b 
        y y b a
        """
        N = len(s)
        M = len(t)
        
        s = '/' + s
        t = '/' + t
        
        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        dp[0][0] = 1
        
        # for j in range(1, M + 1):
        #     dp[0][j] = 0
        for i in range(N + 1):
            dp[i][0] = 1
        
        for i in range(1, N + 1):
            for j in range(1, M + 1):        
                dp[i][j] += dp[i-1][j]
                
                if s[i] == t[j]:
                    dp[i][j] += dp[i-1][j-1]
            
        return dp[N][M]
