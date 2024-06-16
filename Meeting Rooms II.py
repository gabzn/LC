https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        ending_times = []
        res = 0
        
        for start, end in sorted(intervals):
            # Check if any meeting rooms become free
            while ending_times and ending_times[0] <= start:
                heappop(ending_times)
            
            heappush(ending_times, end)
            res = max(res, len(ending_times))
        
        return res
----------------------------------------------------------------------
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        diff = []
        for start, end in intervals:
            diff.append((start, 1))
            diff.append((end, -1))
        
        diff.sort()
        
        res = rooms_in_used = 0
        
        for _, count in diff:
            rooms_in_used += count
            res = max(res, rooms_in_used)
        
        return res
-----------------------------------------------------------------------
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
