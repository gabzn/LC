https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        for idx in range(N):            
            while True:
                correct_idx = nums[idx] - 1
                
                if nums[correct_idx] == nums[idx]:
                    break
                else:
                    nums[idx], nums[correct_idx] = nums[correct_idx], nums[idx]
        
        res = []
        
        for idx, num in enumerate(nums):
            if idx + 1 != num:
                res.append(num)
        
        return res
