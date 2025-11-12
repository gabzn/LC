https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Because the beauty is the longest subsequence of EQUAL elements,
        # we can always sort the input.
        # If you can make any number the same, the order doesn't matter any more.

        # [4, 6, 1, 2] -> [1, 2, 4, 6]
        # Pick index 3 as an example. If we want to know the longest subsequence ending at index 3,
        # the leftmost value cannot be smaller than 4 - 2 * k.
        # Assume the leftmost value is x and the rightmost is y:
        # x, x + 1, x + 2, ... x + k, y - k, y - k + 1, y - k + 2, ..., y
        # The distance between x and y cannot be more than 2 * k.
        nums.sort()
        res = 0
        left = 0

        for right, num in enumerate(nums):
            while num - nums[left] > 2 * k:
                left += 1
            res = max(res, right - left + 1)

        return res
