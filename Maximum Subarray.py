https://leetcode.com/problems/maximum-subarray/
  
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum, ans = 0, -math.inf
        
        for num in nums:
            # If adding num to the running_sum makes it smaller
            # that means it's better to start fresh at num
            running_sum = max(running_sum + num, num)
            ans = max(running_sum, ans)
            
        return ans  
      
------------------------------------------------------------------------------------------------------
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        LEN = len(nums)
        dp = [0] * LEN
        dp[0] = nums[0]

        prev_max = nums[0]

        for idx in range(1, LEN):
            prev_max = max(prev_max + nums[idx], nums[idx])
            dp[idx] = prev_max
        
        return max(dp)    
