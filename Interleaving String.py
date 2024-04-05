https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N = len(s1)
        M = len(s2)
        K = len(s3)
        if N + M != K:
            return False
        
        s1 = '/' + s1
        s2 = '/' + s2
        s3 = '/' + s3
        
        # dp[i][j] = can s3[:i+j] be formed by the interleaving of s1[:i] and s2[:j]
        dp = [[False for _ in range(M + 1)] for _ in range(N + 1)]
        dp[0][0] = True
        
        for i in range(1, N + 1):
            dp[i][0] = dp[i-1][0] and s1[i] == s3[i]
        for j in range(1, M + 1):
            dp[0][j] = dp[0][j-1] and s2[j] == s3[j]
        
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if s1[i] == s3[i+j] and dp[i-1][j]:
                    dp[i][j] = True
                
                if s2[j] == s3[i+j] and dp[i][j-1]:
                    dp[i][j] = True
          
        return dp[N][M]
--------------------------------------------------------------------------------------------
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len, s3_len = map(len, [s1, s2, s3])
        if s1_len + s2_len != s3_len:
            return False
        
        @cache
        def dp(a, b, c):
            if c == s3_len:
                return True
            
            res = False
            
            if a < s1_len and s1[a] == s3[c] and dp(a+1, b, c+1):
                res = True
            
            if b < s2_len and s2[b] == s3[c] and dp(a, b+1, c+1):
                res = True
            
            return res
        
        return dp(0, 0, 0)
