https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        MAJORIY = len(nums) // 2
        left_bound = self.lower_bound(nums, target)   
        right_bound = self.upper_bound(nums, target)

        return (right_bound - left_bound + 1) > MAJORIY
    
    def lower_bound(self, nums, target):
        l, r = -1, len(nums)
        while l + 1 != r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m 
                
        return r
    
    def upper_bound(self, nums, target):
        l, r = -1, len(nums)
        while l + 1 != r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m  
                
        return l
