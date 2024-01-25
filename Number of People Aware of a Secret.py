https://leetcode.com/problems/number-of-people-aware-of-a-secret/

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(1, n + 1):
            for person in range(i + delay, min(i + forget, n + 1)):
                dp[person] += dp[i]
        
        return sum(dp[n - forget + 1: ]) % MOD
