https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(l, r):
            res = 0
            
            while 0 <= l < LEN and 0 <= r < LEN and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            return res
        
        LEN = len(s)
        res = 0
        
        for index in range(LEN):
            res += count(index, index)
            res += count(index, index + 1)
                
        return res
