https://leetcode.com/problems/count-days-without-meetings/


class Solution:
    # https://leetcode.com/problems/merge-intervals/
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort the intervals by their start time.
        Loop through the intervals starting from the second interval. (Kind of 2-pointer)
        Compare the current start to the previous end to see if they are overlapping.
        """
        intervals.sort()
        res = []

        for start, end in intervals:
            if res and res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        
        return res
    
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        for start, end in self.merge(meetings):
            days -= (end - start + 1)

        return days
-----------------------------------------------------------------------------
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        N = len(meetings)
        
        meetings.sort()
        start, end = meetings[0]
        res = 0
        
        for i in range(1, N):    
            cur_start, cur_end = meetings[i]
            if cur_start > end:
                res += (cur_start - end - 1)
            
            start = min(start, cur_start)
            end = max(end, cur_end)
        
        return res + (start - 1) + (days - end)
