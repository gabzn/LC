https://leetcode.com/problems/first-missing-positive/
  
Given an unsorted integer array nums, return the smallest missing positive integer.

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
  
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Given nums with length n, the missing smallest positive integer can only range from [1...n+1]
        if nums is [1, 2, 3], the missing smallest pos int is guaranteed to be between [1, 2, 3, 4]
        """
        positive_nums = set()
        for num in nums:
            if num > 0: 
                positive_nums.add(num)
        
        for i in range(1, len(nums) + 2):
            if i not in positive_nums:
                return i
