https://leetcode.com/problems/maximum-earnings-from-taxi/
https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # dp[i] = the max earned from 1 to i
        dp = [0] * (n + 1)
        
        earning_for_each_ride = defaultdict(list)
        for start, end, tip in rides:
            earning_for_each_ride[end].append((start, end-start+tip))
                
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            
            for start, earning in earning_for_each_ride[i]:
                dp[i] = max(dp[i], dp[start] + earning)
        
        return dp[-1]
