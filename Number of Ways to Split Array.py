https://leetcode.com/classic/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = left = 0
        total = sum(nums)
        for i in range(len(nums) - 1):
            left += nums[i]
            right = total - left
            if left >= right:
                res += 1
        return res
