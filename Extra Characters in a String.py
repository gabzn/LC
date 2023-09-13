https://leetcode.com/problems/extra-characters-in-a-string/

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        LEN = len(s)
        words = set(dictionary)
        
        @cache
        def dp(start):
            if start == LEN:
                return 0
            
            # skip the current char AKA it's an extra one
            res = 1 + dp(start + 1)
            
            for end in range(start, LEN):
                if s[start: end + 1] in words:
                    res = min(res, dp(end + 1))
   
            return res
        
        return dp(0)
