https://leetcode.com/problems/special-array-i/

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for x, y in pairwise(nums):
            if x % 2 == y % 2:
                return False
        return True
--------------------------------------------------------
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        N = len(nums)
    
        for i in range(1, N):
            if nums[i] % 2 == nums[i-1] % 2:
                return False
                
        return True
