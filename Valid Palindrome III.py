https://leetcode.com/problems/valid-palindrome-iii/

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        LEN = len(s)
        
        if LEN == k:
            return True
        
        # dp tells us the min cost to make s palindromic
        @cache
        def dp(left, right):
            if left == right:
                return 0
            
            if left + 1 == right:
                return 1 if s[left] != s[right] else 0
            
            if s[left] == s[right]:
                return dp(left + 1, right - 1)
            
            if s[left] != s[right]:
                return 1 + min(dp(left + 1, right), dp(left, right - 1))
            
        return dp(0, LEN - 1) <= k
