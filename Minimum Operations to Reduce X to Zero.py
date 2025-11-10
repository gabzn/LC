https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        TOTAL = sum(nums)
        if TOTAL < x:
            return -1

        # Find the longest subarray that sums up to total - x
        # If we have such a subarray and it's the longest, 
        # then we can remove everything that's not in the subarray to get a total of x and it's guaranteed to be the shortest.
        longest_subarray_sum = TOTAL - x
        res = -inf
        window_sum = 0
        left = 0

        for right, num in enumerate(nums):
            window_sum += num

            while window_sum > longest_subarray_sum:
                window_sum -= nums[left]
                left += 1

            if window_sum == longest_subarray_sum:
                res = max(right - left + 1, res)

        return len(nums) - res if res != -inf else -1
