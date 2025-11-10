https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        left = 0

        # Always drop the smallest when the condition is not met
        # Condition: nums[right] <= nums[left] * k
        for num in nums:
            if num > nums[left] * k:
                left += 1
                res += 1

        return res
