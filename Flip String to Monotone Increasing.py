https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        LEN = len(s)
        
        @cache
        def dp(idx, is_prev_zero_or_none):
            if idx == LEN:
                return 0
            
            res = LEN
            
            # If previous digit is zero or the beginning and the current digit is 0
            if is_prev_zero_or_none and s[idx] == '0':
                res = min(res, dp(idx + 1, is_prev_zero_or_none), 1 + dp(idx + 1, not is_prev_zero_or_none))
            
            # If previous digit is zero or the beginning and the current digit is 1
            if is_prev_zero_or_none and s[idx] == '1':
                res = min(res, dp(idx + 1, not is_prev_zero_or_none), 1 + dp(idx + 1, is_prev_zero_or_none))
            
            # If previous digit is 1 and the current digit is 0
            if not is_prev_zero_or_none and s[idx] == '0':
                res = min(res, 1 + dp(idx + 1, is_prev_zero_or_none))
                
            # If previous digit is 1 and the current digit is 1
            if not is_prev_zero_or_none and s[idx] == '1':
                res = min(res, dp(idx + 1, is_prev_zero_or_none))
            
            return res
        
        return dp(0, True)
