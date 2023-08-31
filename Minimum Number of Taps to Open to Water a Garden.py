https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # dp[i] is the min number of taps needed to water 1 to i
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        
        for i, dist in enumerate(ranges):
            left = max(0, i - dist)
            right = min(n, i + dist)
            
            for j in range(left, right + 1):
                dp[right] = min(dp[j] + 1, dp[right])
        
        return dp[-1] if dp[-1] != math.inf else -1
-------------------------------------------------------------------------------------
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        Visualizing the intervals helps!
        Be greedy and always pick the interval that covers more area
        """
        max_reach = [0] * (n + 1)        
        
        for i in range(n + 1):
            dist = ranges[i]
            
            left = max(0, i - dist)
            right = min(n, i + dist)
            
            max_reach[left] = max(max_reach[left], right)
        
        res, cur_end, next_end = 0, 0, 0
        
        for i in range(n + 1):
            if i > next_end:
                return -1
            
            if i > cur_end:
                res += 1
                cur_end = next_end
            
            next_end = max(next_end, max_reach[i])
        
        return res
