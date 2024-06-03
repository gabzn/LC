https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        N = len(nums)

        res = 0
        last = -inf

        for i in range(N - 1, -1, -1):
            if nums[i] > last:
                last = nums[i]
            else:
                last += nums[i]

            res = max(res, last)

        return res
