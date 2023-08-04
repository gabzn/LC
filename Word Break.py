https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        LEN = len(s)
        word_set = set(wordDict)
        
        @cache
        def dp(start):
            if start == LEN:
                return True
            
            for i in range(start, LEN + 1):
                if s[start: i] in word_set and dp(i):
                    return True
            return False
        
        return dp(0)
-------------------------------------------------------------------------------
class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        LEN = len(s)
        word_dict = set(word_dict)
        
        def dp(start, memo):
            if start == LEN:
                return True
            if start in memo:
                return memo[start]
            
            memo[start] = False
            for end in range(start, LEN + 1):
                # s[start: end] means the substring from start up to end - 1
                # to include end, we need to do s[start: end + 1]
                if s[start: end + 1] in word_dict and dp(end + 1, memo):
                    memo[start] = True
                    break
                  
            return memo[start]
        return dp(0, {})
