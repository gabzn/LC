https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

class Solution:
    def minSwaps(self, s: str) -> int:
        HALF = len(s) // 2
    
        ones = s.count('1')
        zeros = s.count('0')
        if abs(ones - zeros) > 1:
            return -1
        
        s1 = s2 = None
        if ones == zeros:
            s1 = '01' * HALF
            s2 = '10' * HALF
        elif ones > zeros:
            s1 = s2 = '10' * HALF + '1'
        else:
            s1 = s2 = '01' * HALF + '0'
        
        diff_1 = diff_2 = 0
        for c1, c2, c3 in zip(s, s1, s2):
            if c1 != c2:
                diff_1 += 1
            if c1 != c3:
                diff_2 += 1
        
        return min(diff_1 // 2, diff_2 // 2)
