https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution:
    def minDifficulty(self, difficulties: List[int], d: int) -> int:
        LEN = len(difficulties)
        if LEN < d:
            return -1
        
        @cache
        def dp(i, days_left):
            if days_left == 1:
                return max(difficulties[i: ])
            
            res = math.inf
            hardest_job = difficulties[i]
            
            for idx in range(i, LEN - days_left + 1):
                hardest_job = max(hardest_job, difficulties[idx])
                res = min(res, hardest_job + dp(idx + 1, days_left - 1))

            return res
        
        return dp(0, d)
----------------------------------------------------------------
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        N = len(jobDifficulty)
        
        #dp(i, j) tells us the min difficulty at i-th day and j-th job
        def dp(i_day, j_job, memo):
            # If it is the last day, we need to finish up all the remaining jobs on this day, 
            # and the difficulty of that day will just be the max of the remaining jobs
            if i_day == d:
                return max(jobDifficulty[j_job: ])
            
            if (i_day, j_job) not in memo:
                hardest_job, res = jobDifficulty[j_job], math.inf
                
                for idx in range(j_job, N - (d - i_day)):
                    hardest_job = max(hardest_job, jobDifficulty[idx])
                    res = min(res, hardest_job + dp(i_day + 1, idx + 1, memo))  # idx + 1 because we already took the current job into consideration
                    
                    memo[(i_day, j_job)] = res
                
            return memo[(i_day, j_job)]
        return dp(1, 0, {})
