https://leetcode.com/problems/subsets/
  
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(nums, [], [], 0)
    
    def backtrack(self, nums, current, res, start_idx):
        res.append(current.copy())
        
        for idx in range(start_idx, len(nums)):
            current.append(nums[idx])
            res = self.backtrack(nums, current, res, idx + 1)
            current.pop()
        
        return res
