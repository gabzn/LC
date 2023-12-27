https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        nums.sort()
        
        pref = [nums[0]]
        for i in range(1, LEN):
            pref.append(pref[-1] + nums[i])
        
        for i in range(LEN - 1, 0, -1):
            if pref[i - 1] > nums[i]:
                return pref[i]
        
        return -1    
