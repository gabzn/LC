https://leetcode.com/problems/valid-palindrome/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
  

class Solution:
    def is_valid_char(self, char: str) -> bool:
        return (ord('a') <= ord(char) <= ord('z')) or (ord('0') <= ord(char) <= ord('9'))
    
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        s = s.lower()
        l, r = 0, len(s) - 1
                    
        while l <= r:
            while l < r and not self.is_valid_char(s[l]):
                l += 1
            while l < r and not self.is_valid_char(s[r]):
                r -= 1
            
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
