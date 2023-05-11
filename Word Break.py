https://leetcode.com/problems/word-break/
  
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
