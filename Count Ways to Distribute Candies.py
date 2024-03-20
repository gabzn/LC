https://leetcode.com/problems/count-ways-to-distribute-candies/

class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        
        # dp[i][j] = # of ways to distribute 0 - i cookies to j bags 
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = 1
        
        for i in range(1, n + 1):
            for j in range(2, k + 1):
                # If we put the current candy into a new bag (j-th) 
                # we'll need to know how many ways we put all previous candies in to (j - 1) bags -> dp[i-1][j-1]
                
                # If all previous candies have been put in to j bags
                # we need to choose one bag out of j bags to put the current candy. We'll have j bags to choose from -> dp[i-1][j] * j
                dp[i][j] = (dp[i-1][j-1] + (dp[i-1][j] * j)) % MOD
        
        return dp[n][k] % MOD
