https://leetcode.com/problems/maximum-erasure-value/description/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        window_sum = 0
        left = 0
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
            window_sum += num

            while counter[num] > 1:
                to_remove = nums[left]
                counter[to_remove] -= 1
                window_sum -= to_remove
                left += 1

            res = max(window_sum, res)

        return res
