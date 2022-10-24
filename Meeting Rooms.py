https://www.lintcode.com/problem/920/description
  
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:  (0,30), (5,10) and (0,30),(15,20) will conflict

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation:  Two times will not conflict 
  
  
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if 0 <= len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda interval: interval.start)

        for i in range(1, len(intervals)):
            previous_interval = intervals[i-1]
            current_interval = intervals[i]

            if current_interval.start < previous_interval.end:
                return False
        
        return True
