https://leetcode.com/problems/intersection-of-two-arrays/
  
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return set1 & set2
-------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        
        # Sort the longer list then loop through the shorter one to perform BS on the longer one.
        if len(nums1) > len(nums2):
            nums1.sort()
            for num in nums2:
                self.binary_search(nums1, num, res)
        else:
            nums2.sort()
            for num in nums1:
                self.binary_search(nums2, num, res)
    
        return res
    
    def binary_search(self, nums, num, res):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == num:
                res.add(num)
                return
            
            if nums[m] > num:
                r = m - 1
            else:
                l = m + 1
        return 
