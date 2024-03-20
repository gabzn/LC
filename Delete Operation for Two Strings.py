https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        LEN1 = len(word1)
        LEN2 = len(word2)
        
        # dp[i][j] = min # of steps to make word1[0: i] and word2[0: j] the same
        dp = [[inf for _ in range(LEN2 + 1)] for _ in range(LEN1 + 1)]
        word1 = "/" + word1
        word2 = "/" + word2

        for i in range(LEN1 + 1):
            dp[i][0] = i
        
        for j in range(LEN2 + 1):
            dp[0][j] = j
        
        for i in range(1, LEN1 + 1):
            for j in range(1, LEN2 + 1):
                """
                Problem like this usually has very few states to consider
                [i][j] can only come from [i-1][j-1], [i-1][j] and [i][j-1]
                """
                # The current char is the same, so we only need to copy over the previous state
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                    
                # The curretn char is not the same, we can either:
                #   1. Delete i -> dp[i-1][j] + 1
                #   2. Delete j -> dp[i][j-1] + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[-1][-1]
