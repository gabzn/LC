https://leetcode.com/problems/insert-interval/
  
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        res = []        
        
        for i in range(len(intervals)):
            current_start, current_end = intervals[i]
            new_start, new_end = newInterval
             
            """
            Check if the new interval can be inserted before the current one, 
            if it can be inserted, insert it, append the rest of the intervals to res and return it.
            """
            if new_end < current_start:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
                
            # Check if they can be merged.
            if new_start <= current_end:
                newInterval[0] = min(current_start, new_start)
                newInterval[1] = max(current_end, new_end)
                continue
                
            """
            The new interval cannot be inserted before the current one and they cannot be merged.
            That means the new interval comes after the current one.
            Append the current one and go to the next iteration.
            """
            res.append(intervals[i])
        
        res.append(newInterval)
        return res
