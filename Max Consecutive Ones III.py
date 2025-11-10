https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        zeroes = 0

        # Counter the number of zeroes in the window and make sure it's <= k
        for right, num in enumerate(nums):
            zeroes += (num == 0)

            while zeroes > k:
                zeroes -= (nums[left] == 0)
                left += 1

            res = max(right - left + 1, res)

        return res
