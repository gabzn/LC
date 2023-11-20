https://leetcode.com/problems/make-three-strings-equal/

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0] != s2[0] or s1[0] != s3[0] or s2[0] != s3[0]:
            return -1
        
        LEN1, LEN2, LEN3 = map(len, [s1, s2, s3])
        MIN_LEN = min(LEN1, LEN2, LEN3)
        
        res = 0
        if LEN1 > MIN_LEN:
            res += LEN1 - MIN_LEN
        if LEN2 > MIN_LEN:
            res += LEN2 - MIN_LEN    
        if LEN3 > MIN_LEN:
            res += LEN3 - MIN_LEN 
        
        # Walk backwards to find the leftmost column that has a mismatch
        # Use j to mark the leftmost column
        i, j = MIN_LEN - 1, MIN_LEN
        while i > 0:
            if s1[i] != s2[i] or s1[i] != s3[i] or s2[i] != s3[i]:
                j = i
            i -= 1
        
        return res if j == MIN_LEN else res + ((MIN_LEN - j) * 3)
