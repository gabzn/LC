https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        LEN = len(nums)
        res = 0
        
        for i in range(LEN):
            for j in range(i+1, LEN):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    res = max(res, nums[i] ^ nums[j])
        
        
        return res
