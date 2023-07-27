https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution:
    def minimumTime(self, time: List[int], total_trips: int) -> int:
        l, r = 0, (max(time) * total_trips) + 1
        res = 0
        
        while l + 1 != r:
            m = (l + r) // 2
            
            if self.can_make_all_trips_in_m_minutes(time, total_trips, m):
                r = m
                res = m
            else:
                l = m
                
        return res
    
    
    def can_make_all_trips_in_m_minutes(self, time, total_trips, m):
        trips = 0
        
        for t in time:
            trips += m // t
        
        return trips >= total_trips
