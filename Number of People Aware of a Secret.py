https://leetcode.com/problems/number-of-people-aware-of-a-secret/
https://www.youtube.com/watch?v=dalyTgkiH0s

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(1, n + 1):
            # The i-th person can start sharing at (i + delay) day up to but not including (i + forget)
            for j in range(i + delay, min(i + forget, n + 1)):
                dp[j] += dp[i]
        
        return sum(dp[n - forget + 1: ]) % MOD
