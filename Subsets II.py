https://leetcode.com/problems/subsets-ii/
  
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.backtrack(nums, 0, [], [])
    
    def backtrack(self, nums, idx, current, res):
        res.append(current.copy())
        
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
                
            current.append(nums[i])
            res = self.backtrack(nums, i + 1, current, res)
            current.pop()
            
        return res
