https://leetcode.com/problems/missing-number/
  
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
  
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0
        for num in range(1, len(nums)+1):
            total_sum += num
            
        for num in nums:
            total_sum -= num
            
        return total_sum
