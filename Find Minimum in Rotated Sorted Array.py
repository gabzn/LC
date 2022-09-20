Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    
    
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
  
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
  
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right, min_element = 0, len(nums) - 1, nums[0]
        
        # If the leftmost is less than the rightmost,
        # it's guaranteed that this list maintains ascending order.
        if nums[left] < nums[right]:
            return min_element

        # We want to find the unsorted side because the min will always be in the unsorted side.
        while left <= right:
            mid = (left + right) // 2
            min_element = min(min_element, nums[mid])
            
            # If the rightmost is greater than the mid, that means everything on the right of mid is sorted.
            # Again, we want to find the unsorted side. If right is sorted, left must be unsorted and vice versa.
            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
            
        return min_element
