https://leetcode.com/problems/summary-ranges/
  
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        
        left = 0
        current_range = f"{nums[left]}"
        res = []
        
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1] + 1:
                res.append(current_range)
                left = right
                current_range = f"{nums[left]}"
            else:
                current_range = f"{nums[left]}->{nums[right]}"
                
        res.append(current_range)
        return res  
