https://leetcode.com/problems/count-all-possible-routes/

class Solution:
    def countRoutes(self, locations: List[int], start: int, end: int, fuel: int) -> int:
        LEN = len(locations)
        MOD = 10 ** 9 + 7
        
        # dp[i][f] = # of ways to arrive at city i with f fuel left
        dp = [[0 for _ in range(fuel + 1)] for _ in range(LEN)]
        dp[start][fuel] = 1
        
        for f in range(fuel, -1, -1):
            for destination in range(LEN):
                for source in range(LEN):
                    if source == destination:
                        continue
                    
                    cost = abs(locations[source] - locations[destination])
                    
                    # recall our dp[i][f] = # of ways arriving at city i with f fuel left
                    # to arrive at i, we can come from any of the source as long as we have f + cost fuel left
                    if f + cost <= fuel:
                        dp[destination][f] += (dp[source][f + cost]) % MOD
        
        return sum(dp[end]) % MOD
