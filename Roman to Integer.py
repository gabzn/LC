https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        LEN = len(s)
        MAP = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        res = 0
        for i in range(LEN-1, -1, -1):
            char = s[i]
            
            if char == 'I' and i <= LEN - 2:
                if s[i+1] == 'V' or s[i+1] == 'X':
                    res -= 1
                    continue
                
            if char == 'X' and i <= LEN - 2:
                if s[i+1] == 'L' or s[i+1] == 'C':
                    res -= 10
                    continue
            
            if char == 'C' and i <= LEN - 2:
                if s[i+1] == 'D' or s[i+1] == 'M':
                    res -= 100
                    continue
            
            res += MAP[char]
            
        return res
