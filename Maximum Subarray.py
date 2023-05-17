https://leetcode.com/problems/maximum-subarray/
  
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum, ans = 0, -math.inf
        
        for num in nums:
            # If adding num to the running_sum makes it smaller
            # that means it's better to take num and start fresh
            running_sum = max(running_sum + num, num)
            ans = max(running_sum, ans)
            
        return ans  
