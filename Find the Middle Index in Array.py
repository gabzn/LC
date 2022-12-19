https://leetcode.com/problems/find-the-middle-index-in-array/
  
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        
        for ind, num in enumerate(nums):
            left_sum += num
        
            if left_sum == right_sum:
                return ind
            
            right_sum -= num
         
        return -1
