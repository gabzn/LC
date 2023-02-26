https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # The general idea is to look at the side that is in increasing order!!!
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # When the left half is not rotated meaning the left half still has increasing order
            if nums[m] >= nums[l]:
                # and target falls under the range nums[l] <= t <= nums[m]
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
                    
            # When the left half is rotated, the right half has to be in increasing order
            else:
                # and target falls under the range 
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
        return -1
------------------------------------------------------------------------------------------------------------------------------------------------------  
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
