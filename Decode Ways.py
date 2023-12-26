https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        LEN = len(s)
        
        @cache
        def dp(i):
            if i == LEN:
                return 1
            if s[i] == '0':
                return 0
            
            res = dp(i + 1)
            if i + 1 < LEN and int(s[i] + s[i + 1]) <= 26:
                res += dp(i + 2)
            
            return res
        
        return dp(0)
-------------------------------------------------------------------------------
class Solution:
    def numDecodings(self, s: str) -> int:
        LEN = len(s)
        
        # dp(i) returns the number of ways to decode starting at index i
        def dp(i, memo):
            # If the index is out of bound, that means this str was decoded
            if i == LEN:
                return 1
            # If the current digit is a leading 0 or 0, no str can be decoded
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]

            # We can decode 1 at a time and 2 at a time
            memo[i] = dp(i + 1, memo)
            # We only decode 2 at a time when it's within the length and the digit is less than 26
            if i + 1 < LEN and int(s[i] + s[i + 1]) <= 26:
                memo[i] += dp(i + 2, memo)

            return memo[i]
            
        return dp(0, {})
