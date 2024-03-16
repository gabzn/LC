https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        
        prefix_map = {}
        prefix_map[0] = -1
        
        res = 0
        running_sum = 0
        
        for right in range(N):
            running_sum += (nums1[right] - nums2[right])
            
            if running_sum in prefix_map:
                left = prefix_map[running_sum]
                res = max(res, right - left)
            else:
                prefix_map[running_sum] = right
        
        return res
