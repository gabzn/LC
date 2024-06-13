https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        
        events.sort()
        heap = []
        res = i = current_day = 0
        
        while i < N or heap:
            if current_day == 0:
                current_day = events[i][0]
            
            while i < N and events[i][0] <= current_day:
                heappush(heap, events[i][1])
                i += 1
            
            while heap and heap[0] < current_day:
                heappop(heap)
            
            if heap:
                heappop(heap)
                res += 1
                
            current_day += 1
        
        return res
-------------------------------------------------------------------------------------------
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        
        events.sort()
        heap = []
        res = i = 0
        
        # Go through each day and check if there is any event could attend
        for day in range(1, 100001):
            
            # If the start <= day, that means this event can be attended
            while i < N and events[i][0] <= day:
                heappush(heap, events[i][1])
                i += 1
            
            # We also want to check if there's any expired event
            while heap and heap[0] < day:
                heappop(heap)
            
            if heap:
                heappop(heap)
                res += 1
        
        return res
