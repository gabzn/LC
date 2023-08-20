https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s1_len, s2_len = len(str1), len(str2)        
        l, r = 0, 0
        
        while l < s1_len and r < s2_len:
            s1_char, s2_char = str1[l], str2[r]
            
            if s1_char == s2_char or chr( ( (ord(s1_char) - ord('a') + 1) % 26 ) + 97 ) == s2_char:
                r += 1

            l += 1
        
        return r == s2_len
