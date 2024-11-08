https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], max_bits: int) -> List[int]:
        bit_counts = [0] * max_bits
        for bit in range(max_bits):
            for num in nums:
                bit_counts[bit] += ((num & (1 << bit)) > 0)

        res = []
        for num in reversed(nums):
            k = 0
            for i, count in enumerate(bit_counts):
                if count % 2 == 0:
                    k |= (1 << i)
                
                bit_counts[i] -= ((num & (1 << i)) > 0)
            res.append(k)
        return res
