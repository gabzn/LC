There is an integer array nums sorted in ascending order. 
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
  
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        # Treat this problem like a normal BS problem
        # The only tweak is to perform BS on the correct side.
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # If everything on the left of mid is smaller than mid 
            # AND target falls between this portion, we only want to do BS on this portion.
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Else means everything on the left is greater than mid, we looking at the right side.
            # AND target falls between this portion, we do BS on this portion.
            else:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
