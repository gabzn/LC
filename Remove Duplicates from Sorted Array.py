https://leetcode.com/problems/remove-duplicates-from-sorted-array/
  
# 2-pointer technique

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        k = 1
        
        """
        When [l] and [r] are having the same values, we want to move r until they are not the same.
        when [r] and [l] have different values, we can move l to the right and set [l + 1] to whatever [r] is.
        """
        l, r = 0, 1
        while r < len(nums):
            if nums[l] != nums[r]:
                k += 1
                l += 1
                nums[l] = nums[r]
            else:
                r += 1
            
        return k
