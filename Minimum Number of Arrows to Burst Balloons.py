https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
  
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:  
        points.sort(key=lambda point: point[0])
        arrows = 1
        start, end = points[0]
        
        for x_start, x_end in points:
            if start <= x_start <= end:
                end = min(end, x_end)
            else:
                arrows += 1
                start = x_start
                end = x_end
        
        return arrows
