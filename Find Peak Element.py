https://leetcode.com/problems/find-peak-element/
  
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            
            # The constraints say i != i + 1, so we don't need to care about when they are equal.
            # If the middle > the element to its right, the peak can only be on the left side or the middle.
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1
        
        return l
