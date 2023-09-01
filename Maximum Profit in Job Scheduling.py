https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution:
    def jobScheduling(self, start_time: List[int], end_time: List[int], profit: List[int]) -> int:
        def bisect(cur_start):
            l, r = -1, LEN
            
            while l + 1 != r:
                m = (l + r) // 2
                
                prev_end = jobs[m][0]
                if prev_end <= cur_start:
                    l = m
                else:
                    r = m
              
            return l
                
        LEN = len(profit)
        
        jobs = self.combine(LEN, start_time, end_time, profit)
        dp = [0] * LEN
        
        for i, (cur_end, cur_start, profit) in enumerate(jobs):
            max_profit, prev_job_index = 0, bisect(cur_start)
            
            if prev_job_index == -1:
                max_profit = profit
            else:
                max_profit = profit + dp[prev_job_index]
            
            if i > 0:
                dp[i] = dp[i-1]
            dp[i] = max(dp[i], max_profit)
                        
        return dp[-1]
    
    def combine(self, LEN, start_time, end_time, profit):
        jobs = []
        for i in range(LEN):
            jobs.append((end_time[i], start_time[i], profit[i]))
        return sorted(jobs) 
