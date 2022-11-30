https://leetcode.com/problems/find-pivot-index/
    
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, 0
        
        # Get the total sum of nums
        for num in nums:
            right_sum += num
            
        # If adding num to left_sum makes it equal to right_sum,
        # that means substracting num from both sides will make them equal.
        # Therefore, num is the pivot and its index is the pivot index.
        for ind, num in enumerate(nums):
            left_sum += num
            
            if left_sum == right_sum:
                return ind
            
            right_sum -= num
            
        return -1
---------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left_sum = 0
        right_sum = 0
        
        ## Balance Scale algorithm
        for index in range(1, len(nums)):
            right_sum += nums[index]
        
        if right_sum == 0:
            return 0
        
        for index in range(1, len(nums)):
            left_sum += nums[index-1]
            right_sum -= nums[index]
            
            if left_sum == right_sum:
                return index
                
        return -1
