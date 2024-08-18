https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        res = 0
        for i in range(N):
            ones = 0
            zeroes = 0
            for j in range(i, N):
                ones += (s[j] == '1')
                zeroes += (s[j] == '0')
                
                if ones <= k or zeroes <= k:
                    res += 1
                else:
                    ones = 0
                    zeroes = 0
                    break
        return res
