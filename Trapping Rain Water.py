https://leetcode.com/problems/trapping-rain-water/
  
class Solution:
    def trap(self, height: List[int]) -> int:
        H, water = len(height), 0
        left_max, right_max = [0] * H, [0] * H 
        
        """
        Very important! If you remember this, you'll know how to solve this problem.
        For each cell, how much water is trapped depends on the min of my max left and max right.
        So, we compute the left max and right max for each cell first.
        """
        for ind in range(0, H):
            if ind == 0:
                left_max[ind] = height[ind]
            else:
                left_max[ind] = max(left_max[ind-1], height[ind])
        
        for ind in range(H-1, -1, -1):
            if ind == H-1:
                right_max[ind] = height[ind]
            else:
                right_max[ind] = max(right_max[ind+1], height[ind])

        for ind, cell in enumerate(height):
            min_between_left_right = min(left_max[ind], right_max[ind])
            if min_between_left_right - cell > 0:
                water += (min_between_left_right - cell)

        return water
