https://leetcode.com/problems/frequency-of-the-most-frequent-element/
  
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        window_sum = 0
        left = 0
        res = 1

        for right, num in enumerate(nums):
            window_sum += num

            # num * (right - left + 1) = total sum if we change all nums from [left, right] to num
            # If total sum - window_sum > k, that means we don't have enough operations.
            while num * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1

            res = max(res, right - left + 1)

        return res
