https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        res = 0
        
        for i in range(LEN):
            largest = smallest = nums[i]
            
            for j in range(i, LEN):
                largest = max(largest, nums[j])
                smallest = min(smallest, nums[j])
                
                res += largest - smallest
        
        return res
