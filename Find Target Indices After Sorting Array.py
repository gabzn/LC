https://leetcode.com/problems/find-target-indices-after-sorting-array/

# Python library
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()        
        return range(bisect_left(nums, target), bisect_right(nums, target))  

# My own bisect_left and right
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l, r = 0, len(nums)
        
        while l < r:
            m = (l + r) // 2
            
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        leftmost = l
        
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        rightmost = l
        
        return range(leftmost, rightmost)  
      
# Brute force
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        
        for idx, num in enumerate(nums):
            if num == target:
                res.append(idx)

        return res
