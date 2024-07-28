https://leetcode.com/problems/count-number-of-texts/

class Solution:
    def countTexts(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        N = len(s)
        
        """
        0 1  2 3
        2 2 [2 2]
               i
          
        dp[4] += dp[3]
        dp[4] += dp[2]
        dp[4] += dp[1]
        """
        dp = [0] * (N + 1)
        dp[0] = 1
        for i in range(1, N + 1):
            dp[i] = dp[i - 1]
            
            if i - 2 >= 0 and s[i - 1] == s[i - 2]:
                dp[i] += dp[i - 2]
            else:
                continue
            
            if i - 3 >= 0 and s[i - 1] == s[i - 3]:
                dp[i] += dp[i - 3]
            else:
                continue
            
            if s[i - 1] == '7' or s[i - 1] == '9':
                if i - 4 >= 0 and s[i - 1] == s[i - 4]:
                    dp[i] += dp[i - 4]
            
#             steps = 3
#             if s[i - 1] == '7' or s[i - 1] == '9':
#                 steps = 4
            
#             for j in range(2, steps + 1):
#                 if i - j >= 0 and s[i - 1] == s[i - j]:
#                     dp[i] += dp[i - j]
#                 else:
#                     break
            
            dp[i] %= MOD
                    
        return dp[N] % MOD
