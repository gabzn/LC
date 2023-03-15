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
