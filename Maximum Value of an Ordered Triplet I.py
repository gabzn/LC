https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        LEN = len(nums)
        res = -math.inf
        
        for i in range(LEN):
            for j in range(i + 1, LEN):
                for k in range(j + 1, LEN):
                    res = max((nums[i] - nums[j]) * nums[k], res)
        
        return res if res > 0 else 0
