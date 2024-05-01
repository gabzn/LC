https://leetcode.com/problems/count-pairs-in-two-arrays/

from sortedcontainers import SortedList

class Solution:
    def countPairs(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        
        """
        A[i] + A[j] > B[i] + B[j]
        A[i] - B[i] > B[j] - A[j]
        
        Each iteration you are fixing the right side of the equation (nums1[j] - nums2[j]) 
        and finding an index i from previous differences such that the left side > the right side.
        
        You might attemp to do it the other way around by fixing the left side of the equation. 
        You can't do that becasue i has to come before j. 
        If you fix the left side, and attemp to find a j such that the left side > the right side, 
            that would mean j comes before i.
        """
        res = 0
        sorted_lst = SortedList()
        for a, b in zip(A, B):
            right_side = b - a
            i = sorted_lst.bisect_right(right_side)
            res += len(sorted_lst) - i
            
            left_side = a - b
            sorted_lst.add(left_side)
    
        return res
