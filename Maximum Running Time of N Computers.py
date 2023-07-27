https://leetcode.com/problems/maximum-running-time-of-n-computers/

class Solution:
    def maxRunTime(self, num_of_computers: int, batteries: List[int]) -> int:
        l, r = 0, sum(batteries) + 1
        res = 0
        
        while l + 1 != r:
            m = (l + r) // 2
            
            if self.can_all_run_m_minutes(num_of_computers, batteries, m):
                l = m
                res = m
            else:
                r = m
        
        return res
    
    # Check if every single computer can run for m minutes 
    # which in total is (num_of_computers * m)
    def can_all_run_m_minutes(self, num_of_computers, batteries, m):
        batteries_usage = 0
        
        for battery in batteries:
            # We don't care if a battery has more than m minutes worth of power
            # If a battery has more than m minutes worth of power, we use only m minutes of it
            batteries_usage += min(m, battery)
        
        return batteries_usage >= (num_of_computers * m)
