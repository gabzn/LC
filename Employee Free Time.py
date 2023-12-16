https://leetcode.com/problems/employee-free-time/

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':        
        sorted_intervals = []
        for intervals in schedule:
            for interval in intervals:              
                sorted_intervals.append((interval.start, interval.end))
        
        sorted_intervals.sort()
        
        res = []
        latest_end = sorted_intervals[0][1]
        for idx in range(1, len(sorted_intervals)):
            cur_start, cur_end = sorted_intervals[idx]
            
            if cur_start > latest_end:
                res.append(Interval(latest_end, cur_start))
                
            latest_end = max(latest_end, cur_end)
                
        return res
