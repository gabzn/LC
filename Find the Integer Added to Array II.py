https://leetcode.com/problems/find-the-integer-added-to-array-ii/

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        nums1.sort()
        nums2.sort()
        
        res = inf
        for i in range(N):
            for j in range(i + 1, N):
                nums = [nums1[k] for k in range(N) if k != i and k != j]                
                diff = nums2[0] - nums[0]
                found = True
                
                for k in range(len(nums)):
                    if nums2[k] - nums[k] != diff:
                        found = False
                        break
                
                if found:
                    res = min(res, diff)
        
        return res
