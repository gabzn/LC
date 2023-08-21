https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:     
        dp = [0] * n
        
        memo = defaultdict(list)
        for start, end, value in offers:
            memo[end].append((start, value))
            
        for i in range(n):
            dp[i] = dp[max(0, i - 1)]
            
            for start, value in memo[i]:
                house_prior_to_start = start - 1
                
                if house_prior_to_start == -1:
                    dp[i] = max(dp[i], value)
                else:
                    dp[i] = max(dp[i], dp[house_prior_to_start] + value)

        return dp[-1]
