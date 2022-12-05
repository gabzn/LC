https://leetcode.com/problems/merge-sorted-array/
  
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not n:
            return
        
        m -= 1
        n -= 1
        ptr = len(nums1) - 1
        
        while n >= 0 and m >= 0:
            if nums2[n] >= nums1[m]:
                nums1[ptr] = nums2[n]
                n -= 1
            else:
                nums1[ptr] = nums1[m]
                m -= 1
            
            ptr -= 1
        
        # If possible, fill nums1 with whatever is left in nums2
        while n >= 0:
            nums1[ptr] = nums2[n]
            ptr -= 1
            n -= 1
