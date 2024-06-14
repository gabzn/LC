https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        N = len(nums)

        nums.sort()
        res = 0

        for i in range(1, N):
            if nums[i] <= nums[i - 1]:
                res += ((nums[i - 1] + 1) - nums[i])
                nums[i] = nums[i - 1] + 1

        return res
