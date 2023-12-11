https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
https://www.youtube.com/watch?v=685x-rzOIlY&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g&index=3
https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/discuss/1436811/C%2B%2BJavaPython-From-Straightforward-to-Optimized-Bitmask-DP-O(2n-*-n)-Clean-and-Concise

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        LEN = len(tasks)
        
        @cache
        def dp(bit_mask, time_left_in_cur_session):
            if bit_mask == 0:
                return 0
            
            res = LEN
            
            for i in range(LEN):
        
                # If the current task has not been taken
                if bit_mask & (1 << i) == 1: 
                    if tasks[i] <= time_left_in_cur_session:
                        
                        # Put the current task into the current session and turn off this task
                        res = min(res, dp(bit_mask ^ (1 << i), time_left_in_cur_session - tasks[i]))
                    else:
                        res = min(res, 1 + dp(bit_mask ^ (1 << i), sessionTime - tasks[i]))
            
            return res
        
        # (1 << LEN) - 1 -> set all tasks to 1 meaning they have not been done yet.
        return dp((1 << LEN) - 1, 0)
