https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
  
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        positions = [-1, -1]
        
        # Use binary search to find the first position.
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                # To determine if the current mid is the leftmost target, there's 2 ways to check
                #       1: We check if there's any more elements on the left ==> Check if m - 1 is out of bound
                #       2: We check if the element of the left is also the target  ==> Check if nums[m-1] != target
                if  (m-1 < 0) or nums[m-1] != target:
                    positions[0] = m
                    break
                
                # If the element of the left is also the target, that means the current mid is not the leftmost target. 
                # Move l to m - 1
                if nums[m-1] == target:
                    r = m - 1
                    
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
        
        # Repeat to find the last position.
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                # To determine if the current mid is the rightmost target, there's 2 ways to check
                #       1: We check if there's any more elements on the right ==> Check if m + 1 is out of bound
                #       2: We check if the element of the right is also the target  ==> Check if nums[m+1] != target
                if (m+1 > len(nums)-1) or nums[m+1] != target:
                    positions[1] = m
                    break
                
                # If the element of the right is also the target, that means the current mid is not the rightmost target. 
                # Move l to m + 1
                if nums[m+1] == target:
                    l = m + 1
            
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
        
        return positions
