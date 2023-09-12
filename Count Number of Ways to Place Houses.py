https://leetcode.com/problems/count-number-of-ways-to-place-houses/
https://www.youtube.com/watch?v=Q5JUafX3iMc

class Solution:
    def countHousePlacements(self, n: int) -> int:
        """
        The intuition is that we only need to know 
        how many ways there are to build on one side of the street.
        To find the total #, we just need to find one side and square it.
        """
        MOD = 10**9 + 7
        
        # dp[i][not_build] = dp[i-1][build] + dp[i-1][not_build]        
        # dp[i][build] = dp[i-1][not_build]
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]
        dp[1][0] = 1
        dp[1][1] = 1
        
        for i in range(2, n + 1):
            dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
            dp[i][1] = dp[i-1][0] % MOD
        
        return ((dp[n][0] + dp[n][1]) ** 2) % MOD
