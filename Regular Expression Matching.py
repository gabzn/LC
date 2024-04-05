https://leetcode.com/problems/regular-expression-matching/
https://www.youtube.com/watch?v=l3hda49XcDE

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
                    # The current one char is *
                    # If * zeroes out the char it precedes, 
                    # and it still matches, then x* doesn't really matter
                    if dp[i][j-2]:
                        dp[i][j] = True
                        continue
                    
                    """
                         i
                    s: x a
                           j
                    p: x a *
                    
                    p[j-1] == s[i] -> check if this is good
                        s: x 
                        p: x a *
                    -----------------------
                               i
                    s: x a a a a
                           j
                    p: x a *
                    
                    p[j-1] == s[i] -> check if this is good
                        s: x a a a
                        p: x a *
                    """
                    if p[j-1] == '.' or p[j-1] == s[i]:
                        dp[i][j] = dp[i-1][j]
                                    
        return dp[N][M]
"""
                    i
    s: [X X X X X X a]
                   j
    p: [Y Y Y Y] a *   -> 0's a  (a* removed)
    
                     i                    
    s: [X X X X X X] a
                  j 
    p: [Y Y Y Y . *]   -> ()
    
                     i
    s: [X X X X X X] a
                  j
    p: [Y Y Y Y a *]     -> 
"""    
