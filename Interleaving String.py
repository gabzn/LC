https://leetcode.com/problems/interleaving-string/
  
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        A, B, C = len(s1), len(s2), len(s3)
        if A + B != C:
            return False
        
        def dp(a, b, c, memo):
            if a == A and b == B:
                return True
            if (a, b, c) in memo:
                return memo[(a, b, c)]
            
            memo[(a, b, c)] = False
            
            if a < A and s1[a] == s3[c] and dp(a + 1, b, c + 1, memo):
                memo[(a, b, c)] = True
            if b < B and s2[b] == s3[c] and dp(a, b + 1, c + 1, memo):
                memo[(a, b, c)] = True
                
            return memo[(a, b, c)]
        return dp(0, 0, 0, {})
