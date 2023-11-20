https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        LEN = len(s)
        
        s_prime = ''.join(sorted(s))
        res = 0
        
        # Swap the leftmost mismatch with the rightmost mismatch
        i, j = 0, LEN - 1
        while i < j:
            while i < j and s[i] == s_prime[i]:
                i += 1
            
            while i < j and s[j] == s_prime[j]:
                j -= 1
            
            res += (j - i)
            i += 1
            j -= 1
        
        return res
