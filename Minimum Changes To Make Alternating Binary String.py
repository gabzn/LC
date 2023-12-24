https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        LEN = len(s)
        
        def check_start_with_one_or_zero(start):
            res = 0
            
            for char in s:
                if char != start:
                    res += 1
                
                if start == '1':
                    start = '0'
                else:
                    start = '1'
                    
            return res
                    
        return min(check_start_with_one_or_zero('1'), check_start_with_one_or_zero('0'))
