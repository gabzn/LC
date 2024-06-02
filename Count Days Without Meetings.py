https://leetcode.com/problems/count-days-without-meetings/

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
