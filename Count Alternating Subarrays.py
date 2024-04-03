https://leetcode.com/problems/count-alternating-subarrays/

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        
        res = 0
        streak = 0
        
        for i in range(N):
            if i and nums[i] != nums[i-1]:
                streak += 1
            else:
                streak = 1
            
            res += streak
        
        return res
-------------------------------------------------------------------
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [0] * N
        dp[0] = 1        
        
        for i in range(1, N):
            if nums[i] == nums[i-1]:
                dp[i] = 1
            else:
                dp[i] = dp[i-1] + 1
                
        return sum(dp)
