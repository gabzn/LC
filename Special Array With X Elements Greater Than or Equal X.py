https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:                
        N = len(nums)
        nums.sort()
        
        for x in range(1, N + 1):
            i = bisect_left(nums, x)
            if N - i == x:
                return x
            
        return -1
