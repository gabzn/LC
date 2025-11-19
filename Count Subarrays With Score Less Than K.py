https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        window_sum = 0

        for right, num in enumerate(nums):
            window_sum += num
            window_size = (right - left + 1)

            while window_sum * window_size >= k:
                window_sum -= nums[left]
                window_size -= 1
                left += 1

            res += window_size

        return res
