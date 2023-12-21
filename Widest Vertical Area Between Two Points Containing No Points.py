https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        LEN = len(points)
        
        points.sort()
        res = 0
        
        for idx in range(1, LEN):
            res = max(res, points[idx][0] - points[idx-1][0])
                
        return res
