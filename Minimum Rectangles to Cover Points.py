https://leetcode.com/problems/minimum-rectangles-to-cover-points/

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        N = len(points)
        
        points.sort()
        res = 0
        i = 0
        
        while i < N:
            start = points[i][0]
            end = start + w
            
            j = i
            while j < N:
                if points[j][0] <= end:
                    j += 1
                else:
                    break
            
            res += 1
            i = j
            
        return res
