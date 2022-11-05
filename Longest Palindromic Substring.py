https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
  
  
class Solution:
    def longestPalindrome(self, s: str) -> str:        
        l, r, max_len = 0, 0, 0
        
        for i in range(len(s)):
            odd_len = self.find_palindrome_len(s, i, i)
            even_len = self.find_palindrome_len(s, i, i+1)
            cur_len = max(odd_len, even_len)
            
            if cur_len > max_len:
                max_len = cur_len
                
                l = i - (cur_len-1) // 2
                r = i + cur_len // 2
            
        return s[l:r+1]
            
    def find_palindrome_len(self, s, l, r):
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        """
            a  b  a  c
        -1  0  1  2  3
         l           r
        
         c  a  b  a  
         0  1  2  3  4
         l           r
        
            a  b
            0  1
            l  r
            
        After the while loop, if there's a palindrome exist,
        both l and r are guaranteed to be 1 unit away, the normal way to find length is r - l + 1.
        To find the length of the palindrome, 
            move r 1 unit to its left so it's pointing at the end of the palindrome
            move l 1 unit to its right so it's pointing at the start of the palindrome   
        so it becomes (r-1) - (l+1) + 1
        """
        return (r-1) - (l+1) + 1
        # r - 1 - l - 1 + 1 = r - l - 1
