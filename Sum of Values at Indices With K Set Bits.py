https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        
        for idx, num in enumerate(nums):
            if idx.bit_count() == k:
                res += num
        
        return res
