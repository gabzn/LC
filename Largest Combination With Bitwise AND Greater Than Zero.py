https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution:
    def largestCombination(self, nums):
        res = 0
        for i in range(24):
            count = 0
            for num in nums:
                count += ((num & (1 << i)) > 0)
            res = max(res, count)
        return res
----------------------------------------------------------------------------------
class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        bits = [0] * 24
        for num in nums:
            for bit in range(24):
                is_bit_set = num & (1 << bit)
                bits[bit] += (is_bit_set > 0)
        return max(bits)
