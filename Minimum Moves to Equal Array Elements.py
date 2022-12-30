https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
  
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        nums.sort()
    
        for index in range(len(nums)-1, -1, -1):
            moves += (nums[index] - nums[0])
        
        return moves
