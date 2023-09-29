https://leetcode.com/problems/count-strictly-increasing-subarrays/

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        res = [1 for _ in range(LEN)]
        for idx in range(1, LEN):
            if nums[idx] > nums[idx - 1]:
                res[idx] += res[idx - 1]
        
        return sum(res)
