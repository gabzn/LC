https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        N = len(points)
        
        points.sort()
        res = 0
        left = 0
        
        while left < N:
            right = left + 1
            start, end = points[left]
            
            while right < N and start <= points[right][0] <= end:
                end = min(end, points[right][1])
                right += 1
            
            res += 1
            left = right
        
        return res
--------------------------------------------------------------------------
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
