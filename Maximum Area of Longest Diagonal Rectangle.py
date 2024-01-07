https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diagonal = area = 0
        
        for l, w in dimensions:
            cur_diagonal = (l ** 2) + (w ** 2)
            
            if cur_diagonal > diagonal:
                diagonal = cur_diagonal
                area = l * w
            if cur_diagonal == diagonal:
                area = max(area, l * w)
                    
        return area
