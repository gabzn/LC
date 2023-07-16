https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        res = 1
        
        for num in arr:
            dp[num] = 1 + dp[num - difference]
            res = max(res, dp[num])
        
        return res
