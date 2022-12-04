https://leetcode.com/problems/valid-palindrome-ii/
  
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                substring_without_l, substring_without_r = s[l+1:r+1], s[l:r]
                return (substring_without_l == substring_without_l[::-1]) or (substring_without_r == substring_without_r[::-1])
            
            l += 1
            r -= 1
            
        return True
