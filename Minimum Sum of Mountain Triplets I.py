https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        res = math.inf
        for j in range(1, LEN - 1):
            for i in range(j):
                for k in range(j + 1, LEN):
                    if nums[j] > nums[i] and nums[j] > nums[k]:
                        res = min(res, nums[j] + nums[i] + nums[k])
                        
        return res if res != math.inf else -1
