https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.dp(nums, len(nums) - 1, {})

    def dp(self, nums, i, memo):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        
        if i not in memo:
            memo[i] = max(nums[i] + self.dp(nums, i - 2, memo), self.dp(nums, i - 1, memo))
        
        return memo[i]
--------------------------------------------------------------------------------------------------------------------  
class Solution:
    def rob(self, nums: List[int]) -> int:      
        if 1 <= len(nums) <= 2:
            return max(nums)
        
        l = len(nums)
        dp = [0] * l
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, l):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
