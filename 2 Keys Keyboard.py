https://leetcode.com/problems/2-keys-keyboard/

class Solution:
    def minSteps(self, n: int) -> int:
        if n <= 4:
            return 0 if n == 1 else n

        dp = [inf] * (n + 1)
        dp[1] = 0
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        
        for i in range(5, n + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        
        return dp[-1]
-------------------------------------------------------------
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [inf] * (n + 1)
        dp[1] = 0        
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[-1]
