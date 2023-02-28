https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = math.inf
        
        while l <= r:
            m = (l + r) // 2
            
            res = min(res, nums[l], nums[m], nums[r])
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        
        return res    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------    
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right, min_element = 0, len(nums) - 1, nums[0]
        
        # If the leftmost is less than the rightmost,
        # it's guaranteed that this list maintains ascending order.
        if nums[left] < nums[right]:
            return min_element

        # Only two scenarios could happen:
            # [5, 1, 2, 3, 4]
            # [4, 5, 6, 2, 3]
        # When mid is less than right:
        #       the min will be on the left of mid
        # When mid is greater than right:
        #       the min will be on the right of mid
        
        # The reason we only want to look at the rightmost value instead of the leftmost is
        # becasue leftmost is guaranteed to be greater than the rightmost. Otherwise, the list is never rotated.
        
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
