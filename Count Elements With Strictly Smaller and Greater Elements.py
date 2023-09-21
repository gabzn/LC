https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution:
    def countElements(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        nums.sort()
        res = 0
        
        l, r = 0, LEN - 1
        for i in range(1, r):
            if nums[l] < nums[i] < nums[r]:
                res += 1
                
        return res
