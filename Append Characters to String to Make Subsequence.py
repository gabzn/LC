https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        S = len(s)
        T = len(t)
        
        i = j = 0
        
        while i < S and j < T:
            if s[i] == t[j]:
                j += 1
            
            i += 1
        
        return T - j
