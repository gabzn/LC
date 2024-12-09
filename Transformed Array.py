https://leetcode.com/problems/transformed-array/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        return [nums[((i + num) % size) + size % size] for i, num in enumerate(nums)]
