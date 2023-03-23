https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
  
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        if len(jobDifficulty) == d:
            return sum(jobDifficulty)
        
        # dp(i, cur_day) returns us the mim difficulty starting at job i at cur_day
        def dp(i, cur_day, memo):
            if cur_day == d:
                return max(jobDifficulty[i:])
            
            hardest, res = jobDifficulty[i], math.inf
            
            # caching happens here
            if (i, cur_day) not in memo:    
                for j in range(i, len(jobDifficulty) - (d - cur_day)):
                    hardest = max(hardest, jobDifficulty[j])
                    res = min(res, hardest + dp(j + 1, cur_day + 1, memo))
                    
                    memo[(i, cur_day)] = res
            
            return memo[(i, cur_day)]
        return dp(0, 1, {})
