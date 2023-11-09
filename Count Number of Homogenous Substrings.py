https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution:
    def countHomogenous(self, s: str) -> int:
        """
        a    b b    c c c     a a
        1    1 3    1 3 6     1 3
    
        res: 1 + 3 + 6 + 3
        each number is computed by (count * (count + 1)) // 2
        """
        
        MOD = 10 ** 9 + 7
        res = 0
        
        running_count, consecutive_chars = 1, 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                consecutive_chars += 1
                running_count = (consecutive_chars * (consecutive_chars + 1)) // 2
            else:
                res += running_count % MOD
                consecutive_chars = running_count = 1
        
        return (res + running_count) % MOD
