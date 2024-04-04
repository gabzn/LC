https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N = len(s)
        M = len(p)
        
        s = "/" + s
        p = "/" + p
        
        dp = [[False for _ in range(M + 1)] for _ in range(N + 1)]
        dp[0][0] = True
        for j in range(2, M + 1):
            if p[j] == '*' and dp[0][j-2]:
                dp[0][j] = True
                
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if p[j] == s[i] or p[j] == '.':
                    dp[i][j] = dp[i-1][j-1]
                
                if p[j] == '*':                    
                    if p[j-1] != '.' and p[j-1] != s[i]:
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                                        
        return dp[-1][-1]
"""
if p[j-1] != '.' and p[j-1] != s[i]:
                     i
    s: [X X X X X X] a
                   j
    p: [Y Y Y Y] b *
---------------------------------------
                    i
    s: [X X X X X X a]
                   j
    p: [Y Y Y Y] a *   -> 0's a
    
                    i
    s: [X X X X X X a]
                   j
    p: [Y Y Y Y] a *   -> 1 a    
    
                   i
    s: X X X X X X a
                 j
    p: Y Y Y Y a *     -> multiple a's
"""    
