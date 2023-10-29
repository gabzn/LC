https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero_in_1, zero_in_2 = nums1.count(0), nums2.count(0)
        sum_1, sum_2 = map(sum, [nums1, nums2])
        
        if zero_in_1 == 0 and sum_1 < sum_2 + zero_in_2:
            return -1
        
        if zero_in_2 == 0 and sum_2 < sum_1 + zero_in_1:
            return -1
        
        return max(sum_1 + zero_in_1, sum_2 + zero_in_2)
