https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
  
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        unique_chars = set()
        l, res = 0, 0
        
        for r in range(len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            
            unique_chars.add(s[r])
            
            if r - l + 1 == 3:
                res += 1
            
                # We want to maintain a window of size 3
                # so when we have a window of size 3, we move l to its right
                # if we don't move l to its right, next iteration we'll have a window of size 4 or more.
                unique_chars.remove(s[l])
                l += 1
    
        return res
