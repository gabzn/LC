https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        res = inf
        left = 0
        right = len(nums) - 1
        
        while left < right:
            res = min(res, nums[left] + nums[right])
            left += 1
            right -= 1
        
        return res / 2
