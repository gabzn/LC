https://leetcode.com/problems/word-break/
  
class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        LEN = len(s)
        words = set(words)
        
        def dp(start, memo):
            if start == LEN:
                return True
            
            if start in memo:
                return memo[start]
            
            memo[start] = False
            
            for end in range(start + 1, LEN + 1):
                if s[start: end] in words and dp(end, memo):
                    memo[start] = True
                    break
                    
            return memo[start]   
        return dp(0, {})
