https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/
  
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        visited_chars = set()
        l, res = 0, 0
        
        for r in range(len(s)):
            while s[r] in visited_chars:
                visited_chars.remove(s[l])
                l += 1
            
            visited_chars.add(s[r])
            
            if len(visited_chars) == k:
                res += 1
                visited_chars.remove(s[l])
                l += 1
            
        return res
-----------------------------------------------------------------------------------------------------------------------------------------------------  
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        visited_chars = set()
        l, res = 0, 0
        
        for r in range(len(s)):
            while s[r] in visited_chars or len(visited_chars) >= k:
                visited_chars.remove(s[l])
                l += 1
            
            visited_chars.add(s[r])
            
            if len(visited_chars) == k:
                res += 1
            
        return res
