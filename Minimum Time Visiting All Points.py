https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        
        for i in range(1, len(points)):
            prev_x, prev_y = points[i - 1]
            cur_x, cur_y = points[i]
            
            distance_x = abs(prev_x - cur_x)
            distance_y = abs(prev_y - cur_y)
            
            if distance_x == distance_y:
                res += distance_x
            elif distance_x > distance_y:
                res += distance_y + abs(distance_x - distance_y)
            else:
                res += distance_x + abs(distance_x - distance_y)
        
        return res
