https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dp(i, depth):
            if i == N:
                return True if depth == 0 else False            
            if depth < 0:
                return False
            
            if s[i] == '(':
                return dp(i + 1, depth + 1)
            if s[i] == ')':
                return dp(i + 1, depth - 1)
            if s[i] == '*':
                return dp(i + 1, depth + 1) or dp(i + 1, depth - 1) or dp(i + 1, depth)
        
        N = len(s)
        return dp(0, 0)
