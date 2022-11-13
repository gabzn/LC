https://leetcode.com/problems/non-overlapping-intervals/
  
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
  

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        res, left, right = 0, 0, 1
        intervals.sort(key=lambda interval: interval[0])
        
        while right < len(intervals):
            previous_start, previous_end = intervals[left]
            current_start, current_end = intervals[right]   
            
            # The current interval starts before the previous one ends. They are overlapping.
            if current_start < previous_end:
                res += 1
                
                """
                If the previous one takes longer to complete, we drop the previous interval by moving l to r.
                The reason being we always want to keep the shorter one when they are overlapping.
                """
                if current_end < previous_end:
                    left = right
            else:
                left = right        
            right += 1
            
        return res

#         stack = []
#         intervals.sort(key=lambda interval: interval[0])
        
#         for interval in intervals:
#             cur_start, cur_end = interval
            
#             """
#             Check if the current interval overlaps with the previous one
#                 if it is overlapping, we check which one takes longer to complete.
#                     if the previous one takes longer to complete, we pop the previous one and store the shorter one.
#                     if the the current one takes longer to complete, we keep the previous one and skip the current one.
                
#                 else means they are not overlapping, append it to the stack.
#             """
#             if stack and stack[-1][1] > cur_start: 
#                 if stack[-1][1] >= cur_end:
#                     stack.pop()
#                     stack.append(interval)
#             else:        
#                 stack.append(interval)
            
#         return len(intervals) - len(stack)
