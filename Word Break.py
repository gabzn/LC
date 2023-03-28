https://leetcode.com/problems/word-break/
  
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        
        def dp(start, memo):
            if start == N:
                return True
            
            if start not in memo:
                for end in range(start + 1, N + 1):
                    if s[start: end] in wordDict and dp(end, memo):
                        memo[start] = True
                        return memo[start]
                    
            memo[start] = False
            return memo[start]
        
        return dp(0, {})
