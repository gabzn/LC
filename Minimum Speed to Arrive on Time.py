https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l, r = 0, 10**7 + 1
        res = -1
        
        while l + 1 != r:
            m = (l + r) // 2
            
            if self.can_reach_on_m_speed(dist, m, hour):
                r = m
                res = m 
            else:
                l = m
        
        return res
        
    def can_reach_on_m_speed(self, dist, speed, hour):
        time = 0.0
        
        for idx, distance in enumerate(dist):
            t = distance / speed
            
            # Round off to the next integer, if not the last ride.
            if idx != len(dist) - 1:
                time += math.ceil(t)
            else:
                time += t
        
        return time <= hour        
