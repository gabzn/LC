https://leetcode.com/problems/single-element-in-a-sorted-array/
  
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
    
        while l < r:
            m = (l + r) // 2
            
            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]
            
            is_even_len = (r - m) % 2 == 0
            if nums[m] == nums[m - 1]:
                if is_even_len:
                    r = m - 2
                else:
                    l = m + 1
            else:
                if is_even_len:
                    l = m + 2
                else:
                    r = m - 1
                
        return nums[l]
