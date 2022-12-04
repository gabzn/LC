https://leetcode.com/problems/container-with-most-water/
  
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            distance = r - l
            cur_area = min(height[r], height[l]) * distance            
            max_area = max(cur_area, max_area)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
                
        return max_area
