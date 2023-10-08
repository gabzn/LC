https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, initial_times: List[int], task_times: List[int]) -> int:
        initial_times.sort()
        task_times.sort(reverse=True)
        
        res, i = 0, 0
        
        for time in initial_times:
            res = max(res, time + task_times[i])
            i += 4

        return res
