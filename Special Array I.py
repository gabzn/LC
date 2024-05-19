https://leetcode.com/problems/special-array-i/

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        N = len(nums)
        prev = nums[0] % 2
        
        for i in range(1, N):
            if nums[i] % 2 == prev:
                return False
            prev = nums[i] % 2
            
        return True
