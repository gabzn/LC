https://leetcode.com/problems/longest-common-subsequence/
  
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        LEN1, LEN2 = len(text1), len(text2)
        
        # dp(l, r) returns the longest subsequence when the index for text1 is at l and the index for text 2 is at r.
        def dp(l, r, memo):
            if l == LEN1 or r == LEN2:
                return 0
            
            if (l, r) not in memo:
                if text1[l] == text2[r]:
                    memo[(l, r)] = 1 + dp(l + 1, r + 1, memo)
                else:
                    memo[(l, r)] = max(dp(l + 1, r, memo), dp(l, r + 1, memo))
                
            return memo[(l, r)]
        
        return dp(0, 0, {})
-------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        LEN1, LEN2 = len(text1), len(text2)
        dp = [[0 for j in range(LEN2 + 1)] for i in range(LEN1 + 1)]
        
        for i in range(0, LEN1):
            for j in range(0, LEN2):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[-1][-1]
