https://leetcode.com/problems/find-k-closest-elements/
  
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        
        # Find the largest num that is less than or equal to x
        l = self.find_largest_num_less_or_equal_to_x(arr, x) - 1
        r = l + 1
        
        """
        Expand the window from l and r
        if both l and r are inbound, we move l when abs(arr[l] - x) <= abs(arr[r] - x). Otherwise, move r.
        elif r is out of bound, just move l
        else means l is out of bound, move r
        """
        while k:
            if l >= 0 and r < len(arr):
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    l -= 1
                else:
                    r += 1
            
            elif l >= 0:
                l -= 1
            else:
                r += 1
            
            k -= 1

        return arr[l+1: r]
    
    def find_largest_num_less_or_equal_to_x(self, arr, x):
        l, r = 0, len(arr) - 1
        
        while l < r:
            m = (l + r) // 2
            
            if arr[m] < x:
                l = m + 1
            else:
                r = m
                
        return l
