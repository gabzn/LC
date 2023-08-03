https://leetcode.com/problems/count-special-quadruplets/

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        LEN = len(nums)
        res = 0
        
        for first in range(LEN):
            for second in range(first + 1, LEN):
                for third in range(second + 1, LEN):
                    for fourth in range(third + 1, LEN):
                        if nums[first] + nums[second] + nums[third] == nums[fourth]:
                            res += 1
        
        return res
