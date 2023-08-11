https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = 1000
        
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == target:
                res = min(res, abs(start - l))
            if nums[r] == target:
                res = min(res, abs(start - r))
            l += 1
            r -= 1
        
        return res
