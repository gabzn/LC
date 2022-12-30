https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
  
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        # Find the medium of the entire array and try to make every number close to it.
        medium = nums[len(nums) // 2]
        moves = 0
        
        for num in nums:
            moves += abs(medium - num)
        
        return moves
