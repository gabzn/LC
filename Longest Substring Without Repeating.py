https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        l, res = 0, 0
        
        for r in range(len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
                
            unique_chars.add(s[r])
            res = max(res, r - l + 1)
        
        return res
-------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if 0 <= len(s) <= 1:
            return len(s)
        
        l, r, max_length = 0, 0, 0
        character_set = set()
        
        # Sliding window question:
        # If the current char previously showed up and was added to the set, we remove all the characters before and including that character from the set.
        # Otherwise, just add the current char to the set and compare the size.
        while r < len(s):
            if s[r] in character_set:
                character_set.remove(s[l])
                l += 1
            else:
                character_set.add(s[r])
                r += 1
                max_length = max(max_length, len(character_set))
                
        return max_length
