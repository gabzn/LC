Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
  
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
  
class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) == 1:
            return False
        
        unique_set = set()
        for num in nums:
            if num in unique_set:
                return True
            unique_set.add(num)
            
        return False
