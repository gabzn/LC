https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dp(left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            
            if s[left] == s[right]:
                return 2 + dp(left + 1, right - 1)
            else:
                return max(dp(left + 1, right), dp(left, right - 1))
        
        return dp(0, len(s) - 1)
----------------------------------------------------------------------------------
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
    
        def dp(left, right, memo):
            if left > right:
                return 0
            if left == right:
                return 1
            if (left, right) in memo:
                return memo[(left, right)]
            
            if s[left] == s[right]:
                memo[(left, right)] = dp(left+1, right-1, memo) + 2
            else:
                memo[(left, right)] = max(dp(left+1, right, memo), dp(left, right-1, memo))
                
            return memo[(left, right)]
        
        return dp(0, len(s)-1, {})
