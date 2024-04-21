https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        
        pre_max = [0] * N
        pre_max[0] = height[0]
        for i in range(1, N):
            pre_max[i] = max(pre_max[i-1], height[i])
            
        suf_max = [0] * N
        suf_max[-1] = height[-1]
        for i in range(N - 2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])
        
        res = 0
        for left_max, right_max, h in zip(pre_max, suf_max, height):
            res += min(left_max, right_max) - h
        
        return res
--------------------------------------------------------------------------------
class Solution:
    def trap(self, height: List[int]) -> int:
        H, water = len(height), 0
        left_max, right_max = [0] * H, [0] * H 
        
        """
        Very important! If you remember this, you'll know how to solve this problem.
        For each cell, how much water is trapped on that cell depends on the min of its max left and max right.
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
