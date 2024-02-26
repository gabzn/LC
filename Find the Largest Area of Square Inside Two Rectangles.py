https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

class Solution:
    def largestSquareArea(self, bottom: List[List[int]], top: List[List[int]]) -> int:
        LEN = len(top)
        
        res = 0
        
        for i in range(LEN):                        
            ax1, ay1 = bottom[i]
            ax2, ay2 = top[i]
            
            for j in range(i + 1, LEN):
                bx1, by1 = bottom[j]
                bx2, by2 = top[j]
                
                # Check for non-intersection
                to_the_left = ax2 <= bx1
                to_the_right = ax1 >= bx2
                to_the_top = ay1 >= by2
                to_the_bottom = ay2 <= by1
                
                # Negate the condition meaning if any fails, there's an intersection
                if not (to_the_left or to_the_right or to_the_top or to_the_bottom):
                    x = min(ax2, bx2) - max(ax1, bx1)
                    y = min(ay2, by2) - max(ay1, by1)
                
                    res = max(res, min(x, y) ** 2)
            
        return res
---------------------------------------------------------------------------------------------------
class Solution:
    def largestSquareArea(self, bottom: List[List[int]], top: List[List[int]]) -> int:
        LEN = len(top)
        
        res = 0
        
        for i in range(LEN):
            ix_start, ix_end = bottom[i][0], top[i][0]
            iy_start, iy_end = bottom[i][1], top[i][1]
            
            for j in range(i + 1, LEN):
                jx_start, jx_end = bottom[j][0], top[j][0]
                jy_start, jy_end = bottom[j][1], top[j][1]
                
                x = min(ix_end, jx_end) - max(ix_start, jx_start)
                y = min(iy_end, jy_end) - max(iy_start, jy_start)
                
                # If there are no overlapping, min(x, y) will either give negative or 0
                res = max(res, max(min(x, y), 0) ** 2)
                    
        return res
