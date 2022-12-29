https://leetcode.com/problems/jump-game/
  
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        LEN = len(nums)
        if LEN == 1:
            return True
        
        target_index, can_reach = LEN - 1, True
        
        for index in range(LEN-2, -1, -1):
            if nums[index] + index >= target_index:
                target_index = index
                can_reach = True
            else:
                can_reach = False
        
        return can_reach
