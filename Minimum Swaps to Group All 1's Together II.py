https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)

        # We can use a sliding window of size X where X is the number of one in the input
        # because the end result has X consecutive ones.
        window_size = nums.count(1)
        res = window_size

        # Double the input to handle the circular part.
        nums = nums + nums

        # This is the number of zeroes we want to swap out in the window.
        zeroes_in_window = 0

        # The end condition is:
        # Say nums is [1, 0, 1, 1] before doubling
        # and [1, 0, 1, 1, 1, 0, 1, 1] after doubling.
        # Left pointer should stop when it's at index 4.
        left = right = 0
        while left != N:
            if nums[right] == 0:
                zeroes_in_window += 1

            # If the current window size is less than the expected window size,
            # move right pointer by 1.
            if (right - left + 1) < window_size:
                right += 1
                continue

            # We have a valid window now. Check to see how many swaps needed to swap out all the 0's.
            res = min(res, zeroes_in_window)
            if nums[left] == 0:
                zeroes_in_window -= 1

            left += 1
            right += 1

        return res
