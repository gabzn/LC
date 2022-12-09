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
        s_to_t, t_to_s = dict(), dict()
        
        for s_char, t_char in zip(s, t):
            if s_char not in s_to_t and t_char not in t_to_s:
                s_to_t[s_char] = t_char
                t_to_s[t_char] = s_char
            
            if (s_char in s_to_t and s_to_t[s_char] != t_char) or (t_char in t_to_s and t_to_s[t_char] != s_char):
                return False
            
        return True
-----------------------------------------------------------------------------------------------------------------------------------------------------------
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
