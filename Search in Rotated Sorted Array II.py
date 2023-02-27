https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
  
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            
            # If we have duplicates, we just remove them.
            if nums[m] == nums[l]:
                l += 1
                continue
            if nums[m] == nums[r]:
                r -= 1
                continue
                
            # Same logic as Q1
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return False
