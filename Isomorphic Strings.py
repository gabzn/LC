Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
https://leetcode.com/problems/isomorphic-strings/

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
  
  
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t: 
            return True

        char_map = dict()
        new_str = ""
        
        """
            loop through both strings at the same time,
            use a dict to keep track of the chars mapping from s to t
        """
        for s_char, t_char in zip(s, t):
            if s_char not in char_map:
                char_map[s_char] = t_char
                
                # Check if this 2 characters from s are mapping to the same character in t.
                if t_char in new_str:
                    return False
            new_str += char_map[s_char]

        return new_str == t
