https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        max_len = 1
        
        for right in range(1, N):
            for left in range(0, right):
                if nums[right] > nums[left]:
                    dp[right] = max(dp[right], 1 + dp[left])
                    max_len = max(max_len, dp[right])
                    
        return max_len
