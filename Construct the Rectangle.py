https://leetcode.com/problems/construct-the-rectangle/

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        res = [area, 1]
        
        for width in range(1, math.floor(sqrt(area)) + 1):
            prev_diff = res[0] - res[1]    
            
            length = area // width
            if length * width == area:
                cur_diff = length - width
                if cur_diff < prev_diff:
                    res = [length, width]
    
        return res
