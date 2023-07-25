https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = -1, len(arr)
        
        while l + 1 != r:
            m = (l + r) // 2
            
            if m == 0 or arr[m] > arr[m - 1]:
                l = m
            else:
                r = m
        
        return l
