https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        N = len(profit)
        
        job_and_profit = sorted([(d, p) for d, p in zip(difficulty, profit)])
        res = i = current_max_profit = 0
        
        for ability in sorted(worker):
            while i < N and job_and_profit[i][0] <= ability:
                current_max_profit = max(current_max_profit, job_and_profit[i][1])
                i += 1
            
            res += current_max_profit
        
        return res
