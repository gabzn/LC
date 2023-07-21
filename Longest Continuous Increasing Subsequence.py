https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l, max_len = 0, 1
        
        for r in range(len(nums)):
            if r > 0 and nums[r] > nums[r - 1]:
                max_len = max(max_len, r - l + 1)
            else:
                l = r
            
        return max_len
