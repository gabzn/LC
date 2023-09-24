https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = Counter(s)
        res = []
        
        while counter['1'] > 1:
            res.append('1')
            counter['1'] -= 1
        
        while counter['0']:
            res.append('0')
            counter['0'] -= 1
            
        res.append('1')
        return ''.join(res)
