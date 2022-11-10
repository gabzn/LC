https://leetcode.com/problems/house-robber/
  
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

#         max_money = nums[0]
        
#         for i in range(1, len(nums)):
#             previous_max = 0
#             for j in range(0, i-1):
#                 previous_max = max(previous_max, nums[j])
            
#             nums[i] += previous_max
#             max_money = max(nums[i], max_money)
        
#         return max_money
