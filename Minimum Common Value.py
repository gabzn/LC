https://leetcode.com/problems/minimum-common-value/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        
        l = r = 0
        
        while l < N and r < M:
            if nums1[l] == nums2[r]:
                return nums1[l]
            
            if nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        
        return -1
