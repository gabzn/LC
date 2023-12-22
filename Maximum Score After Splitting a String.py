https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        LEN = len(s)
        ones = s.count('1')
        res = zeros = 0
        
        for idx in range(LEN - 1):
            if s[idx] == '0':
                zeros += 1
            else:
                ones -= 1
            
            res = max(res, zeros + ones)
        
        return res
