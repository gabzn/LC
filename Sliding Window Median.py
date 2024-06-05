https://leetcode.com/problems/sliding-window-median/

from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        N = len(nums)
        MID = k // 2
        
        sl = SortedList()
        res = []
        
        for i, num in enumerate(nums):
            if len(sl) == k:
                sl.discard(nums[i - k])
            
            sl.add(num)
            
            if i >= k - 1:
                res.append(sl[MID] if k % 2 else (sl[MID] + sl[MID - 1]) / 2)
                
        return res
