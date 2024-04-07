https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        increasing_streak = 1
        decreasing_streak = 1
        
        for i, num in enumerate(nums):
            if i and num > nums[i-1]:
                increasing_streak += 1
            else:
                increasing_streak = 1
                
            if i and num < nums[i-1]:
                decreasing_streak += 1
            else:
                decreasing_streak = 1
            
            res = max(res, increasing_streak, decreasing_streak)
                
        return res
