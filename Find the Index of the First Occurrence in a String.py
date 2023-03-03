https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
  
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        haystack_len, window_size = len(haystack), len(needle)
        
        for l in range(haystack_len):
            r = l + window_size
            if r <= haystack_len and haystack[l: r] == needle:
                return l
                
        return -1 
