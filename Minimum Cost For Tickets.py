https://leetcode.com/problems/minimum-cost-for-tickets/
  
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        days = set(days)
        
        def dp(day, memo):
            if day <= 0:
                return 0
            
            if day in memo:
                return memo[day]
            
            # Two scenarios: either we need to travel today or we don't need to
            # if we need to travel today, pick the minimum from all three options
            # if we don't need to travel today, just use the previous memo value
            if day in days:
                memo[day] = min(costs[0] + dp(day - 1, memo), 
                                costs[1] + dp(day - 7, memo), 
                                costs[2] + dp(day - 30, memo))
            else:
                memo[day] = dp(day - 1, memo)
            
            return memo[day]
            
        return dp(last_day, {})
------------------------------------------------------------------------------------------------------------------
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [0 for _ in range(last_day + 1)]
        days = set(days)
        
        for day in range(1, last_day + 1):
            if day in days:
                dp[day] = min(dp[max(day-1, 0)] + costs[0], dp[max(day-7, 0)] + costs[1], dp[max(day-30, 0)] + costs[2])    
            else:
                dp[day] = dp[day - 1]
        
        return dp[-1]
