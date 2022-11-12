https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Input: intervals = [[7,10],[2,4]]
Output: true

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) == 1:
            return True
        
        intervals.sort(key=lambda interval: interval[0])
        
        l, r = 0, 1
        while r < len(intervals):
            first_meeting = intervals[l]
            second_meeting = intervals[r]
            
            if first_meeting[1] > second_meeting[0]:
                return False
            
            l += 1
            r += 1
            
        return True

-------------------------------------------------------------------------------------------------------------------------------------------------------- 
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
