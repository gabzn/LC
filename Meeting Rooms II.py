https://leetcode.com/problems/meeting-rooms-ii/
      
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        total_rooms, current_rooms_needed = 0, 0
        room_allocations = []
        
        intervals.sort(key=lambda interval: interval[0])
        for interval in intervals:
            start, end = interval
            room_allocations.append([start, 1])
            room_allocations.append([end, -1])
        
        room_allocations.sort(key=lambda allocation: allocation[0])
        for allocation in room_allocations:
            current_rooms_needed += allocation[1]
            total_rooms = max(total_rooms, current_rooms_needed)
            
        return total_rooms

-------------------------------------------------------------------------------------------------------------------------

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation: We need two meeting rooms  room1: (0,30)   room2: (5,10),(15,20)
      
Input: intervals = [(2,7)]
Output: 1
Explanation:  Only need one meeting room
  
  
class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        rooms, current_rooms_needed = 0, 0
        room_allocations = []

        for interval in intervals:
            room_allocations.append((interval.start, 1))
            room_allocations.append((interval.end, -1))

        room_allocations.sort(key=lambda interval: interval[0])
        for room_allocation in room_allocations:
            current_rooms_needed += room_allocation[1]
            rooms = max(rooms, current_rooms_needed)
            
        return rooms
