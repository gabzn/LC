https://leetcode.com/problems/max-consecutive-ones-ii/
  
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, zeroes, res = 0, 0, 0
        
        # We keep track of the number of zeroes we have seen
        # If we have more than one zero, we move the left ptr until we have one zero.
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
