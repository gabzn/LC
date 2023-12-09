https://leetcode.com/problems/patching-array/
https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        max_range = res = idx = 0
        
        while max_range < n:
            if idx < len(nums) and nums[idx] <= max_range + 1:
                max_range += nums[idx]
                idx += 1
            else:
                res += 1
                max_range += (max_range + 1)
                
        return res
