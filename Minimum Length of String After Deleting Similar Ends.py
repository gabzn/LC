https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:        
        l, r = 0, len(s) - 1
        
        while l < r and s[l] == s[r]:
            
            while l + 1 != r and s[l] == s[l + 1]:
                l += 1
            
            while r - 1 != l and s[r] == s[r - 1]:
                r -= 1
            
            l += 1
            r -= 1
            
        return r - l + 1
