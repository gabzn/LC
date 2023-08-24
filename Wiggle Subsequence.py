https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        LEN = len(nums)
        if LEN == 1:
            return 1
        
        # dp[i][0] = max len at i ending with +
        # dp[i][1] = max len at i ending with -
        dp = [[1, 1] for _ in range(LEN)] 
      
        for r in range(1, LEN):
            for l in range(r):
                if nums[r] - nums[l] > 0:
                    dp[r][0] = max(dp[l][1] + 1, dp[r][0])
                if nums[r] - nums[l] < 0:
                    dp[r][1] = max(dp[l][0] + 1, dp[r][1])
        
        return max(dp[-1])
