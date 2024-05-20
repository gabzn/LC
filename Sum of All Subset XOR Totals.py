https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        
        for size in range(1, N + 1):
            subsets = combinations(nums, size)
            
            for sub in subsets:
                sub_res = 0
                for x in sub:
                    sub_res ^= x
                res += sub_res
            
        return res
