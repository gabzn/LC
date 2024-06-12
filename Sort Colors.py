https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:        
        N = len(nums)
        
        insertion_idx = 0
        for i, num in enumerate(nums):
            if num == 0:
                nums[insertion_idx], nums[i] = nums[i], nums[insertion_idx]
                insertion_idx += 1

        for i, num in enumerate(nums):
            if num == 1:
                nums[insertion_idx], nums[i] = nums[i], nums[insertion_idx]
                insertion_idx += 1
