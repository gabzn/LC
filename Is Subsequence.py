Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Input: s = "abc", t = "ahbgdc"
Output: true
  
Input: s = "axc", t = "ahbgdc"
Output: false
  
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t or not s:
            return True

        if len(s) > len(t):
            return False
        
        s_char_index = 0
        for t_char in t:
            if t_char == s[s_char_index]:
                s_char_index += 1
            
            if s_char_index == len(s):
                return True
        
        return False   
      
      
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True

        if len(s) > len(t):
            return False
        
        latest_index = -1
        for index, s_char in enumerate(s):
            if len(s) > len(t) or s_char not in t:
                return False
            
            s = s[index + 1:]
            
            s_char_in_t = t.index(s_char)
            t = t[s_char_in_t + 1:]
        
        return True    
