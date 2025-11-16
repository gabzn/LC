https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        left = 0
        res = inf

        for right, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                res = min(res, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return res if res != inf else 0
