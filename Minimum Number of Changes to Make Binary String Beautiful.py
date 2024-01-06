https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution:
    def minChanges(self, s: str) -> int:
        LEN = len(s)
        
        res = 0
        ones = zeros = 0
        
        for idx, char in enumerate(s):
            ones += (char == '1')
            zeros += (char == '0')
            
            if (idx + 1) % 2 == 0:
                res += min(ones, zeros)
                ones = zeros = 0
            
        return res
