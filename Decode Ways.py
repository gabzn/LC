https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        LEN = len(s)
        
        def dp(i, memo):
            if i >= LEN:
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]

            memo[i] = dp(i + 1, memo)
            if i + 1 < LEN and int(s[i] + s[i + 1]) <= 26:
                memo[i] += dp(i + 2, memo)

            return memo[i]
            
        return dp(0, {})
