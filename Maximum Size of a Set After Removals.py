https://leetcode.com/problems/maximum-size-of-a-set-after-removals/
https://www.youtube.com/watch?v=U9ME81R6LjY&t=253s
https://www.youtube.com/watch?v=63dNVenHJ_c&t=502s

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        HALF = len(nums1) // 2
        
        """
        Instead of thinking about deleting elements, think about adding elements.
        """
        set1 = set(nums1)
        set2 = set(nums2)   
        common_in_both_sets = set1 & set2
        
        unique_to_num1 = list(set1 - common_in_both_sets)
        unique_to_num2 = list(set2 - common_in_both_sets)
                
        for num in common_in_both_sets:
            if len(unique_to_num1) < HALF:
                unique_to_num1.append(num)
            else:
                unique_to_num2.append(num)
        
        return min(len(unique_to_num1), HALF) + min(len(unique_to_num2), HALF)
